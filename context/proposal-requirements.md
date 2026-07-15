# Proposal Requirement Traceability

This document normalizes the requirements that are explicitly present in
`pkm_proposal.md`. It is a navigation and traceability aid, not a replacement
for the proposal. If this file conflicts with the proposal, the proposal wins.

Status and evidence are intentionally kept in `progress-tracker.md` so target
requirements are not confused with current implementation.

## Source integrity and interpretation rules

- The stored proposal extraction omits most of section 3.2 Fase 1–3 and ends
  mid-sentence in Fase 5. Requirements below rely only on readable sections.
- “Acceptance evidence” defines what would demonstrate the requirement; it is
  not a claim that the evidence already exists.
- Product details absent from the proposal are labeled `supporting` or
  `operational` in other documents.
- The proposal's statements that the system is a “first” solution or that no
  integrated solution exists are research hypotheses until supported by a
  reproducible literature review.
- “Shock therapy visual” is interpreted in product UX as a short, non-clinical
  Pattern Interrupt stimulus. It must never be represented as medical shock
  therapy or used to justify harmful content.

## Core outcome map

The proposal describes one continuous protection and recovery loop:

```text
local signal acquisition
  -> URL rule features + DOM text features
  -> Bag-of-Words + Logistic Regression
  -> local hybrid decision
  -> real-time local block
  -> 5–10 second Pattern Interrupt
  -> web psychoeducation / self-regulation
  -> social accountability against unilateral uninstall
  -> measured technical and behavioral outcomes
```

Every core link must be represented in target scope. A website, model file, or
native service by itself does not satisfy the end-to-end outcome.

## Platform and protection requirements

| ID | Requirement derived from proposal | Source | Primary owner | Acceptance evidence |
|---|---|---|---|---|
| `PKM-PLAT-001` | Provide a multiplatform prototype for Android mobile and Windows desktop. | §1.1, §1.2, §1.3 | Flutter/native client | Installable prototype on both platforms with documented supported versions and limitations. |
| `PKM-PLAT-002` | Protection operates as a background service rather than only as an ordinary browser page. | §1.1, §1.2 | Android Accessibility Service; Windows System Service | Protection remains active through documented background scenarios and platform lifecycle tests. |
| `PKM-PLAT-003` | Use Android Accessibility Service and a Windows System Service for local inspection/intervention within OS limits. | §1.3 | Flutter Android bridge; Windows service | Runtime wiring evidence on real target devices; permissions and user disclosure documented. |
| `PKM-BLOCK-001` | Detect and block gambling content locally in real time. | §1.1, §1.2 | Native protection client | A repeatable end-to-end trace from local input through decision to block, including offline behavior. |
| `PKM-BLOCK-002` | Reduce mistaken blocking of legal, academic, and government sites. | §1.2, §3.2.4 | Model/evaluation workstream | Representative negative test set and reported false-positive rate by relevant site category. |

“Protection for all network activity” in §1.2 is a target claim whose exact OS
coverage is unresolved. The prototype must publish a coverage matrix instead
of implying that inaccessible encrypted or application-private content is
inspected.

## Hybrid on-device AI requirements

| ID | Requirement derived from proposal | Source | Primary owner | Acceptance evidence |
|---|---|---|---|---|
| `PKM-AI-001` | Use Hybrid Analysis combining a Rule-Based System and Logistic Regression. | §1.1, §1.2 | Model + native client | Versioned decision specification and fixture set showing how rule and model outputs are combined. |
| `PKM-AI-002` | Extract URL characteristics for explicit gambling-pattern rules/features. | §1.1, §1.2 | Native sensor/model feature layer | Documented local feature schema and fixtures; no raw URL leaves the device. |
| `PKM-AI-003` | Analyze DOM text from page `title`, headings, and anchor text. | §1.2 | Browser/native sensor | Extraction fixtures for each element type, limits for dynamic/unsupported content, and local-only relay evidence. |
| `PKM-AI-004` | Represent relevant page text as Bag-of-Words numeric features. | §1.2 | Model pipeline | Reproducible tokenizer/vocabulary/vectorizer artifact and preprocessing specification. |
| `PKM-AI-005` | Train and evaluate a Logistic Regression classifier on labeled gambling/non-gambling URL and DOM data. | §1.2, §2.1, §3.1 | Research/model workstream | Reproducible Python/scikit-learn training pipeline, dataset card, split manifest, metrics, and versioned artifact. |
| `PKM-AI-006` | Run feature extraction and inference on the user's device using a lightweight model. | §1.2, §1.3, §2.2.4 | Flutter/native client | No remote inference call; profiled artifact size, memory, CPU, and latency on representative Android/Windows devices. |
| `PKM-AI-007` | Make the local decision robust to dynamic domains and content camouflage, including compromised government/education domains. | §1.1, §1.2 | Model/evaluation workstream | Holdout scenarios covering URL churn, legal-domain camouflage, and benign government/education controls. |

The current `0.72` threshold and any model-size number are engineering
baselines, not proposal mandates. They may be retained only when calibrated
and recorded with evaluation evidence.

## Privacy requirements

| ID | Requirement derived from proposal | Source | Primary owner | Acceptance evidence |
|---|---|---|---|---|
| `PKM-PRIV-001` | Feature extraction, inference, and block decisions occur locally. | §1.2, §1.3, §2.2.4 | Native client | Data-flow review and network inspection show no detection input sent to a remote service. |
| `PKM-PRIV-002` | Browsing history and screenshots are not transmitted off-device. | §1.3 | All components | Schema denylist, backend rejection, client tests/inspection, and privacy notice. |
| `PKM-PRIV-003` | Apply data minimization consistent with UU PDP principles. | §1.2, §1.3 | Product + all components | Data inventory, purpose/retention/access rules, consent surfaces, and deletion/export mechanisms for server-side data. |

Engineering clarification: URL and DOM inputs are also treated as local-only,
because they are the proposal's detection inputs and would reveal browsing
behavior. Account, consent, partner-approval, and voluntarily entered recovery
data may use the backend only under the boundaries in `privacy-security.md`.

## Pattern Interrupt requirements

| ID | Requirement derived from proposal | Source | Primary owner | Acceptance evidence |
|---|---|---|---|---|
| `PKM-INT-001` | Trigger a visual Pattern Interrupt automatically after a positive local detection. | §1.1, §1.2, §1.3, §2.2.3 | Native client | End-to-end runtime trace from detection to intervention without website/backend dependency. |
| `PKM-INT-002` | Present a short animation/video lasting 5–10 seconds. | §1.2, §1.3, §3.1.2 | Native client/content workstream | Timed media behavior, asset provenance, reduced-motion alternative, and device usability evidence. |
| `PKM-INT-003` | Use the intervention to interrupt an impulsive response at the moment of attempted access. | §1.1, §1.2, §2.2.3 | Psychology/research workstream | Ethical protocol and outcome measure distinguish interruption from unvalidated treatment claims. |
| `PKM-INT-004` | Continue from Pattern Interrupt to the web psychoeducation experience. | §2.2.3 | Native client + website | Safe handoff/deep-link flow that does not include the detected URL or DOM content. |

## Social Accountability requirements

| ID | Requirement derived from proposal | Source | Primary owner | Acceptance evidence |
|---|---|---|---|---|
| `PKM-ACC-001` | A protected user can register an Accountability Partner who is a parent or peer. | §1.1, §1.2 | Client + website + backend | Consent-based invitation, acceptance, relationship status, revoke/replace policy, and audit trail. |
| `PKM-ACC-002` | Uninstall/removal requires explicit approval from the registered partner. | §1.1, §1.2 | Native client + approval service | State-machine evidence that pending, approved, denied, expired, and emergency cases behave as specified. |
| `PKM-ACC-003` | Detect relevant settings/uninstall interaction and introduce high-friction double verification within OS limits. | §1.3 | Android Accessibility/Windows service | Real-device scenario evidence, permission disclosure, and documented platform limitations. |
| `PKM-ACC-004` | Resist unilateral manipulation without unsafe OS mechanisms. | §1.1–§1.4, §3.2.4 | Native client | Kill-process stress protocol passes without critical-process APIs, boot loops, lockout, or device instability. |

Group codes, WhatsApp deep links, batching, administrative emergency unlock,
and a multi-member partner dashboard are supporting implementation choices;
they do not replace explicit partner consent and approval semantics.

## Web psychoeducation and self-regulation requirements

| ID | Requirement derived from proposal | Source | Primary owner | Acceptance evidence |
|---|---|---|---|---|
| `PKM-WEB-001` | Provide a web-based psychoeducation follow-up after blocking. | §1.1, §2.2.1–§2.2.3 | Website + content | Accessible recovery entry route and reviewed psychoeducation content journey. |
| `PKM-WEB-002` | Let the student set an intention or personal change goal. | §2.2.3 | Website | Create/review/update flow with private-by-default data handling. |
| `PKM-WEB-003` | Teach awareness of impulses and adaptive alternatives. | §2.2.1, §2.2.3 | Website/content | Structured modules, comprehension/reflection interaction, and content review record. |
| `PKM-WEB-004` | Provide mood tracking as part of self-monitoring. | §2.2.3 | Website | Check-in history and trends without exposing raw private entries to a partner. |
| `PKM-WEB-005` | Provide daily self-control missions. | §2.2.3 | Website/backend | Daily assignment, completion/reflection, accessible alternatives, and progress state. |
| `PKM-WEB-006` | Recommend constructive skill-development activities. | §2.2.3 | Website/content | Explainable, non-diagnostic recommendations linked to available activities/resources. |
| `PKM-WEB-007` | Support the Self-Regulation cycle: goal, self-monitoring, evaluation, and behavioral adjustment. | §2.2.3 | Website | The five recovery features form a coherent loop rather than isolated dashboard widgets. |

The detailed website roadmap, including many optional supporting features, is
defined in `website-product.md`.

## Evaluation requirements

| ID | Requirement derived from proposal | Source | Primary owner | Acceptance evidence |
|---|---|---|---|---|
| `PKM-EVAL-001` | Report Precision, Recall, and F1-Score for the AI model. | §3.2.4 | Research/model workstream | Reproducible evaluation report with class distribution and confidence intervals where feasible. |
| `PKM-EVAL-002` | Measure and minimize False Positive Rate, especially for academic/government sites. | §1.2, §3.2.4 | Research/model workstream | FPR definition, target agreed before final evaluation, category breakdown, and error analysis. |
| `PKM-EVAL-003` | Measure blocking latency with a target below 200 ms. | §3.2.4 | Native client/model | Device matrix, start/end event definition, percentile results, warm/cold distinction. |
| `PKM-EVAL-004` | Measure retention rate as an early indicator of intervention engagement. | §3.2.4 | Product/research | Cohort, event, period, consent, and aggregation definitions established before collection. |
| `PKM-EVAL-005` | Stress-test forced process termination and anti-uninstall consistency. | §3.2.4 | Native/platform workstream | Safe scenario matrix and recovery results for Android/Windows. |
| `PKM-EVAL-006` | Evaluate the preventive psychological effect of Pattern Interrupt without overstating causality. | §1.2, §1.4 | Psychology/research workstream | Ethics-reviewed study design, validated or justified measures, limitations, and non-clinical claims. |

The proposal does not state numeric minimums for Precision, Recall, F1, FPR,
retention, or psychological effect. Those targets require an explicit research
decision; do not invent them in implementation documentation.

## PKM execution and deliverable requirements

| ID | Requirement derived from proposal | Source | Acceptance evidence |
|---|---|---|---|
| `PKM-DATA-001` | Prepare labeled URL and DOM data for `Judi` and `Non-Judi` classes. | §3.1.2 | Dataset card, provenance/consent/license record, labeling guide, quality review, and leakage-safe split. |
| `PKM-DATA-002` | Use Python and scikit-learn for model training. | §3.1.1 | Reproducible environment, training script/notebook, locked dependencies, and artifact hash. |
| `PKM-CONTENT-001` | Prepare 5–10 second Pattern Interrupt media and interface assets. | §3.1.2 | Versioned asset inventory, review criteria, provenance/license, and accessibility variant. |
| `PKM-DOC-001` | Produce the PKM progress report. | §1.5, §3.2.5 | Approved report artifact and submission record. |
| `PKM-DOC-002` | Produce the PKM final report. | §1.5, §3.2.5 | Approved report artifact and submission record. |
| `PKM-DOC-003` | Produce the Android/Windows prototype and usage documentation. | §1.5, §3.2.5 | Versioned demo release, installation/use guide, limitations, and traceability report. |
| `PKM-COMMS-001` | Maintain the required social-media account for dissemination. | §1.5 | Account ownership, content plan, publication archive, and access continuity. |
| `PKM-COMMS-002` | Produce an educational video as an additional output. | §3.2.5 | Reviewed video, source assets, caption/transcript, and publication record. |
| `PKM-PUB-001` | Prepare a scientific article as an additional academic contribution. | §3.2.5 | Draft/manuscript with method, results, limitations, ethics, and references. |

## Known proposal questions requiring owner input

1. Restore the missing Fase 1–3 and truncated Fase 5 text from the original
   proposal source.
2. Define dataset source, sampling, labeling authority, licensing, and class
   balance.
3. Set evaluation targets for Precision, Recall, F1, FPR, and retention.
4. Define “retention rate”, its observation period, and the minimum data needed.
5. Approve an ethical, accessible Pattern Interrupt content protocol and
   psychological evaluation method.
6. Define the supported protection surface per OS/browser/application instead
   of relying on the broad “all network activity” phrase.
7. Confirm safe emergency recovery behavior that does not become a routine
   accountability bypass.
8. Resolve the literal “all data stays local” wording against voluntary
   account, recovery, and partner-approval data needed by the web platform.
