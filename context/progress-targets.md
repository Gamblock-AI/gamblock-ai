# PKM-KC Versioned Progress-Report Target Registry

This registry separates academic reporting targets from the report files that
quote them. The proposal remains the authority for PKM intent. A report copy
is the authority for what that specific version claims. This file records the
target history and the decision needed before a target can be used by a later
report or test runner.

## Version boundary

- `laporan-kemajuan-v5.md` is a frozen source snapshot. Do not edit it to add
  later measurements, new targets, or retrospective corrections.
- A future `laporan-kemajuan-v6.md` will be created by copying v5. It is not
  created by this registry and must not be assumed to exist yet.
- `progress-testing.md` remains a live status map for evidence. It may update
  `pending`, `partial`, or `passed (recorded)` status, but it does not redefine
  the target of an existing report version.
- `gamblock-ai-testing/docs/config/targets.json` remains the active v5 machine
  configuration until a later report version is explicitly activated.

The same target may be retained in a later report, but it must still be
referenced by its report version and target ID. A new target is never silently
inserted into an older report's table.

## Target lifecycle

| Status | Meaning | Effect on v5 runner/report |
| --- | --- | --- |
| `proposed` | A candidate target or change has been recorded for discussion. | None. It is documentation only. |
| `approved` | The PKM team/owner has accepted the target for a future report version. | None until that report version is activated. |
| `active` | The target is assigned to the current report version and its runner configuration. | It may gate the active report/evidence. |
| `retired` | The target is no longer used for new evidence but is retained for history. | It cannot change historical results. |

Every change entry must include a stable target ID, intended report version,
status, metric or behavior, threshold, scope, evidence requirement, reason,
and effective date or activation condition. A status change is an append-only
decision in this file; do not rewrite the meaning of an older report.

## Frozen baseline: laporan kemajuan v5

The following targets are the baseline currently represented by the v5
context and active testing configuration. Their status is `active` for v5;
their presence here is a record, not permission to edit the v5 report.

| Target ID | Area | v5 target | Evidence boundary |
| --- | --- | --- | --- |
| `v5-detection-pkm` | Hybrid detection | Accuracy, precision, recall, and F1 >=95%; FPR <=2% on a leakage-safe split. | Must be a named, leakage-safe result; historical or provisional metrics do not qualify. |
| `v5-artifact-local` | On-device artifact | The Hybrid artifact actually loaded by Android/Windows is under 5 MB combined and passes hash/provenance/parity checks. | Source ONNX provenance is not runtime evidence. |
| `v5-latency-feasibility` | Latency feasibility | One homogeneous group, >=30 successful samples, no block/visibility failure, p95 `input_to_visible_ms` <200 ms. | A source-side measurement remains unpromoted until its privacy-safe aggregate is validated. |
| `v5-latency-demo` | Progress-report demonstration | Android `researchRelease` + Chrome + `warm_foreground_online`, >=30 successful samples, no block/visibility failure, p95 <200 ms. | This is the smaller v5 demonstration checkpoint; it does not require the final matrix. |
| `v5-latency-final` | Final readiness latency | Android/Windows × Chrome/Edge/Opera × profile/release, with the same per-cell sample, failure, and p95 criteria. | Retained as final-readiness evidence, not a prerequisite for the reduced progress checkpoint. |
| `v5-pattern-interrupt` | Intervention | Pattern Interrupt duration remains within 5–10 seconds; implemented demonstration duration is 7 seconds. | Runtime and accessibility evidence remain separate from source/unit coverage. |
| `v5-anti-uninstall` | Android protection | Required OEM/scenario matrix is completed with valid lifecycle evidence. | Manual system UI evidence is required; partial AOSP coverage is not full matrix coverage. |
| `v5-usability-formative` | User feedback | Formative findings may document prototype issues; no SUS or efficacy score is claimed. | The nine-student activity remains off-repository formative feedback. |

## Target change register

No additional v6 target is active or approved in this registry yet. When a new
target is considered, add it here using this format and leave it `proposed`
until the report-version decision is made:

| Target ID | Intended report version | Status | Proposed target/change | Reason and evidence need | Activation condition |
| --- | --- | --- | --- | --- | --- |
| — | `v6` | — | No entry yet. | — | Create the v6 copy, then record and approve the target before activation. |

## Activation procedure for v6

1. Copy `laporan-kemajuan-v5.md` to `laporan-kemajuan-v6.md`; preserve v5 as
   the historical source snapshot.
2. Add or update the target entry here, keeping the v6 target ID and status
   explicit. Do not alter the v5 baseline rows.
3. Move only the accepted target to `approved`, then `active` after the v6
   report and the corresponding machine-readable runner configuration are
   reviewed together.
4. Update `progress-testing.md` so each evidence status identifies the report
   version and target ID it supports.
5. Retain the v5 runner/configuration for historical reproduction; do not
   reinterpret old v5 evidence using v6 thresholds.

Until these steps occur, all new measurements are either evidence against the
active v5 targets or exploratory material. They are not silently eligible for
a future report claim.
