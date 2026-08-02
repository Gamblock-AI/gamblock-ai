# Phase 5 — Finalization, Reporting, and Dissemination

Status: `implemented` repository preparation; external approval, submission, evaluation, and publication
records remain required

Scope: PKM core `PKM-DOC-001`, `PKM-DOC-002`, `PKM-DOC-003`,
`PKM-COMMS-001`, `PKM-COMMS-002`, and `PKM-PUB-001`; supporting product
`WEB-SUP-PUB-002`

## Authority and completion rule

Section 3.2.5 of the protected proposal requires the team to document the
program and disseminate its outputs through a progress report, final report,
application usage documentation, an educational video, and a scientific
article. Section 1.5 also requires the prototype and a social-media account.
The extracted final Phase 5 paragraph is truncated, so this contract uses only
the readable proposal text and the normalized requirements in
`proposal-requirements.md`.

Phase 5 has two distinct completion layers:

```text
repository-controlled preparation
= truthful drafts + user guide + traceability + production packages
+ public transparency surface + fail-closed evidence verifier

accepted PKM delivery
= approved immutable artifacts + actual submission/publication records
+ reviewed Phase 4 results + accountable owner/date/hash
```

Repository preparation cannot substitute for lecturer/team approval,
Simbelmawa submission, signed Android/Windows release evidence, a published
video, or an executed evaluation. A template or configured social link is not
an accepted deliverable.

## Requirement matrix

| Requirement     | Repository-controlled evidence                                                                                                        | External evidence required                                                                                   |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `PKM-DOC-001`   | Factual progress-report draft, approval-record schema, and submission-record schema.                                                  | Approved report artifact and real submission receipt.                                                        |
| `PKM-DOC-002`   | Final-report working draft that keeps unexecuted Phase 4 results explicit.                                                            | Reviewed final results, approved report, and real submission receipt.                                        |
| `PKM-DOC-003`   | Android/Windows installation and use guide, limitation register, full proposal traceability report, and release-record schema.        | Immutable versioned demo binaries, checksums/signatures as applicable, and reviewed device evidence.         |
| `PKM-COMMS-001` | Official-link register, eight-week content plan, publication-archive schema, and access-continuity procedure.                         | Verified account ownership, real publications, archive links/hashes, and tested account recovery/continuity. |
| `PKM-COMMS-002` | Reviewed-content candidate package: script, storyboard, Indonesian/English captions, source register, and review/publication schemas. | Rendered accessible video, accountable review, and real publication record.                                  |
| `PKM-PUB-001`   | Scientific-manuscript draft with method, evidence-state results, limitations, ethics, and verified references.                        | Phase 4 results, author approval, venue formatting, and submission/publication record if pursued.            |

## Evidence package

The canonical repository package is `deliverables/phase5/`. Its verifier is:

```sh
python3 deliverables/phase5/verify_evidence.py \
  deliverables/phase5/evidence-manifest.json
```

Copy `evidence-manifest.example.json` to `evidence-manifest.json` only when
assembling the real immutable evidence set. The verifier must fail while any
required artifact is missing, unapproved, unhashed, internally inconsistent,
or still contains an incomplete marker. That failure is an honest status, not
a tooling defect.

Every accepted artifact descriptor records:

- relative path and SHA-256;
- accountable owner/reviewer and date;
- approval state;
- publication restriction;
- submission or publication URL/receipt when required;
- related PKM requirement and report section.

The package must connect to the final Phase 4 evidence manifest rather than
copying raw study or browsing data into reports.

## Public transparency

The website route `/pkm` is the supporting `WEB-SUP-PUB-002` publication
surface. It presents the project objective, method, evidence maturity,
milestones, safeguards, limitations, and deliverable states. It must not expose
draft reports as approved or link to unpublished evidence. Report, video, and
article links become public only after the corresponding review and
publication record exists.

## Privacy, ethics, and claim controls

- Reports, video assets, social posts, and the article never include raw URL,
  domain, DOM, browsing history, screenshot, per-page score, credentials, or
  identifiable research rows.
- Product consent, partner consent, research consent, and media/testimonial
  consent remain separate.
- Public evidence uses aggregate results with declared sample/device/cohort,
  suppression, limitations, and reviewer metadata.
- The terms `evaluated`, `effective`, `accurate`, and `below 200 ms` require
  the accepted Phase 4 evidence package; supplied model metrics are not used as
  project results.
- Gamblock-AI is described as a digital self-control and prevention-support
  prototype, not a clinical treatment, cure, or guarantee.
- Educational video captions, meaningful alt text, reduced-motion treatment,
  and non-color status cues are mandatory.

## Delivery workflow

1. Freeze the implementation/runtime, model, rules, and content versions.
2. Complete and approve the Phase 4 evidence manifest.
3. Replace draft result statements in the reports and manuscript only from
   reviewed aggregate evidence.
4. Review the progress report, final report, guide, video, social content, and
   manuscript for academic, psychological, privacy, accessibility, and claim
   safety.
5. Render immutable deliverables and calculate SHA-256 hashes.
6. Submit or publish through the owner-authorized channels.
7. Record receipts, URLs, reviewers, dates, restrictions, and hashes in the
   Phase 5 evidence manifest.
8. Run the verifier and publish only artifacts whose gate passes.

## Current completion truth

As of 2026-08-02, repository-controlled Phase 5 preparation is implemented:
the deliverable drafts/packages, public transparency route, and fail-closed
evidence contract exist. Accepted PKM delivery remains `blocked` on external
actions and Phase 4 evidence: owner-provided original proposal restoration,
academic/ethical review, real-device and UTY evaluation, report approval and
submission, account ownership verification, video rendering/review/publication,
and manuscript approval. Those actions must never be synthesized or
self-approved by automation.
