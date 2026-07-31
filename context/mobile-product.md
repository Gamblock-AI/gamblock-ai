# Mobile and Desktop Protection Product Specification

## Purpose and status boundary

The Flutter/native client is the local protection authority for Android and
Windows. It senses supported local browser signals, runs Hybrid Analysis,
performs supported blocking/navigation, presents Pattern Interrupt, enforces
the accountability workflow within OS limits, and reports only coarse
protection aggregates.

This file is the target product specification. Current code/evidence status
belongs in `gamblock_ai_apps/docs/ai/README.md`. A code path or UI screen is not
real-device, model-evaluation, security-review, or release-readiness evidence.

## Feature classes

- `MOB-CORE-*` implements proposal core requirements.
- `MOB-SUP-*` is supporting product scope needed for a usable prototype.
- `MOB-OPS-*` is operational/release scope.

Supporting or operational work may not replace unfinished core behavior.

## Actors

### Protected student

- understands what the client observes and what remains private;
- can complete platform setup without guessing;
- receives immediate local intervention after a positive decision;
- can request a scoped pause/disable/removal from a trusted partner;
- can see truthful degraded/offline state and use a safe emergency path;
- can continue to web recovery without exposing detected context.

### Accountability partner

- is invited with explicit consent and relationship scope;
- resolves device/action-specific requests;
- never receives URL, DOM, page title, per-site timeline, or raw recovery text.

### Platform administrator

- handles exceptional device-bound emergency recovery under two-operator
  control;
- cannot access browsing inputs;
- sees audit/status metadata needed for the operational action only.

## Information architecture

The ordinary Flutter shell has four top-level destinations:

1. **Dashboard** — local health, setup, self-test, approval and emergency
   state.
2. **Analytics** — broad 7/30-day protection counters and data sufficiency.
3. **Partner** — relationship setup, invitation, request history, and consent.
4. **Settings** — account/password, locale, haptics, health notifications,
   pairing, versions, privacy, help, and logout.

Pattern Interrupt is a native/full-screen state outside ordinary navigation.
The detailed intention, check-in, mission, education, skill, and weekly-review
journey remains on the website.

The client is intentionally a thin protection surface. It does not duplicate
the website's missions, EXP/level, journey badges, independent breathing
exercise, pause acknowledgements, or recovery-practice bookkeeping. The
Pattern Interrupt breathing cue and 5-4-3-2-1 grounding remain local safety
intervention steps. Android may provide an opt-in, local daily check-in
reminder; Windows treats that notification service as a no-op.

`MOB-SUP-004` records this boundary: the client may show aggregate protection
health and the consented partner workflow, but detailed rehabilitation belongs
to the website.

## Core protection features

### `MOB-CORE-001` — multi-platform background protection

Implements `PKM-PLAT-001`, `PKM-PLAT-002`, and `PKM-PLAT-003`.

- Android uses an explicitly disclosed Accessibility Service.
- Windows uses a normal LocalSystem service with SCM recovery plus a
  user-session agent for UI/input actions.
- Setup shows permission/service/sensor/model state separately.
- Protection never claims active coverage when the required sensor is absent.
- Sideload/install limitations are documented honestly.

### `MOB-CORE-002` — Hybrid-v2 local decision

Implements `PKM-AI-001`, `PKM-AI-002`, `PKM-AI-003`, `PKM-AI-004`,
`PKM-AI-005`, `PKM-AI-006`, and `PKM-AI-007`.

The versioned contract includes:

- bounded URL features and rule patterns;
- bounded DOM title, headings, and anchor text;
- deterministic normalization/tokenization;
- Bag-of-Words counts with a declared vocabulary;
- Logistic Regression bias/weights and sigmoid;
- versioned threshold and fusion precedence;
- model/rules/fixture hashes and compatibility version;
- last-known-good fallback on invalid updates.

A supplied trained artifact may be wired as a prototype when its source hash,
conversion, preprocessing assumptions, and evidence gaps are explicit. It is
not `evaluated` until the governed dataset/training/evaluation workstream can
reproduce its metrics and platform parity.

### `MOB-CORE-003` — local block/navigation

Implements `PKM-BLOCK-001` and `PKM-BLOCK-002`.

- A positive decision triggers the supported local Back/navigation action.
- The backend and extension never perform the block.
- Unsupported surfaces are visible as coverage limitations.
- Internal classifier failure degrades transparently and does not upload the
  input.

### `MOB-CORE-004` — Pattern Interrupt

Implements `PKM-INT-001`, `PKM-INT-002`, `PKM-INT-003`, and `PKM-INT-004`.

- Starts automatically after a positive local decision.
- Lasts 5–10 seconds; the prototype baseline is seven seconds.
- Uses one calm focal visual and supportive, non-clinical copy.
- Supports reduced motion and an offline grounding action.
- Does not display or persist the detected URL/title/content.
- Web handoff includes only locale and fixed source category.

### `MOB-CORE-005` — social accountability enforcement

Implements `PKM-ACC-001`, `PKM-ACC-002`, `PKM-ACC-003`, and
`PKM-ACC-004`.

- Both parties explicitly establish the relationship.
- Pause/disable/uninstall requests are scoped to user, relationship, device,
  action, reason, duration, and expiry.
- Partner decision is authoritative on the backend.
- The client applies an approved request once within a bounded application
  window, then stores only the local expiring grant.
- Android settings friction and Windows service/settings friction stay within
  documented OS capabilities.
- Denied, expired, cancelled, offline, and partner-unavailable states never
  silently become approved.

## Supporting features

### `MOB-SUP-001` — account and device lifecycle

- A persisted three-step onboarding precedes login/register; returning
  authenticated students open the dashboard directly.
- Register/login/logout with rotating session handling, non-enumerating email
  code password reset, and explicit email-verification state.
- Google sign-in uses the official Android provider flow and a Windows
  installed-app loopback flow with state, nonce, and PKCE; existing password
  accounts link the same verified email from Settings.
- Stable per-install client instance ID and per-user device registration.
- Profile and current-password-protected password update.
- Reauthentication after password change.
- Privacy-safe heartbeat and version/status update.

### `MOB-SUP-002` — aggregate analytics

- Native counters use an allowlist and UTC day bucket.
- Completed days sync with deterministic idempotency keys.
- Current local day may merge into the displayed 7/30-day server aggregate.
- Empty/local-only/degraded states are explicit.
- No URL, domain, title, DOM, score, fingerprint, or millisecond page event.

### `MOB-SUP-003` — emergency device recovery

- The protected user creates a request for an owned device.
- One platform administrator reviews the request.
- A different platform administrator issues a random, hashed, single-use key.
- Request review expires after 30 minutes; the key expires after 24 hours.
- Key use is tied to the device and produces a ten-minute local grant.
- This is exceptional recovery, not a routine partner-approval bypass.

### `MOB-SUP-004` — artifact health and update

- Bundled artifacts are integrity checked before use.
- Remote release metadata/download is accepted only for compatible platform,
  contract, and SHA-256.
- Writes use temporary/replace behavior and retain a last-known-good artifact.
- Health UI reports versions without exposing detection inputs.

### `MOB-SUP-005` — accessible preferences and help

- Indonesian and English locale selection.
- Optional haptics and health notification.
- 48dp-or-platform-guidance touch targets.
- Reduced-motion route and intervention behavior.
- Privacy, help, about, and platform limitation links.

## Platform coverage

### Android

Supported prototype browsers:

- Google Chrome package `com.android.chrome`;
- Microsoft Edge package `com.microsoft.emmx`.

The sensor may use known address-bar resource IDs with a bounded editable-field
fallback and extracts only title/headings/clickable anchor-like text. Other
browsers and arbitrary WebViews are best-effort/unverified and must not be
advertised as covered.

Accessibility is disclosed and permissioned. The client does not request broad
package enumeration, overlay permission, battery-optimization exemption,
critical-device-owner behavior, or process-kill authority for this flow.

### Windows

The service/agent split is mandatory:

- LocalSystem service owns authenticated loopback input, validation,
  classification, pairing/grant protection, aggregate counters, and SCM state.
- User-session agent owns Flutter UI, `SendInput` navigation, foreground
  settings monitoring, and Pattern Interrupt presentation.
- Service-to-agent IPC uses a named pipe restricted to LocalSystem and the
  active logon SID.
- Pairing and grants use machine-scoped DPAPI at rest.
- The extension remains passive and receives only auth acknowledgements/pong.

Never add gambling executable-name scanning, arbitrary process termination,
`SeDebugPrivilege`, or critical-process behavior.

## State model

Protection health distinguishes:

- `inactive` — required permission/service is not active;
- `active` — local classifier and required sensor are connected;
- `paused` — an unexpired approved/emergency grant is active;
- `degraded` — service exists but a required sensor/artifact/runtime condition
  is unavailable.

Backend connectivity is separate. Local protection continues when the backend
or website is unavailable; approval creation/application and aggregate sync
show their own pending/error state.

## Release and evidence gates

### `MOB-OPS-001` — release packaging

- Android release tags require a real keystore; no debug-signing fallback.
- Windows release tags require Authenticode signing for executables.
- Bundles include the service, Flutter agent, assets, and install/uninstall
  scripts.
- Checksums/signature guidance and supported OS versions appear on the website
  download surface before public release.

### `MOB-OPS-002` — completion evidence

Before “runtime verified” or “release ready”:

- run Android real-device Chrome/Edge scenarios;
- run Windows signed VM/device extension/service/agent scenarios;
- test accessibility, reduced motion, screen reader, and failure recovery;
- measure classifier size, memory, CPU, latency, and battery impact;
- validate SCM/Accessibility lifecycle and safe removal recovery;
- complete model dataset/evaluation/calibration and document limitations;
- execute privacy/network inspection showing no browsing data leaves device.

Until those gates pass, use **code-complete prototype**.
