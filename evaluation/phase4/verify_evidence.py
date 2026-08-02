#!/usr/bin/env python3
"""Fail-closed Phase 4 evidence-manifest verifier."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any


SHA256 = re.compile(r"^[a-f0-9]{64}$")
REQUIRED_ARTIFACTS = {
    "dataset_card",
    "split_manifest",
    "model_report",
    "device_matrix",
    "latency_report",
    "resilience_matrix",
    "android_resilience_report",
    "windows_resilience_report",
    "resilience_report",
    "retention_protocol",
    "retention_report",
    "ethics_approval",
    "pattern_interrupt_protocol",
    "pattern_interrupt_report",
    "adverse_event_review",
    "limitations_review",
}


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reviewed(value: Any) -> bool:
    return (
        isinstance(value, dict)
        and value.get("approved") is True
        and value.get("reviewer") not in {None, "", "REQUIRED"}
        and value.get("reviewed_at") not in {None, "", "REQUIRED"}
    )


def validate_json_artifact(name: str, path: Path) -> list[str]:
    failures: list[str] = []
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return [f"{name}: expected valid JSON"]
    if not isinstance(value, dict) or "REQUIRED" in json.dumps(value):
        return [f"{name}: incomplete JSON artifact"]
    if value.get("schema_version") != 1:
        failures.append(f"{name}: schema_version must be 1")
    expected_kinds = {
        "model_report": "phase4_model_evaluation",
        "latency_report": "phase4_block_latency",
        "android_resilience_report": "phase4_resilience_run",
        "windows_resilience_report": "phase4_resilience_run",
        "resilience_report": "phase4_resilience",
        "retention_report": "phase4_retention",
        "pattern_interrupt_report": "phase4_pattern_interrupt",
    }
    if name in expected_kinds and value.get("report_kind") != expected_kinds[name]:
        failures.append(f"{name}: report_kind is invalid")
    if name in expected_kinds and not reviewed(value.get("review")):
        failures.append(f"{name}: embedded review approval is required")
    metrics = value.get("metrics")
    if name == "model_report" and (
        not isinstance(metrics, dict) or "hybrid" not in metrics
    ):
        failures.append("model_report: Hybrid metrics are missing")
    if name == "model_report" and isinstance(metrics, dict):
        if value.get("mode") != "final":
            failures.append("model_report: final evaluation mode is required")
        hybrid = metrics.get("hybrid")
        if not isinstance(hybrid, dict) or any(
            hybrid.get(key) is None
            for key in ("precision", "recall", "f1_score", "false_positive_rate")
        ):
            failures.append("model_report: required Hybrid rates are incomplete")
        slices = value.get("slice_metrics")
        for required_slice in ("government", "education"):
            slice_hybrid = (
                slices.get(required_slice, {}).get("hybrid")
                if isinstance(slices, dict)
                and isinstance(slices.get(required_slice), dict)
                else None
            )
            if (
                not isinstance(slice_hybrid, dict)
                or slice_hybrid.get("false_positive_rate") is None
            ):
                failures.append(
                    f"model_report: {required_slice} FPR slice is required"
                )
    coverage = value.get("coverage")
    if name == "latency_report" and (
        not isinstance(coverage, dict)
        or coverage.get("complete") is not True
        or value.get("all_groups_meet_target") is not True
        or value.get("target_ms") != 200
    ):
        failures.append("latency_report: coverage or <200 ms gate failed")
    if name == "resilience_report" and (
        not isinstance(coverage, dict)
        or coverage.get("complete") is not True
        or value.get("all_required_scenarios_pass") is not True
        or value.get("unsafe_critical_process_api_used") is not False
    ):
        failures.append("resilience_report: coverage or safety gate failed")
    if name == "retention_report":
        cohorts = value.get("cohorts")
        windows = [
            window
            for cohort in cohorts.values()
            if isinstance(cohort, dict)
            for window in (
                cohort.get("windows", {}).values()
                if isinstance(cohort.get("windows"), dict) else []
            )
            if isinstance(window, dict) and window.get("suppressed") is False
        ] if isinstance(cohorts, dict) else []
        if not windows:
            failures.append("retention_report: no unsuppressed cohort/window result")
    if name == "pattern_interrupt_report":
        conditions = value.get("conditions", {})
        nonsuppressed = [
            item for item in conditions.values()
            if isinstance(item, dict) and item.get("suppressed") is False
            and item.get("completed", 0) > 0
        ] if isinstance(conditions, dict) else []
        difference = value.get("descriptive_mean_change_difference", {})
        if (
            len(nonsuppressed) != 2
            or not isinstance(difference, dict)
            or difference.get("first_minus_second") is None
        ):
            failures.append("pattern_interrupt_report: two analyzable groups are required")
    if name in {"android_resilience_report", "windows_resilience_report"}:
        expected_platform = "android" if name.startswith("android") else "windows"
        if value.get("platform") != expected_platform:
            failures.append(f"{name}: platform is invalid")
    if name in {"device_matrix", "resilience_matrix", "retention_protocol",
                "pattern_interrupt_protocol"} and (
        not value.get("approved_by") or not value.get("approved_at")
    ):
        failures.append(f"{name}: protocol/matrix approval is required")
    if name == "dataset_card" and (
        not value.get("owner") or not value.get("approved_at")
    ):
        failures.append("dataset_card: owner/approval is required")
    if name == "split_manifest" and (
        not value.get("leakage_reviewed_by") or not value.get("frozen_at")
    ):
        failures.append("split_manifest: leakage review is required")
    if name == "adverse_event_review" and value.get("approved") is not True:
        failures.append("adverse_event_review: approval is required")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    if not args.manifest.is_file():
        parser.error(f"manifest not found: {args.manifest}")
    manifest: dict[str, Any] = json.loads(args.manifest.read_text(encoding="utf-8"))
    failures: list[str] = []
    if manifest.get("schema_version") != 1:
        failures.append("schema_version must be 1")
    if manifest.get("phase") != "phase_4_system_hardening":
        failures.append("phase identifier is invalid")
    if manifest.get("status") != "evaluated":
        failures.append("status must be evaluated")
    if manifest.get("reviewer") in {None, "", "REQUIRED"}:
        failures.append("reviewer is required")
    if manifest.get("reviewed_at") in {None, "", "REQUIRED"}:
        failures.append("reviewed_at is required")
    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, dict):
        failures.append("artifacts object is required")
        artifacts = {}
    missing = sorted(REQUIRED_ARTIFACTS - set(artifacts))
    if missing:
        failures.append(f"missing artifacts: {', '.join(missing)}")
    root = args.manifest.parent.resolve()
    for name in sorted(REQUIRED_ARTIFACTS & set(artifacts)):
        item = artifacts[name]
        if not isinstance(item, dict):
            failures.append(f"{name}: descriptor must be an object")
            continue
        declared = str(item.get("sha256", ""))
        raw_path = str(item.get("path", ""))
        if item.get("approved") is not True:
            failures.append(f"{name}: reviewer approval is required")
        if not SHA256.fullmatch(declared):
            failures.append(f"{name}: valid SHA-256 is required")
            continue
        candidate = (root / raw_path).resolve()
        try:
            candidate.relative_to(root)
        except ValueError:
            failures.append(f"{name}: path must stay inside the evidence directory")
            continue
        if not candidate.is_file():
            failures.append(f"{name}: file not found")
            continue
        if file_hash(candidate) != declared:
            failures.append(f"{name}: SHA-256 mismatch")
            continue
        if name not in {"ethics_approval", "limitations_review"}:
            failures.extend(validate_json_artifact(name, candidate))
    if failures:
        print("Phase 4 evidence is incomplete:")
        for failure in failures:
            print(f"- {failure}")
        return 3
    print("Phase 4 evidence manifest verified: status=evaluated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
