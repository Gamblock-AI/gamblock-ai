# Gamblock-AI Umbrella Agent Rules


This workspace coordinates six independent product repositories plus one
testing repository. The umbrella
repository owns shared product context, cross-repository contracts, and
workspace validation. Every component repository also carries a self-contained
`AGENTS.md` so a standalone clone remains safe to work on.

## Start here

1. Read `context/README.md` and follow its proposal-first, task-based routing.
2. Read the relevant section of `context/pkm_proposal.md` for any product or
   implementation task.
3. Load the relevant domain context (`architecture.md`, `privacy-security.md`,
   or `research-evaluation.md`).
4. Before reading or changing a component, read that component's `AGENTS.md`.
   Starting an agent from this root does not automatically load descendant
   instructions.
5. Inspect the relevant repository's `git status` before editing. Preserve
   unrelated user changes and never use blanket cleanup commands.

`context/pkm_proposal.md` is the primary authority for PKM intent and core
features. It is protected academic source material: do not rewrite it to match
code or invent its missing extracted sections. Supporting features must be
labeled and may not displace proposal requirements.

Do not rely on instruction-file precedence to resolve contradictions. If root,
component, README, context, tests, and implementation disagree, stop the
affected change, establish current behavior from code/tests, preserve the
proposal's target intent, and record the gap in durable documentation. Code
does not override a PKM core requirement.

## Repository topology

| Component         | Directory                     | Default AI lint/static check             |
| ----------------- | ----------------------------- | ---------------------------------------- |
| Backend           | `gamblock-ai-backend/`        | `make lint`                              |
| Website           | `gamblock-ai-website/`        | `npm run lint -- <changed-source-files>` |
| Flutter client    | `gamblock_ai_apps/`           | `flutter analyze`                        |
| Browser extension | `browser_extension/`          | `npm run lint`                           |
| Infrastructure    | `gamblock-ai-infrastructure/` | `make lint`                              |
| Model             | `gamblock-ai-model/`          | *(no lint configured)*                   |
| Testing           | `gamblock-ai-testing/`        | `python3 orchestration/scripts/verify_public_evidence.py` |

Use `repos.yaml` for repository URLs and `context/manifest.yaml` for the
versioned context contract. A component may be cloned alone; never assume a
sibling checkout exists. Cross-repository test orchestration and its public
summary belong to `gamblock-ai-testing`; product components retain their own
source code and unit tests. For a cross-repository change, update each
available repository independently and report any sibling that still needs a
matching change.

## Non-negotiable product invariants

### Privacy by design

All classification and inference run on-device. Raw DOM text, URLs, domains,
screenshots, and browsing history never leave the device. The backend accepts
aggregate protection events, system-generated blocked-event timestamps
(metadata about when a block fired; never URL/domain/content), and LLM
personalization that uses only the SPK decision plus the user's self-reported
context. Students control the SPK recommendation and each data category
(protection/recovery/personal) plus LLM personalization through per-category
toggles on the Settings page; toggles govern usage, never storage. Do not
weaken `PrivacyGuard`, widen the blocked-timestamp scope to any other browsing
data, or send blocked-event timestamps or raw data to the LLM.

### Passive browser extension

The extension only extracts permitted DOM text and relays it over an
authenticated loopback WebSocket. It never classifies, blocks, redirects,
closes tabs, or renders Pattern Interrupt. Blocking authority belongs to the
Android/Windows client.

### Safe anti-tamper

Android uses Accessibility Service and Windows uses a LocalSystem service with
SCM recovery. Never use `RtlSetProcessIsCritical` or any critical-process
mechanism; it can crash the operating system.

### Encrypted recovery data

Journal/reflection text is encrypted with AES-256-GCM before persistence.
Never log or store journal plaintext outside the encrypted workflow.

### Error catalog synchronization

Stable API error codes must exist in all three catalogs:

- `gamblock-ai-backend/internal/i18n/messages.go`
- `gamblock-ai-website/lib/messages.ts`
- `gamblock_ai_apps/lib/core/messaging/app_messages.dart`

Run `./scripts/verify-ai-context.sh` from this root after changing a catalog.

## Cross-repository changes

- WebSocket message shape: update the extension implementation and README,
  Windows service implementation, relevant tests, and contract documentation.
- Backend API endpoint: register it in `internal/routes/routes.go`, document the
  envelope, and update consuming website/Flutter clients if applicable.
- Website page route or access policy: update `routes.ts` and the active Next.js
  route-protection mechanism when applicable. This does not apply to every
  backend API endpoint.
- ent schema: use the backend `make generate` target; never hand-edit generated
  ent output.
- New browsing-related payload field: do not send it. Redesign the contract to
  use a privacy-preserving aggregate.

## Change workflow

- Work in one verifiable feature unit. Split unrelated components or system
  boundaries.
- Confirm whether a capability is `implemented`, `stub`, `not wired`, or
  `planned` (or `prototype`/`blocked`); never promote a target-state statement
  into an implementation claim without evidence.
- Put stable behavior and decisions in context/architecture docs. Keep current
  status and evidence in the affected component's `docs/ai/README.md`.
- Update the affected component `README.md`, `AGENTS.md`, and `docs/ai/` when
  commands, paths, architecture, or capability status change.
- At the end of normal development work, run only the narrowest relevant
  linter/analyzer and the context validator when context changed. Do not run
  tests, builds, packaging, coverage, end-to-end suites, or composite full
  verification unless the user explicitly requests them in the current
  conversation. If a lint check cannot run, report the exact command/reason;
  do not replace it with a test or build.
- Infrastructure deploys, vault operations, remote writes, releases, pushes,
  and secret changes always require explicit user authorization. Local lint is
  allowed by default; syntax/check-mode validation is opt-in, and any command
  that contacts a configured host also requires external-contact approval.

## Protected files and generated output

- Do not edit website `components/ui/*` unless explicitly requested; those are
  generated shadcn primitives.
- Do not edit `context/pkm_proposal.md` without an explicit academic-source
  request from the proposal owners.
- Do not hand-edit backend generated `ent/` files.
- Do not edit `.env` or plaintext secret files. Update `.env.example` instead.
- Do not commit generated binaries, build outputs, coverage, dependency caches,
  decrypted vault material, or machine-specific credentials.

## Documentation language

Use English for code and identifiers. Durable technical documentation may use
English while proposal-facing material may remain in Bahasa Indonesia; keep
terms aligned through `context/glossary.md`. Respond to the user in their
language unless they request otherwise.
