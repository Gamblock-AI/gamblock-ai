# Gamblock-AI Product Overview

## Document role

Gamblock-AI is a PKM Karsa Cipta prototype for Indonesian university students:
an Android/Windows on-device gambling-content blocker that combines Hybrid AI,
a short behavioral Pattern Interrupt, web psychoeducation grounded in
Self-Regulation Theory, and an Accountability Partner protocol.

`pkm_proposal.md` is the primary product authority. This overview translates
the proposal into a coherent product shape and clearly separates additions:

- **PKM core** — directly required by the proposal;
- **supporting product** — useful additions that improve delivery or recovery;
- **operational** — capabilities needed to administer and run the prototype.

See `proposal-requirements.md` for requirement-level traceability and each
component's `docs/ai/README.md` for current implementation truth. Target
behavior in this document is not evidence that the runtime is wired.

## North-star outcome

At the critical moment when a student attempts to access online gambling
content, Gamblock-AI should locally recognize the content, stop the access,
interrupt the impulsive pattern, offer a safe path into self-regulation
activities, and make unilateral removal of the protection meaningfully harder
through a trusted partner—without exposing browsing behavior to a server.

The product is a self-control and digital-wellbeing aid. It is not a clinical
diagnostic tool, a substitute for professional treatment, or a covert
surveillance product.

## Problem being addressed

The proposal identifies four connected problems:

1. DNS and static blacklist blocking is brittle because gambling operators
   rotate URLs, use dynamic domains, and camouflage content on otherwise
   trusted domains.
2. Blocking without behavioral follow-up can produce reactance, including use
   of VPN or proxy alternatives.
3. Students need support at the moment of impulse and beyond that moment,
   through structured self-regulation and psychoeducation.
4. A user in an impulsive state can remove ordinary browser blockers, so the
   protection needs a consent-based social-accountability layer.

## Primary audiences and actors

### Proposal actors

| Actor | Product name | Need and authority |
|---|---|---|
| University student | Protected Student / Member (`user`) | Owns their recovery journey, receives local protection and Pattern Interrupt, uses private self-regulation tools, requests removal approval. |
| Parent or peer | Accountability Partner (`partner`) | Consents to a trusted relationship and explicitly approves/denies protection-removal requests. Does not receive raw browsing data or private recovery text. |
| PKM team | Research and Product Team | Builds/evaluates the prototype, curates content, governs claims, and produces PKM deliverables. |
| Education institution or family | Adoption context | Potential future environment for voluntary, transparent use; not permission for covert monitoring. |

“Kepala” is an existing UI/business label for the partner/group supervisor. In
proposal-facing content, use “Accountability Partner (Pendamping)” first so it
is clear that the person may be a parent or peer and is not necessarily an
institutional authority.

### Supporting operational role

The codebase models one operational account role, `admin`, alongside `user`
and `partner`. Admins support content, releases, support, research, audit, and
platform operations and are not proposal actors. They never gain access to raw
browsing signals or unnecessary private recovery content.

### Adoption paths

The same `user` student experience supports two clearly labeled entry paths:

- **Self-directed recovery** — a student installs protection because they want
  to reduce gambling access and use the private web recovery journey.
- **Partner/institution-directed installation** (`PROD-SUP-ADOPT-001`) — a
  lecturer, campus program, or other partner may require installation through
  an external, transparent policy. This supporting adoption context does not
  create a fourth role, automatically create a relationship, or disclose
  whether someone has installed, declined, or not yet joined.

In both paths, the student reviews privacy boundaries, activates protection,
and explicitly previews/confirms any partner relationship and aggregate
sharing categories. Installation does not imply consent to monitoring,
recovery sync, or research participation. The proposal's core accountability
actor remains a parent or peer; lecturer/institution use is an adoption
extension and must not be presented as a PKM core actor.

## Core protection-to-recovery journey

1. **Transparent setup** — through either adoption path, the student installs
   the Android or Windows client, reviews permissions and privacy boundaries,
   and optionally links an Accountability Partner with mutual consent.
2. **Local sensing** — supported local interfaces obtain URL characteristics
   and/or page text. On Windows, the browser extension is a passive local DOM
   sensor for the service; it is a supporting implementation choice.
3. **Hybrid local analysis** — explicit URL rules and a Logistic Regression
   model using Bag-of-Words DOM features produce a local decision.
4. **Local block** — a positive decision blocks access without requiring a
   backend connection.
5. **Pattern Interrupt** — the native client presents an accessible 5–10 second
   visual intervention designed to create a pause, not to shame or diagnose.
6. **Recovery handoff** — the user is offered a privacy-safe route to the web
   psychoeducation hub. The detected URL, DOM, or model features are never
   placed in the link or sent to the web service.
7. **Self-regulation loop** — the student sets an intention, learns about
   impulses, checks mood, completes daily missions, reviews progress, and sees
   constructive skill recommendations.
8. **Accountability** — attempted removal enters a partner-approval flow. Safe
   emergency recovery exists for device access, with audit and abuse controls.
9. **Evaluation** — the team evaluates detection quality, false positives,
   latency, engagement/retention, platform resilience, usability, and the
   limited preventive claim defined by the research protocol.

## PKM core capability pillars

### 1. Multiplatform local protection

- Android and Windows prototype (`PKM-PLAT-001`).
- Background protection using OS-appropriate services (`PKM-PLAT-002`,
  `PKM-PLAT-003`).
- Real-time, offline-capable local blocking (`PKM-BLOCK-001`).
- Explicit platform coverage and limitations; no unsupported claim that every
  encrypted application/network stream can be inspected.

### 2. Hybrid On-Device AI

- Rule-based URL characteristics (`PKM-AI-001`, `PKM-AI-002`).
- DOM extraction from title, headings, and anchor text (`PKM-AI-003`).
- Bag-of-Words preprocessing and Logistic Regression (`PKM-AI-004`,
  `PKM-AI-005`).
- Local feature extraction, inference, and decision (`PKM-AI-006`).
- Evaluation against dynamic/camouflaged sites and false positives
  (`PKM-AI-007`, `PKM-BLOCK-002`).

Model training is in PKM scope. Runtime inference is in the client
repositories; reproducible Python/scikit-learn training, dataset governance,
and artifact evaluation require a dedicated model/research workstream.

### 3. Pattern Interrupt

- Automatic trigger after local detection (`PKM-INT-001`).
- Visual animation/video for 5–10 seconds (`PKM-INT-002`).
- Safe, non-clinical interruption framing (`PKM-INT-003`).
- Privacy-safe handoff to psychoeducation (`PKM-INT-004`).

### 4. Social Accountability Protocol

- Parent or peer partner relationship (`PKM-ACC-001`).
- Explicit approval before uninstall/removal (`PKM-ACC-002`).
- High-friction verification around relevant settings interactions within OS
  limitations (`PKM-ACC-003`).
- Safe resilience to ordinary process-kill/uninstall attempts without critical
  process APIs, lockout, or OS instability (`PKM-ACC-004`).

### 5. Web psychoeducation and Self-Regulation

- Post-block psychoeducation entry (`PKM-WEB-001`).
- Intention/change-goal setting (`PKM-WEB-002`).
- Impulse-awareness education (`PKM-WEB-003`).
- Mood tracking (`PKM-WEB-004`).
- Daily self-control missions (`PKM-WEB-005`).
- Constructive skill recommendations (`PKM-WEB-006`).
- A continuous goal → monitor → evaluate → adjust loop (`PKM-WEB-007`).

These seven requirements take priority over supporting dashboard polish. See
`website-product.md` for the full website specification.

## Supporting product capabilities

Supporting features are approved product direction but not evidence-backed
proposal mandates. They may be reprioritized without removing PKM core work.

### Onboarding and trust

- Account registration/login, Google OAuth, password recovery, and locale.
- Consent-led partner invitation with relationship expectations and expiry.
- Group Code onboarding as a convenient 1:N partner/member implementation.
- Device registration, protection-health status, permission/setup checklist.
- Privacy center explaining what stays local and what is voluntarily synced.
- Download/install guides and platform compatibility matrix.

### Recovery and wellbeing

- Encrypted private journal/reflections.
- Recovery streaks and progress summaries that avoid punitive gamification.
- Personalized weekly plan assembled from intentions, mood, and mission choices.
- Coping-plan builder for triggers and alternative actions.
- Skill/resource library for study, finance, sport, creativity, and social
  connection.
- Scheduled reminders controlled by the student.
- Help pathway to campus counseling, trusted contacts, and professional/crisis
  resources; never imply the app alone treats addiction.
- False-positive feedback and temporary safe review without uploading a URL.
- Data export/delete and consent withdrawal.

### Accountability and supervision

- Partner dashboard with protection health and consented aggregate progress.
- Approval queue with single-use, expiring links (including WhatsApp as an
  optional delivery channel).
- Batched, user-configurable notifications to reduce fatigue.
- Relationship pause, replacement, and revocation policies.
- Non-browsing weekly summaries and positive-support suggestions.
- Audit history for approval decisions and emergency recovery.

### Public education and dissemination

- Landing, impact, technology, privacy, FAQ/help, contact, and download pages.
- Interactive explanation of Hybrid AI and on-device privacy.
- Educational article/module library with reviewed sources.
- PKM project page for milestones, team, method, limitations, and outputs.
- Social-media content hub and reusable educational-video transcript/captions.
- Accessibility statement, data-policy changelog, and security contact.

### Operations

- Content-management workflows for psychoeducation and missions.
- Versioned model/ruleset release metadata and rollback.
- Support-case workflow and operational audit logs.
- Aggregate-only product health metrics.
- Admin policy management with least privilege.
- Infrastructure automation for backend/website delivery.

## Component responsibilities

| Component | Core responsibility | Explicit non-responsibility |
|---|---|---|
| Flutter Android/Windows client | Local inference/blocking, Pattern Interrupt, native service integration, protection status, onboarding | Must not upload raw detection inputs; UI presence alone is not runtime wiring. |
| Browser extension | Passive Windows browser DOM/URL sensor over authenticated loopback IPC | No classification, blocking, redirect, remote telemetry, or Pattern Interrupt. |
| Website | Self-regulation/psychoeducation, partner approval/supervision, public education, operations portals | No browsing-detail dashboard; not the real-time block authority. |
| Backend | Identity, consent/relationships, approvals, recovery content/state, encrypted voluntary text, aggregate events, release metadata | No remote classification and no storage of raw URL/DOM/history/screenshot data. |
| Model/research workstream | Dataset, labeling, BoW/vectorizer, Logistic Regression training, evaluation, artifact/version documentation | Must not depend on production browsing surveillance or unlicensed data. |
| Infrastructure | Deploy backend/website and operational storage safely | Does not deploy cloud inference or browsing-data collection. |

## Data boundary summary

### Must remain on device

- raw URL and domain;
- DOM text and extracted title/headings/anchor text;
- browsing history and screenshots;
- rule/model feature vectors and per-page classification score;
- block decision context and app/window identifiers that reveal activity.

### May be server-side with purpose, minimization, and consent

- account and role data;
- partner relationship and approval state;
- device/protection heartbeat stripped of browsing context;
- aggregate block counts over a stated period;
- intention, mood, mission, and progress data entered for the recovery service;
- encrypted journal/reflection text;
- support requests and consent/data-request records.

See `privacy-security.md` for the detailed classification and threat model.

## Product priorities

1. **P0 — proposal core loop:** local sensing → Hybrid AI → block → Pattern
   Interrupt → recovery handoff; partner-controlled removal; required recovery
   features; privacy boundary.
2. **P0 — evidence foundation:** dataset/training reproducibility, metric
   definitions, platform coverage, ethical intervention protocol.
3. **P1 — prototype usability:** onboarding, status, partner invitation and
   approval, reliable recovery content, false-positive/help paths.
4. **P2 — supporting depth:** journal, reminders, richer partner aggregates,
   public education, admin/CMS, release operations.
5. **P3 — optional exploration:** adaptive presentation, additional
   dissemination/community features, institution-facing rollout pilots.

Supporting work must not consume the evidence or integration work needed for a
P0 requirement without an explicit product-owner decision.

## Non-functional requirements

- **Privacy:** detection inputs stay local; server data follows purpose
  limitation, minimization, consent, retention, and access control.
- **Latency:** measure block latency using the protocol in
  `research-evaluation.md`; proposal target is below 200 ms.
- **False-positive safety:** prioritize legal, academic, and government
  controls in evaluation and provide a safe recovery/report path.
- **Offline behavior:** local protection and intervention do not depend on the
  website/backend; syncable supporting events queue safely.
- **Resource use:** profile the lightweight model and background services on
  representative devices; do not invent an unmeasured size/RAM guarantee.
- **Accessibility:** reduced motion, readable contrast, screen-reader support,
  captions, keyboard navigation, and non-visual alternatives are mandatory.
- **Psychological safety:** no shame, fear manipulation, diagnosis, or
  unsupported treatment claim; provide professional-help pathways.
- **Platform safety:** use OS-supported lifecycle/recovery mechanisms; never
  mark Windows processes critical.
- **Security:** least privilege, authenticated loopback IPC, expiring
  single-use approval tokens, encrypted sensitive recovery text, audit trails.

## Product success versus engineering checks

Product/PKM success is demonstrated by traceable requirements and the metrics
defined in `research-evaluation.md`: Precision, Recall, F1, FPR, latency,
retention/engagement, resilience, usability, safety, and PKM deliverables.

Lint, tests, and builds are engineering checks; they are not product outcomes.
The AI development workflow runs only the relevant linter by default. Tests
and builds are opt-in on explicit user request, while CI may retain automated
quality gates on repository events.

## Explicitly out of scope unless the proposal owners expand it

- Cloud or backend classification of browsing content.
- GPS/location tracking or private-chat inspection.
- Covert monitoring or partner access to raw browsing history.
- iOS protection prototype for the current PKM deliverable.
- Clinical diagnosis, medical treatment claims, or guaranteed recovery.
- Unsafe critical-process/BSOD-prone anti-tamper techniques.
- Automatic institution-wide surveillance without individual transparency,
  lawful basis, consent/governance review, and a separately approved scope.

## Unresolved product decisions

- Restore the proposal's missing phase text from the original source.
- Define real Android/Windows coverage and supported browser/app matrix.
- Decide dataset provenance, labels, splits, and numeric metric targets.
- Define retention and psychological-effect study protocols.
- Confirm partner relationship/recovery and emergency-unlock policy.
- Resolve exact server-side recovery-data consent and retention rules.
- Decide which supporting website features are required for the PKM demo
  versus a post-PKM roadmap.
