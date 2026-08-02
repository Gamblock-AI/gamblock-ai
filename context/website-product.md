# Website Product Specification

## Purpose and boundary

The website is the psychoeducation, self-regulation, accountability, public
education, and operational surface of Gamblock-AI. It supports the local
Android/Windows protector; it is not the component that classifies or blocks a
page in real time.

The website has two feature classes:

- `WEB-CORE-001`, `WEB-CORE-002`, `WEB-CORE-003`, `WEB-CORE-004`,
  `WEB-CORE-005`, `WEB-CORE-006`, and `WEB-CORE-007` implement
  `PKM-WEB-001`, `PKM-WEB-002`, `PKM-WEB-003`, `PKM-WEB-004`,
  `PKM-WEB-005`, `PKM-WEB-006`, `PKM-WEB-007`, and the recovery handoff
  from `PKM-INT-004`.
- IDs with the `WEB-SUP` and `WEB-OPS` prefixes are supporting/operational
  additions. They may
  enrich the product but must not displace unfinished core recovery work.

Current implementation status belongs in component `docs/ai/README.md` files;
this file is the target product specification.

## Experience principles

1. **Recovery before surveillance** — help the student regulate behavior; do
   not expose browsing detail to a partner or administrator.
2. **Actionable, not preachy** — each page offers one understandable next step.
3. **Private by default** — a student's mood, intention, reflection, and
   journal are not partner-visible unless a separately defined, granular
   consent feature is approved.
4. **Progress without shame** — lapses do not erase progress or produce
   humiliating alerts, red states, or partner notifications.
5. **Explain the system** — clearly distinguish on-device detection, optional
   server data, partner authority, limitations, and emergency recovery.
6. **Evidence-aware** — educational and psychological content shows reviewer,
   source, review date, and non-clinical limitations.
7. **Accessible under stress** — concise Indonesian copy, low cognitive load,
   keyboard/screen-reader support, reduced motion, and visible help options.

## Actors and access

| Surface                                      |                             Protected Student |                            Accountability Partner |                        Operational role |                                Public |
| -------------------------------------------- | --------------------------------------------: | ------------------------------------------------: | --------------------------------------: | ------------------------------------: |
| Personal intention, mood, private reflection |                                 Own data only |                                                No |                           No by default |                                    No |
| Missions, education, skill recommendations   |                                   Own journey |                  Support summary only if approved | Content management, not private answers |             Selected public education |
| Protection aggregate/status                  |                                    Own device |                          Consented aggregate only |           Aggregate support diagnostics |                                    No |
| Removal approval                             |                                Request/status |                     Approve or deny linked member |        Audited emergency/support action | Token holder only for single-use flow |
| Partner relationship                         | Preview/join one group; leave or stop sharing | Own multiple groups; rotate codes; remove members |       Limited safety/support resolution |                                    No |
| Content administration                       |                                            No |                                                No |                                   Admin |                Published content only |
| Model/release operations                     |                            Version visibility |                                                No |                                   Admin |      Public transparency summary only |

Possessing an operational role does not grant access to raw browsing data or
private recovery text.

## Core recovery journey

### `WEB-CORE-001` — privacy-safe post-block entry

After Pattern Interrupt, the native client offers a web/deep-link entry that:

- contains no URL, domain, DOM text, rule hit, score, or page identifier;
- can open a lightweight unauthenticated grounding page when the user is not
  signed in;
- returns an authenticated user to today's recovery check-in;
- lets the user dismiss/continue later without punishment;
- provides immediate help resources and a reduced-motion path.

### `WEB-CORE-002` — intention and change-goal setting

The student can:

- write a short personal reason for change;
- choose an achievable focus period and one next action;
- review, revise, pause, or archive an intention;
- see where private reminders are configured without exposing the intention to
  the partner. Delivery remains an opt-in Android-local utility; the website
  does not claim browser notification delivery.
- see the intention at relevant recovery moments without exposing it to the
  partner.

Avoid a single irreversible “commitment contract”. Self-regulation requires
adjustment, not forced permanence.

### `WEB-CORE-003` — impulse-awareness psychoeducation

Content covers, in approachable language:

- the trigger → thought/urge → action → consequence loop;
- common online-gambling interface tactics and cognitive biases;
- delay, grounding, environment change, and help-seeking alternatives;
- financial and psychological impacts without sensationalism;
- the limits of blocking tools and when professional support is appropriate.

Each module has estimated time, learning objective, short interaction or
reflection, optional knowledge check, source/reviewer metadata, and an
accessible completion state.

Published modules use immutable bilingual revisions. A shared section/check
identifier across locales preserves progress when the student changes
language. Completion is calculated from required sections, explicitly required
content media, and required knowledge checks; a new published revision starts a
separate progress record. Content administrators author allowlisted structured
rich text, attach one to eight ordered thumbnails, and move drafts through
review before publication. Uploaded images, video, and PDFs are validated by
the backend. External education media is allowlisted and click-to-load so no
third-party request occurs before the student chooses it.

### `WEB-CORE-004` — mood and urge check-in

A quick check-in records only what is needed:

- mood on a defined, accessible scale;
- optional urge intensity;
- optional user-selected trigger category, never an automatically captured
  URL/app;
- optional private note under the sensitive-text policy;
- date/time and consented context needed for the student's own trend view.

The UI offers a “prefer not to say” path. Partner dashboards receive no raw
check-in unless a future explicit sharing design is approved.

### `WEB-CORE-005` — daily self-control missions

Missions are small, achievable, and adaptable, for example:

- practice a 10-minute delay before a risky action;
- remove a payment shortcut;
- contact a trusted person;
- complete a short grounding or budgeting exercise;
- plan a study, sport, creative, or social alternative.

The student can complete, skip with a reason, choose an accessible
alternative, and reflect briefly. Missing a day never resets all progress.

The website adds a supporting, account-private progression layer around these
missions. Every `Asia/Jakarta` day has exactly five slots, each worth 10 EXP.
The student may create up to five private custom missions for the day; every
custom mission replaces one system slot, so three custom missions leave two
system missions. Pending custom missions may be edited or deleted, and delete
immediately restores a system slot. The fixed, self-directed system catalog is
active protection, daily check-in, education section, education module, and a
recovery practice. System claims are server-verified from existing
purpose-bound account state. A custom mission is a student self-attestation;
the backend records the completion idempotently but cannot verify the private
activity itself. Custom titles are encrypted sensitive recovery text, and the
custom mission/self-attestation is never projected to partners or admins. EXP has no chance-based outcome,
purchasable currency, public leaderboard, punitive streak reset, or
partner/admin projection. This supporting layer implements `PKM-WEB-005`; it
does not replace the core completion, accessible-alternative, reflection, and
next-step requirements above.

### `WEB-CORE-006` — skill-development recommendations

Recommendations help build alternative routines in categories such as:

- study and career skills;
- financial literacy and debt-help resources;
- sports and physical wellbeing;
- creative hobbies;
- social connection and campus activities;
- relaxation and emotional regulation.

Recommendations must be explainable (“suggested because you selected...”),
non-diagnostic, dismissible, and based on voluntary recovery inputs—not
browsing behavior.

### `WEB-CORE-007` — self-regulation review loop

A weekly review connects the core features:

1. revisit the current intention;
2. view private mood/urge and mission patterns;
3. note what helped or was difficult;
4. choose an adjustment and next mission;
5. select a skill/resource recommendation.

The review emphasizes learning and adjustment. It must not calculate a hidden
clinical risk score or share a detailed behavioral profile with the partner.

## Supporting student features

### `WEB-SUP-ONB-001` — onboarding and setup

- Account registration/login, Google OAuth, password recovery, and locale.
- Plain-language privacy and permission walkthrough.
- Partner invitation or Group Code join with relationship consent.
- Device list and protection-health checklist.
- Guided Android/Windows setup with platform-specific troubleshooting.
- Demo/sandbox recovery journey for evaluators without real browsing data.
- Notification preferences and timezone.

### `WEB-SUP-REC-001` — deeper recovery tools

- Encrypted private journal/reflection is the only free-text recovery surface.
  The student daily journal supports a bounded private rich-text document
  (headings, emphasis, lists, quotations, and up to five embedded private
  images) and exactly one editable entry per `Asia/Jakarta` day.
- Personal coping-plan builder: triggers selected by the user, warning signs,
  alternative actions, trusted contacts, and emergency resources.
- “Urge surfing” timer and grounding exercise with reduced-motion mode.
- A calm, keyboard-accessible dorm-room workspace exposes urge surfing at the
  window, 5-4-3-2-1 grounding at the rug, a focus sprint at the desk, journal
  at the notebook, and support at the phone. Deterministic decor records
  participation without chance, currency, leaderboards, or loss framing.
- Personal 7/30/90-day recovery calendar combines check-ins, practices,
  journal entries, missions, education, and weekly reviews without red failure
  markers; each populated day can be inspected.
- Flexible streaks (“days engaged”) and milestone reflections.
- Weekly plan and printable/private offline plan.
- Favorite/bookmarked modules and resources.
- Search/filter by topic, duration, accessibility, and content type.
- Optional reminders for intention review, check-ins, and missions.
- Data export, deletion, consent history, and account deactivation.
- False-positive report guide that creates a local/redacted report rather than
  uploading the visited URL by default.
- Professional-help directory with campus, national, financial, and crisis
  resources maintained by an accountable content owner.

The intention manager is the authoritative web recovery surface for
`WEB-CORE-002`. It stores the full title, next action, focus period, and
pause/resume/archive lifecycle local-first, and connects the current intention
to weekly review. Android's optional local reminder is a delivery utility,
not partner-visible recovery data or a second native recovery journey.

### `WEB-SUP-PROG-001` — progress and reflection

- Private personal dashboard for intention, current mission, recent mood, and
  suggested next action.
- Trend views using clear definitions and sufficient data warnings.
- Module/mission completion timeline.
- Recovery milestones with non-monetary, non-chance-based visuals.
- Personal notes attached to a week or mission.
- Downloadable progress summary controlled by the student.
- “What changed?” annotations when goals or notification preferences change.

Never use casino-like reward mechanics, loot boxes, random spins, loss-framed
streak resets, or variable-ratio engagement patterns.

## Accountability Partner features

### `WEB-SUP-ACC-001` — relationship lifecycle

- A verified partner creates one or more named groups and receives a rotatable,
  hashed-at-rest join code.
- A verified student previews the group and partner identity, then explicitly
  confirms one active membership.
- Student and partner see active, leave-pending, support-review,
  safety-suspended, left, removed, and archived states where relevant.
- Normal exit, unsafe immediate stop-sharing, partner removal, and group
  archive rules are explicit.
- Relationship changes generate a minimal audit event.
- Abuse/help pathway exists when the relationship is unsafe.

### `WEB-SUP-ACC-002` — removal approval hub

- Show which linked member requested removal, request time, expiry, and a
  student-provided reason when they choose to share it.
- Approve/deny with confirmation and an optional supportive response.
- Use single-use, short-lived, revocable tokens for quick-approval links.
- Prevent token previews/logs/analytics from exposing the secret.
- Provide pending/approved/denied/expired/cancelled/emergency states.
- Batch notifications where practical and allow quiet hours.

WhatsApp is the supporting transactional notification channel, not the
approval authority.
The backend state transition is authoritative.

### `WEB-SUP-ACC-003` — aggregate supervision dashboard

Allowed examples:

- protection enabled/attention-needed state;
- last privacy-safe heartbeat;
- aggregate block count by broad time period;
- missions engaged/completed only if sharing is expressly defined;
- approval requests and relationship status;
- supportive conversation suggestions.

Forbidden examples:

- URLs, domains, titles, screenshots, DOM excerpts, search queries;
- per-site timestamps that reconstruct browsing history;
- raw mood, intention, journal, or reflection text;
- a secret risk score inferred from private activity;
- competitive ranking of members.

Partner guidance may include a reviewed, bilingual response simulator published
through the psychoeducation CMS and launched as a dialog from partner
`/progress`; `/recovery` remains student-only. It teaches supportive wording
with answer rationale and retry, but reads no student journal, mood, practice,
focus-task, room, or private progress record.

### `WEB-SUP-SUPPORT-001` — threaded support

- Student and partner accounts can create and read only their own support
  cases, reply within one encrypted thread, close a resolved case, and reopen
  it within seven days.
- Admins use a role-gated queue with explicit ownership and status transitions.
  They reply to student/partner reports from the operations ticket workspace
  and cannot use the requester support surface.
- The partner contact channel is asymmetric by role: a student creates and
  tracks a request to their connected partner, while a partner receives,
  acknowledges, and closes member requests. Shared route labels must describe
  the current role's action rather than calling an incoming student request
  “my partner”.
- Attachments are not accepted. Redaction guidance forbids passwords, tokens,
  URLs, domains, and browsing history.

## Public and dissemination features

### `WEB-SUP-PUB-001` — public product education

- Landing page with the problem, target user, four core pillars, and CTA.
- Impact page with dated, cited statistics and careful claim wording.
- Technology page explaining rules + BoW + Logistic Regression, local
  processing, limitations, and evaluation status.
- Privacy page with a simple local/server data table.
- Download page with supported platforms, checksums/signature guidance,
  permissions, and troubleshooting.
- Help/FAQ, contact, terms, accessibility statement, and security contact.

### `WEB-SUP-PUB-002` — PKM transparency and outputs

- The canonical public route is `/pkm`; it shows evidence maturity and keeps
  download/publication links closed until the corresponding approval,
  submission, or publication record exists.
- PKM project page: title, theme fit, team, objectives, method, current phase,
  limitations, and ethical safeguards.
- Public milestone timeline linked to evidence, not aspirational claims.
- Progress/final report publication metadata when approved.
- Prototype/demo guide.
- Social-media archive/content hub for required dissemination.
- Educational video page with captions, transcript, sources, and alt text.
- Scientific article/publication page when a manuscript is ready.
- Media kit with approved logo, Gami assets, fact sheet, and claim guide.

### `WEB-SUP-PUB-003` — learning resource library

- Public reviewed articles and myth/fact explainers.
- Glossary of gambling, recovery, AI, and privacy terms.
- Filter by student, parent/peer, educator, and researcher audience.
- Source and last-reviewed metadata.
- Shareable pages that never expose a user's activity.

## Operational features

### `WEB-OPS-CONTENT-001`

- Draft/review/publish/archive workflow for modules, missions, skills, help
  resources, and Pattern Interrupt metadata.
- Reviewer identity, sources, version, locale, reading time, accessibility
  checklist, and scheduled review date.
- Preview and rollback; audit every publish action.
- Separate content, release, support, emergency, and platform work areas even
  though the unified `admin` account role authorizes them.

### `WEB-OPS-RELEASE-001`

- Versioned model, vocabulary/vectorizer, URL ruleset, network ruleset, and
  Pattern Interrupt asset metadata.
- Compatibility, artifact hash/signature, rollout cohort, rollback, and
  release notes.
- Publicly safe model-card summary without exposing evasion-enabling detail.

### `WEB-OPS-SUPPORT-001`

- Encrypted threaded support cases with category, impact, priority, owner,
  explicit status, reply history, and redaction guidance.
- Data access/deletion requests and consent questions.
- Emergency recovery workflow with least privilege and immutable audit.
- Known-issue/status information without device-specific browsing telemetry.

### `WEB-OPS-RESEARCH-001`

- Participant information/consent screens for approved studies.
- Pseudonymous study assignment separated from operational accounts where
  feasible.
- Aggregate metric dashboards with cohort thresholds that prevent singling out
  an individual.
- Dataset/model-card publication metadata and experiment registry links.
- Export restricted to the approved research schema.

Research functionality is planned until an ethics/data-governance protocol is
approved; product consent is not automatically research consent.

## Proposed information architecture

```text
Public
  Home
  Dampak
  Teknologi & Privasi
  Cara Kerja
  Edukasi / Resources
  PKM & Research Transparency
  Download
  Help / Contact / Legal / Accessibility

Student app
  Today
    intention
    mood/urge check-in
    daily mission
    next recommended skill
  Recovery
    psychoeducation modules
    coping plan
    private journal
    grounding tools
  Progress
    weekly review
    trends and milestones
  Protection
    devices and status
    partner relationship
    removal request
  Privacy & Settings

Partner app
  Linked members
  Aggregate support view
  Approval queue/history
  Relationship and notification settings
  Support guidance

Operations
  Content
  Releases
  Support and data requests
  Aggregate research/evaluation
  Audit and policy
```

## Route guidance

Current locale-aware Next.js routes already cover landing/legal pages, auth,
dashboard, recovery, progress, education, accountability, partner invitation,
quick approval, settings/profile/support, data requests, and an admin surface.
The current prototype also includes a public `/post-intervention` route with a
local grounding exercise and no browsing-context parameters, plus a
student-only `/skills` page (supporting feature around `WEB-CORE-006`) that
combines short internal skill practices with curated outbound links to free
course/certification platforms; those links open externally and carry no
account or browsing data.

When adding target features:

- keep user-facing routes below `app/[locale]/`;
- keep protected student/partner/ops screens in the authenticated dashboard
  group unless token-authenticated by design;
- keep quick-approval tokens outside session-required middleware but validate
  them server-side as single-use and expiring;
- update `routes.ts` and the active middleware whenever page access policy
  changes;
- never put detected-page details in URL parameters, analytics, referrers, or
  client error reporting.

## State and error requirements

Every core action needs loading, empty, success, validation, offline/degraded,
permission, expired-token, and safe error states. UI messages use concise,
non-technical catalog copy in every environment. Sanitized code/status context
may appear only in the development console, never in production diagnostics;
tokens, URLs, form values, and recovery/browsing content are never logged.

Specific recovery states include:

- no intention yet / active / paused / archived;
- check-in available / completed / skipped;
- mission available / completed / skipped; custom mission pending / edited /
  deleted;
- insufficient data for trend;
- group preview / active / leave pending / support review / sharing stopped /
  left / removed / archived;
- removal request pending / approved / denied / expired / cancelled;
- content draft / published / archived / review overdue.

## Analytics boundary

Permitted product analytics are coarse and purpose-limited: page/function
usage, module completion, mission state, consented recovery engagement, error
codes, and performance. Do not attach raw detection/browsing context. Apply
minimum cohort sizes to partner/research aggregates and avoid third-party
trackers on sensitive recovery/approval pages.

## Prioritization

1. Implement/verify `WEB-CORE-001`, `WEB-CORE-002`, `WEB-CORE-003`,
   `WEB-CORE-004`, `WEB-CORE-005`, `WEB-CORE-006`, and `WEB-CORE-007`, plus
   the post-block handoff.
2. Make partner approval and privacy boundaries reliable and understandable.
3. Provide core onboarding, help, false-positive, and data-control paths.
4. Deepen recovery/support/public education.
5. Add operational CMS/release/research features only as needed for prototype
   delivery and evidence collection.

## Implemented operational workspace boundary

The current operational workspace uses one shared visual shell with strictly
separated server-authorized work areas:

- every authenticated role lands on `/dashboard`; the student, partner, and
  admin dashboards expose distinct role-relevant summaries;
- admins author bilingual modules, upload/crop media, submit,
  publish, archive, inspect revisions, and restore a historical version as a
  new draft;
- admins claim cases from a shared queue, work the encrypted
  thread, transition status, release ownership with a reason, and retry or
  reject eligible failed data requests;
- admins upload model/ruleset/network artifacts, review their
  computed checksum, create validated releases, and run manual cohort
  rollouts;
- admins directly create immutable-role `user`, `partner`, or `admin` accounts,
  enable/disable other accounts, manage public social links and audit history,
  and process dual-control emergency requests. Legacy specialist invitations
  are retired.

Content, releases, tickets, emergency access, and platform settings are
first-class admin sidebar destinations rather than tabs inside one page.
Operational counts live on the admin dashboard; the tickets destination is the
only admin support surface.

The landing footer renders a social icon only when its administrator-managed
record is enabled and has a validated URL. Empty/null records produce no
placeholder. Research sandbox access is included in the unified admin
workspace.
