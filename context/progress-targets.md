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
| `flutter-model-balanced` | Flutter local model balanced evaluation | Android and Windows Research release, with 50 gambling and 50 non-gambling fixtures per platform; accuracy, precision, recall, and F1 >=90%, FPR <=5%. Evidence is grouped as `<platform>/<case>` under the client-runtime evidence root. | Runtime evidence must come from the local client on both platforms; the existing 30-sample latency evidence does not satisfy this target. |
| `browser-support-regression` | Cross-platform browser support regression | One Android device and one Windows VM; Android: Chrome, Edge, Samsung Internet, Brave, Firefox; Windows: Chrome, Edge, Brave, Opera, Firefox; 5 gambling and 5 non-gambling fixtures per browser. These are required evaluation candidates, not a current support claim. Evidence is grouped as `<platform>/<browser>/<case>` under the client-runtime evidence root. | Runtime evidence must record aggregate `allow` for non-gambling and `intervention` for gambling. This is separate from anti-uninstall and latency evidence. |
| `pattern-interrupt` | Intervention | Pattern Interrupt duration remains within 5–10 seconds; implemented demonstration duration is 7 seconds. | Runtime and accessibility evidence remain separate from source/unit coverage. |
| `anti-uninstall` | Android protection | The supported OEM/scenario matrix is completed with valid lifecycle evidence. | Manual system UI evidence is required; partial AOSP coverage is not full matrix coverage. Android/OEM Settings limitations remain honest failures/limitations, not code defects. |
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
