# UI and Experience Context

## Experience intent

The design language is **Trust & Recovery**: calm, optimistic, human, and
transparent. It should help a student pause and take the next constructive
step without shame, fear, or covert surveillance. The mascot may add warmth,
but serious approval, privacy, help, and research-consent moments remain clear
and direct.

The website and Flutter client share brand tokens and interaction principles.
They do not have to mirror layout exactly: protection/intervention follows
platform-native safety and accessibility patterns, while the website supports
longer recovery, education, and administration workflows.

## Audiences and jobs to be done

### Protected Student

- understand what protection can and cannot see;
- finish setup without guessing about permissions;
- pause safely after an attempted access;
- identify mood/urge and choose one manageable action;
- learn without being lectured;
- review progress privately and adjust goals;
- ask a trusted partner for accountable support;
- find help and regain device access safely when something goes wrong.

### Accountability Partner

- understand consent, responsibilities, and privacy limits;
- resolve a removal request confidently;
- see only useful aggregate support information;
- respond supportively rather than punish;
- manage notification load and relationship lifecycle;
- find an abuse/support route for exceptional situations.

### PKM/operations team

- manage reviewed content and artifacts with clear status/version;
- understand aggregate prototype health without browsing visibility;
- publish accurate evidence/limitations and required PKM outputs;
- handle support, data requests, and emergency actions with audit/least
  privilege.

## Core experience loop

```text
local block
  -> Pattern Interrupt (5–10s, accessible)
  -> choose: recovery check-in / grounding / help / later
  -> intention + mood/urge + daily mission
  -> education and skill alternative
  -> weekly private review and adjustment
```

The experience must preserve this proposal-derived loop. A generic analytics
dashboard, journal, or marketing page is not a substitute for intention,
impulse education, mood tracking, missions, and skill recommendations.

## Visual foundation

### Theme

Light-first. Use near-white/soft-blue surfaces, navy for trust and hierarchy,
crimson sparingly for urgency/destructive actions, cyan for protective-system
signals, sage for constructive progress, and amber for attention. A future
dark mode is supporting scope and must not delay core accessibility.

Landing, authentication, and authenticated website shells share the canonical
cyan-blue mesh background. Dashboard panels use a scoped higher-contrast token
layer over that mesh so consistency never reduces form, text, border, or focus
visibility.

Avoid casino/gambling visual vocabulary: neon spectacle, gold jackpots,
spinning wheels, chips/cards, confetti rewards, countdown pressure, variable
rewards, or “winning/losing” recovery language.

### Brand palette

| Token | Hex | Use |
|---|---|---|
| Navy primary | `#16294C` | Primary action, headings, body emphasis |
| Navy light | `#24487F` | Hover/focus-supporting state |
| Navy dark | `#0D1B35` | Deep text/surface contrast, footer |
| Crimson accent | `#C8102E` | Destructive/critical action only; never routine progress |
| Crimson light | `#E63B51` | Hover/active destructive state |
| Crimson dark | `#9D0C24` | High-contrast critical text/border |
| Sky cyan | `#3DD6F5` | Protection/technology accent and Gami LED |
| Sky light | `#BFE9F5` | Soft decorative/protection surface |
| Azure | `#DCEBFB` | Background wash/container fill |
| Sage success | `#2F9E6F` | Completion, recovery, safe status |
| Amber | `#E0A516` | Needs attention, pending approval, permission warning |

Website components use semantic CSS tokens in `app/globals.css`; Flutter uses
semantic values from `AppColors`. Do not hardcode raw hex inside feature
components. Verify text/icon contrast in every semantic state.

### Surface tokens

| Surface | Web | Flutter | Approximate hex |
|---|---|---|---|
| Background | `--background` | `AppColors.background` | `#F4F9FE` |
| Card | `--card` | `AppColors.surface` | `#FFFFFF` |
| Muted | `--muted` | `AppColors.muted` | `#EAF0F6` |
| Border | `--border` | `AppColors.border` | `#E3ECF5` |

### Typography

| Role | Font |
|---|---|
| Web UI/display | Plus Jakarta Sans, Inter fallback |
| Web mono | Geist Mono |
| Flutter UI | Plus Jakarta Sans with safe platform fallback |

Prefer sentence case, short paragraphs, descriptive buttons, and direct
Indonesian. Avoid all-caps warnings except compact status labels. Numeric trend
views explain units and periods in text, not color alone.

### Shape and elevation

- Base radius `1rem`; compact UI about 12–16px, cards about 22–30px, modals up
  to 42px, pills `999px`.
- Shadows are soft and functional (`--shadow-soft`, `--shadow-card`,
  `--shadow-float`), never glossy casino-style depth.
- Prefer one clear container hierarchy. Avoid nested cards for every text
  fragment.
- Dashboard card identity icons use the navy icon tile by default. Sage, amber,
  and crimson icon tiles are reserved for confirmed success/progress, pending
  or attention states, and critical/destructive states respectively; do not
  alternate icon colors merely to decorate adjacent cards.
- Dashboard card and notice headers place the icon and title on the first row,
  with compact status or actions at the end. Supporting descriptions use the
  available width below that row instead of remaining squeezed beside the
  icon.

## Component systems

- **Web:** Tailwind + shadcn/ui base-nova primitives in `components/ui/`.
  Compose protected primitives; do not casually rewrite generated UI files.
- **Flutter:** Material 3 with `AppTheme.light` and brand widgets in
  `lib/core/widgets/` (`Pressable`, `GlassCard`, `EyebrowPill`, `IconChip`,
  `SkeletonBox`, `EmptyState`).
- **Icons:** Lucide React on web; Material icons on Flutter. Pair unfamiliar or
  high-stakes icons with text.
- **Mascot:** “Gami”, a chibi guardian robot with navy body, crimson emblem,
  and cyan LED face. Canonical tracked reference: `assets/gami-maskot.png`.
  A generated pose set (`gami-{meditate,thumbsup,peek,wave,celebrate,point}`)
  ships in the website's `public/images/mascot/` (webp) with the four poses
  the client needs copied into the Flutter `assets/images/`; regenerate poses
  from the shared character description rather than editing them by hand.

Use Gami as a guide/supporter in onboarding, education, encouragement, empty
states, and public explanation. Sanctioned calm-engagement mechanics (all
additive, deterministic, criteria always readable, never punitive): cosmetic
level rewards (decor items, mascot poses, hero accents, a second room theme),
a tiered recovery-room decor economy with placement slots, capped daily EXP
for completed practices, a single calm level-up dialog (no confetti/sound), a
non-punitive presence-rhythm line ("hadir N hari" — never a breakable
streak), a curated mood-by-urge Gami dialog bank with deterministic daily
variants, daily myth-vs-fact and quick-quiz retrieval practice, fictional
response-practice scenarios, a private device-local "what you kept"
estimator (baseline never sent), a private weekly recap, and an opt-in daily
check-in reminder with neutral lock-screen copy. Positive-reinforcement moments — a supportive
reply to the selected check-in mood and a participation-focused celebration on
the progress page — are sanctioned Gami uses; keep them warm, brief, and free
of clinical or perfection language. Do not use a cheerful mascot to soften
consent, data deletion, denied approval, crisis/help, or destructive-action
warnings.

## Pattern Interrupt UX

This section implements `PKM-INT-001`, `PKM-INT-002`, `PKM-INT-003`, and
`PKM-INT-004`.

Pattern Interrupt is native client behavior, not a website redirect page.

### Required behavior

- appears immediately after a local positive decision;
- lasts 5–10 seconds as specified by the proposal;
- creates a pause with one focal visual and minimal copy;
- does not reveal the detected URL/title/content;
- remains functional offline;
- ends with clear options: recovery check-in, grounding/help, or later according
  to the approved behavior;
- hands off to web without browsing parameters.

Approved in-pause presentation: a synced breath-phase cue (inhale/exhale text
with a static combined cue under reduced motion), a thin digit-free ring that
visualises the sanctioned pause filling up (never urgency styling), stable
height-reserved layout so nothing jumps when the pause ends, and gentle
haptics. The grounding option is an interactive 5-4-3-2-1 stepper — one sense
per step with progress dots and a calm completion state — and an exit back to
protection stays visible on every step.

### Psychological safety

- No flashing/strobing, jump-scare audio, humiliation, threats, guilt, loss
  amounts inferred by the app, or simulated emergency alerts.
- Provide reduced-motion behavior, captions when audio exists, and a
  non-animated equivalent.
- Respect platform accessibility settings; do not rely on color/motion alone.
- Use supportive copy such as “Ambil jeda sejenak” and “Pilih langkah kecil
  berikutnya”, not “Kamu gagal lagi”.
- Avoid clinical treatment claims. “Pattern Interrupt” is a micro-intervention,
  not shock therapy in the medical sense.

Stimulus assets require content, psychology, accessibility, provenance/license,
and device-performance review before release.

## Recovery feature patterns

### Intention setting

- One concise personal reason plus one achievable next action.
- Private-by-default label visible near the field.
- Edit/pause/archive without punitive confirmation.
- Optional reminder and review date.
- Empty state explains why an intention helps and offers an example without
  pre-filling sensitive content.

### Mood and urge check-in

- Use labeled scales with text/icons. The urge question names the behavior
  plainly (“Seberapa kuat dorongan untuk berjudi hari ini?”) and its scale
  starts at an explicit “Tidak ada dorongan” (none) point rather than an
  appended opt-out, so a calm day is a real answer instead of a refusal.
- Selecting a mood may show a short supportive Gami response (warm, first
  person, never clinical); the mascot reinforces honesty, it never gates or
  judges the answer.
- Ask no more than necessary on the quick path.
- Trigger category is user-selected, never inferred from browsing.
- Show privacy audience before optional free text.
- If a value indicates distress, offer help resources without claiming a
  diagnosis or automatically alerting a partner unless an explicit approved
  safety protocol says otherwise.

### Psychoeducation

- State learning objective, estimated time, source/reviewer, and last review.
- Break content into short sections with reflection/action prompts.
- Knowledge checks teach; they do not shame wrong answers.
- Completion is visible but optional; content remains revisit-able.
- Library cards use the first ordered thumbnail as the cover; additional
  thumbnails appear in an accessible carousel inside the module.
- Uploaded media may render inline. External media shows a consent gate before
  contacting its provider, and PDFs also provide a new-tab fallback.
- Admin authoring keeps Indonesian and English content adjacent in one
  workspace, uses a structured WYSIWYG document, and crops thumbnails to 16:9
  before upload.

### Daily missions

- Present one primary mission and a way to choose an alternative.
- A supporting FAB may also show two clearly optional bonus tasks and personal
  EXP progress. Keep the main task visually dominant and bonuses compact.
- Show each fixed EXP value before action and distinguish “not verified”,
  “ready to claim”, and “claimed” with text plus iconography. Level progress
  may carry deterministic, forward-only journey titles (shared verbatim
  between website and client), and participation may unlock additive-only
  journey badges whose criteria are always visible — never mystery boxes,
  never rankings, never losable. The claim control
  is enabled only from server-derived eligibility; the task card itself is not
  a completion toggle. Never use random rewards, spins, loot, loss-framed
  streaks, countdown pressure, or casino celebration language.
- The daily task boundary and deterministic rotation use `Asia/Jakarta`.
- States: available, in progress, completed, skipped, replaced.
- Skipping never becomes a public failure or breaks all progress.
- End with a short optional reflection and next-step suggestion.

### Skill recommendations

- Show category, time/effort, why suggested, and dismiss/save controls.
- Never imply personalization from browsing history.
- Offer diverse low-cost and accessible alternatives.
- Avoid recommendation loops optimized only for engagement time.
- A supporting student-only skills page pairs short internal practices with a
  curated list of free external course/certification platforms. External
  entries are plain outbound links (new tab, no account or browsing data);
  label costs honestly and prefer free or audit-mode options.

### Weekly review

- Use a calm sequence: intention → trends → what helped → adjustment → next
  plan.
- Warn when data is insufficient; never fabricate a trend.
- Keep private detail separate from any partner-shared aggregate.
- Celebrate participation/learning, not perfect abstinence or competitive rank.

### Recovery room and calendar

- The student recovery hub is framed as daily self-control missions: the
  server-verified daily mission card leads the page, and the practice
  activities use mission-oriented, positive-action copy. The reflective
  journal and support routes stay clearly available beside the missions.
- The hub may use a calm 2.5D dorm-room scene, but every
  hotspot also has a 44px semantic button and an equivalent labeled mobile
  dock action. The scene is orientation, not the only navigation mechanism.
- Window starts a three-minute urge-surfing sequence, rug guides 5-4-3-2-1
  grounding, desk starts a ten-minute focus sprint, notebook opens the
  encrypted reflection journal, and phone opens partner/support choices.
- Active timers and draft task labels are browser-local. A completed practice
  can ask only for lighter, same, heavier, or prefer-not-to-say feedback.
- Decor unlocks are deterministic evidence of participation. Do not add random
  drops, currencies, leaderboards, streak-loss warnings, or confetti.
- Progress uses a 7/30/90-day calendar with selectable populated days and a
  category legend. Empty days are neutral; trend language is unavailable below
  three check-ins. Weekly review is a short guided sequence rather than another
  unstructured note card.

## Accountability UX

### Relationship setup

- Both student and partner see role, permissions, visibility limits, removal
  responsibility, emergency/help route, and how to end/replace the relationship.
- Student enters a group code, previews the named group and verified partner,
  then confirms membership as a separate active decision.
- Partner verifies email and WhatsApp before group creation, can rotate a code,
  and cannot archive a group with live members.
- Unsafe exit is visually distinct from normal exit and explains that sharing
  stops immediately; it is never hidden behind color alone.
- Aggregate-sharing controls are staged: students review changes, then use
  explicit Save or Discard actions instead of committing on every toggle.
- Normal exit remains reversible while its request is pending. Cancelling it
  restores the active relationship and prevents a later partner decision on
  that request.
- Unsafe exit has no direct undo because sharing stops immediately. The UI
  presents a clear support-review path for rebuilding the relationship safely.

### Removal approval

- Student sees request status, expiry, and what the partner can see.
- Partner sees only the scoped request and optional student-authored reason.
- Approve and deny are equally clear; high-impact action has confirmation.
- Status vocabulary: pending, approved, denied, expired, cancelled, emergency
  review.
- Token links handle invalid/expired/already-used states without leaking token
  detail or requiring unrelated login.
- Copy encourages a supportive conversation, not punishment.

### Aggregate partner dashboard

Use broad period summaries and protection-health states. Never show URLs,
titles, page timelines, raw mood/intention/journal, hidden risk scores, or
member rankings. Make the privacy boundary visible in the interface so an empty
detail view is understood as intentional protection, not missing data.

### Support, progress, and recovery

- Support uses one readable thread per case with author, timestamp, status,
  reply field, and close/reopen actions; badge copy accompanies every color.
- Student progress offers 7/30/90-day ranges, an insufficient-data state below
  three check-ins, and a privacy warning before client-side CSV/PDF export.
- Partner progress never reuses the student trend response; it renders only
  per-category aggregates or an explicit “not shared” state.
- Recovery drafts are labeled local and unsent. Account-saved records are
  labeled encrypted, reminders are off by default, and partner recovery pages
  are guidance—not a hidden route into student records.
- Partner recovery guidance may use a CMS-authored response simulator with
  reviewed scenarios, visible rationale, retry, and completion progress. It
  must never load student practice, journal, mood, focus-task, or room state.

## Information architecture patterns

- **Public:** full-width educational/marketing sections; evidence and privacy
  explanations before aggressive download CTAs.
- **Auth:** split layout may use brand art, but forms remain the visual focus.
- **Student dashboard:** “Today” first—intention, quick check-in, daily mission,
  next skill—then recovery library and progress.
- **Partner dashboard:** linked-member status, approval queue, privacy-safe
  aggregate, support guidance.
- **Admin dashboard:** attention counts and concise links to each operational
  work area; it does not present a requester support form.
- **Operations:** the `admin` navigation exposes Content, AI Releases, Tickets,
  Emergency Access, Platform, and Research as separate destinations. Dense but
  readable tables/forms show immutable role, verification/status, one-time
  temporary-password handoff, audit, and destructive-action confirmation.
- **Flutter:** four labeled destinations—Dashboard, Analytics, Partner, and
  Settings. Widths below 720dp use bottom navigation; wider Android/Windows
  layouts use a navigation rail and constrain content to 1120dp. Setup is an
  optional dashboard task, while Pattern Interrupt remains outside the shell.

Detailed website sitemap and feature states are in `website-product.md`.

## Motion and micro-interactions

- GSAP is for public storytelling; Framer Motion for small web transitions and
  press feedback; Flutter uses shared tactile/transition helpers.
- Respect `prefers-reduced-motion` / platform reduce-motion everywhere.
- Motion must clarify state or hierarchy. Never animate sensitive values for
  spectacle.
- Route transitions are subtle fade/slide; loading uses skeletons only where
  shape is predictable.
- Buttons show hover, focus, active, disabled, loading, and success/error
  feedback without layout shift.
- Haptics are optional and meaningful; no haptic punishment for lapse/denial.

## Accessibility baseline

- WCAG 2.2 AA target for website flows.
- Full keyboard and visible focus order.
- Semantic headings, landmarks, form labels, instructions, and errors.
- Screen-reader status announcements for asynchronous approval/recovery actions.
- Touch targets at least platform guidance; no precision-only gestures.
- Contrast checked for all semantic states.
- Zoom/reflow and Indonesian text expansion supported.
- Reduced motion and non-visual Pattern Interrupt alternatives.
- Captions/transcripts for educational video and meaningful audio.
- Alt text for informative images; decorative art hidden.
- Do not encode trend/status using color alone.

## Content tone

Use:

- empathetic, concise, non-judgmental Bahasa Indonesia;
- “kamu/Anda” consistently per selected product voice;
- practical choices and transparent consequences;
- “pendamping” explanations and privacy reassurance;
- evidence-aware phrases such as “dirancang untuk membantu” and “hasil awal”.

Avoid:

- “pecandu”, “lemah”, “gagal”, “nakal”, or moral condemnation;
- promises to cure/prevent all gambling;
- unsupported “100% accurate/secure/private” claims;
- fear-based partner copy;
- jargon without an explanation;
- fake urgency or forced countdown outside the defined intervention duration.

## Error, empty, and degraded states

- Explain what happened, what remains safe, and the next action.
- Protection degraded/offline messages distinguish local protection status from
  backend connectivity.
- No data means “not enough data”, never “perfect recovery”.
- Partner unavailable or token expired routes to a defined safe support path.
- False-positive path does not request/upload the blocked URL by default.
- User-facing messages remain friendly and non-technical in every environment.
  Sanitized technical detail is limited to the development console and is
  suppressed from production browser diagnostics.

## Design review checklist

- Which proposal requirement or labeled supporting feature does this screen
  serve?
- Is the student or partner audience and data visibility clear?
- Does it preserve the local browsing-data boundary?
- Are privacy, consent, offline, loading, empty, error, and permission states
  designed?
- Does it avoid shame, clinical overclaim, casino mechanics, and dark patterns?
- Is reduced-motion/keyboard/screen-reader behavior defined?
- Does the current implementation status remain separate from the target mock?
- Were only the relevant linter/context checks run by default, with tests/builds
  left for explicit user request?
