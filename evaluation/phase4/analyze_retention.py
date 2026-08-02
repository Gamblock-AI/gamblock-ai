#!/usr/bin/env python3
"""Analyze separately consented pseudonymous retention rows with suppression."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any


FORBIDDEN_KEYS = {
    "url", "domain", "dom", "title", "heading", "anchor", "history",
    "screenshot", "journal", "reflection", "mood", "urge",
}
OPAQUE = re.compile(r"^[A-Za-z0-9_-]{1,64}$")


def parse_date(value: Any, field: str) -> date:
    try:
        return date.fromisoformat(str(value))
    except ValueError as error:
        raise ValueError(f"invalid {field} date") from error


def wilson(successes: int, total: int) -> list[float] | None:
    if total <= 0:
        return None
    z = 1.959963984540054
    p = successes / total
    denominator = 1 + z * z / total
    center = (p + z * z / (2 * total)) / denominator
    margin = z * math.sqrt(p * (1 - p) / total + z * z / (4 * total * total)) / denominator
    return [max(0.0, center - margin), min(1.0, center + margin)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--protocol", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if not args.protocol.is_file():
        parser.error(f"file not found: {args.protocol}")
    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    if not isinstance(protocol, dict) or "REQUIRED" in json.dumps(protocol):
        parser.error("retention protocol must be completed and approved")
    if (
        protocol.get("schema_version") != 1
        or protocol.get("activity_window") != "exact_day"
        or not protocol.get("approved_by")
        or not protocol.get("approved_at")
    ):
        parser.error("retention protocol schema/approval is invalid")
    withdrawal_policy = str(protocol.get("withdrawal_policy", ""))
    if withdrawal_policy not in {"exclude_after_withdrawal", "not_retained"}:
        parser.error("retention protocol withdrawal policy is invalid")
    minimum_cohort = int(protocol.get("minimum_cohort", 0))
    if minimum_cohort < 5:
        parser.error("minimum cohort must be at least 5")
    window_values = protocol.get("windows_days", [])
    if not isinstance(window_values, list):
        parser.error("retention protocol windows_days must be a list")
    windows = sorted({int(item) for item in window_values})
    if not windows or min(windows) < 1 or max(windows) > 365:
        parser.error("windows must be between 1 and 365 days")
    if not args.input.is_file():
        parser.error(f"file not found: {args.input}")

    participants: set[str] = set()
    cohorts: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for line_number, line in enumerate(args.input.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        if not isinstance(row, dict):
            raise ValueError(f"line {line_number}: expected object")
        forbidden = sorted({str(key).lower() for key in row} & FORBIDDEN_KEYS)
        if forbidden:
            raise ValueError(f"line {line_number}: forbidden fields {forbidden}")
        participant = str(row.get("participant_id", ""))
        cohort = str(row.get("cohort", ""))
        if (
            not OPAQUE.fullmatch(participant)
            or not OPAQUE.fullmatch(cohort)
            or row.get("consented") is not True
        ):
            raise ValueError(
                f"line {line_number}: consented opaque participant/cohort required"
            )
        if participant in participants:
            raise ValueError(f"line {line_number}: duplicate participant")
        participants.add(participant)
        index_date = parse_date(row.get("index_date"), "index_date")
        activity_values = row.get("activity_dates", [])
        if not isinstance(activity_values, list):
            raise ValueError(f"line {line_number}: activity_dates must be a list")
        activities = {parse_date(value, "activity") for value in activity_values}
        withdrawal = (
            parse_date(row["withdrawn_at"], "withdrawn_at")
            if row.get("withdrawn_at")
            else None
        )
        if withdrawal is not None and withdrawal < index_date:
            raise ValueError(f"line {line_number}: withdrawal predates index")
        cohorts[cohort].append({
            "index": index_date,
            "activities": activities,
            "withdrawal": withdrawal,
        })

    output_cohorts: dict[str, Any] = {}
    suppressed: list[str] = []
    for cohort, rows in sorted(cohorts.items()):
        if len(rows) < minimum_cohort:
            suppressed.append(cohort)
            continue
        window_results: dict[str, Any] = {}
        for window in windows:
            eligible = 0
            retained = 0
            for row in rows:
                target = row["index"] + timedelta(days=window)
                withdrawal = row["withdrawal"]
                if (
                    withdrawal_policy == "exclude_after_withdrawal"
                    and withdrawal is not None
                    and withdrawal <= target
                ):
                    continue
                eligible += 1
                if target in row["activities"]:
                    retained += 1
            if eligible < minimum_cohort:
                window_results[f"d{window}"] = {
                    "suppressed": True,
                    "minimum_cohort": minimum_cohort,
                }
            else:
                window_results[f"d{window}"] = {
                    "suppressed": False,
                    "eligible": eligible,
                    "retained": retained,
                    "rate": retained / eligible,
                    "ci95_wilson": wilson(retained, eligible),
                }
        output_cohorts[cohort] = {
            "participants": len(rows),
            "windows": window_results,
        }
    report = {
        "schema_version": 1,
        "report_kind": "phase4_retention",
        "analysis_status": "unreviewed",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
        "protocol_sha256": hashlib.sha256(args.protocol.read_bytes()).hexdigest(),
        "definition": {
            "activity_window": "exact_day",
            "windows_days": windows,
            "withdrawal_policy": withdrawal_policy,
            "minimum_cohort": minimum_cohort,
        },
        "cohorts": output_cohorts,
        "suppressed_cohorts": suppressed,
        "privacy": {
            "participant_rows_emitted": False,
            "browsing_or_recovery_content_emitted": False,
        },
        "review": {"approved": False, "reviewer": None, "reviewed_at": None},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote retention report for {len(participants)} consented participants: {args.output}")
    has_unsuppressed_window = any(
        window.get("suppressed") is False
        for cohort in output_cohorts.values()
        for window in cohort["windows"].values()
    )
    return 0 if has_unsuppressed_window else 3


if __name__ == "__main__":
    raise SystemExit(main())
