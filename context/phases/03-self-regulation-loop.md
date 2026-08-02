# Phase 3 — Self-Regulation Loop

Status: `implemented` for the structured weekly-review vertical slice

Scope: PKM core `PKM-WEB-002` and `PKM-WEB-007`, plus supporting weekly-review EXP

## Decision

The extracted academic proposal does not contain a reliable Phase 3 section, so
this phase is defined from the explicit, readable product contract rather than
invented proposal text. Phase 3 completes the loop:

```text
intention → private check-in → mission/skill action → weekly review
→ adjustment → next week
```

The intention manager remains local-first. Only the separately consented
intention title/status sync continues to use `/intentions`. Weekly review data
contains bounded selections plus length-limited adjustment and next-mission
text. It contains no URL, DOM, browsing history, or provider account data. The
backend encrypts the complete review payload before persistence.

## Implemented contract

- `GET /v1/weekly-reviews/current` restores the current Jakarta week review.
- `PUT /v1/weekly-reviews/current` upserts one review for the current Jakarta
  week, normalizes the website fields, and returns the review, EXP result, cap
  state, and current experience.
- A review saves under the existing encrypted `weekly_review` recovery-record
  workflow and reuses the server record ID on subsequent saves.
- A successful review earns one idempotent 10-EXP grant keyed by
  `(user, weekly_review, week_start)` and shares the existing Jakarta daily cap
  of 50 EXP.
- The authenticated progress sheet reads the current review from the endpoint,
  writes through that same account-backed flow, publishes the returned
  server-authoritative experience snapshot, and refreshes review/room queries
  concurrently.

## Acceptance evidence

- A review can be saved, refreshed, and restored without a duplicate record.
- Re-saving the same week cannot grant EXP twice.
- A full daily cap reports `cap_reached` without failing the review save.
- The authenticated response contains the current user's decrypted review
  fields, but no separate journal entry or browsing data.
- Existing legacy weekly-review fields remain readable during migration.

## Remaining outside this phase

- Android-local reminder delivery remains a client delivery utility, not a web
  notification claim.
- Partner visibility of raw check-ins remains planned until consent and
  revocation semantics are explicitly designed.
