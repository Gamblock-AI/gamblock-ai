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
- A new progress report is always the next integer version after the latest
  report in scope (for example, v5 becomes v6 and v6 becomes v7). The previous
  report remains read-only and is never silently revised.

The same target may be retained in a later report, but it must still be
referenced by its report version and target ID. A new target is never silently
inserted into an older report's table.

## Target lifecycle

| Status | Meaning | Effect on the selected runner/report |
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

The following v6 target is approved but not active. It may not reinterpret v5
evidence or be used by the runner until the v6 report copy exists and the
activation procedure below is completed. Future versions follow the same
append-only pattern.

| Target ID | Intended report version | Status | Proposed target/change | Reason and evidence need | Activation condition |
| --- | --- | --- | --- | --- | --- |
| `v6-detection-progress` | `v6` | `approved` | Accuracy, precision, recall, and F1 >=90%; FPR <=5% on a leakage-safe split. | Align the progress gate with the already-passed developmental checkpoint without removing any proposal metric or false-positive analysis. No retraining is required. | Create `laporan-kemajuan-v6.md`, review the v6 config, then change this row and the config activation status to `active`. |
| `v6-latency-final-chrome-release` | `v6` | `approved` | Final-readiness latency is limited to Android/Windows × Chrome × release; each cell requires >=30 successful samples, no block/visibility failure, and p95 `input_to_visible_ms` <200 ms. | Focuses the retained final check on the production build and the primary supported browser while preserving the proposal's real-time latency intent. The v5 broader matrix remains historical and unchanged. | Create `laporan-kemajuan-v6.md`, review the v6 config and this registry entry together, then change this row and the config activation status to `active`. |

## Activation procedure for v6

1. Copy `laporan-kemajuan-v5.md` to `laporan-kemajuan-v6.md`; preserve v5 as
   the historical source snapshot. If the user asks for a newer report after
   v6, repeat this step with v7 (the next integer version).
2. Update only the new report copy to reference the approved versioned target;
   do not alter the v5 baseline rows or source report.
3. Change the accepted target row from `approved` to `active` and set the
   matching `targets-v6.json` `activation_status` to `active` after both files
   are reviewed together.
4. Run the versioned evaluator with `--report-version v6`; each evidence row
   must identify the report version and target ID it supports.
5. Retain the v5 runner/configuration for historical reproduction; do not
   reinterpret old v5 evidence using later-version thresholds.

Until these steps occur, all new measurements are either evidence against the
active v5 targets or exploratory material. They are not silently eligible for
a future report claim.
