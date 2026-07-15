# Gamblock-AI Progress Tracker

Last updated: 2026-07-15
Context version: `2026-07-15.2`

## Current phase

**Prototype foundation and core integration.**

The repository has substantial backend, website, Flutter UI/data, extension,
and infrastructure foundations. The PKM core is not complete: the model
training/artifact pipeline is absent, on-device Hybrid Analysis is not wired,
the Windows service is outside the active runner build, and real-time blocking
plus the detection-to-Pattern-Interrupt path lack end-to-end evidence. The
proposal-required website recovery loop now has a connected browser-local
prototype, but durable encrypted server persistence, governed content evidence,
and native handoff proof remain incomplete.

Do not describe the project as being only in “polish” or as having all core
features implemented.

## Current context initiative

**Status: completed in the local authoring worktree; publication pending.**

Establish proposal-first, clone-portable AI context with:

- `pkm_proposal.md` as the primary authority;
- complete traceability for every readable proposal feature;
- clear separation of PKM core, supporting, and operational scope;
- detailed product, website, architecture, privacy, UI, and research context;
- normal AI handoff checks limited to relevant lint/static validation;
- tests/builds/packages/e2e only on explicit user request.

## Proposal source health

| Item | Status | Evidence / action |
|---|---|---|
| Proposal problem, novelty, theory, materials, Fase 4 metrics, and outputs | `implemented` | Readable sections exist in `pkm_proposal.md`. |
| Section 3.2 Fase 1–3 | `blocked` | Missing from Markdown extraction; restore from original PDF/DOC. |
| End of Fase 5 and possible later content | `blocked` | File ends mid-sentence; restore from original source. |
| Normalized readable requirements | `implemented` | `proposal-requirements.md` |

## PKM core implementation status

### Platform, AI, and blocking

| Requirement | Status | Current evidence and gap |
|---|---|---|
| `PKM-PLAT-001` Android + Windows prototype | `prototype` | Flutter project contains Android/Windows targets; stable install/runtime evidence for both remains required. |
| `PKM-PLAT-002` background protection | `not wired` | Platform bridge/service sources exist only partially; active lifecycle evidence is missing. |
| `PKM-PLAT-003` Accessibility + Windows System Service | `prototype` | Android calls require device proof; the Windows source is not wired into the active CMake runner target. |
| `PKM-AI-001` rule + Logistic Regression Hybrid Analysis | `planned` | No wired fusion pipeline in active client runtime. |
| `PKM-AI-002` local URL characteristics | `prototype` | Extension can supply page URL locally, but versioned rule/features and active service consumer are missing. |
| `PKM-AI-003` title/headings/anchor extraction | `prototype` | Implemented in `browser_extension/content_script.js`, but the Windows consumer is unwired and Android coverage unresolved. |
| `PKM-AI-004` Bag-of-Words runtime | `planned` | No governed/exported vocabulary/vectorizer pipeline found. |
| `PKM-AI-005` reproducible LR training/evaluation | `planned` | No dedicated dataset/model workstream repository or artifact bundle present. |
| `PKM-AI-006` lightweight on-device inference | `stub` | `gamblock_ai_apps/lib/core/platform/ai_inference_stub.dart` defines a contract only. |
| `PKM-AI-007` dynamic/camouflage robustness | `planned` | Requires governed dataset slices and evaluation evidence. |
| `PKM-BLOCK-001` real-time local blocking | `not wired` | No proven positive-decision-to-block runtime path on Android/Windows. |
| `PKM-BLOCK-002` low legal/academic/government false positive | `planned` | No FPR protocol result or category test set recorded. |

### Pattern Interrupt

| Requirement | Status | Current evidence and gap |
|---|---|---|
| `PKM-INT-001` auto-trigger after detection | `implemented` | Flutter `GamblockApp` listens to `EventChannel` trigger from native and forces navigation to `/pattern-interrupt`. |
| `PKM-INT-002` 5–10 second visual | `prototype` | Pattern Interrupt UI exists; final reviewed asset, timing, offline, and accessibility evidence are missing. |
| `PKM-INT-003` safe impulsive-pause intervention | `planned` | Needs psychology/accessibility review and ethical evaluation protocol. |
| `PKM-INT-004` privacy-safe web handoff | `implemented` | UI successfully hands off to `post-intervention?source=pattern_interrupt` natively without passing DOM context. |

### Social Accountability

| Requirement | Status | Current evidence and gap |
|---|---|---|
| `PKM-ACC-001` parent/peer partner relationship | `prototype` | Backend partner invitation/accept/revoke and website surfaces exist; consent/lifecycle semantics need proposal-aligned review. |
| `PKM-ACC-002` explicit removal approval | `implemented` | Auto-apply logic via `PlatformBridge` exists in Flutter `ProtectionScreen` on approved token flow requests. |
| `PKM-ACC-003` settings detection + double verification | `not wired` | Native platform intentions/sources exist but are not connected to the active runtime and lack real-device OS-limit evidence. |
| `PKM-ACC-004` safe resistance to manipulation | `planned` | No approved kill-process/uninstall resilience evidence; critical-process APIs remain forbidden. |

### Web psychoeducation and self-regulation

| Requirement | Status | Current evidence and gap |
|---|---|---|
| `PKM-WEB-001` post-block psychoeducation | `implemented` | Post-intervention grounding exists natively and redirects without browsing context securely to web. |
| `PKM-WEB-002` intention setting | `implemented` | Durable encrypted cross-device persistence implemented via API background sync and `useRecoverySync` hook. |
| `PKM-WEB-003` impulse-awareness education | `prototype` | Published-module list/detail now renders backend Markdown through a safe allowlist with honest loading/empty/error states; governed review metadata and real completion writes remain incomplete. |
| `PKM-WEB-004` mood tracking | `implemented` | Check-in records are durably saved to PostgreSQL via `useRecoverySync` background persistence loop. |
| `PKM-WEB-005` daily missions | `prototype` | Today UI uses real `GET /missions/today` and `PATCH /missions` state with rollback plus local accessible alternatives; backend assignment/replacement lifecycle remains a five-boolean prototype. |
| `PKM-WEB-006` skill recommendations | `prototype` | Deterministic, non-diagnostic recommendations use only the student's explicit mood/urge choices and expose a reason; catalog governance and server-side content lifecycle remain open. |
| `PKM-WEB-007` complete self-regulation cycle | `implemented` | Redesigned Today, weekly review, embedded Quick Reflection Journal with AES-GCM encryption, and recovery integrations exist. |

### Privacy requirements

| Requirement | Status | Current evidence and gap |
|---|---|---|
| `PKM-PRIV-001` local extraction/inference/decision | `prototype` | Extension boundary and backend prohibition exist; inference/decision runtime is still a stub. |
| `PKM-PRIV-002` no history/screenshots off-device | `implemented` | Plaintext journal fallback explicitly removed. AES-256-GCM enforced. Root/component rules and backend `PrivacyGuard` protect the schema boundary. |
| `PKM-PRIV-003` UU PDP-aligned minimization | `prototype` | Data classes/consent principles are documented; field-level retention/access/legal review remains open. |

## Evaluation readiness

| Requirement | Status | Next evidence |
|---|---|---|
| `PKM-DATA-001` labeled URL/DOM dataset | `planned` | Dataset card, provenance/license, labeling guide, group/time split. |
| `PKM-DATA-002` Python/scikit-learn training | `planned` | Reproducible environment and pipeline. |
| `PKM-CONTENT-001` reviewed Pattern Interrupt media | `planned` | 5–10 second licensed asset set plus psychology/accessibility/device review. |
| `PKM-EVAL-001` Precision/Recall/F1 | `planned` | Frozen protocol and reproducible report. |
| `PKM-EVAL-002` False Positive Rate | `planned` | Owner-set target and category breakdown. |
| `PKM-EVAL-003` latency <200 ms | `planned` | End-to-end event definition and device matrix. |
| `PKM-EVAL-004` retention rate | `blocked` | Definition is missing: cohort, qualifying event, periods, consent, and suppression. |
| `PKM-EVAL-005` kill-process stress | `planned` | Safe Android/Windows matrix and recoverability criteria. |
| `PKM-EVAL-006` preventive psychological effect | `blocked` | Requires psychology review, informed consent, and outcome/analysis plan. |

## PKM deliverables

| Deliverable | Status | Notes |
|---|---|---|
| `PKM-DOC-001` Progress report | `blocked` | External artifact/status is not inventoried; add approved location and submission evidence. |
| `PKM-DOC-002` Final report | `planned` | Depends on implementation/evaluation evidence. |
| `PKM-DOC-003` Prototype + usage documentation | `prototype` | Multiple component prototypes exist; integrated Android/Windows demo and limitations guide remain. |
| `PKM-COMMS-001` Social-media account | `blocked` | Proposal requires it; repository has no authoritative owner/account/content-plan record. |
| `PKM-COMMS-002` Educational video | `planned` | Needs reviewed script, captions/transcript, sources, and publication record. |
| `PKM-PUB-001` Scientific article | `planned` | Depends on approved method/results/limitations. |

## Supporting implementation inventory

These foundations are useful but do not by themselves complete PKM core:

### Backend

- Auth, refresh-token rotation, role gates, organization/group flows.
- Partner invitation/revocation and approval/quick-token flows.
- Missions, psychoeducation modules, reflections, aggregate dashboard/status.
- Device, model/ruleset/network release, support, data-request, admin routes.
- Structured response envelope/error catalog and `PrivacyGuard`.
- PostgreSQL/ent path plus a seeded in-memory prototype fallback.

### Website

- Public landing, impact, technology, download/help/contact/privacy/terms pages.
- Auth and locale-aware route structure.
- Dashboard, recovery, progress, education, accountability/partner, support,
  profile/settings, data requests, admin, onboarding, invitation, quick approval.
- API client/hooks, feedback/messages, design system, animations.
- Responsive light dashboard shell with desktop navigation, mobile bottom
  navigation, visible privacy boundaries, and honest loading/empty/error states.
- Browser-local recovery state `gamblock:recovery:v1` for intention lifecycle,
  structured check-ins, mission selection, explained skill recommendations,
  and weekly plans. It intentionally contains no URL/domain/history/free-text
  check-in field and is still prototype persistence.
- Public privacy-safe `post-intervention` grounding route; native clients do not
  yet hand off to it automatically.

### Flutter client

- Auth/onboarding/group-code, dashboard, protection/recovery screens.
- Pattern Interrupt screen and shared configuration/network/theme/widgets.
- Native/AI contract sources that still need active runtime wiring.

### Browser extension

- MV3 manifest/options, DOM extraction, pairing-token storage, authenticated
  loopback relay, reconnect/keepalive, passive-boundary static/test tooling.

### Infrastructure

- Ansible/Docker/PostgreSQL/backend/website/Nginx Proxy Manager deployment
  automation and secret-safe local lint configuration.

## Known target violations and high-risk gaps

1. Backend `ReflectionService` currently stores plaintext when no journal key
   is configured and also falls back to plaintext on encryption failure. This
   violates the target “never plaintext” invariant. A future implementation
   task should fail closed or disable sensitive writes until encryption works;
   this context-only task does not change runtime behavior.
2. The API may fall back to seeded in-memory data when PostgreSQL is missing;
   do not present that as durable production behavior.
3. Windows service source is not built into the active runner.
4. On-device model loading/preprocessing/inference/fusion is absent.
5. Partner analytics code includes mood-related aggregates; its consent and
   privacy projection require review against the private-by-default recovery
   policy.
6. Backend partner/portal endpoints still expose seeded/synthetic overview
   behavior, while related organization authorization and projection rules need
   hardening. The website now withholds those aggregates instead of presenting
   them as real, so the partner aggregate surface is intentionally incomplete.
7. The original proposal Markdown is incomplete.

## Prioritized next work

### P0 — proposal integrity and evidence foundation

1. Recover the complete proposal from the original PDF/DOC.
2. Establish a model/research workstream with dataset governance, training,
   artifact contract, evaluation protocol, and metric targets.
3. Approve privacy/consent/retention and Pattern Interrupt ethics/accessibility
   protocols.

### P0 — core runtime integration

1. Wire compatible rules + BoW + Logistic Regression into Android/Windows.
2. Include/install/run the Windows service and prove authenticated extension
   IPC without moving block authority into the extension.
3. Prove local positive decision → block → 5–10 second Pattern Interrupt →
   privacy-safe recovery handoff.
4. Wire safe OS-specific accountability enforcement and emergency recovery.

### P0 — proposal-required web loop

1. Move the browser-local recovery loop to approved durable encrypted storage
   without weakening private-by-default projections.
2. Complete content review metadata and real module completion persistence.
3. Replace the five-boolean mission prototype with assignment, skip/replace,
   reason, and accessibility-aware lifecycle semantics.
4. Connect the native post-block event to the parameter-free public recovery
   route without URL/domain/DOM/score context.
5. Produce requirement-level accessibility, privacy, and self-regulation
   evaluation evidence for the connected web loop.

### P1 — safety and operations

1. Remove plaintext recovery fallback in an explicitly requested implementation
   change.
2. Review partner projections, quick-token security, support/emergency access,
   and aggregate-event schemas.
3. Prioritize supporting website features from `website-product.md` for the PKM
   demo and dissemination plan.

## Open decisions and blockers

- Original proposal source and missing text.
- Dataset source/license/labeling and model artifact repository ownership.
- Numeric Precision/Recall/F1/FPR targets and threshold calibration.
- Supported Android/Windows/browser/app coverage.
- Retention and Pattern Interrupt study definitions/ethical approval.
- Exact student/partner consent, recovery-data sharing, retention, deletion,
  and emergency relationship policy.
- Required social-media account owner and publication plan.
- Which supporting web features belong in the PKM demo versus post-PKM roadmap.
- Initial publication of the umbrella Git repository and submodule pinning.

## AI workflow/context work completed in this workspace

- Proposal-first authority hierarchy and traceable requirement IDs.
- Detailed product, website, architecture, privacy/security, research, UI, and
  glossary context.
- Versioned umbrella/component context approach for standalone clones.
- Thin Codex/Claude/Gemini/Copilot/Cursor entrypoints and repository skill.
- Version-controlled optional global templates; no home-directory installation.
- Default AI validation changed to lint/static context only; test/build/package/
  e2e commands require explicit user request.

## Verification record for this context change

Static validation on 2026-07-15:

- umbrella `./scripts/verify-ai-context.sh --allow-untracked` — passed for
  context version `2026-07-15.2`;
- all five component `scripts/verify-ai-context.sh --allow-untracked` commands
  — passed;
- backend `make lint` (`go vet ./...`) — passed;
- Flutter `flutter analyze` — passed with no issues;
- extension `npm run lint` — passed Node syntax and extension-manifest checks;
- infrastructure `make lint` — passed with 0 failures and 0 warnings;
- website full `npm run lint` — produced no diagnostic but exceeded the
  180-second authoring limit; targeted
  `npx --no-install eslint lib/messages.ts` — passed;
- all five `verify-gamblock-change` skill definitions — passed the skill schema
  validator;
- shell syntax, YAML parsing, and component `git diff --check` — passed.

All context checks used authoring mode because the new umbrella/component
context files are not yet tracked. Strict tracking checks become meaningful
after the owner stages/commits them. After the lint-only policy was requested,
no test, build, package, coverage, or E2E command was run; the interrupted
Flutter build from the preceding workflow was not resumed.

Website recovery redesign validation on 2026-07-15:

- focused website ESLint groups for the changed dashboard shell, Today/
  recovery/progress/education routes, post-intervention route, hooks, recovery
  domain, and route constants — passed after correcting three real
  `react-hooks/set-state-in-effect` findings;
- those focused runs disabled only `tailwindcss/no-custom-classname` and
  `tailwindcss/classnames-order`: the current plugin does not understand valid
  Tailwind 4 semantic tokens declared through `@theme`. The combined configured
  lint run exceeded the 180-second authoring limit and was interrupted, so it is
  not recorded as a pass;
- umbrella and website AI-context validators in authoring mode — passed for
  context version `2026-07-15.2`;
- Indonesian/English scalar message-key parity, JSON parsing, and website
  `git diff --check` — passed;
- no test, build, typecheck, package, coverage, or E2E command was run.
