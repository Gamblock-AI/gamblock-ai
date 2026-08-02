#!/usr/bin/env python3
"""Summarize privacy-safe native latency JSONL into Phase 4 percentiles."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


FORBIDDEN_KEYS = {
    "url", "uri", "domain", "dom", "title", "headings", "anchor_texts",
    "anchors", "history", "screenshot", "query", "score", "probability",
}
REQUIRED_FIELDS = {
    "platform", "run_id", "sample_id", "device_alias", "scenario",
    "model_version", "ruleset_version", "input_to_visible_ms",
}
ALLOWED_FIELDS = REQUIRED_FIELDS | {
    "schema_version", "extraction_ms", "relay_ms", "queue_ms",
    "classification_ms", "dispatch_to_visible_ms", "scan_to_visible_ms",
}
ALLOWED_PERCENTILES = {"p50": 0.50, "p95": 0.95, "p99": 0.99}
OPAQUE = re.compile(r"^[A-Za-z0-9_.-]{1,96}$")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def percentile(values: list[float], quantile: float) -> float:
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    position = (len(ordered) - 1) * quantile
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    return ordered[lower] + (ordered[upper] - ordered[lower]) * (position - lower)


def summary(values: list[float]) -> dict[str, float | int]:
    return {
        "samples": len(values),
        "p50_ms": percentile(values, 0.50),
        "p95_ms": percentile(values, 0.95),
        "p99_ms": percentile(values, 0.99),
        "maximum_ms": max(values),
    }


def validate_row(row: dict[str, Any], source: Path, line_number: int) -> None:
    lowered = {str(key).lower() for key in row}
    forbidden = sorted(lowered & FORBIDDEN_KEYS)
    if forbidden:
        raise ValueError(f"{source}:{line_number}: forbidden fields {forbidden}")
    unknown = sorted(set(row) - ALLOWED_FIELDS)
    if unknown:
        raise ValueError(f"{source}:{line_number}: unknown fields {unknown}")
    missing = sorted(REQUIRED_FIELDS - set(row))
    if missing:
        raise ValueError(f"{source}:{line_number}: missing fields {missing}")
    duration = row.get("input_to_visible_ms")
    if (
        not isinstance(duration, (int, float))
        or not math.isfinite(float(duration))
        or duration < 0
        or duration > 60000
    ):
        raise ValueError(f"{source}:{line_number}: invalid duration")
    for key in (
        "run_id", "sample_id", "device_alias", "scenario",
        "model_version", "ruleset_version",
    ):
        if not OPAQUE.fullmatch(str(row[key])):
            raise ValueError(f"{source}:{line_number}: {key} must be opaque")
    if row["platform"] not in {"android", "windows"}:
        raise ValueError(f"{source}:{line_number}: invalid platform")
    for key in ALLOWED_FIELDS - REQUIRED_FIELDS - {"schema_version"}:
        if key in row and (
            not isinstance(row[key], (int, float))
            or not math.isfinite(float(row[key]))
            or row[key] < 0
            or row[key] > 60000
        ):
            raise ValueError(f"{source}:{line_number}: invalid {key}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", action="append", required=True, type=Path)
    parser.add_argument("--device-matrix", required=True, type=Path)
    parser.add_argument("--target-percentile", choices=tuple(ALLOWED_PERCENTILES), required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    matrix = json.loads(args.device_matrix.read_text(encoding="utf-8"))
    target_ms = float(matrix.get("target_ms", 200))
    matrix_target_percentile = str(matrix.get("target_percentile", ""))
    required_scenarios = {
        str(value) for value in matrix.get("required_scenarios", [])
    }
    device_entries = matrix.get("devices", [])
    required_devices = {
        str(item.get("alias")): str(item.get("platform"))
        for item in device_entries
        if isinstance(item, dict)
    }
    if (
        not required_scenarios
        or not required_devices
        or "REQUIRED" in json.dumps(matrix)
        or not matrix.get("approved_by")
        or not matrix.get("approved_at")
        or target_ms != 200
        or matrix_target_percentile != args.target_percentile
        or len(required_devices) != len(device_entries)
        or any(not OPAQUE.fullmatch(value) for value in required_scenarios)
        or any(
            not OPAQUE.fullmatch(alias) or platform not in {"android", "windows"}
            for alias, platform in required_devices.items()
        )
    ):
        parser.error("device matrix must be completed and approved")

    rows: list[dict[str, Any]] = []
    sources: list[dict[str, str]] = []
    seen_samples: set[tuple[str, str]] = set()
    for path in args.input:
        if not path.is_file():
            parser.error(f"file not found: {path}")
        sources.append({"name": path.name, "sha256": sha256(path)})
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            row = json.loads(line)
            if not isinstance(row, dict):
                raise ValueError(f"{path}:{line_number}: expected object")
            validate_row(row, path, line_number)
            identity = (str(row["run_id"]), str(row["sample_id"]))
            if identity in seen_samples:
                raise ValueError(f"{path}:{line_number}: duplicate sample")
            seen_samples.add(identity)
            rows.append(row)
    if not rows:
        parser.error("latency input is empty")

    observed_scenarios = {str(row["scenario"]) for row in rows}
    observed_devices = {str(row["device_alias"]) for row in rows}
    missing_scenarios = sorted(required_scenarios - observed_scenarios)
    missing_devices = sorted(set(required_devices) - observed_devices)
    required_cells = {
        (platform, alias, scenario)
        for alias, platform in required_devices.items()
        for scenario in required_scenarios
    }
    observed_cells = {
        (str(row["platform"]), str(row["device_alias"]), str(row["scenario"]))
        for row in rows
    }
    unexpected_platforms = sorted({
        f"{row['device_alias']}:{row['platform']}"
        for row in rows
        if required_devices.get(str(row["device_alias"])) != row["platform"]
    })
    missing_cells = sorted(":".join(cell) for cell in required_cells - observed_cells)
    grouped: dict[tuple[str, str, str], list[float]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["platform"]), str(row["device_alias"]), str(row["scenario"]))].append(
            float(row["input_to_visible_ms"])
        )
    groups = []
    percentile_key = f"{args.target_percentile}_ms"
    for (platform, device, scenario), values in sorted(grouped.items()):
        item = summary(values)
        item.update({
            "platform": platform,
            "device_alias": device,
            "scenario": scenario,
            "target_ms": target_ms,
            "target_percentile": args.target_percentile,
            "target_met": float(item[percentile_key]) < target_ms,
        })
        groups.append(item)
    complete = (
        not missing_scenarios
        and not missing_devices
        and not missing_cells
        and not unexpected_platforms
    )
    report = {
        "schema_version": 1,
        "report_kind": "phase4_block_latency",
        "analysis_status": "unreviewed",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "inputs": sources,
        "device_matrix_sha256": sha256(args.device_matrix),
        "target_ms": target_ms,
        "target_percentile": args.target_percentile,
        "coverage": {
            "complete": complete,
            "missing_scenarios": missing_scenarios,
            "missing_devices": missing_devices,
            "missing_device_scenario_cells": missing_cells,
            "unexpected_device_platforms": unexpected_platforms,
        },
        "groups": groups,
        "all_groups_meet_target": complete and all(bool(item["target_met"]) for item in groups),
        "privacy": {"raw_browsing_data_emitted": False},
        "review": {"approved": False, "reviewer": None, "reviewed_at": None},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote latency report for {len(rows)} samples: {args.output}")
    return 0 if report["all_groups_meet_target"] else 3


if __name__ == "__main__":
    raise SystemExit(main())
