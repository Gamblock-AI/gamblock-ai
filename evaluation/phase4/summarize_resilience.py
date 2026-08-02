#!/usr/bin/env python3
"""Verify reviewed Android/Windows Phase 4 resilience scenario coverage."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


OPAQUE = re.compile(r"^[A-Za-z0-9_.-]{1,96}$")
ALLOWED_PLATFORMS = {"android", "windows"}
TOP_LEVEL_FIELDS = {
    "schema_version", "report_kind", "platform", "run_id", "device_alias",
    "host_identifier_emitted", "unsafe_critical_process_api_used",
    "scenario_results", "review",
}
SCENARIO_FIELDS = {
    "scenario", "attempted", "passed", "device_recoverable",
    "protection_recovered", "unsafe_behavior_observed", "evidence_reference",
    "recovery_within_seconds",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", action="append", required=True, type=Path)
    parser.add_argument("--matrix", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if not args.matrix.is_file():
        parser.error(f"file not found: {args.matrix}")
    matrix = json.loads(args.matrix.read_text(encoding="utf-8"))
    if not isinstance(matrix, dict) or "REQUIRED" in json.dumps(matrix):
        parser.error("resilience matrix must be completed and approved")
    if not matrix.get("approved_by") or not matrix.get("approved_at"):
        parser.error("resilience matrix approval is required")
    scenarios = {str(value) for value in matrix.get("scenarios", [])}
    device_entries = matrix.get("devices", [])
    devices = {
        str(item.get("alias")): str(item.get("platform"))
        for item in device_entries
        if isinstance(item, dict)
    }
    if (
        not scenarios
        or len(devices) != len(device_entries)
        or any(not OPAQUE.fullmatch(value) for value in scenarios)
        or any(
            not OPAQUE.fullmatch(alias) or platform not in ALLOWED_PLATFORMS
            for alias, platform in devices.items()
        )
    ):
        parser.error("resilience matrix scenarios/devices are invalid")
    pass_criteria = matrix.get("pass_criteria")
    recovery_limit = (
        pass_criteria.get("protection_recovers_within_seconds")
        if isinstance(pass_criteria, dict) else None
    )
    if (
        not isinstance(pass_criteria, dict)
        or pass_criteria.get("device_recoverable") is not True
        or pass_criteria.get("no_critical_process_api") is not True
        or pass_criteria.get("no_boot_loop") is not True
        or pass_criteria.get("no_destructive_lockout") is not True
        or not isinstance(recovery_limit, (int, float))
        or not math.isfinite(float(recovery_limit))
        or recovery_limit <= 0
        or recovery_limit > 3600
    ):
        parser.error("resilience matrix pass criteria are invalid")

    observed: dict[tuple[str, str, str], dict[str, Any]] = {}
    sources: list[dict[str, str]] = []
    unapproved_reports: list[str] = []
    for path in args.input:
        if not path.is_file():
            parser.error(f"file not found: {path}")
        sources.append({"name": path.name, "sha256": sha256(path)})
        report = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(report, dict) or set(report) - TOP_LEVEL_FIELDS:
            raise ValueError(f"{path}: unexpected report fields")
        platform = str(report.get("platform", ""))
        run_id = str(report.get("run_id", ""))
        device_alias = str(report.get("device_alias", ""))
        if (
            report.get("schema_version") != 1
            or report.get("report_kind") != "phase4_resilience_run"
            or platform not in ALLOWED_PLATFORMS
            or not OPAQUE.fullmatch(run_id)
            or not OPAQUE.fullmatch(device_alias)
            or devices.get(device_alias) != platform
            or report.get("host_identifier_emitted") is not False
            or report.get("unsafe_critical_process_api_used") is not False
        ):
            raise ValueError(f"{path}: invalid or unsafe report metadata")
        review = report.get("review")
        approved = (
            isinstance(review, dict)
            and review.get("approved") is True
            and review.get("reviewer") not in {None, "", "REQUIRED"}
            and review.get("reviewed_at") not in {None, "", "REQUIRED"}
        )
        if not approved:
            unapproved_reports.append(path.name)
        results = report.get("scenario_results")
        if not isinstance(results, list) or not results:
            raise ValueError(f"{path}: scenario_results are required")
        for result in results:
            if not isinstance(result, dict) or set(result) - SCENARIO_FIELDS:
                raise ValueError(f"{path}: invalid scenario result fields")
            scenario = str(result.get("scenario", ""))
            reference = str(result.get("evidence_reference", ""))
            if scenario not in scenarios or not OPAQUE.fullmatch(reference):
                raise ValueError(f"{path}: invalid scenario/reference")
            for key in (
                "attempted", "passed", "device_recoverable",
                "protection_recovered", "unsafe_behavior_observed",
            ):
                if not isinstance(result.get(key), bool):
                    raise ValueError(f"{path}: {key} must be boolean")
            recovery_seconds = result.get("recovery_within_seconds")
            if recovery_seconds is None or (
                not isinstance(recovery_seconds, (int, float))
                or not math.isfinite(float(recovery_seconds))
                or recovery_seconds < 0
                or recovery_seconds > 3600
            ):
                raise ValueError(f"{path}: invalid recovery duration")
            cell = (platform, device_alias, scenario)
            if cell in observed:
                raise ValueError(f"{path}: duplicate device/scenario result")
            observed[cell] = {
                "approved": approved,
                "attempted": result["attempted"],
                "passed": result["passed"],
                "device_recoverable": result["device_recoverable"],
                "protection_recovered": result["protection_recovered"],
                "unsafe_behavior_observed": result["unsafe_behavior_observed"],
                "recovery_within_seconds": float(recovery_seconds),
            }

    required = {
        (platform, alias, scenario)
        for alias, platform in devices.items()
        for scenario in scenarios
    }
    missing = sorted(":".join(cell) for cell in required - set(observed))
    unapproved_cells = sorted(
        ":".join(cell) for cell in required & set(observed)
        if not observed[cell]["approved"]
    )
    failed = sorted(
        ":".join(cell) for cell in required & set(observed)
        if observed[cell]["approved"] and not (
            observed[cell]["attempted"]
            and observed[cell]["passed"]
            and observed[cell]["device_recoverable"]
            and observed[cell]["protection_recovered"]
            and not observed[cell]["unsafe_behavior_observed"]
            and observed[cell]["recovery_within_seconds"] <= recovery_limit
        )
    )
    complete = not missing and not unapproved_cells
    report = {
        "schema_version": 1,
        "report_kind": "phase4_resilience",
        "analysis_status": "unreviewed",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "matrix_sha256": sha256(args.matrix),
        "inputs": sources,
        "coverage": {
            "complete": complete,
            "required_cells": len(required),
            "observed_cells": len(required & set(observed)),
            "missing_cells": missing,
            "unapproved_cells": unapproved_cells,
            "unapproved_reports": sorted(set(unapproved_reports)),
        },
        "failed_cells": failed,
        "all_required_scenarios_pass": complete and not failed,
        "unsafe_critical_process_api_used": False,
        "privacy": {"host_or_participant_identifiers_emitted": False},
        "review": {"approved": False, "reviewer": None, "reviewed_at": None},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"Wrote resilience report for {len(observed)} scenario cells: {args.output}")
    return 0 if complete and not failed else 3


if __name__ == "__main__":
    raise SystemExit(main())
