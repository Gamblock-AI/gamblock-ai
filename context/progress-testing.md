# PKM-KC Progress Testing Traceability

`laporan-kemajuan-v5.md` is the proposal-facing report context. This document
maps each testing claim in that report to its evidence, status, limitation, and
final gate. It does not change the authority of `pkm_proposal.md` or turn an
unexecuted check into a result.

## Evidence terms

- **passed (recorded):** a validated, committed report or aggregate evidence
  records the stated scope.
- **provisional:** a recorded result has a material method limitation and must
  not support the stronger final claim.
- **recorded, unpromoted:** a source-side measurement exists but no validated
  public aggregate ledger has been promoted.
- **pending:** the required check has not been executed or cannot yet be
  represented by the public evidence contract.

The canonical run-specific reports and ledgers are owned by
`gamblock-ai-testing/`. This context deliberately contains no raw browsing
data, participant data, screenshots, URLs, domains, DOM text, or logs.

## Version boundary

This file is a live evidence-status map, not a replacement for a report
version. Statuses may change as validated evidence is added, but the target
definition for v5 is frozen in `progress-targets.md` and in the v5 testing
configuration. New or changed targets must be recorded in that registry first;
they must not be inserted into `laporan-kemajuan-v5.md` or used to reinterpret
its existing claims. When a v6 copy exists, each new status row must identify
the report version and target ID that it supports.

## Current progress-report traceability

| Claim or test scope | Recorded evidence/status | Interpretation and remaining gate |
| --- | --- | --- |
| Historical Hybrid result on 2,592 rows | **provisional**; model metadata records Accuracy 97.22%, Precision 96.25%, Recall 95.10%, F1 95.67%, FPR 1.77%. | The historical split has hostname overlap and lacks required slices; it cannot establish leakage-safe generalization even though its numeric values meet `pkm_progress_v5`. |
| Domain-grouped candidate evaluation (2,523 rows) | **passed (recorded)** only for `developmental_checkpoint`: Accuracy 96.59%, Precision 94.22%, Recall 94.71%, F1 94.47%, FPR 2.57%. | Split audit is leakage-safe, but this candidate does not meet the stricter `pkm_progress_v5` 95%/2% gate and is not a deployed-result claim. |
| Hybrid artifact loaded locally | **pending** artifact-contract execution. Current Android/Windows implementations load serialized Hybrid model/rules JSON; the repository source ONNX is provenance, not a demonstrated runtime format. | Verify the actual loaded artifacts, combined size < 5 MB, hash/provenance, parity/integrity, and local-only execution. |
| Android anti-uninstall | **partial, recorded**: seven valid AOSP Pixel lifecycle records. | Complete all required OEM-family and scenario cells in the versioned device matrix. |
| Android latency (Redmi 12C, 30 samples) | **passed (recorded)** in run `redmi12c_release_probe` in the privacy-safe Phase 4 ledger for Research release, Chrome, `warm_foreground_online`; 30/30 visible and completed, p95 `input_to_visible_ms` 182.34 ms, no failures. | The v5 progress-demo checkpoint is **passed** for this homogeneous demonstrated group. The broader Android/Windows × Chrome/Edge/Opera × profile/release matrix remains a final-readiness gate, not a progress-report prerequisite. |
| Android Research UI runtime observation (Redmi 12C, v1.6.5) | **passed (recorded)** for the user-visible demonstration: the operator confirms the dashboard displayed “Proteksi Aktif” and Pattern Interrupt was visibly rendered; the same run now has 30 privacy-safe Phase 4 records in the testing ledger. | The official metric is the Phase 4 `input_to_visible_ms` ledger (p95 182.34 ms). The earlier external overlay proxy remains diagnostic only and is not used for the gate. |
| Windows extension-to-model / blocking E2E | **pending** interactive Windows VM evidence. | Keep the Windows final-readiness procedure and promote only aggregate-safe results. |
| Pattern Interrupt, recovery, and accountability flow | Product source/unit coverage exists; the cross-repository Flutter unit receipt is **pending** because its runner has not included Flutter. | Run the explicit Flutter scope and retain its canonical report result; runtime and accessibility scenarios remain part of final readiness. |
| Backend integration | **pending** because an isolated `DATABASE_URL` was not available for the retained integration procedure. | Execute only with an isolated approved database and publish its testing-repository result. |
| Formative user feedback, 9 UTY students | **completed formative activity, off-repository**. Participants tried the prototype, described flow/bug feedback, and exposed an uninstall-permission issue; the emergency route was the follow-up. | This was not SUS, a quantitative usability score, or an efficacy result. No identities, raw feedback, consent records, or recordings are retained in the repository. |
| Structured task usability + SUS | **planned.** | Confirm the appropriate campus/authority governance before recruitment; use the privacy-safe protocol in `gamblock-ai-testing/docs/ai/pkm-usability-testing.md` and publish only approved aggregates. |

## Named metric gates

| Gate | Accuracy / Precision / Recall / F1 | FPR | Purpose |
| --- | --- | --- | --- |
| `developmental_checkpoint` | >=90% each | <=5% | Candidate screening and engineering regression. |
| `pkm_progress_v5` | >=95% each | <=2% | Historical acceptance gate for a leakage-safe model result represented as a v5 progress-report achievement. |
| `pkm_progress_v6` | >=90% each | <=5% | Approved v6 progress gate; inactive until the v6 report and registry target are activated. |

Both gate outputs must be retained in evaluator output. A legacy unqualified
`numeric_gate_passed` field, where retained for compatibility, denotes only
the developmental checkpoint and must not be used for report acceptance.

The recorded 2,523-row grouped candidate is numerically eligible for the
approved v6 90%/5% gate, but it is not a v6 claim yet. A versioned replay and
evidence report must be generated only after `laporan-kemajuan-v6.md` exists
and `v6-detection-progress` is active in the target registry.

The approved v6 latency scope is narrower than the frozen v5 final-readiness
matrix: Android/Windows × Chrome × release only. It remains inactive until
`laporan-kemajuan-v6.md` exists and `v6-latency-final-chrome-release` is
activated together with the v6 configuration.

## Final-readiness gates retained

No pending final technical gate is removed by this traceability update. Final
readiness requires: leakage-safe strict model evaluation; actual runtime
artifact contract; complete Android device matrix; complete privacy-safe
latency matrix (Android/Windows × Chrome/Edge/Opera × profile/release);
Windows VM end-to-end evidence; isolated backend integration;
and the approved structured usability protocol if human-participant results
are to be claimed. The future usability study must distinguish formative
feedback from a measured usability result and must not use product consent as
research consent.
