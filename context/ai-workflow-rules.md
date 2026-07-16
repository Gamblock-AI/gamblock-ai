# AI Development Workflow Rules

## Objective

Leave enough version-controlled context that a fresh developer or AI agent can
continue from either the umbrella workspace or a standalone component clone
without relying on chat history. Keep the workflow lightweight during normal
development: lint/static context validation is the default; tests and builds
are explicit opt-in actions.

## 1. Load authority before implementation

1. Read the root and closest component `AGENTS.md` files.
2. Read `context/README.md` and the relevant proposal sections.
3. Use `proposal-requirements.md` to identify applicable registered PKM
   requirement
   IDs and supporting/domain documents.
4. Read the affected component's `docs/ai/README.md` to distinguish target
   behavior from current capability.
5. Inspect `git status` in every repository in scope. Existing modifications,
   untracked files, and deletions belong to the user unless proven otherwise.
6. Inspect adjacent implementation and documentation before proposing a change.

`pkm_proposal.md` is protected source material. Do not edit it to match code,
fill missing OCR/extraction content from imagination, or promote a supporting
feature into the proposal. Academic edits require an explicit request and
reliable owner-provided source.

## 2. Resolve conflicts by source class

Use this conflict order:

1. proposal for academic intent and PKM core requirements;
2. normalized requirement IDs for traceability;
3. product/domain context for approved derived design;
4. component status documentation and code for current-state evidence;
5. component instructions for local engineering conventions.

When current code conflicts with the proposal target, do not pretend either
one does not exist. Preserve the proposal requirement, label the code state
(`implemented`, `prototype`, `stub`, `not wired`, `planned`, `blocked`), and
record the gap/open decision.

## 3. Classify scope before adding a feature

Every feature is one of:

- `PKM core` — cite one or more exact PKM requirement IDs;
- `supporting product` — assign or retain an exact supporting/domain ID and
  explain which
  core outcome it helps;
- `operational` — administration/delivery/evidence capability with least
  privilege and no expansion of proposal claims.

Supporting website features may be extensive, but they may not weaken privacy,
replace a proposal feature, or silently outrank unfinished P0 core work.

Keep one coherent behavior or contract per change unit. Split unrelated API,
UI, native-service, infrastructure, and cleanup work unless they implement one
explicit cross-component contract.

## 4. Implement inside non-negotiable boundaries

- All browsing-content sensing, features, inference, and decisions stay on
  device.
- Raw URL/domain/DOM/history/screenshot/app/window/search data never enters the
  backend, website analytics, logs, or partner/admin views.
- The extension remains a passive local sensor only.
- Blocking and Pattern Interrupt authority stays with Android/Windows.
- Anti-uninstall uses safe OS-supported mechanisms; never critical-process APIs.
- Recovery-sensitive text stays private by default and follows encryption/
  access rules.
- Preserve response-envelope, error-catalog, IPC, and artifact-version
  contracts.
- Do not edit generated/protected files directly.
- Do not add production dependencies, change secrets, deploy, release, push,
  publish, decrypt vaults, or mutate external systems without explicit user
  authorization.
- Patch only task-owned lines in a dirty worktree; never discard unrelated
  changes or user deletions.

## 5. Default verification: lint only

At the end of a normal development prompt, run only the narrowest relevant
linter/analyzer. If AI context changed, also run the relevant context-integrity
validator. Do not run tests, builds, packaging, coverage, end-to-end suites, or
composite “full verify” commands unless the user explicitly asks for them in
the current conversation.

| Scope | Default AI check |
|---|---|
| Umbrella/context-only | `./scripts/verify-ai-context.sh --allow-untracked` |
| Backend | `make lint` |
| Website | `npm run lint -- <changed-source-files>` |
| Flutter | `flutter analyze` |
| Browser extension | `npm run lint` (syntax + manifest/static validation; not ESLint) |
| Infrastructure | `make lint` |

Rules:

- Run only commands relevant to touched files/components.
- A context validator is required when instructions, manifests, adapters,
  snapshots, or shared contracts change.
- Do not substitute an unrelated test/build merely because a repository lacks
  a linter; add or document a safe static check as a separate workflow change.
- Typecheck, unit/integration tests, race tests, builds, APK/Windows builds,
  Playwright, packaging/smoke tests, Ansible syntax/check mode, coverage, and
  release verification are opt-in.
- “Finish”, “verify”, or “definition of done” in older docs is not permission
  to run tests/builds; this policy wins. A user must explicitly request the
  extra category in the current conversation.
- When explicitly requested, run only the requested relevant checks and report
  exact commands/results. Never describe an unrun command as passing.
- If a linter cannot run, report the concrete environment/permission/tooling
  limitation. Do not run a test or build as a fallback.

### CI distinction

Repository CI may continue to run tests and builds automatically on push,
pull-request, or release events. This local AI policy does not weaken CI. It
also does not authorize the AI to push or open a PR merely to trigger CI.

## 6. Preserve durable context

Update documentation in the same change when reality changes:

| Change | Durable context |
|---|---|
| Proposal scope/claim | owner-authorized proposal edit, `proposal-requirements.md`, affected domain docs |
| Product scope/supporting feature | `project-overview.md` / `website-product.md` |
| Architecture/trust/data boundary | `architecture.md`, `privacy-security.md`, ADR when long-lived |
| Model/dataset/metrics | `research-evaluation.md` and affected component status |
| UI behavior/system | `ui-context.md` |
| Commands/paths/conventions | closest `AGENTS.md`, README, component `docs/ai/` |
| Capability state/evidence | affected component `docs/ai/README.md` |
| Shared workflow/contract | context version, manifest, component snapshots, provider adapters/skills |

Update affected component status after a meaningful capability, scope,
architecture, workflow, evidence, or blocker change—not after formatting-only
edits. Record dates and exact evidence; avoid brittle file/test counts.

## 7. Cross-repository coordination

For one shared contract, use this dependency order where applicable:

1. proposal/requirement and shared contract;
2. backend/shared state model;
3. website/Flutter/extension consumers;
4. infrastructure;
5. status/context validation.

This is sequencing guidance, not authorization to touch every repository. A
standalone clone may not have siblings. In that case, record the sibling URL,
exact file/contract/version, required change, and default lint command.

Mandatory coordination examples:

- WebSocket shape: extension implementation/README and Windows service.
- Stable API error code: backend, website, Flutter catalogs.
- Client-facing endpoint: backend registration and available consumers.
- Website page/access route: `routes.ts` and active middleware.
- ent schema: generate through the supported command; never hand-edit output.
- Browsing-related payload: redesign as a non-reconstructive aggregate; do not
  coordinate a raw field into multiple clients.

## Protected files and material

- `context/pkm_proposal.md` without explicit academic-owner/source request.
- Website `components/ui/*` unless the task explicitly targets generated UI
  primitives.
- Backend generated `ent/` output; use the generator.
- Generated localization/artifact files except through their generator.
- `.env`, credentials, keystores, decrypted vaults, pairing/approval tokens,
  local databases, dependency caches, and build outputs.
- Third-party dependency internals.

## Handoff checklist

- [ ] Proposal/core/supporting/operational scope is labeled and requirement IDs are cited.
- [ ] Current status is evidence-based and separate from target architecture.
- [ ] Privacy, passive-extension, encryption, accountability, and safe anti-tamper boundaries remain intact.
- [ ] Relevant API/error/IPC/artifact/route contracts are synchronized or named as follow-up.
- [ ] Relevant README, `AGENTS.md`, `docs/ai/`, domain context, and tracker match reality.
- [ ] Only the relevant linter/analyzer and context validator were run by default.
- [ ] Tests/builds/packages/e2e are reported only if the user explicitly requested and they actually ran.
- [ ] No unrelated user change/deletion was overwritten.
- [ ] No unauthorized external mutation, secret access, deploy, release, commit, or push occurred.
