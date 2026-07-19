# Privacy and Security Context

## Objective

Gamblock-AI must provide local protection and social accountability without
becoming a browsing-surveillance system. This document operationalizes the
proposal's On-Device AI and UU PDP data-minimization intent. It is an
engineering policy, not legal advice or a declaration of certified compliance.

## Trust boundaries

```text
untrusted web/app content
  -> device-local sensor
  -> authenticated local IPC
  -> device-local features/model/decision/block/intervention
       | no raw detection data crosses this boundary
       v
optional minimal aggregate/account/recovery API
  -> backend/database
  -> student web experience or consented partner aggregate
```

The browser extension and Windows service are on the same device but remain
separate trust zones. Loopback is not automatically trusted; pairing and
message validation are required.

## Data classification

| Class                              | Examples                                                                                                                                              | Location and policy                                                                                                                       |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `D0 Local detection secret`        | URL/domain, DOM text, title/headings/anchor text, history, screenshot, search query, app/window identifier, rule hits, feature vector, per-page score | Device only; never sent to backend, analytics, crash reporting, partner, or admin. Shortest practical local lifetime.                     |
| `D1 Local protection state`        | model/rules versions, pairing token, offline queue, current block/intervention state                                                                  | Device only except explicitly allowed non-browsing version/health aggregates; pairing token never leaves paired local processes.          |
| `D2 Account and relationship`      | identity, role, contact, partner relationship, consent, approval status                                                                               | Backend allowed for defined purpose; least privilege, retention, audit, export/delete rules.                                              |
| `D3 Recovery sensitive`            | intention/next step, mood/urge check-in, private reflection/journal, focus-practice task label, weekly review                                          | Backend only when voluntarily entered for web recovery; private by default; encrypt sensitive text; never partner-visible by implication. |
| `D4 Aggregate protection/recovery` | broad-period block count, privacy-safe heartbeat, mission/education/practice completion, deterministic room unlock                                    | Backend allowed only if non-reconstructive, purpose-limited, and disclosed; apply cohort/time granularity.                                |
| `D5 Public/operational`            | published modules, app versions, model card, help resources, support status                                                                           | Backend/public as appropriate; still protect credentials, audit detail, and internal security metadata.                                   |
| `D6 Research`                      | approved pseudonymous study events and outcomes                                                                                                       | Separate purpose/consent/schema/access/retention; product consent is insufficient.                                                        |

When uncertain, assign the more sensitive class and ask the product/privacy
owner before widening collection or access.

## Non-negotiable privacy invariants

1. Feature extraction, model inference, threshold/rule decision, and blocking
   occur on the device.
2. `D0` data never leaves the device. This includes a “hashed URL”: predictable
   domains can be dictionary-reversed, so hashing does not make it aggregate.
3. The extension only relays supported inputs to an authenticated loopback
   Windows service. It never calls the remote backend with browsing content.
4. Partner and admin surfaces never expose raw browsing behavior or a timeline
   precise enough to reconstruct it.
5. A backend field capable of carrying `D0` data is rejected or redesigned,
   even if a current client promises not to fill it.
6. Journal/reflection text is encrypted with AES-256-GCM before persistence;
   plaintext is not logged or included in telemetry.
7. No third-party analytics/session replay runs on sensitive recovery,
   approval, auth, or administration pages without a separately approved
   privacy review; session replay of these surfaces is prohibited by default.
8. Research collection requires separate informed consent and an approved
   protocol.

## Allowed aggregate contract

An aggregate protection event may contain only fields such as:

- pseudonymous/authorized device reference;
- coarse period or server receipt time;
- non-browsing event category (for example `blocked_count_increment`);
- bounded count;
- protection health/status;
- client/model/rules version needed for compatibility;
- request ID and integrity metadata.

It must not contain or encode:

- URL/domain/title/DOM/app/window/query;
- a unique page/content fingerprint;
- per-page probability or feature vector;
- millisecond browsing timestamp paired with an event;
- free-text field populated from detected content;
- error/stack/log context containing browsing input.

Prefer client-side aggregation over sending one event per page. Specify coarse
time buckets, retention, and partner visibility before introducing a new
aggregate.

## Server-side recovery data

The proposal broadly says user information remains local while also requiring
a web psychoeducation experience. The adopted engineering interpretation is:

- detection/browsing inputs always remain local;
- account, consent, accountability, and recovery data deliberately entered by
  the user may be processed server-side to provide the web service;
- collection must be transparent, minimal, purpose-bound, and controllable;
- the student remains the default audience for their recovery detail;
- the partner sees only explicitly approved aggregate support information.

This interpretation must be reviewed by the proposal/privacy owners and is
tracked as an open decision, not presented as a formal UU PDP compliance
opinion.

Recovery practice completion and weekly-review records use a rolling 12-month
product retention window. Deterministic recovery-room unlock and placement
state remains for the account lifetime because it is user-visible workspace
configuration. Both are included in account export and account deletion.
Active timers and the current focus-sprint task label stay browser-local; the
server receives a completed practice record only after the student finishes.

## Consent and control

Provide distinct, understandable choices for:

- terms/privacy acceptance;
- partner relationship invitation and acceptance;
- notification channels;
- optional recovery fields;
- any optional aggregate sharing with a partner;
- research participation;
- publication/use of testimonials or media.

Consent is specific and revocable. Reject bundled “use the app = consent to
everything” patterns. Provide access, correction, export, deletion, and
withdrawal paths consistent with defined legal/academic obligations.

## Authentication and authorization

- Use short-lived access tokens and rotating refresh tokens.
- Enforce RBAC on the backend; hiding a website menu is not authorization.
- Keep quick-approval routes token-authenticated and session-independent only
  where designed; tokens are high-entropy, short-lived, single-use, revocable,
  and excluded from logs/referrers/analytics.
- Bind partner actions to the approved relationship/member and requested state.
- Use the backend role as authority. Navigation visibility and local storage
  labels never grant student, partner, support, or admin access.
- Require verified email for student group entry; require verified email and
  WhatsApp plus a recent (15-minute) authentication context for sensitive
  partner group/decision actions.
- Treat `admin` as the single operational role while retaining least privilege
  through resource ownership, verified email, recent authentication, audit,
  and dual-control checks.
- Password-reset requests do not reveal whether an email exists. Store only a
  hash of the latest active recovery code, expire it after 30 minutes, cap
  failed attempts, consume it once, and revoke existing refresh sessions after
  a successful reset. Never log reset codes or Google tokens.
- Native Google OAuth uses public client identifiers only. Validate ID-token
  audience and optional nonce on the backend; desktop loopback callbacks also
  require state and PKCE. Discard provider access/refresh tokens after the
  backend session is established.
- Emergency recovery starts from the protected user's owned device. One
  platform administrator reviews it and a distinct second platform
  administrator issues the key. The request expires after 30 minutes; the
  resulting hashed key is device-bound, single-use, and expires after 24
  hours. It is not ordinary access or a partner-approval substitute.

## Local IPC security

For the Windows extension/service WebSocket:

- bind to loopback only;
- require a pairing token before accepting data;
- validate message type, size, schema, and rate;
- reject/ignore service messages that ask the extension to block or redirect;
- rotate/revoke pairing credentials when re-paired;
- protect the Windows pairing token and local grants with DPAPI at rest;
- restrict service/agent named-pipe access to LocalSystem and the active logon
  SID;
- do not put pairing tokens in logs or error reports;
- document origin assumptions and defend against another local process sending
  malformed messages;
- version protocol changes across both repositories.

## Safe anti-tamper and accountability

The protection must be resistant, not destructive:

- Android uses documented Accessibility/administrative capabilities with
  transparent permission disclosure.
- Windows uses a normal LocalSystem service and SCM recovery as appropriate.
- Windows user-interaction actions run in a separate user-session agent; the
  LocalSystem service does not request `SeDebugPrivilege`, scan gambling
  process names, or terminate arbitrary processes.
- Never use `RtlSetProcessIsCritical`, undocumented critical-process behavior,
  boot-loop tactics, filesystem sabotage, or anything that can BSOD/brick the
  device.
- Accountability approval has pending, approved, denied, expired, cancelled,
  and safe emergency states.
- A partner relationship includes an abuse/help path and recoverability when a
  partner is unavailable.
- Sharing is category-specific and revocable. The only partner projections are
  protection health, coarse protection activity, recovery engagement counts,
  and education progress bands; disabled categories return no substitute
  detail. Unsafe exit and partner removal stop sharing immediately.
- Stress testing uses controlled devices/VMs and includes device recovery as a
  pass criterion.

## Threat and abuse cases

| Threat                                              | Required control direction                                                                |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Gambling site rotates domain or camouflages content | Hybrid URL + DOM model, time-shifted evaluation, local rules/model updates.               |
| Malicious page injects huge/adversarial DOM         | Input length/rate limits, normalization, timeouts, safe parser, no code execution.        |
| Local process impersonates extension/service        | Loopback binding, pairing token, schema/rate validation, credential rotation.             |
| User tries ordinary process kill/uninstall          | OS-supported service recovery and consented partner approval; no unsafe critical process. |
| Partner abuses supervisory access                   | Aggregate-only views, relationship revocation/help, audit, least privilege.               |
| Quick-approval token leaks                          | Short expiry, single use, revocation, no analytics/referrer/log exposure.                 |
| Admin/support overreach                             | RBAC, audited break-glass, no browsing schema, sensitive recovery access restriction.     |
| Crash/analytics tool captures sensitive input       | Redaction at source, no `D0`, no recovery plaintext, vendor review.                       |
| Model/rules artifact tampered with                  | Signed/hashed artifact, compatibility manifest, trusted release channel, rollback.        |
| False positive blocks important content             | FPR evaluation, accessible report/recovery path, safe bounded override policy.            |
| Research re-identifies participant                  | Separate pseudonym, minimal schema, cohort suppression, restricted access/retention.      |

## Logging and observability

Safe logs use event codes, request IDs, component/version, coarse duration, and
redacted status. Never log request bodies by default on sensitive routes.
Never log tokens, journal plaintext, mood/intention text, DOM, URL, titles,
headers that contain secrets, or model feature inputs.

Error catalogs provide friendly user messages in every environment. Sanitized
website code/status context may appear only in the development console and is
suppressed in production; form values, tokens, URLs, and recovery/browsing
content never enter client diagnostics. The three stable catalogs stay
synchronized.

## Storage and retention decisions

For every server field, document owner, purpose, sensitivity class, lawful/
consent basis, visibility, encryption, retention, deletion behavior, and audit
need. “Keep forever in case useful” is not a valid purpose.

Current architecture uses PostgreSQL for account/relationship/recovery state,
hashed approval/emergency tokens, daily aggregate events, and encrypted journal
text. Production fails closed when PostgreSQL or required JWT/AES configuration
is unavailable. Empty memory and contextual demo records are non-production
behaviors only. Secrets live outside source control; environment examples
contain placeholders only.

Threaded support stores message bodies with the same fail-closed AES-256-GCM
boundary as other sensitive free text. Only student and partner requesters can
create or access their own cases. Verified admins access the role-gated support
queue to claim, read, and reply; they cannot use the requester support surface.
Status transitions are explicit
(`waiting_support`, `waiting_user`, `resolved`, `closed`), and a requester may
reopen a resolved case only within seven days.

Daily mission completion rows may store the authenticated student's mission
date, stable mission key, fixed EXP reward, status, and completion timestamp.
The user record may store a non-negative cumulative EXP total used only for the
student's own level display. Claim eligibility is derived from existing
purpose-bound records and is not a new analytics event or duplicated sensitive
payload. Claims are idempotent and cannot be undone by the student. These
fields contain no browsing context and are not part of partner/admin projections
or research exports by default.

## Security/privacy review triggers

Require a focused review before:

- adding/changing any API field, aggregate, analytics event, or log;
- changing extension/native IPC;
- adding partner/admin visibility;
- adding third-party SDKs, crash reporting, analytics, or notification vendors;
- changing approval/emergency/revocation state machines;
- collecting dataset/research data;
- releasing model/rules/assets or changing signature/update logic;
- expanding Accessibility/System Service permissions;
- changing encryption/key management or retention.

The default AI check remains the relevant linter/context validator. Tests,
builds, and security experiments run only when explicitly requested, but the
review must still name the unexecuted evidence needed before release.
