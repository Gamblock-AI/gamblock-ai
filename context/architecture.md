# Architecture Context

## Document role

This document maps the PKM requirements in `proposal-requirements.md` to a
target technical architecture. It does not claim that every path is currently
wired. See component `docs/ai/README.md` files for implementation evidence.

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
| `gamblock-ai-infrastructure/` | Ansible + Docker + Caddy | Backend/website delivery, automated TLS, and database infrastructure |
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

- Rule branch evaluates explicit URL characteristics plus supplied keyword
  matches over the bounded URL/DOM text locally; the model's
  `url_keyword_count` feature remains URL-only.
- Model branch vectorizes DOM text using the exported Bag-of-Words vocabulary
  and applies Logistic Regression locally.
- The fusion policy defines precedence, score normalization, exception/safe
  rule behavior, threshold, and ambiguous/error fallback.
- Hybrid-v2 imports the supplied ONNX graph into a dependency-free portable
  runtime artifact containing 5,664 unigram weights, 4,336 bigram weights, 14
  scaled URL features, and the Logistic Regression coefficients. Android and
  Windows consume the same hashed JSON contract locally.
- The supplied `0.75/0.25` fusion weights and `0.4` threshold are calibratable
  engineering inputs, not permanent product requirements. Exact parity of the
  reconstructed URL preprocessing with the training pipeline remains an
  evidence gate because its source implementation was not supplied.

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
The Windows implementation separates the LocalSystem authority from the
interactive user-session agent. The service owns loopback validation,
classification, pairing/grants, aggregate counters, and SCM recovery. The
agent owns Flutter UI, supported `SendInput` navigation, settings-surface
friction, and Pattern Interrupt. Their named pipe is restricted to LocalSystem
and the active logon SID. Source/CMake inclusion is still only code-complete
prototype evidence until a Windows build and VM/device trace pass.

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
Student membership:
no_group -> code_preview -> explicit_confirm -> active
active -> leave_pending -> active | left
active -> unsafe_exit -> safety_suspended -> support_review
active -> partner_removal -> removed

Partner group:
verified_email_and_phone -> active_group -> code_rotated
active_group -- only when no live members --> archived

Protection request on an active membership:
pending -> approved -> bounded apply grant
        -> denied | expired | cancelled
```

Rules:

- one account has one authoritative role: `user` (student), `partner`, or
  `admin`; organization roles belong to membership relations;
- a student has at most one live membership; a partner may own multiple groups;
- code preview identifies the group and partner before explicit confirmation;
- join codes are hashed at rest, rate-limited, and rotatable;
- both parties understand and accept the relationship;
- partner may be a parent or peer;
- approval is explicit, scoped to one request/device/action, expiring, and
  auditable;
- a WhatsApp deep link is only a delivery mechanism for a backend token;
- native client validates authoritative request state before allowing action;
- offline/unavailable behavior is defined without silently bypassing approval;
- emergency recovery is least-privilege and cannot be the routine shortcut;
- normal student exit is reviewable and may be cancelled by its student while
  pending; an unsafe exit stops all sharing immediately and enters support
  review; partner removal also stops sharing;
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

Psychoeducation is persisted as a mutable bilingual draft plus an immutable
published document revision. Media metadata is stored separately from files;
filesystem-backed uploads use configured persistent storage and external media
stores only an allowlisted HTTPS URL. Student progress is keyed by user,
module, and published revision. The website renders validated document JSON
without raw HTML, while the admin WYSIWYG emits the same schema.

Website recovery state uses deliberately separated paths:

- mission completion, protection status, profile, partner approvals, and
  support cases use authenticated APIs;
- `GET /v1/missions/today` derives a deterministic one-primary/two-bonus task
  set from the `Asia/Jakarta` date and returns the student's account-private EXP
  level plus server-derived claim eligibility; `POST /v1/missions/claim`
  rechecks that eligibility and atomically grants the disclosed fixed EXP once.
  `POST /v1/missions/adjust` lets the student replace the unresolved primary
  task once with one of the two non-assigned catalog tasks, then optionally
  skip that effective primary with a bounded reason. Adjustment never changes
  EXP. Legacy `PATCH /v1/missions` is claim-only compatibility and rejects undo;
- structured mood/urge check-ins remain local-first in
  `gamblock:recovery:v1`; submitted account records are separate from drafts;
- the student recovery room is an account-backed workspace. Completed urge
  surfing, grounding, and focus practices are retained for a rolling 12-month
  window, while deterministic room unlocks and placements remain for the
  account lifetime until the user exports or deletes the account;
- reflection text is the only free-text recovery record. Its AES-256-GCM JSON
  payload is versioned and may include an optional mood score and next step;
  the daily-mission closeout uses the same private encrypted path with a bounded
  feeling, optional note, and optional next-step suggestion;
  one reflection can be marked as the current focus without exposing it to a
  partner. Legacy browser-local intention text is imported only after an
  explicit one-time student action;
- `GET/PUT /v1/weekly-reviews/current` stores the current structured weekly
  review in the encrypted recovery-record workflow. The full focus-period and
  reminder lifecycle required by `PKM-WEB-002` remains a tracked core gap; the
  supporting room does not redefine that proposal requirement;
- daily check-ins use the `Asia/Jakarta` day, update that day's entry, and do
  not accept user-selected backfill dates;
- progress supports 7/30/90-day private views and requires three check-ins
  before declaring a trend. It returns category-tagged activity days for a
  selectable recovery calendar, and student CSV/PDF export is generated
  client-side.

Published education documents carry an explicit audience (`student`,
`partner`, or `all`) and experience type (`article` or
`response_simulator`). Both list and direct-slug reads enforce the caller's
role. The partner recovery simulator is therefore CMS-authored guidance, not a
client-only gate and never a projection of student recovery data.

The browser-local schema has no URL, domain, DOM, browsing-history, device,
partner, or detected-page field. Optional synchronization is a per-category
choice and must never imply partner sharing. The public `/post-intervention`
route accepts no detected context; Flutter opens it with locale plus the fixed
`source=pattern_interrupt` category only.

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
| Website `localStorage` (`gamblock:recovery:v1`) | local-first intention lifecycle, structured mood/urge check-ins, selected mission alternative, weekly plan, and unsent recovery-record draft | No browsing fields; bounded records and explicit clear action. A draft is not account data until explicit submission. |
| Research storage (future/approved) | governed labeled dataset and pseudonymous study data | Separate access, consent, retention, license, and publication policy. |

Non-production can use an empty in-memory store and may explicitly enable
contextual demo records. Production rejects demo/dev modes and fails closed if
PostgreSQL cannot open, migrate, or load.

## Authentication and API contracts

- JWT access token + rotating refresh token for normal sessions.
- Backend RBAC is authoritative.
- Website token cookie/middleware and Flutter Bearer client are consumers, not
  substitutes for backend checks.
- Partner invitations are email-bound, expire after seven days, and require
  recipient consent. Multiple relationship records are supported.
- Quick approval uses a high-entropy, 24-hour, single-use scoped token stored
  only as a hash. Relationship authorization is checked on every decision.
- Emergency recovery begins with the protected user requesting access for an
  owned device. One platform administrator reviews it and a distinct second
  platform administrator issues the key within the 30-minute request window;
  the issued hashed key is device-bound, single-use, and expires after 24
  hours.
- API stable error codes remain synchronized across backend, website, Flutter.
- Student account recovery uses a non-enumerating email request followed by a
  hashed, single-use 12-character code that expires after 30 minutes and
  revokes all refresh sessions on success. Google ID tokens are accepted only
  for an allowlisted audience; Windows uses installed-app loopback OAuth with
  state, nonce, and PKCE, while an existing password account must explicitly
  link the same verified Google email after password authentication.
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

## Engineering conventions

- Backend layering as above; ent schema changes use generation, never hand-edit
  generated files.
- Flutter feature-first clean architecture: `domain/`, `data/`,
  `presentation/`; presentation does not call Dio directly.
- Website App Router; hooks call `lib/api-client.ts`; pages/components do not
  scatter raw authenticated `fetch()` calls.
- Website next-intl catalogs are split into matching domain modules per locale,
  loaded concurrently through an explicit server loader, and checked for valid
  JSON, unique namespaces, and identical nested keys before delivery.
- Configuration through committed examples and typed config modules; secrets
  remain gitignored/encrypted.
- One component/widget per file where component rules require it; generated
  UI primitives remain protected.

Default AI completion runs only the relevant linter/analyzer and context
validator. Tests/builds do not become architecture evidence unless the user
explicitly requested and they were actually run.

## Operational control-plane v1

The website/backend operational control plane is an operational supporting
feature, not a PKM core replacement. Its implemented contract is:

- account roles are exactly `user`, `partner`, and `admin`; the admin role owns
  content, release, support-queue, research, platform, audit, and emergency
  operations;
- all three roles land on `/dashboard`, with a student recovery summary, a
  consent-bounded partner summary, or an operational admin overview. Admin
  content, releases, tickets, emergency access, and platform settings are
  separate sidebar routes;
- admins create accounts directly with an immutable role. The backend returns
  a cryptographically random temporary password once, forces its replacement
  before issuing a normal session, and requires verified email for admin
  operations;
- mutable role/disabled state is checked for every bearer request. Refresh
  rotation preserves the original primary-authentication time so refresh does
  not satisfy recent-auth gates;
- only students and partners may create requester support cases. Admins use the
  role-gated queue and atomically claim an unassigned case before reading or
  replying; releases require an audited reason;
- content saves immutable revision snapshots. Rollback creates a new draft and
  does not rewrite a published revision;
- admins upload an allowlisted release artifact into managed storage; the
  server computes SHA-256 and validates that stored content before creating a
  release. Manual cohorts support stage/activate/pause/complete/rollback;
- account export produces a server-side AES-256-GCM-encrypted ZIP with a
  seven-day download window. Account deletion is limited to student/partner
  self-service, requires a hashed 30-minute email token plus recent auth, and
  anonymizes retained audit/request records;
- the public footer reads enabled social links only. Administrators may use
  the fixed platform list, exact HTTPS host allowlists, and no query,
  fragment, user-info, or non-standard port.

These flows are locally wired and linted. External SMTP delivery, production
storage lifecycle jobs, automated rollout health decisions, artifact signing,
and production deployment remain environment/operations responsibilities and
must not be inferred from route presence.
