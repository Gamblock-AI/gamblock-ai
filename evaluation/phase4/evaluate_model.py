#!/usr/bin/env python3
"""Evaluate the local Hybrid-v2 classifier without emitting raw browsing data."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


ALLOWED_LABELS = {"gambling": 1, "benign": 0}
ALLOWED_SLICES = {
    "gambling",
    "dynamic",
    "camouflage",
    "benign",
    "government",
    "education",
    "other",
}
OPAQUE_ID = re.compile(r"^[A-Za-z0-9_-]{1,64}$")
TOKEN = re.compile(r"[a-zA-Z0-9_]+")
RULE_SEPARATOR = re.compile(r"[^a-z0-9_]+")
URL_PATTERN = re.compile(r"^(https?)://([^/?#]+)")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return value


def normalize_rules(value: str) -> str:
    return RULE_SEPARATOR.sub(" ", value.lower()).strip()


def contains_phrase(haystack: str, needle: str) -> bool:
    return bool(needle) and f" {needle} " in f" {haystack} "


def bounded_strings(value: Any, maximum: int, maximum_bytes: int) -> list[str]:
    if not isinstance(value, list):
        return []
    result: list[str] = []
    for item in value[:maximum]:
        if not isinstance(item, str):
            continue
        encoded = item.encode("utf-8")[:maximum_bytes]
        result.append(encoded.decode("utf-8", errors="ignore").lower())
    return result


def url_features(url: str, keyword_count: int) -> dict[str, float]:
    parsed = URL_PATTERN.search(url)
    scheme = parsed.group(1) if parsed else ""
    host = parsed.group(2) if parsed else ""
    if "@" in host:
        host = host.rsplit("@", 1)[1]
    if ":" in host:
        host = host.split(":", 1)[0]
    host = host.rstrip(".")
    labels = [label for label in host.split(".") if label]
    suffix = labels[-1] if labels else ""
    subdomain = ".".join(labels[:-2]) if len(labels) > 2 else ""
    digit_count = sum(character.isdigit() for character in url)
    valid = parsed is not None and bool(host)
    return {
        "url_length": float(len(url)),
        "url_digit_count": float(digit_count),
        "url_dot_count": float(url.count(".")),
        "url_slash_count": float(url.count("/")),
        "url_hyphen_count": float(url.count("-")),
        "url_question_count": float(url.count("?")),
        "url_equal_count": float(url.count("=")),
        "url_keyword_count": float(keyword_count),
        "url_has_number": 1.0 if digit_count else 0.0,
        "url_has_https": 1.0 if scheme == "https" else 0.0,
        "url_is_valid": 1.0 if valid else 0.0,
        "domain_length": float(len(host)),
        "subdomain_length": float(len(subdomain)),
        "suffix_length": float(len(suffix)),
    }


class HybridClassifier:
    def __init__(self, model: dict[str, Any], rules: dict[str, Any]) -> None:
        if model.get("contract_version") != "hybrid-v2":
            raise ValueError("model contract must be hybrid-v2")
        if rules.get("contract_version") != "hybrid-v2":
            raise ValueError("rules contract must be hybrid-v2")
        self.model = model
        self.rules = rules
        self.unigrams = model.get("unigram_weights", {})
        self.bigrams = model.get("bigram_weights", {})
        self.feature_specs = model.get("url_features", [])
        self.keywords = [normalize_rules(str(item)) for item in rules.get("keywords", [])]
        if not self.unigrams or not self.bigrams or len(self.feature_specs) != 14:
            raise ValueError("model weights or URL feature contract are incomplete")
        if not self.keywords:
            raise ValueError("ruleset is empty")

    def classify(self, row: dict[str, Any]) -> dict[str, float | bool]:
        url = str(row.get("url", ""))[:2048].lower()
        title = str(row.get("title", ""))[:512].lower()
        headings = bounded_strings(row.get("headings"), 32, 256)
        anchors = bounded_strings(row.get("anchor_texts"), 64, 256)
        normalized_url = normalize_rules(url)
        url_keyword_count = sum(
            contains_phrase(normalized_url, keyword) for keyword in self.keywords
        )
        document = f"{title} {' '.join(headings)} {' '.join(anchors)} "
        rule_input = f"{normalized_url} {normalize_rules(document)}".strip()
        rule_score = (
            float(self.rules.get("match_score", 1.0))
            if any(contains_phrase(rule_input, keyword) for keyword in self.keywords)
            else 0.0
        )
        tokens = TOKEN.findall(document.lower())
        unigram_counts = Counter(tokens)
        bigram_counts = Counter(
            f"{tokens[index - 1]} {tokens[index]}"
            for index in range(1, len(tokens))
        )
        linear = float(self.model.get("bias", 0.0))
        linear += sum(float(self.unigrams.get(token, 0.0)) * count for token, count in unigram_counts.items())
        linear += sum(float(self.bigrams.get(token, 0.0)) * count for token, count in bigram_counts.items())
        values = url_features(url, url_keyword_count)
        for spec in self.feature_specs:
            raw = values.get(str(spec.get("name")), 0.0)
            linear += (
                (raw - float(spec.get("offset", 0.0)))
                * float(spec.get("scale", 1.0))
                * float(spec.get("weight", 0.0))
            )
        model_score = 1.0 / (1.0 + math.exp(-max(-700.0, min(700.0, linear))))
        threshold = float(self.model.get("threshold", 0.4))
        hybrid_score = (
            float(self.model.get("ml_weight", 0.75)) * model_score
            + float(self.model.get("rule_weight", 0.25)) * rule_score
        )
        return {
            "hybrid": hybrid_score >= threshold,
            "model_only": model_score >= threshold,
            "rule_only": rule_score >= threshold,
            "model_score": model_score,
            "rule_score": rule_score,
            "hybrid_score": hybrid_score,
        }


def wilson(successes: int, total: int) -> list[float] | None:
    if total <= 0:
        return None
    z = 1.959963984540054
    proportion = successes / total
    denominator = 1 + z * z / total
    center = (proportion + z * z / (2 * total)) / denominator
    margin = z * math.sqrt(
        proportion * (1 - proportion) / total + z * z / (4 * total * total)
    ) / denominator
    return [max(0.0, center - margin), min(1.0, center + margin)]


def safe_rate(numerator: int, denominator: int) -> float | None:
    return numerator / denominator if denominator else None


def metric_block(truth: Iterable[int], predicted: Iterable[int]) -> dict[str, Any]:
    pairs = list(zip(truth, predicted))
    tp = sum(actual == 1 and guess == 1 for actual, guess in pairs)
    fp = sum(actual == 0 and guess == 1 for actual, guess in pairs)
    tn = sum(actual == 0 and guess == 0 for actual, guess in pairs)
    fn = sum(actual == 1 and guess == 0 for actual, guess in pairs)
    precision = safe_rate(tp, tp + fp)
    recall = safe_rate(tp, tp + fn)
    fpr = safe_rate(fp, fp + tn)
    f1 = (
        2 * precision * recall / (precision + recall)
        if precision is not None and recall is not None and precision + recall > 0
        else None
    )
    return {
        "samples": len(pairs),
        "confusion_matrix": {"tp": tp, "fp": fp, "tn": tn, "fn": fn},
        "precision": precision,
        "precision_ci95_wilson": wilson(tp, tp + fp),
        "recall": recall,
        "recall_ci95_wilson": wilson(tp, tp + fn),
        "f1_score": f1,
        "false_positive_rate": fpr,
        "false_positive_rate_ci95_wilson": wilson(fp, fp + tn),
    }


def load_rows(path: Path, mode: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        if not isinstance(row, dict):
            raise ValueError(f"dataset line {line_number}: expected object")
        sample_id = str(row.get("id", ""))
        group_id = str(row.get("group_id", ""))
        label = str(row.get("label", ""))
        slice_name = str(row.get("slice", ""))
        split = str(row.get("split", ""))
        if not OPAQUE_ID.fullmatch(sample_id) or not OPAQUE_ID.fullmatch(group_id):
            raise ValueError(f"dataset line {line_number}: IDs must be opaque")
        if sample_id in seen_ids:
            raise ValueError(f"dataset line {line_number}: duplicate sample ID")
        if label not in ALLOWED_LABELS or slice_name not in ALLOWED_SLICES:
            raise ValueError(f"dataset line {line_number}: invalid label or slice")
        if mode == "final" and split != "final_test":
            raise ValueError(f"dataset line {line_number}: final mode requires final_test rows")
        seen_ids.add(sample_id)
        rows.append(row)
    if not rows:
        raise ValueError("dataset is empty")
    if len({str(row["group_id"]) for row in rows}) == 1 and len(rows) > 1:
        raise ValueError("dataset needs more than one opaque site/template group")
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", required=True, type=Path)
    parser.add_argument("--dataset-card", type=Path)
    parser.add_argument("--split-manifest", type=Path)
    parser.add_argument("--model", required=True, type=Path)
    parser.add_argument("--rules", required=True, type=Path)
    parser.add_argument("--mode", choices=("smoke", "pilot", "final"), required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if args.mode != "smoke" and (args.dataset_card is None or args.split_manifest is None):
        parser.error("pilot/final modes require --dataset-card and --split-manifest")
    for path in (args.dataset, args.model, args.rules, args.dataset_card, args.split_manifest):
        if path is not None and not path.is_file():
            parser.error(f"file not found: {path}")

    model = load_json(args.model)
    rules = load_json(args.rules)
    if args.mode != "smoke":
        dataset_card = load_json(args.dataset_card)
        split_manifest = load_json(args.split_manifest)
        if "REQUIRED" in json.dumps(dataset_card) or "REQUIRED" in json.dumps(split_manifest):
            parser.error("dataset card and split manifest must be completed")
        declared_dataset = str(split_manifest.get("final_test_sha256", ""))
        if args.mode == "final" and declared_dataset != sha256(args.dataset):
            parser.error("split manifest final_test_sha256 does not match the dataset")
    rows = load_rows(args.dataset, args.mode)
    classifier = HybridClassifier(model, rules)
    decisions: dict[str, list[int]] = defaultdict(list)
    truths: list[int] = []
    failures: dict[str, list[str]] = defaultdict(list)
    slices: dict[str, list[int]] = defaultdict(list)
    for index, row in enumerate(rows):
        truth = ALLOWED_LABELS[str(row["label"])]
        truths.append(truth)
        slices[str(row["slice"])].append(index)
        result = classifier.classify(row)
        for variant in ("hybrid", "model_only", "rule_only"):
            guess = 1 if result[variant] else 0
            decisions[variant].append(guess)
            if guess != truth:
                failures[variant].append(str(row["id"]))

    slice_metrics: dict[str, Any] = {}
    for slice_name, indexes in sorted(slices.items()):
        slice_metrics[slice_name] = {
            variant: metric_block(
                (truths[index] for index in indexes),
                (decisions[variant][index] for index in indexes),
            )
            for variant in ("hybrid", "model_only", "rule_only")
        }
    report = {
        "schema_version": 1,
        "report_kind": "phase4_model_evaluation",
        "analysis_status": "unreviewed",
        "evidence_maturity": "pilot" if args.mode == "pilot" else "instrumented",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": args.mode,
        "dataset": {
            "sha256": sha256(args.dataset),
            "samples": len(rows),
            "opaque_groups": len({str(row["group_id"]) for row in rows}),
            "label_counts": dict(sorted(Counter(str(row["label"]) for row in rows).items())),
            "slice_counts": dict(sorted(Counter(str(row["slice"]) for row in rows).items())),
            "dataset_card_sha256": sha256(args.dataset_card) if args.dataset_card else None,
            "split_manifest_sha256": sha256(args.split_manifest) if args.split_manifest else None,
        },
        "artifacts": {
            "contract_version": model.get("contract_version"),
            "model_version": model.get("version"),
            "model_sha256": sha256(args.model),
            "ruleset_version": rules.get("version"),
            "ruleset_sha256": sha256(args.rules),
            "threshold": model.get("threshold"),
            "ml_weight": model.get("ml_weight"),
            "rule_weight": model.get("rule_weight"),
        },
        "metrics": {
            variant: metric_block(truths, decisions[variant])
            for variant in ("hybrid", "model_only", "rule_only")
        },
        "slice_metrics": slice_metrics,
        "opaque_failure_ids": {key: sorted(value) for key, value in failures.items()},
        "privacy": {
            "raw_url_or_dom_emitted": False,
            "participant_data_emitted": False,
        },
        "review": {"approved": False, "reviewer": None, "reviewed_at": None},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote aggregate model report for {len(rows)} samples: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
