# PKM-KC Progress Testing Traceability

`laporan-kemajuan.md` is the proposal-facing report context. This document
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

## Current target boundary

This file is the live evidence-status map for the current report. Statuses may
change as validated evidence is added, but the target definitions remain in
`progress-targets.md` and `gamblock-ai-testing/docs/config/targets.json`.
Evidence rows must preserve their scope, limitations, and privacy boundary.

## Current progress-report traceability

| Claim or test scope | Recorded evidence/status | Interpretation and remaining gate |
| --- | --- | --- |
| Historical Hybrid result on 2,592 rows | **provisional**; model metadata records Accuracy 97.22%, Precision 96.25%, Recall 95.10%, F1 95.67%, FPR 1.77%. | The historical split has hostname overlap and lacks required slices; it cannot establish leakage-safe generalization. |
| Domain-grouped candidate evaluation (2,523 rows) | **passed (recorded)** for `developmental_checkpoint`: Accuracy 96.59%, Precision 94.22%, Recall 94.71%, F1 94.47%, FPR 2.57%. | Split audit is leakage-safe and the candidate meets the current 90%/5% gate, but it is not a deployed-result claim. |
| Hybrid artifact loaded locally | **pending** artifact-contract execution. Current Android/Windows implementations load serialized Hybrid model/rules JSON; the repository source ONNX is provenance, not a demonstrated runtime format. | Verify the actual loaded artifacts, combined size < 5 MB, hash/provenance, parity/integrity, and local-only execution. |
| Android anti-uninstall | **partial, recorded**: 18 samples across 17 groups, with 16 passing assertions and 2 Android/OEM Settings limitations; the seven valid AOSP Pixel lifecycle records are a subset. | Complete all required OEM-family and scenario cells in the device matrix; retain Settings limitations as platform constraints, not assumed Flutter code defects. |
| Android latency (Redmi 12C, 30 samples) | **passed (recorded)** in run `redmi12c_release_probe` in the privacy-safe Phase 4 ledger for Research release, Chrome, `warm_foreground_online`; 30/30 visible and completed, p95 `input_to_visible_ms` 182.34 ms, no failures. | The current progress-demo checkpoint is **passed** for this homogeneous demonstrated group. The former final-readiness latency matrix has been replaced by separate client runtime contracts. |
| Android Research UI runtime observation (Redmi 12C, v1.6.5) | **passed (recorded)** for the user-visible demonstration: the operator confirms the dashboard displayed “Proteksi Aktif” and Pattern Interrupt was visibly rendered; the same run now has 30 privacy-safe Phase 4 records in the testing ledger. | The official metric is the Phase 4 `input_to_visible_ms` ledger (p95 182.34 ms). The earlier external overlay proxy remains diagnostic only and is not used for the gate. |
| Flutter local model balanced evaluation | **pending** Android and Windows runtime evidence. | Execute 50 gambling + 50 non-gambling fixtures per platform on Research release and apply the 90%/5% classification gate. |
| Cross-platform browser support regression | **pending** one Android device and one Windows VM. | Execute the five-browser platform matrix with 5 gambling + 5 non-gambling fixtures per browser; promote only aggregate-safe allow/intervention outcomes. |
| Pattern Interrupt, recovery, and accountability flow | Product source/unit coverage exists; the cross-repository `flutter_pattern_interrupt_unit` check is **passed (recorded)** in the current Flutter report. | This is source/unit evidence only; runtime and accessibility scenarios remain separate from the client model/browser contracts. |
| Backend integration | **passed (recorded)**: the explicit local PostgreSQL run and cross-repository runner completed migration/encrypted persistence, transaction rollback, and concurrent aggregate idempotency checks. | The isolated backend integration gate is no longer pending; retain the aggregate report and receipt as the current evidence. |
| Formative user feedback, 9 UTY students | **completed formative activity, off-repository**. Participants tried the prototype, described flow/bug feedback, and exposed an uninstall-permission issue; the emergency route was the follow-up. | This was not SUS, a quantitative usability score, or an efficacy result. No identities, raw feedback, consent records, or recordings are retained in the repository. |
| Structured task usability + SUS | **planned.** | Confirm the appropriate campus/authority governance before recruitment; use the privacy-safe protocol in `gamblock-ai-testing/docs/ai/pkm-usability-testing.md` and publish only approved aggregates. |
| User retention rate | **planned / not measured.** | Define the observation window, eligible-user denominator, return/continued-protection event, consent boundary, and minimum cohort before reporting any retention percentage. No current prototype or runtime record establishes this metric. |

### Android anti-uninstall limitation

The Research APK provides best-effort removal resistance through the supported
Android Device Administrator and Accessibility mechanisms. Device Administrator
blocks uninstall while it remains active, but Android/OEM Settings may require
the user to deactivate that administrator before continuing with removal. The
`DeviceAdminReceiver` callback can warn and persist a tamper event; it cannot
veto the OS deactivation. Accessibility can detect the system-UI transition and
attempt a safe back/home action, but it cannot override Settings or the package
installer, and an OEM may stop the protection process during the transition.

The Redmi 12C Research release evidence demonstrates this boundary: the
Settings path reached “Nonaktifkan & uninstal” and removed the package after
user confirmation. This remains a recorded `failed` result and is not relabeled
as a pass. The current prototype scope therefore covers detection, warning,
audit, recovery, and approved-grant removal; guaranteed prevention using
Device Owner/MDM/kiosk provisioning is outside the current APK scope.

## Named metric gates

| Gate | Accuracy / Precision / Recall / F1 | FPR | Purpose |
| --- | --- | --- | --- |
| `developmental_checkpoint` | >=90% each | <=5% | Candidate screening and engineering regression. |
| `progress_gate` | >=90% each | <=5% | Current acceptance gate for a leakage-safe model result. |

Both gate outputs must be retained in evaluator output. A legacy unqualified
`numeric_gate_passed` field, where retained for compatibility, denotes only
the developmental checkpoint and must not be used for report acceptance.

The recorded 2,523-row grouped candidate is numerically eligible for the
current 90%/5% gate, but it remains subject to the deployed-artifact and
evidence-maturity boundaries above.

## Remaining readiness gates

Readiness still requires: leakage-safe strict model evaluation; actual runtime
artifact contract; complete Android device matrix; the Flutter local model
balanced evaluation (50 gambling + 50 non-gambling fixtures on Android and
Windows); the cross-platform browser support regression (one Android device,
one Windows VM, five browsers per platform, and 5+5 fixtures per browser); and
the approved structured usability protocol if human-participant results are to
be claimed. The former Android/Windows Chrome latency matrix is no longer a
separate gate. The isolated backend integration gate is passed and recorded.
The future usability study must distinguish formative feedback from a measured
usability result and must not use product consent as research consent.
