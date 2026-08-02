#!/usr/bin/env python3
"""Aggregate an ethics-approved Pattern Interrupt study without clinical claims."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import statistics
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


OPAQUE = re.compile(r"^[A-Za-z0-9_-]{1,64}$")
ALLOWED_EVENT_CATEGORIES = {
    "none",
    "mild_distress",
    "moderate_distress",
    "severe_distress",
    "other_reviewed",
}
FORBIDDEN_KEYS = {
    "url", "domain", "dom", "title", "heading", "anchor", "history",
    "screenshot", "journal", "reflection", "mood", "urge", "free_text",
    "name", "email", "phone", "student_number",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mean_ci95(values: list[float]) -> list[float] | None:
    if len(values) < 2:
        return None
    margin = 1.959963984540054 * statistics.stdev(values) / math.sqrt(len(values))
    center = statistics.mean(values)
    return [center - margin, center + margin]


def summarize(rows: list[dict[str, Any]], minimum_group: int) -> dict[str, Any]:
    enrolled = len(rows)
    completed = [row for row in rows if row["completed"]]
    if enrolled < minimum_group:
        return {"suppressed": True, "minimum_group": minimum_group}
    if len(completed) < minimum_group:
        return {
            "suppressed": True,
            "minimum_group": minimum_group,
            "enrolled": enrolled,
            "completed": len(completed),
            "completion_rate": len(completed) / enrolled,
        }
    changes = [row["post_score"] - row["pre_score"] for row in completed]
    adverse = sum(row["adverse_event_category"] != "none" for row in rows)
    return {
        "suppressed": False,
        "enrolled": enrolled,
        "completed": len(completed),
        "completion_rate": len(completed) / enrolled,
        "mean_pre": statistics.mean(row["pre_score"] for row in completed)
        if completed else None,
        "mean_post": statistics.mean(row["post_score"] for row in completed)
        if completed else None,
        "mean_change": statistics.mean(changes) if changes else None,
        "mean_change_ci95_normal": mean_ci95(changes),
        "participants_with_adverse_event": (
            adverse if adverse == 0 or adverse >= minimum_group else None
        ),
        "adverse_event_count_suppressed": 0 < adverse < minimum_group,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--protocol", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    for path in (args.input, args.protocol):
        if not path.is_file():
            parser.error(f"file not found: {path}")
    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    if not isinstance(protocol, dict) or "REQUIRED" in json.dumps(protocol):
        parser.error("protocol must be completed and approved")
    if protocol.get("schema_version") != 1 or not protocol.get("approved_by"):
        parser.error("protocol schema/approval is invalid")
    conditions = protocol.get("conditions")
    if (
        not isinstance(conditions, list)
        or len(conditions) != 2
        or any(not OPAQUE.fullmatch(str(value)) for value in conditions)
    ):
        parser.error("protocol requires two opaque condition labels")
    instrument = str(protocol.get("primary_instrument_id", ""))
    if not OPAQUE.fullmatch(instrument):
        parser.error("primary instrument ID must be opaque")
    minimum_group = int(protocol.get("minimum_group", 0))
    score_min = float(protocol.get("score_min", 0))
    score_max = float(protocol.get("score_max", 0))
    if minimum_group < 10 or not score_max > score_min:
        parser.error("protocol minimum_group or score range is invalid")

    participants: set[str] = set()
    included: list[dict[str, Any]] = []
    withdrawn = 0
    for line_number, line in enumerate(
        args.input.read_text(encoding="utf-8").splitlines(), 1
    ):
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
        condition = str(row.get("condition", ""))
        event_category = str(row.get("adverse_event_category", "none"))
        if not OPAQUE.fullmatch(participant) or not OPAQUE.fullmatch(cohort):
            raise ValueError(f"line {line_number}: participant/cohort must be opaque")
        if participant in participants:
            raise ValueError(f"line {line_number}: duplicate participant")
        participants.add(participant)
        if row.get("consented") is not True:
            raise ValueError(f"line {line_number}: explicit research consent required")
        if condition not in conditions or event_category not in ALLOWED_EVENT_CATEGORIES:
            raise ValueError(f"line {line_number}: invalid condition/event category")
        if row.get("withdrawn") is True:
            withdrawn += 1
            continue
        completed = row.get("completed") is True
        pre_score = row.get("pre_score")
        post_score = row.get("post_score")
        if completed:
            if not isinstance(pre_score, (int, float)) or not isinstance(
                post_score, (int, float)
            ):
                raise ValueError(f"line {line_number}: completed rows require scores")
            if not score_min <= float(pre_score) <= score_max or not score_min <= float(
                post_score
            ) <= score_max:
                raise ValueError(f"line {line_number}: score outside protocol range")
        included.append({
            "cohort": cohort,
            "condition": condition,
            "completed": completed,
            "pre_score": float(pre_score) if completed else None,
            "post_score": float(post_score) if completed else None,
            "adverse_event_category": event_category,
        })
    if not participants:
        parser.error("study input is empty")

    by_condition: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_cohort_condition: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in included:
        by_condition[row["condition"]].append(row)
        by_cohort_condition[(row["cohort"], row["condition"])].append(row)
    condition_summary = {
        condition: summarize(by_condition.get(condition, []), minimum_group)
        for condition in conditions
    }
    cohort_summary: dict[str, Any] = {}
    for cohort in sorted({row["cohort"] for row in included}):
        cohort_summary[cohort] = {
            condition: summarize(
                by_cohort_condition.get((cohort, condition), []), minimum_group
            )
            for condition in conditions
        }
    first, second = conditions
    first_change = condition_summary[first].get("mean_change")
    second_change = condition_summary[second].get("mean_change")
    descriptive_difference = (
        first_change - second_change
        if isinstance(first_change, float) and isinstance(second_change, float)
        else None
    )
    event_totals = Counter(row["adverse_event_category"] for row in included)
    report = {
        "schema_version": 1,
        "report_kind": "phase4_pattern_interrupt",
        "analysis_status": "unreviewed",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "protocol_sha256": sha256(args.protocol),
        "input_sha256": sha256(args.input),
        "instrument_id": instrument,
        "participants_received": len(participants),
        "withdrawn_excluded": withdrawn,
        "conditions": condition_summary,
        "cohort_condition_slices": cohort_summary,
        "descriptive_mean_change_difference": {
            "first_condition": first,
            "second_condition": second,
            "first_minus_second": descriptive_difference,
        },
        "adverse_event_category_counts": {
            category: count
            for category, count in sorted(event_totals.items())
            if count >= minimum_group
        },
        "suppressed_adverse_event_category_count": sum(
            0 < count < minimum_group for count in event_totals.values()
        ),
        "interpretation": protocol.get("causality_limit"),
        "privacy": {
            "participant_rows_emitted": False,
            "free_text_emitted": False,
            "browsing_or_recovery_content_emitted": False,
        },
        "review": {"approved": False, "reviewer": None, "reviewed_at": None},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"Wrote Pattern Interrupt report for {len(participants)} participants: {args.output}")
    return 0 if descriptive_difference is not None else 3


if __name__ == "__main__":
    raise SystemExit(main())
