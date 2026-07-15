# Gamblock-AI Workspace

This is the umbrella workspace for Gamblock-AI, an on-device gambling blocker
and recovery platform for Indonesian university students. It coordinates five
independent component repositories while preserving shared product context and
cross-repository contracts.

## Repository model

The five components remain independently clonable and releasable:

| Directory | Repository | Purpose |
|---|---|---|
| `gamblock-ai-backend/` | `Gamblock-AI-Backend` | Go API and PostgreSQL persistence |
| `gamblock-ai-website/` | `Gamblock-AI-Website` | Next.js recovery and supervision web app |
| `gamblock_ai_apps/` | `Gamblock-AI-Apps` | Flutter Android/Windows protection client |
| `browser_extension/` | `Gamblock-AI-Browser-Extention` | Passive Chrome/Edge DOM sensor |
| `gamblock-ai-infrastructure/` | `Gamblock-AI-Infrastructure` | Ansible deployment automation |

The umbrella repository owns `context/`, `AGENTS.md`, workspace scripts, and
the pinned component composition in `.gitmodules`. Every component duplicates
the minimum safety and architecture context it needs under `docs/ai/`, so its
context does not disappear in a standalone clone.

## Clone the full workspace

Once this umbrella folder is published as a Git repository:

```sh
git clone --recurse-submodules https://github.com/Gamblock-AI/Gamblock-AI.git
cd Gamblock-AI
./scripts/bootstrap.sh --install
./scripts/verify-ai-context.sh
```

For an existing umbrella clone:

```sh
git submodule sync --recursive
git submodule update --init --recursive
./scripts/bootstrap.sh
```

Without `--install`, `bootstrap.sh` only synchronizes submodules and creates
missing local `.env` files from templates. `--install` also downloads component
dependencies. It never deploys, decrypts vaults, changes secrets, or mutates
remote systems.

## AI context entry points

| Agent | Version-controlled entry point |
|---|---|
| Codex and AGENTS-compatible agents | `AGENTS.md` |
| Claude Code | `CLAUDE.md` importing `AGENTS.md` |
| Gemini CLI | `GEMINI.md` importing `AGENTS.md` |
| GitHub Copilot | `.github/copilot-instructions.md` |
| Cursor | `.cursor/rules/gamblock-ai.mdc` |

Start with `context/README.md`; it defines the proposal-first authority order
and routes each task to only the context that is needed. The PKM proposal is
the product core. Derived documents normalize its requirements and clearly
label supporting/operational additions. Personal global defaults are templates
under `templates/global/` and are never installed automatically.

## Default AI validation

During normal AI-assisted development, run only the relevant component linter
or analyzer. After documentation, protocol, catalog, provider, or composition
changes, also run the umbrella context-integrity check:

```sh
./scripts/verify-ai-context.sh
```

During initial authoring, before new files are staged, use:

```sh
./scripts/verify-ai-context.sh --allow-untracked
```

Tests, builds, packaging, coverage, E2E, and composite full-verification
commands run only when the user explicitly asks for them in the current
conversation. CI may retain its automatic push/PR quality gates. The umbrella
validator checks context presence, provider adapters, shared version markers,
error-catalog parity, and obvious machine-specific paths; it is a static
context check, not a test/build trigger.

## First umbrella publication

This workspace has been initialized as a local umbrella Git repository, but no
files have been staged/committed and no umbrella remote has been created or
pushed by this workflow. The repository owner should review all component
worktrees, create the initial umbrella commit, ensure component directories are
recorded as submodule gitlinks, create the intended remote, and push it when
ready. No AI context depends on an uncommitted chat session, but a fresh clone
will receive it only after the relevant repositories are committed/published.
