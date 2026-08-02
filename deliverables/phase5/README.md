# Phase 5 Deliverable Package

This directory contains the repository-controlled preparation for PKM Phase 5.
It is deliberately safe to review and version: no raw browsing data,
participant rows, credentials, approval tokens, or private recovery content
belongs here.

## Package map

| Directory             | Deliverable                                                          | Requirement                  |
| --------------------- | -------------------------------------------------------------------- | ---------------------------- |
| `reports/`            | Progress and final report drafts plus approval/submission schemas    | `PKM-DOC-001`, `PKM-DOC-002` |
| `prototype/`          | Android/Windows guide, limitations, release schema, and traceability | `PKM-DOC-003`                |
| `social-media/`       | Account register, content plan, archive, and access continuity       | `PKM-COMMS-001`              |
| `educational-video/`  | Script/storyboard, captions, sources, and review/publication schemas | `PKM-COMMS-002`              |
| `scientific-article/` | Evidence-aware manuscript and bibliography                           | `PKM-PUB-001`                |
| `media-kit/`          | Fact sheet and public-claim guide                                    | supporting `WEB-SUP-PUB-002` |

All narrative artifacts are complete working drafts, not approvals. They use
the weakest evidence label supported by the workspace. In particular, Phase 4
is `instrumented`, not `evaluated`, so final numerical and causal claims remain
absent.

## Finalization

1. Complete the Phase 4 evidence package and freeze implementation versions.
2. Have accountable academic, technical, psychology, privacy, and accessibility
   reviewers approve the applicable artifacts.
3. Render immutable report/video/release artifacts outside generated build
   directories and record their SHA-256 values.
4. Submit or publish only through owner-authorized channels.
5. Copy `evidence-manifest.example.json` to `evidence-manifest.json`, replace
   every `REQUIRED` value with real evidence, and set approvals only after the
   review occurred.
6. Run:

   ```sh
   python3 deliverables/phase5/verify_evidence.py \
     deliverables/phase5/evidence-manifest.json
   ```

The verifier intentionally returns non-zero for the committed example. Never
change it merely to make an incomplete package pass.

## Publication boundary

Drafts may be shared with the project team and reviewers. Public publication
requires the per-artifact restriction and review record to permit it. Dataset,
device, study, and security-sensitive evidence stays in its governed Phase 4
location; Phase 5 cites its aggregate report and hash instead of copying raw
inputs.
