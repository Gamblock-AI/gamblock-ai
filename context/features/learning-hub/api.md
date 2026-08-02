# Learning Hub API Contract

Status: `implemented` for the student vertical slice, Phase 2 admin CMS, and Phase 3 review loop

Audience: authenticated student (`user`) and verified admin (`admin`)

All endpoints use the standard `{data,error,request_id}` response envelope.
The catalog is small enough for client-side filtering. Program and goal
selection must not be sent as query parameters.

## Student endpoints

### `GET /v1/learning-hub/catalog?locale=id`

Returns published clusters, programs, catalog items, and the current user's
non-sensitive progress state. It never returns reflection or outcome plaintext.

### `GET /v1/learning-hub/items/:slug?locale=id`

Returns one published item, including path steps and project instructions where
applicable.

### `GET /v1/learning-hub/progress`

Returns the current user's saved/started/completed item states.

### `PUT /v1/learning-hub/items/:id/state`

Request:

```json
{ "state": "saved" }
```

Allowed states are `saved` and `started`. State changes are idempotent.

### `POST /v1/learning-hub/items/:id/checkpoint`

Request:

```json
{
  "reflection": "Satu hal yang saya pelajari...",
  "outcome": "Ringkasan hasil mini-project..."
}
```

The service validates the item, encrypts supplied text, stores completion once,
and attempts one 10-EXP grant. The response reports whether EXP was granted or
the daily cap had already been reached.

## Phase 3 weekly review endpoints

### `GET /v1/weekly-reviews/current`

Returns the current `Asia/Jakarta` weekly review for the authenticated student.
The account-backed response contains bounded selections plus length-limited
adjustment and next-mission text. It contains no separate journal entry or
browsing content.

### `PUT /v1/weekly-reviews/current`

The active progress sheet sends `what_helped`, `what_was_hard`, `adjustment`,
`next_mission`, and `recommended_skill`. The backend also accepts the normalized
aliases `intention_id`, `outcome`, `helpful_action`, `next_mission_number`, and
`selected_skill_id`, upserts one encrypted schema-v3 `weekly_review` record for
the current week, and returns
`{review, exp_granted, cap_reached, experience}`. The reward is idempotent per
student/week and uses the shared 50-EXP Jakarta daily cap.

## Admin endpoints

The verified-admin surface is an operational capability supporting
`PKM-WEB-006`. It contains no individual student progress, checkpoint,
reflection, outcome, provider-account, or browsing data.

Items are created as `draft`. A complete bilingual item with a HTTPS source,
provider, review metadata, cluster/program mappings, and outcomes can move to
`in_review`; only an in-review item can be published. Publishing writes an
immutable snapshot. Editing a published item creates a new draft, so student
catalog reads remain on the last published snapshot until the next publish.
Archiving removes an item from the student catalog without deleting revisions.

- `GET/POST /v1/admin/content/learning-hub/items`
- `GET/PUT /v1/admin/content/learning-hub/items/:id`
- `POST /v1/admin/content/learning-hub/items/:id/submit-review`
- `POST /v1/admin/content/learning-hub/items/:id/publish`
- `POST /v1/admin/content/learning-hub/items/:id/archive`
- `GET /v1/admin/content/learning-hub/items/:id/revisions`
- `POST /v1/admin/content/learning-hub/items/:id/revisions/:revision_id/rollback`
- `GET /v1/admin/content/learning-hub/taxonomy`
- `POST /v1/admin/content/learning-hub/taxonomy/clusters`
- `PUT/DELETE /v1/admin/content/learning-hub/taxonomy/clusters/:id`
- `POST /v1/admin/content/learning-hub/taxonomy/programs`
- `PUT/DELETE /v1/admin/content/learning-hub/taxonomy/programs/:id`

Taxonomy DELETE is a soft deactivation. A cluster with active programs cannot
be deactivated or renamed until its program mappings are adjusted. Every
mutation is audited with its actor and stable target identifier; rollback also
requires an audit reason and restores a revision only as a new draft.
