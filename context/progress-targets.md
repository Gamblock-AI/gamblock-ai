# PKM-KC Current Target Contract

This file is the single target contract for the active progress report and
cross-repository evaluator. The PKM proposal remains the authority for product
intent and academic requirements. This contract defines the current engineering
thresholds and the evidence boundary; it does not promote unexecuted work to a
result.

## Current target set

| Target ID | Area | Current target | Evidence boundary |
| --- | --- | --- | --- |
| `detection-progress` | Hybrid detection | Accuracy, precision, recall, and F1 >=90%; FPR <=5% on a leakage-safe split. | The result must identify the split, leakage audit, slices, and actual deployed artifact. Historical or provisional metrics do not qualify as a final claim. |
| `artifact-local` | On-device artifact | The Hybrid artifact actually loaded by Android/Windows is under 5 MB combined and passes hash, provenance, and parity checks. | Source ONNX provenance is not runtime evidence. |
| `latency-feasibility` | Latency feasibility | One homogeneous group, >=30 successful samples, no block/visibility failure, p95 `input_to_visible_ms` <200 ms. | Source-side measurements remain unpromoted until their privacy-safe aggregate is validated. |
| `latency-demo` | Progress demonstration | Android `researchRelease` + Chrome + `warm_foreground_online`, >=30 successful samples, no block/visibility failure, p95 <200 ms. | Debug measurements cannot satisfy this release demonstration target. |
| `browser-support-regression` | Cross-platform browser support regression | One required Android device running Chrome, Edge, Brave, Firefox, Samsung Internet, Xiaomi Browser, and UPX Browser; optional Windows coverage may use one VM running Chrome, Edge, Brave, Opera, and Firefox; 5 gambling and 5 non-gambling fixtures per browser. Current Android evidence must also demonstrate dynamic standalone-browser discovery, exclusion of Custom Tabs/internal/transient surfaces from classification and opacity counting, explanation-first-frame before Home for an opaque browser fixture, and the native Activity fallback when overlay presentation is unavailable. | Android browser cells and current-source capability evidence are gating; Windows is optional and non-gating. Runtime evidence predating a sensing implementation change remains historical and cannot verify the changed source commit. |
| `pattern-interrupt` | Intervention | Pattern Interrupt duration remains within 5–10 seconds; implemented demonstration duration is 7 seconds. | Runtime and accessibility evidence remain separate from source/unit coverage. |
| `anti-uninstall` | Android protection | The AOSP/Pixel, Samsung, Xiaomi/Redmi, OPPO/realme/OnePlus, vivo/iQOO, and Transsion scenario matrix, including partner removal, two-admin emergency removal, and approved-removal cancellation recovery, is completed with valid lifecycle evidence. | Manual system UI evidence is required; source/unit coverage or partial AOSP coverage is not full matrix coverage. Android/OEM Settings limitations remain honest failures/limitations, not code defects. |
| `usability-formative` | User feedback | Formative findings may document prototype issues; no SUS or efficacy score is claimed. | The nine-student activity remains formative and off-repository as participant-level data. |
| `retention-rate` | User retention | Planned metric only; define an observation window, eligible-user denominator, return/continued-protection event, consent boundary, and minimum cohort before calculating a percentage. | No retention claim is currently supported by product or testing evidence. |

## Operational rules

- The active machine-readable configuration is
  `gamblock-ai-testing/docs/config/targets.json`.
- The active proposal-facing report is `context/laporan-kemajuan.md`.
- `context/progress-testing.md` records evidence status and limitations; it
  does not redefine these thresholds.
- Evidence must distinguish source checks, offline replay, and physical
  Android/Windows runtime behavior.
- A missing device, browser, build, or runtime cell remains `pending`.
- Android/OEM behavior that the operating system does not allow an ordinary APK
  to prevent remains documented as a platform limitation.
- Changes to this contract require a review of the report, evaluator, and
  affected component snapshots together.
