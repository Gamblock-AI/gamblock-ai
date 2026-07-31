# ADR-0005: Transparent adoption paths and a thin protection client

## Status

Accepted — 2026-07-31

## Decision

Gamblock-AI keeps exactly three account roles: `user` (student), `partner`,
and `admin`. A student may reach the same product through either of two
adoption paths:

1. **Self-directed recovery** — the student chooses to install protection and
   use the web recovery journey.
2. **Partner/institution-directed installation** — a lecturer, campus program,
   or other partner may require installation as an external adoption policy.
   This is supporting product capability `PROD-SUP-ADOPT-001`, not a new PKM
   actor or a new account role.

An installation requirement never bundles consent to a partner relationship,
aggregate sharing, recovery sync, or research. The student must still review
privacy boundaries, activate the client, and explicitly preview/confirm a
partner relationship and each aggregate-sharing category. The product does
not maintain a roster of people who have not installed, declined, or not yet
joined, and it does not auto-enroll accounts.

The Android/Windows client is intentionally thin. It owns local sensing,
classification, blocking, Pattern Interrupt, grounding, accountability
enforcement, aggregate protection status, and device-local opt-in reminders.
Intentions, check-ins, missions, education, skills, journaling, and weekly
review remain website capabilities. Pattern Interrupt's breathing cue and
5-4-3-2-1 grounding remain because they are part of the immediate local safety
intervention, not a duplicate recovery program.

## Rationale

- The two adoption paths converge on the same privacy and protection
  contracts, so they do not require separate student roles or code paths.
- The PKM proposal names a parent/peer accountability partner; institutional
  adoption is therefore documented as a transparent supporting expansion
  rather than silently rewriting proposal actors.
- Removing duplicate recovery engagement from the client reduces surface area,
  keeps detailed recovery in the web experience, and avoids sending local
  practice bookkeeping from the protection authority.
- Local notification delivery remains an Android utility because it is
  opt-in, private, and reliable without adding a web push/service-worker
  subsystem.

## Consequences

- Partner dashboards remain aggregate-only and only for relationships the
  student explicitly joins.
- Policy owners must document any institution-facing installation rule
  outside the application; the application must not infer compliance status.
- Website and Flutter capability documents must describe the same boundary.
