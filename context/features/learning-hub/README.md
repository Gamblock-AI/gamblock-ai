# Learning Hub and Focused Gamification

Status: `Phase 1, Phase 2, and Phase 3 implemented`

Scope: supporting product around `PKM-WEB-005`, `PKM-WEB-006`, and
`PKM-WEB-007`

Pilot audience: students across all Universitas Teknologi Yogyakarta (UTY)
programs

## Document map

- `api.md` — student, CMS, and weekly-review API contracts;
- `catalog.md` — UTY taxonomy, baseline composition, and source policy;
- `seeding.md` — production-safe idempotency rules and baseline counts;
- `assets.md` — optional supporting visuals that must not block the text-first
  experience.

## Product intent

Gamblock's primary job remains local protection, Pattern Interrupt, and the
privacy-preserving recovery loop. Learning Hub is a constructive alternative
that gives a student a meaningful next action after recovery, not an endless
course marketplace.

The student journey is:

```text
Protection → Pattern Interrupt → recovery choice → next action
→ constructive learning/project activity → reflection → weekly adjustment
```

## Information architecture

The authenticated student shell groups existing routes into:

- **Today**: protection status, check-in, one next action, and a compact EXP
  milestone.
- **Recover**: grounding, Recovery Room, psychoeducation, intention, and
  journal.
- **Learn & Grow**: the Learning Hub.
- **Progress**: weekly review, private trends, and milestones.
- **Protection**: devices and Accountability Partner.
- **Support**: safety and technical support.

Existing route URLs remain available during the pilot. The `/skills` route is
the compatible URL for Learn & Grow.

## Learning Hub interaction

Every visit starts with a transient selector:

1. program;
2. optional goal (`basics`, `career`, `portfolio`, `certification`,
   `exploration`);
3. optional time, difficulty, language, and cost filters.

Program and goal selections remain in page state only. They are not saved to
the account, local storage, analytics, or API query parameters.

Phase 1 also includes local-only filters for suggested starter-session time,
difficulty, language, and cost. Starter-session time helps a student choose a
realistic first action; it is not presented as the provider's full course
duration. Filters are applied after the catalog response arrives and do not
alter the privacy boundary.

The catalog has four views:

- learning paths;
- courses and certifications;
- mini-projects;
- career snapshots and toolkits.

Every published item explains its relevance, outcome, suggested starter time,
difficulty, language, cost, certificate status, source, and last review date. External
links open in a new tab with `noopener noreferrer` and never include account or
browsing context.

Progress states are `saved`, `started`, and `completed`. A course or project
completion may include a short private reflection/outcome. A completion is
self-attested; the product does not upload proof or integrate provider
accounts.

## Focused gamification

The existing five daily mission slots remain the compatibility contract. Each
slot is worth 10 EXP and the daily boundary is `Asia/Jakarta`.

The main screen shows one deterministic “next action”. The full five-slot
list, custom mission creation, and remaining capacity remain available in a
secondary panel. No mission becomes a higher-value primary mission.

All new EXP grants use an idempotent grant record while the historical
`user.experience_points` total remains authoritative. The shared daily cap is
50 EXP. Skill and weekly-review checkpoints earn 10 EXP only once per item or
review window and only when the cap has room.

Level progress remains 100 EXP per level. Gami poses, titles, Recovery Room
decorations, and themes unlock deterministically at existing milestone
thresholds. There are no leaderboards, purchases, chance rewards, loot boxes,
punitive streak resets, or casino-like celebration language.

## Privacy

Learning Hub progress belongs only to the student. Reflection and mini-project
outcome text use the existing AES-256-GCM encrypted-text workflow. No selected
program, goal, course click, external provider account, URL, domain, DOM text,
or browsing history is sent to the backend.

## Phase 2 editorial operations

The admin-only `/admin/learning-hub` workspace manages bilingual item drafts,
UTY clusters, and study-program taxonomy. It supports draft, review, publish,
archive, immutable revision history, and reasoned rollback. Published catalog
reads use the immutable published snapshot, never an editor's current draft.

Administration is an operational supporting capability for `PKM-WEB-006`.
Admin responses intentionally exclude student progress and encrypted checkpoint
text. Taxonomy deletion deactivates records rather than removing historical
mapping data; an in-use cluster must be remapped before deactivation.

## Phase 3 self-regulation loop

The structured weekly-review vertical slice implements the readable
`PKM-WEB-002`/`PKM-WEB-007` self-regulation loop. The authenticated progress
sheet restores the current review from the backend and pushes saves to
`PUT /v1/weekly-reviews/current`. The backend upserts one encrypted
weekly-review record per Jakarta week, preserves legacy fields, and awards one
idempotent 10-EXP grant per review window under the shared daily cap. The
response includes the current review, cap state, and experience so the shared
level chip can converge without a second reward path.

The Phase 3 boundary deliberately excludes browser notification delivery,
partner access to private review/check-in data, and any browsing-derived
personalization.

## Pilot acceptance

- Each of the 22 UTY programs maps to a primary cluster and at least one
  learning path or project.
- A student can reach a relevant path in three decisions or fewer.
- A catalog click never grants EXP.
- Repeating a checkpoint cannot grant EXP twice.
- Dashboard interaction presents one clear next action without an unclosable
  modal.
- Existing missions, points, level, and Recovery Room unlocks remain readable.
