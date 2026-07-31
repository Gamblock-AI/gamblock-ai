# Gamblock-AI Glossary

Use these terms consistently in proposal-derived context, UI copy, code
documentation, and status reports.

## Product and people

| Term | Meaning and usage |
|---|---|
| Gamblock-AI | The complete PKM prototype ecosystem: Android/Windows protection, web recovery/accountability, model/research work, backend, and supporting delivery components. |
| Protected Student / Mahasiswa Terlindungi | Primary proposal user. Existing API role code is `user`; “Member” is acceptable in group/account contexts. Avoid “target” or stigmatizing labels in UI. |
| Accountability Partner / Pendamping | Parent or peer who mutually accepts responsibility for removal approval and supportive accountability. Existing code/UI may use `partner` or “Kepala”; proposal-facing copy should explain the equivalence. |
| Self-directed recovery | A student-initiated adoption path where the student chooses protection and uses the private web recovery journey. It is not a separate role. |
| Partner/institution-directed installation | Supporting adoption path `PROD-SUP-ADOPT-001` where an external lecturer/campus policy may require installation transparently. It never auto-enrolls a student or bundles consent to monitoring, sharing, recovery sync, or research. |
| Admin | The single operational account role (`admin`) for content, release, support queue, research, platform, audit, and emergency work. It never grants raw browsing or private recovery access. |
| Organization membership role | Relation-level `owner`, `admin`, `member`, or `viewer` inside an organization. It is not an account role. |
| PKM Team | Researchers/developers responsible for prototype, evidence, content governance, and deliverables. Not automatically an application role. |
| Supporting feature | Product capability not explicitly required by the proposal but useful for usability, safety, recovery, supervision, or dissemination. |
| Operational feature | Administration, content/release management, support, infrastructure, or audit needed to operate the prototype. |

## Protection and AI

| Term | Meaning and usage |
|---|---|
| On-Device AI / Edge AI | Feature extraction and inference executed on the user's device. It does not mean that every account/recovery feature must avoid a backend. Detection inputs remain local. |
| Hybrid Analysis | The proposal-required combination of URL Rule-Based analysis and a Logistic Regression model using page-content features. Do not use it to mean DOM-only classification. |
| Rule-Based System | Explicit local URL characteristic/pattern logic that contributes to the hybrid decision. It is not a remote blacklist service. |
| DOM Analysis | Extraction of supported page text, specifically title, headings, and anchor text in the proposal. Raw DOM/page text remains device-local. |
| Bag-of-Words (BoW) | A fixed vocabulary/vectorization method that converts normalized text into numeric features for Logistic Regression. Vocabulary and preprocessing are part of the versioned model artifact. |
| Logistic Regression | Lightweight supervised classifier specified by the proposal. Model training/evaluation is a PKM workstream; runtime inference belongs on-device. |
| Threshold | Engineering decision used to turn a score into a local action. Hybrid-v2 imports `0.4` from supplied metadata; it is not a proposal mandate and requires reproducible calibration evidence. |
| False Positive | Benign content classified/blocked as gambling. Government, education, and legal-site false positives receive explicit evaluation attention. |
| Passive sensor | Browser extension boundary: extract and relay permitted local inputs over authenticated loopback IPC; never classify, block, redirect, or call the backend with browsing data. |

## Intervention and recovery

| Term | Meaning and usage |
|---|---|
| Pattern Interrupt | A short 5–10 second visual micro-intervention after detection, intended to create a pause before an impulsive response. It is non-clinical and must have accessible alternatives. |
| “Shock therapy visual” | Phrase present in the proposal. In product language, translate it to safe Pattern Interrupt stimulus; never imply electroconvulsive/medical shock treatment. |
| Psychoeducation | Reviewed educational support that helps users understand impulses, risks, and adaptive alternatives. It is not clinical diagnosis or therapy. |
| Self-Regulation Theory loop | Goal/intention → self-monitoring → evaluation → behavioral adjustment. Website features must form this loop rather than unrelated widgets. |
| Intention | A private, revisable personal reason/goal for change. Not a punitive or legally binding contract. |
| Mood/urge check-in | Voluntary self-monitoring input. It is private recovery data, not automatically visible to a partner. |
| Daily mission | Small, adaptable self-control activity; it can be completed, skipped, or replaced without wiping progress. |
| Skill recommendation | Explainable suggestion for constructive alternative activity based on voluntary recovery choices, not browsing history. |

## Accountability and privacy

| Term | Meaning and usage |
|---|---|
| Social Accountability Protocol | Consent-based partner relationship plus explicit removal approval and OS-compliant high-friction verification. It is not covert surveillance. |
| Anti-uninstall | Resistance to unilateral removal using supported Android/Windows mechanisms. Never means critical-process APIs, device sabotage, or unrecoverable lockout. |
| Local detection data (`D0`) | URL/domain, DOM text, history, screenshot, app/window identifier, features, rules hits, score, and block context. Never leaves the device. |
| Aggregate event | Minimal non-reconstructive count/health event without URL, DOM, page fingerprint, precise browsing timestamp, or free text. |
| Recovery-sensitive data (`D3`) | Intention, mood/urge, reflection/journal, and coping-plan data voluntarily entered for recovery. Private by default and governed separately from browsing data. |
| Quick approval | Single-use, expiring token flow that lets a partner resolve a specific request without a normal session. The token is not a permanent credential. |
| Emergency recovery | Narrow, audited safety path for loss of partner/device access. It must not become an ordinary accountability bypass. |

## Capability status

| Label | Meaning |
|---|---|
| `implemented` | Behavior is connected to the active runtime path. |
| `prototype` | Runnable partial behavior with documented limitations. |
| `stub` | Interface/placeholder exists but does not perform the target behavior. |
| `not wired` | Source exists but is not connected to the active runtime/build. |
| `planned` | Requirement exists without implementation evidence. |
| `blocked` | A named decision/source/platform/resource is required before progress. |

## Evidence language

- Use “proposal target” for intended outcomes.
- Use “current implementation” only with a path/runtime reference.
- Use “evaluated” only with a documented protocol and result.
- Use “UU PDP-aligned data-minimization design”, not “UU PDP compliant”,
  unless a qualified review has established that claim.
- Use “associated with” rather than “caused” for observational outcomes.
- Do not use “first”, “proven”, “accurate”, “stable”, “secure”, or
  “production-ready” without a cited evidence scope.
