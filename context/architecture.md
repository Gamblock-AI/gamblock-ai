# Architecture Context

## Document role

This document maps the PKM requirements in `proposal-requirements.md` to a
target technical architecture. It does not claim that every path is currently
wired. See `progress-tracker.md` and component `docs/ai/README.md` files for
implementation evidence.

Privacy/data details live in `privacy-security.md`; research and model
evaluation details live in `research-evaluation.md`.

## Repository topology

Gamblock-AI uses five independently releasable component repositories plus an
umbrella context repository:

| Repository directory | Stack | Primary responsibility |
|---|---|---|
| `gamblock_ai_apps/` | Flutter + Android/Windows native code | Local protection authority, Pattern Interrupt, device/accountability integration |
| `browser_extension/` | Chrome/Edge MV3 JavaScript | Passive Windows browser DOM/URL sensor over authenticated loopback IPC |
| `gamblock-ai-website/` | Next.js 16, React 19, TypeScript | Web psychoeducation/self-regulation, accountability UI, public/ops surfaces |
| `gamblock-ai-backend/` | Go + Gin + ent + PostgreSQL | Identity, relationships, approvals, recovery state/content, aggregate APIs, release metadata |
| `gamblock-ai-infrastructure/` | Ansible + Docker + Nginx Proxy Manager | Backend/website delivery and database infrastructure |
| umbrella root | Context, composition, validators | Proposal-first shared governance and cross-repository contracts |

Each component keeps a self-contained `AGENTS.md` and `docs/ai/` snapshot so a
standalone clone retains its safety boundaries. See ADR-0001.

The proposal also requires a model/research workstream (dataset, Python/
scikit-learn training, vectorizer/model artifact, evaluation). It currently
has no dedicated repository in this workspace; this is a core gap, not “out of
scope”.

## Architecture principles

1. **Proposal-first:** the architecture must cover every registered PKM core
   requirement; supporting services cannot substitute for the local core loop.
2. **Local protection authority:** sensing inputs, feature extraction,
   inference, rule/model decision, block, and Pattern Interrupt stay on device.
3. **Explicit trust boundaries:** loopback IPC is authenticated; server APIs
   accept only declared non-browsing schemas.
4. **Offline-first core:** blocking/intervention cannot depend on backend or
   website availability.
5. **Safe resistance:** anti-uninstall uses supported OS mechanisms and remains
   recoverable; never mark a process critical.
6. **Evidence over presence:** a file, route, screen, schema, or C++ prototype
   does not prove end-to-end runtime behavior.
7. **Versioned artifacts/contracts:** model, vocabulary, preprocessing, URL
   rules, threshold, protocol, media, API error codes, and content have
   compatible versions and rollback paths.

## Target system flow

```text
Android supported local surface       Windows Chrome/Edge page
  Accessibility/native sensor           MV3 passive extension
             |                              |
             |                      authenticated loopback WS
             +--------------+---------------+
                            v
                 local protection runtime
             normalize/limit supported inputs
              /                           \
     URL rule/features             DOM title/headings/anchors
                                          |
                                   Bag-of-Words vectorizer
                                          |
                                 Logistic Regression score
              \                           /
                  versioned hybrid decision
                            |
                local block + aggregate counter
                            |
              5–10 second Pattern Interrupt
                            |
             privacy-safe recovery web handoff
                            v
    intention -> self-monitor -> evaluate -> adjust

Accountability removal path (separate from browsing path):
native settings/uninstall signal -> approval request -> partner decision
-> client receives approved/denied/expired state -> controlled action
```

## Hybrid detection pipeline

This pipeline maps `PKM-AI-001`, `PKM-AI-002`, `PKM-AI-003`, `PKM-AI-004`,
`PKM-AI-005`, `PKM-AI-006`, and `PKM-AI-007`.

### 1. Input acquisition

- URL characteristics and required DOM text are acquired only on supported
  surfaces.
- DOM contract includes page title, headings, and anchor text.
- Sensors cap input length/rate, normalize safely, and never execute page text.
- Windows extension relays only to the paired loopback service. Android uses
  the platform bridge/accessibility path available to the prototype.
- Publish a coverage matrix for browsers/apps and known blind spots.

### 2. Deterministic preprocessing

The training and runtime implementations share versioned rules for Unicode,
case, tokenization, whitespace, feature limits, vocabulary, and unknown terms.
The runtime must reject incompatible artifacts rather than silently changing
feature order.

### 3. Rule and model branches

- Rule branch evaluates explicit URL characteristics/patterns locally.
- Model branch vectorizes DOM text using the exported Bag-of-Words vocabulary
  and applies Logistic Regression locally.
- The fusion policy defines precedence, score normalization, exception/safe
  rule behavior, threshold, and ambiguous/error fallback.
- The current `0.72` threshold is a calibratable engineering baseline. It is
  not hard-coded as a permanent product requirement.

### 4. Decision and action

- A positive hybrid decision is consumed by the native client/service, never
  the extension or backend.
- A negative/uncertain/internal-error decision follows a documented safe
  fallback and is available to local diagnostics without exposing content.
- Local aggregate counters may be queued for later sync under the allowed
  aggregate schema; the page context is discarded.

## Android target flow

This flow maps `PKM-PLAT-001`, `PKM-PLAT-002`, and `PKM-PLAT-003`.

1. User sees transparent setup and grants the required Accessibility/other
   supported permission.
2. Background runtime observes only the declared supported local signals.
3. Runtime invokes the version-compatible Hybrid Analysis artifacts.
4. Positive decision invokes supported blocking/overlay/navigation behavior.
5. Native Flutter route presents Pattern Interrupt and optional recovery link.
6. Settings/uninstall interaction invokes the accountability state machine.
7. Service lifecycle recovers through documented Android mechanisms.

Real-device evidence is required for each step. Flutter UI/method-channel code
alone is a prototype, not proof that Android protection is active.

## Windows target flow

This flow maps `PKM-PLAT-001`, `PKM-PLAT-002`, and `PKM-PLAT-003`.

1. A LocalSystem Windows service is installed through a transparent, signed
   setup path and configured with normal SCM recovery.
2. The Chrome/Edge extension reads supported page fields and authenticates to
   `ws://127.0.0.1:9090` using a local pairing token.
3. Service validates schema/type/size/rate and executes Hybrid Analysis.
4. The service/native client performs the block and invokes Pattern Interrupt.
5. Service state is surfaced to Flutter without giving Flutter web content.
6. Removal/stop requests use the accountability workflow and safe recovery.

The extension never receives block commands and never closes/redirects tabs.
The current Windows service source is a prototype and must be included in the
active build/install/runtime path before claiming this flow is implemented.

## Pattern Interrupt and recovery handoff

This flow maps `PKM-INT-001`, `PKM-INT-002`, `PKM-INT-003`, and
`PKM-INT-004`.

- Trigger comes from a local positive decision.
- Media metadata and assets are versioned, integrity-checked, licensed, and
  cached locally so the intervention works offline.
- Standard duration is 5–10 seconds with reduced-motion/non-visual accessible
  behavior.
- Interruption copy is supportive and non-clinical.
- Recovery handoff contains only an intent/source category such as
  `post_intervention`; it contains no detected URL, DOM, score, or fingerprint.
- If website/auth is unavailable, show a local grounding/help action and allow
  later recovery entry.

## Social Accountability state machine

This state machine maps `PKM-ACC-001`, `PKM-ACC-002`, `PKM-ACC-003`, and
`PKM-ACC-004`.

```text
no_partner -> invite_pending -> active
     ^             |             |
     |             v             +-> removal_requested
     +---------- expired                |
                                       +-> approved -> bounded removal window
                                       +-> denied
                                       +-> expired
                                       +-> cancelled
                                       +-> emergency_review (audited)
active -> paused/revoked/replaced according to approved relationship policy
```

Rules:

- both parties understand and accept the relationship;
- partner may be a parent or peer;
- approval is explicit, scoped to one request/device/action, expiring, and
  auditable;
- a WhatsApp deep link is only a delivery mechanism for a backend token;
- native client validates authoritative request state before allowing action;
- offline/unavailable behavior is defined without silently bypassing approval;
- emergency recovery is least-privilege and cannot be the routine shortcut;
- Accessibility/SCM resistance stays within OS limits and remains recoverable.

## Web recovery architecture

This architecture maps `PKM-WEB-001`, `PKM-WEB-002`, `PKM-WEB-003`,
`PKM-WEB-004`, `PKM-WEB-005`, `PKM-WEB-006`, and `PKM-WEB-007`.

Next.js pages consume typed hooks, which call the single API client and the Go
response envelope. Core recovery services model:

- intention lifecycle;
- mood/urge check-in;
- psychoeducation content/progress;
- daily mission assignment/state/reflection;
- skill recommendations and explanation;
- weekly self-regulation review.

These are student-private by default. Partner projections are separate,
aggregate read models, not reuse of private student API responses. See
`website-product.md` for surface behavior.

## Backend boundaries and conventions

### Layering

`cmd/* -> internal/api -> internal/routes -> internal/handler ->
internal/service -> internal/repository -> ent/PostgreSQL`

- handlers parse/validate and produce `{ data, error, request_id }`;
- services own business rules/transactions/state machines;
- repositories own persistence;
- domain types live in `internal/model/`;
- every route is registered in `internal/routes/routes.go`.

### Server responsibilities

- identity/auth/RBAC and consent;
- partner/group relationship and approval state;
- published psychoeducation/missions/skills and student recovery state;
- encrypted sensitive reflections/journal;
- privacy-safe aggregate events and device health;
- support/data requests, content/release metadata, operational audit.

### Server prohibitions

- URL/domain/DOM/history/screenshot/app/window/search-query ingestion;
- remote model inference on browsing content;
- per-page score/feature storage;
- partner/admin access to raw recovery content by default;
- technical error detail or sensitive payload in production responses/logs.

`PrivacyGuard` rejects forbidden field names. Its existence complements, but
does not replace, allowlisted request schemas and code review.

## Storage model

| Store | Target data | Important boundary |
|---|---|---|
| Device local | model/vectorizer/rules/media, pairing token, protection state, offline aggregate queue | Detection data stays here; encrypt/protect credentials; bounded retention. |
| PostgreSQL | accounts, consent/relationships, approvals, recovery content/state, encrypted text, aggregate events, release/support/audit data | No browsing schema; field-level purpose/retention/access documented. |
| `chrome.storage.local` | local pairing token and connection configuration | No remote sync/telemetry; token not logged. |
| Research storage (future/approved) | governed labeled dataset and pseudonymous study data | Separate access, consent, retention, license, and publication policy. |

The backend's seeded in-memory fallback is current prototype behavior, not a
production persistence guarantee.

## Authentication and API contracts

- JWT access token + rotating refresh token for normal sessions.
- Backend RBAC is authoritative.
- Website token cookie/middleware and Flutter Bearer client are consumers, not
  substitutes for backend checks.
- Quick approval uses a high-entropy, expiring, single-use scoped token.
- API stable error codes remain synchronized across backend, website, Flutter.
- Client-facing API changes update all available consumers and document absent
  repository follow-ups.

## Model and rules lifecycle

```text
governed dataset -> train/validate -> freeze test -> evaluate/calibrate
-> export model + vectorizer + preprocessing + rules + threshold metadata
-> sign/hash -> staged client rollout -> local compatibility check
-> aggregate health monitoring -> rollback/re-evaluate
```

The model artifact is not independent of its vocabulary and preprocessing.
Release metadata includes schema version, supported client versions, artifact
hash/signature, evaluation reference, rollout/rollback information, and known
limitations. Training belongs in the PKM scope even if delivered from a future
dedicated repository.

## Degraded and failure behavior

- Backend unavailable: local block/Pattern Interrupt continue; permitted
  aggregates/approval polling queue with bounded retry.
- Website unavailable: local recovery/help fallback; do not weaken protection.
- Extension disconnected: Windows shows degraded sensor status; do not claim
  coverage or upload data elsewhere.
- Model/rules incompatible/corrupt: reject artifact, retain known-good version,
  report privacy-safe health state.
- Partner unavailable: keep defined pending state and offer audited support/
  emergency procedure; no hidden automatic approval.
- False positive: provide safe exit/report/help path and collect only locally
  redacted/explicitly consented evidence.
- Permission removed/service stopped: display transparent health status and
  follow approved accountability/setup recovery.

## Current known target-versus-runtime gaps

At context version `2026-07-15.2`:

- Flutter exposes an AI inference contract stub but does not load/run the
  proposal-required model pipeline.
- Windows service/WebSocket source is not in the active runner build target.
- Extension DOM extraction/loopback relay exists, but end-to-end Windows
  protection depends on the unwired service.
- Pattern Interrupt UI exists, but local detection-to-intervention wiring needs
  proof.
- Several web/backend recovery and accountability supporting surfaces exist;
  the full proposal-mandated intention/impulse/mood/mission/skill loop and
  privacy-safe post-block handoff need requirement-level evidence.
- No dedicated governed model-training/dataset pipeline is present in the
  workspace.

Do not remove these gaps from architecture language until the tracker records
the runtime/evaluation evidence.

## Engineering conventions

- Backend layering as above; ent schema changes use generation, never hand-edit
  generated files.
- Flutter feature-first clean architecture: `domain/`, `data/`,
  `presentation/`; presentation does not call Dio directly.
- Website App Router; hooks call `lib/api-client.ts`; pages/components do not
  scatter raw authenticated `fetch()` calls.
- Configuration through committed examples and typed config modules; secrets
  remain gitignored/encrypted.
- One component/widget per file where component rules require it; generated
  UI primitives remain protected.

Default AI completion runs only the relevant linter/analyzer and context
validator. Tests/builds do not become architecture evidence unless the user
explicitly requested and they were actually run.
