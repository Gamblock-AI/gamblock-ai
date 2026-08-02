#!/usr/bin/env python3
"""Fail-closed verifier for the accepted Phase 5 evidence package."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any


SHA256 = re.compile(r"^[a-f0-9]{64}$")
INCOMPLETE = re.compile(r"\b(REQUIRED|TBD|TODO|DRAFT ONLY)\b")
REQUIRED_ARTIFACTS = {
    "progress_report",
    "progress_report_approval",
    "progress_report_submission",
    "final_report",
    "final_report_approval",
    "final_report_submission",
    "prototype_release",
    "usage_guide",
    "limitations",
    "traceability_report",
    "social_account_ownership",
    "social_content_plan",
    "social_publication_archive",
    "social_access_continuity",
    "educational_video",
    "video_sources",
    "video_captions",
    "video_transcript",
    "video_review",
    "video_publication",
    "scientific_article",
}

JSON_KINDS = {
    "progress_report_approval": "phase5_artifact_approval",
    "progress_report_submission": "phase5_submission_record",
    "final_report_approval": "phase5_artifact_approval",
    "final_report_submission": "phase5_submission_record",
    "prototype_release": "phase5_prototype_release",
    "social_account_ownership": "phase5_social_ownership",
    "social_publication_archive": "phase5_social_archive",
    "video_review": "phase5_video_review",
    "video_publication": "phase5_publication_record",
}


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def completed_text(name: str, path: Path) -> list[str]:
    if path.suffix.lower() not in {".md", ".txt", ".vtt"}:
        return []
    try:
        value = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return [f"{name}: expected UTF-8 text"]
    failures: list[str] = []
    if len(value.strip()) < 200:
        failures.append(f"{name}: artifact is unexpectedly short")
    if INCOMPLETE.search(value):
        failures.append(f"{name}: incomplete marker remains")
    return failures


def validate_json(name: str, path: Path) -> list[str]:
    try:
        value: Any = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return [f"{name}: expected valid JSON"]
    if not isinstance(value, dict):
        return [f"{name}: JSON root must be an object"]
    failures: list[str] = []
    if value.get("schema_version") != 1:
        failures.append(f"{name}: schema_version must be 1")
    if name in JSON_KINDS and value.get("record_kind") != JSON_KINDS[name]:
        failures.append(f"{name}: record_kind is invalid")
    if INCOMPLETE.search(json.dumps(value)):
        failures.append(f"{name}: incomplete marker remains")
    if name.endswith("approval") or name in {"video_review"}:
        if value.get("approved") is not True:
            failures.append(f"{name}: approval is required")
    if name.endswith("submission") or name in {"video_publication"}:
        if not value.get("submitted_at") and not value.get("published_at"):
            failures.append(f"{name}: submission/publication date is required")
        if not value.get("receipt_or_url"):
            failures.append(f"{name}: receipt_or_url is required")
    if name == "prototype_release":
        if value.get("evaluated") is not True:
            failures.append("prototype_release: evaluated release is required")
        platforms = set(value.get("platforms", []))
        if platforms != {"android", "windows"}:
            failures.append("prototype_release: Android and Windows are required")
        if not value.get("version") or not value.get("release_url"):
            failures.append("prototype_release: version and release_url are required")
    if name == "social_account_ownership":
        accounts = value.get("accounts")
        if not isinstance(accounts, list) or not accounts:
            failures.append("social_account_ownership: verified accounts are required")
        elif any(
            not isinstance(item, dict)
            or item.get("ownership_verified") is not True
            or not item.get("continuity_owner")
            for item in accounts
        ):
            failures.append("social_account_ownership: ownership/continuity is incomplete")
    if name == "social_publication_archive":
        publications = value.get("publications")
        if not isinstance(publications, list) or not publications:
            failures.append("social_publication_archive: at least one publication is required")
        elif any(
            not isinstance(item, dict)
            or not item.get("url")
            or not item.get("published_at")
            or not SHA256.fullmatch(str(item.get("archive_sha256", "")))
            for item in publications
        ):
            failures.append("social_publication_archive: publication evidence is incomplete")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    if not args.manifest.is_file():
        parser.error(f"manifest not found: {args.manifest}")

    try:
        manifest: Any = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        parser.error(f"invalid manifest: {error}")
    if not isinstance(manifest, dict):
        parser.error("manifest root must be an object")

    failures: list[str] = []
    if manifest.get("schema_version") != 1:
        failures.append("schema_version must be 1")
    if manifest.get("phase") != "phase_5_finalization_reporting":
        failures.append("phase identifier is invalid")
    if manifest.get("status") != "complete":
        failures.append("status must be complete")
    for field in ("owner", "reviewer", "reviewed_at"):
        if manifest.get(field) in {None, "", "REQUIRED"}:
            failures.append(f"{field} is required")

    root = args.manifest.parent.resolve()
    phase4 = manifest.get("phase4_evidence")
    if not isinstance(phase4, dict):
        failures.append("phase4_evidence is required")
    else:
        if phase4.get("status") != "evaluated":
            failures.append("phase4_evidence: status must be evaluated")
        phase4_path = str(phase4.get("path", ""))
        phase4_hash = str(phase4.get("sha256", ""))
        if not SHA256.fullmatch(phase4_hash):
            failures.append("phase4_evidence: valid SHA-256 is required")
        else:
            candidate = (root / phase4_path).resolve()
            if not candidate.is_file() or file_hash(candidate) != phase4_hash:
                failures.append("phase4_evidence: file or SHA-256 is invalid")

    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, dict):
        failures.append("artifacts object is required")
        artifacts = {}
    missing = sorted(REQUIRED_ARTIFACTS - set(artifacts))
    if missing:
        failures.append(f"missing artifacts: {', '.join(missing)}")

    for name in sorted(REQUIRED_ARTIFACTS & set(artifacts)):
        item = artifacts[name]
        if not isinstance(item, dict):
            failures.append(f"{name}: descriptor must be an object")
            continue
        if item.get("approved") is not True:
            failures.append(f"{name}: reviewer approval is required")
        raw_path = str(item.get("path", ""))
        declared = str(item.get("sha256", ""))
        if not SHA256.fullmatch(declared):
            failures.append(f"{name}: valid SHA-256 is required")
            continue
        candidate = (root / raw_path).resolve()
        try:
            candidate.relative_to(root)
        except ValueError:
            failures.append(f"{name}: path must stay inside the Phase 5 package")
            continue
        if not candidate.is_file():
            failures.append(f"{name}: file not found")
            continue
        if file_hash(candidate) != declared:
            failures.append(f"{name}: SHA-256 mismatch")
            continue
        failures.extend(completed_text(name, candidate))
        if candidate.suffix.lower() == ".json":
            failures.extend(validate_json(name, candidate))

    if failures:
        print("Phase 5 evidence is incomplete:")
        for failure in failures:
            print(f"- {failure}")
        return 3
    print("Phase 5 evidence manifest verified: status=complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
