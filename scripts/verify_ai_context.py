#!/usr/bin/env python3
"""Validate portable AI context and cross-repository contracts."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

COMPONENTS = {
    "backend": ROOT / "gamblock-ai-backend",
    "website": ROOT / "gamblock-ai-website",
    "flutter": ROOT / "gamblock_ai_apps",
    "extension": ROOT / "browser_extension",
    "infrastructure": ROOT / "gamblock-ai-infrastructure",
    "model": ROOT / "gamblock-ai-model",
    "testing": ROOT / "gamblock-ai-testing",
}

COMPONENT_CONTRACTS = {
    "backend": (
        "proposal_authority",
        "privacy_boundary",
        "api_error_catalog",
        "protection_grant",
    ),
    "website": (
        "proposal_authority",
        "privacy_boundary",
        "api_error_catalog",
    ),
    "flutter": (
        "proposal_authority",
        "privacy_boundary",
        "websocket_loopback",
        "api_error_catalog",
        "protection_grant",
    ),
    "extension": (
        "proposal_authority",
        "privacy_boundary",
        "websocket_loopback",
    ),
    "infrastructure": (
        "proposal_authority",
        "privacy_boundary",
    ),
    "model": (
        "proposal_authority",
        "privacy_boundary",
    ),
    "testing": (
        "proposal_authority",
        "privacy_boundary",
        "testing_evidence",
    ),
}

ROOT_REQUIRED = (
    "AGENTS.md",
    "README.md",
    "CLAUDE.md",
    "GEMINI.md",
    ".github/copilot-instructions.md",
    ".github/workflows/context-integrity.yml",
    ".cursor/rules/gamblock-ai.mdc",
    "context/README.md",
    "context/manifest.yaml",
    "context/pkm_proposal.md",
    "context/architecture.md",
    "context/privacy-security.md",
    "context/research-evaluation.md",
    "context/testing-evaluation.md",
    "context/glossary.md",
    "repos.yaml",
    ".gitmodules",
    ".gitattributes",
    "scripts/bootstrap.sh",
    "scripts/verify-ai-context.sh",
    "scripts/verify_ai_context.py",
)

COMPONENT_REQUIRED = (
    ".gitattributes",
    "AGENTS.md",
    "README.md",
    "CLAUDE.md",
    "GEMINI.md",
    ".github/copilot-instructions.md",
    ".cursor/rules/gamblock-ai.mdc",
    "docs/ai/README.md",
    "docs/ai/manifest.yaml",
    "scripts/verify-ai-context.sh",
    ".agents/skills/verify-gamblock-change/SKILL.md",
    ".agents/skills/verify-gamblock-change/agents/openai.yaml",
)


def run(*args: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def git_repo(path: Path) -> bool:
    return run("git", "rev-parse", "--is-inside-work-tree", cwd=path).returncode == 0


def tracked(path: Path, relative: str) -> bool:
    return run("git", "ls-files", "--error-unmatch", relative, cwd=path).returncode == 0


def manifest_value(path: Path, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*([^#\s]+)", path.read_text())
    return match.group(1).strip("'\"") if match else None


def contract_version(path: Path, key: str) -> str | None:
    match = re.search(
        rf"(?m)^\s+{re.escape(key)}:\s*([1-9][0-9]*)\s*$",
        path.read_text(),
    )
    return match.group(1) if match else None


def backend_codes(path: Path) -> set[str]:
    return set(re.findall(r'(?m)^\s*"([a-z][a-z0-9_]*)"\s*:', path.read_text()))


def website_codes(path: Path) -> set[str]:
    text = path.read_text()
    match = re.search(r"export const MESSAGES[^=]*=\s*\{(.*?)\n\};", text, re.S)
    if not match:
        return set()
    return set(re.findall(r"(?m)^\s*([a-z][a-z0-9_]*)\s*:", match.group(1)))


def flutter_codes(path: Path) -> set[str]:
    return set(re.findall(r"case '([a-z][a-z0-9_]*)':", path.read_text()))


def emitted_backend_codes(component: Path) -> set[str]:
    codes: set[str] = set()
    for directory in (component / "internal/handler", component / "internal/middleware"):
        for path in directory.glob("*.go"):
            text = path.read_text()
            codes.update(
                re.findall(
                    r"(?:respondCode|respondErrorErr|respondError)\s*\("
                    r"\s*[^,]{1,200},\s*[^,]{1,200},\s*"
                    r'"([a-z][a-z0-9_]*)"',
                    text,
                    re.S,
                )
            )
    return codes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--allow-untracked",
        action="store_true",
        help="validate new authoring files before they are staged",
    )
    args = parser.parse_args()
    errors: list[str] = []

    for relative in ROOT_REQUIRED:
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing umbrella file: {relative}")
        elif not args.allow_untracked and git_repo(ROOT) and not tracked(ROOT, relative):
            errors.append(f"umbrella file is not tracked: {relative}")

    root_manifest = ROOT / "context/manifest.yaml"
    context_version = manifest_value(root_manifest, "context_version") if root_manifest.is_file() else None
    if not context_version:
        errors.append("context/manifest.yaml has no context_version")

    for name, component in COMPONENTS.items():
        if not component.is_dir():
            errors.append(f"missing component directory: {component.name}")
            continue
        for relative in COMPONENT_REQUIRED:
            path = component / relative
            if not path.is_file():
                errors.append(f"{name}: missing {relative}")
            elif not args.allow_untracked and git_repo(component) and not tracked(component, relative):
                errors.append(f"{name}: file is not tracked: {relative}")

        local_manifest = component / "docs/ai/manifest.yaml"
        if local_manifest.is_file():
            local_version = manifest_value(local_manifest, "context_version")
            if local_version != context_version:
                errors.append(
                    f"{name}: context_version {local_version!r} != umbrella {context_version!r}"
                )
            if manifest_value(local_manifest, "schema_version") != "1":
                errors.append(f"{name}: docs/ai manifest schema_version must be 1")
            for contract in COMPONENT_CONTRACTS[name]:
                expected_version = contract_version(root_manifest, contract)
                local_contract_version = contract_version(local_manifest, contract)
                if expected_version is None:
                    errors.append(f"umbrella manifest lacks contract {contract}")
                elif local_contract_version != expected_version:
                    errors.append(
                        f"{name}: contract {contract} version "
                        f"{local_contract_version!r} != umbrella {expected_version!r}"
                    )

        claude = component / "CLAUDE.md"
        if claude.is_file() and "@./AGENTS.md" not in claude.read_text():
            errors.append(f"{name}: CLAUDE.md must import @./AGENTS.md")
        gemini = component / "GEMINI.md"
        if gemini.is_file() and "@./AGENTS.md" not in gemini.read_text():
            errors.append(f"{name}: GEMINI.md must import @./AGENTS.md")
        cursor = component / ".cursor/rules/gamblock-ai.mdc"
        if cursor.is_file():
            cursor_text = cursor.read_text()
            has_agents_reference = "@AGENTS.md" in cursor_text or "@./AGENTS.md" in cursor_text
            if "alwaysApply: true" not in cursor_text or not has_agents_reference:
                errors.append(f"{name}: Cursor rule must always apply and reference @AGENTS.md")

        local_agents = component / "AGENTS.md"
        if local_agents.is_file():
            agents_text = local_agents.read_text()
            if "explicit" not in agents_text or "test" not in agents_text:
                errors.append(
                    f"{name}: AGENTS.md must document explicit opt-in tests"
                )

        skill = component / ".agents/skills/verify-gamblock-change/SKILL.md"
        if skill.is_file() and "Do not run tests, builds" not in skill.read_text():
            errors.append(f"{name}: verification skill must enforce lint-only default")

    root_claude = ROOT / "CLAUDE.md"
    root_gemini = ROOT / "GEMINI.md"
    if root_claude.is_file() and "@./AGENTS.md" not in root_claude.read_text():
        errors.append("umbrella CLAUDE.md must import @./AGENTS.md")
    if root_gemini.is_file() and "@./AGENTS.md" not in root_gemini.read_text():
        errors.append("umbrella GEMINI.md must import @./AGENTS.md")

    root_agents = ROOT / "AGENTS.md"
    if root_agents.is_file():
        agents_text = root_agents.read_text()
        if "context/pkm_proposal.md" not in agents_text or "primary authority" not in agents_text:
            errors.append("umbrella AGENTS.md must declare proposal-first authority")
        if "Do not run" not in agents_text or "tests, builds" not in agents_text:
            errors.append("umbrella AGENTS.md must enforce lint-only default")

    for relative in (
        "templates/global/codex-AGENTS.md",
        "templates/global/claude-CLAUDE.md",
        "templates/global/gemini-GEMINI.md",
        "templates/global/copilot-instructions.md",
        "templates/global/cursor-user-rules.txt",
    ):
        path = ROOT / relative
        if path.is_file():
            text = path.read_text().lower()
            if (
                "explicit" not in text
                or "typecheck" not in text
                or "test" not in text
                or "build" not in text
            ):
                errors.append(f"global template lacks lint-only policy: {relative}")

    requirements_path = ROOT / "context/proposal-requirements.md"
    if requirements_path.is_file():
        requirement_ids = set(
            re.findall(r"`(PKM-[A-Z]+-[0-9]{3})`", requirements_path.read_text())
        )
        context_ids: set[str] = set()
        for path in (ROOT / "context").rglob("*.md"):
            if path.name == "pkm_proposal.md":
                continue
            context_ids.update(
                re.findall(r"`(PKM-[A-Z]+-[0-9]{3})`", path.read_text())
            )
        unknown_ids = sorted(context_ids - requirement_ids)
        if unknown_ids:
            errors.append(
                "context references undefined proposal requirements: "
                + ", ".join(unknown_ids)
            )

        shorthand_pattern = re.compile(
            r"`(?:PKM-[^`\n]*(?:\*|/|\.\.)[^`\n]*|(?:WEB|SUP)-[^`\n]*\*[^`\n]*)`"
            r"|`(?:PKM|WEB)-[A-Z]+-[0-9]{3}`\s+(?:through|to)\s+"
            r"`(?:PKM|WEB)-[A-Z]+-[0-9]{3}`",
            re.IGNORECASE,
        )
        shorthand_files = [ROOT / "AGENTS.md", ROOT / "README.md"]
        shorthand_files.extend((ROOT / "context").rglob("*.md"))
        for component in COMPONENTS.values():
            shorthand_files.extend(
                [component / "AGENTS.md", component / "docs/ai/README.md"]
            )
        for path in shorthand_files:
            if path.name == "pkm_proposal.md" or not path.is_file():
                continue
            if shorthand_pattern.search(path.read_text()):
                errors.append(
                    "noncanonical requirement shorthand found: "
                    + str(path.relative_to(ROOT))
                )

        for name, component in COMPONENTS.items():
            reference_files = (
                component / "AGENTS.md",
                component / "docs/ai/README.md",
                component / "docs/ai/manifest.yaml",
            )
            component_ids: set[str] = set()
            for path in reference_files:
                if path.is_file():
                    component_ids.update(
                        re.findall(r"PKM-[A-Z]+-[0-9]{3}", path.read_text())
                    )
            unknown_component_ids = sorted(component_ids - requirement_ids)
            if unknown_component_ids:
                errors.append(
                    f"{name}: references undefined proposal requirements: "
                    + ", ".join(unknown_component_ids)
                )

    catalog_paths = {
        "backend": COMPONENTS["backend"] / "internal/i18n/messages.go",
        "website": COMPONENTS["website"] / "lib/messages.ts",
        "flutter": COMPONENTS["flutter"] / "lib/core/messaging/app_messages.dart",
    }
    if all(path.is_file() for path in catalog_paths.values()):
        catalogs = {
            "backend": backend_codes(catalog_paths["backend"]),
            "website": website_codes(catalog_paths["website"]),
            "flutter": flutter_codes(catalog_paths["flutter"]),
        }
        all_codes = set.union(*catalogs.values())
        for name, codes in catalogs.items():
            missing = sorted(all_codes - codes)
            extra = sorted(codes - catalogs["backend"]) if name != "backend" else []
            if missing:
                errors.append(f"{name}: missing error codes: {', '.join(missing)}")
            if extra:
                errors.append(f"{name}: codes absent from backend: {', '.join(extra)}")

        emitted = emitted_backend_codes(COMPONENTS["backend"])
        uncataloged = sorted(emitted - catalogs["backend"])
        if uncataloged:
            errors.append(
                "backend: emitted error codes absent from catalog: "
                + ", ".join(uncataloged)
            )

    forbidden_absolute = "/home/alfiang"
    text_candidates = [
        ROOT / "repos.yaml",
        COMPONENTS["infrastructure"] / "inventory/hosts.ini",
        COMPONENTS["infrastructure"] / "README.md",
        COMPONENTS["infrastructure"] / "AGENTS.md",
    ]
    for path in text_candidates:
        if path.is_file() and forbidden_absolute in path.read_text(errors="ignore"):
            errors.append(f"machine-specific absolute path found: {path.relative_to(ROOT)}")

    flutter_env = COMPONENTS["flutter"] / ".env"
    if git_repo(COMPONENTS["flutter"]) and tracked(COMPONENTS["flutter"], ".env"):
        errors.append("flutter: .env must not be tracked")
    if flutter_env.exists() and not (COMPONENTS["flutter"] / ".env.example").is_file():
        errors.append("flutter: .env exists without a tracked .env.example template")

    if errors:
        print("AI context verification failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"AI context verification passed (context_version={context_version})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
