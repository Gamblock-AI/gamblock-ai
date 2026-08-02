# Research and Evaluation Context

## Purpose

This document turns the proposal's evaluation intentions into a reproducible
evidence plan. It does not claim that an experiment has been completed.
Results and current readiness belong in component status documents and approved
PKM reports.

The evaluation has four distinct questions:

1. Can Hybrid Analysis distinguish gambling and non-gambling content?
2. Can Android/Windows apply the decision locally, quickly, and reliably?
3. Can the social-accountability mechanism resist ordinary manipulation safely?
4. Is the Pattern Interrupt and web recovery journey usable, safe, and
   associated with the defined engagement/preventive outcomes?

Do not collapse these questions into one “accuracy” or “success” number.

## Evidence maturity labels

- `planned` — protocol/requirement exists but evidence collection has not begun;
- `instrumented` — events/fixtures can be collected under an approved schema;
- `pilot` — small preliminary evidence, not a final claim;
- `evaluated` — protocol executed on the declared sample/device matrix;
- `replicated` — repeated by another run/team or an independent evaluator.

Use the weakest label supported by evidence.

## Dataset protocol (`PKM-DATA-001`)

Before collecting or training, create a dataset card containing:

- objective, classes, unit of observation, and intended/forbidden uses;
- source and collection date range;
- legal/ethical basis, license, and access restrictions;
- whether a row contains URL characteristics, DOM text, or both;
- label definition for `Judi`, `Non-Judi`, and any excluded/uncertain class;
- annotator instructions, review/escalation process, and agreement measure;
- class counts and relevant subgroups;
- duplicate/near-duplicate removal;
- handling of government/education camouflage and benign controls;
- sensitive-content handling and researcher safety;
- retention, deletion, and publication policy;
- known bias, language, time-drift, and coverage limitations.

Production user browsing must not silently become training data. Any future
user-contributed false-positive sample needs a separate explicit, revocable
consent flow and redaction review.

## Split and leakage controls

Random row splits can overstate performance when pages from one domain or site
template appear in both train and test. At minimum:

1. group records by registrable domain/site family and template fingerprint;
2. isolate train, validation, and final test groups;
3. reserve a time-shifted or newly collected set for domain-churn evaluation;
4. keep camouflage cases and benign government/education cases visible as
   separate evaluation slices;
5. fit vocabulary/vectorizer only on training data;
6. freeze the final test set before threshold selection;
7. record split manifests and hashes so results can be reproduced.

If a public benchmark is used, report its license and whether it represents
Indonesian language/content and current gambling-site behavior.

## Model pipeline

This pipeline covers `PKM-AI-001`, `PKM-AI-002`, `PKM-AI-003`, `PKM-AI-004`,
`PKM-AI-005`, `PKM-AI-006`, `PKM-AI-007`, and `PKM-DATA-002`.

The versioned training bundle should include:

- Python/scikit-learn environment lock;
- deterministic preprocessing and tokenization rules;
- URL rule/feature specification;
- title, heading, and anchor-text extraction contract;
- Bag-of-Words vocabulary/vectorizer artifact;
- Logistic Regression configuration and random seed;
- class weighting or resampling rationale;
- threshold-calibration method;
- model, vectorizer, ruleset, metadata, and cryptographic hashes;
- evaluation script/report and model card;
- export/conversion procedure for Android/Windows runtime format.

The runtime artifact set is more than a coefficient file: preprocessing,
vocabulary, feature ordering, rule version, threshold, and compatibility must
stay aligned.

## Detection metrics (`PKM-EVAL-001`, `PKM-EVAL-002`)

Report at least:

- confusion matrix (`TP`, `FP`, `TN`, `FN`);
- Precision = `TP / (TP + FP)`;
- Recall = `TP / (TP + FN)`;
- F1-Score as the harmonic mean of Precision and Recall;
- False Positive Rate = `FP / (FP + TN)`;
- counts and uncertainty/confidence intervals where feasible;
- performance by slice: ordinary gambling, dynamic/new-domain, camouflage,
  ordinary benign, government, education, and other declared cohorts;
- Hybrid system result plus rule-only and model-only ablations;
- error analysis with representative redacted failure categories.

Do not choose or publicize a “high accuracy” claim based only on an imbalanced
accuracy percentage. Numeric acceptance targets for Precision, Recall, F1, and
FPR remain an owner decision and must be set before final-test evaluation.

## Threshold selection

The imported Hybrid-v2 metadata specifies a `0.4` hybrid threshold with model
and rule weights of `0.75/0.25`. These are supplied engineering inputs, not a
proposal requirement or independently reproduced calibration result. Calibrate
the threshold on validation data using an explicit cost trade-off that gives
strong weight to false positives on legal, academic, and government sites
while still detecting harmful content.

The bundle reports accuracy, precision, recall, and F1, but does not include a
dataset card, split manifest, training/evaluation source, FPR, uncertainty, or
slice results. Preserve those values only as `reported_metrics_unverified`;
do not promote them to evaluated project results.

Record:

- dataset/model/ruleset versions;
- candidate thresholds and resulting metrics;
- chosen objective and stakeholder rationale;
- per-platform numerical consistency;
- final threshold owner/date;
- conditions that trigger recalibration.

Never tune against the final test set.

## Latency and resource evaluation (`PKM-EVAL-003`)

The proposal target is block latency below 200 ms. Define the measurement
before reporting it:

- start event: when the complete supported local input is available;
- end event: when block/intervention is visibly committed;
- separate extraction, preprocessing, rule, inference, decision, IPC, and UI
  durations;
- report median, p95, p99, maximum, and sample count;
- distinguish warm/cold start, online/offline, and foreground/background;
- test a declared Android and Windows device matrix;
- record model/artifact version, OS, CPU, memory, and power mode;
- profile memory, CPU, energy/battery, and artifact storage alongside latency.

Do not claim the 200 ms target from a model-only microbenchmark if IPC and UI
are excluded. Report any platform where the target is not met.

Repository-controlled tooling and native capture contracts live in
`evaluation/phase4/` and `phases/04-system-hardening.md`. They deliberately keep
generated evidence unreviewed until a declared device matrix and reviewer
approval exist.

## Functional and resilience evaluation (`PKM-EVAL-005`)

Use a safe, platform-specific scenario matrix:

- normal navigation and dynamic page updates;
- offline protection and reconnect behavior;
- browser/client/service restart;
- device reboot and expected service recovery;
- ordinary process kill and service-stop attempts;
- uninstall/settings interaction and partner approval states;
- expired, reused, revoked, and malformed approval token;
- partner unavailable and defined emergency recovery;
- update/rollback of model, rules, and assets;
- false-positive recovery;
- accessibility/reduced-motion behavior.

Pass criteria must include device usability and recoverability. Never use
`RtlSetProcessIsCritical`, boot-loop behavior, destructive lockout, or a test
that risks a BSOD. Use disposable test devices/VMs where appropriate.

## Pattern Interrupt safety and effectiveness

This evaluation covers `PKM-INT-001`, `PKM-INT-002`, `PKM-INT-003`,
`PKM-INT-004`, and `PKM-EVAL-006`.

Before a human-subject study, define and obtain the required academic/ethical
review for:

- participant population, inclusion/exclusion, and informed consent;
- stimulus content, 5–10 second duration, reduced-motion/non-visual options,
  photosensitivity review, and stop/withdraw path;
- primary outcome and observation window;
- comparison/control condition and allocation method;
- validated measure or justification for a custom measure;
- adverse-event/help protocol;
- data minimization, pseudonymization, retention, and access;
- compensation and conflict-of-interest disclosure;
- statistical analysis and limitation plan.

Potential staged evidence:

1. expert review for psychological safety and content validity;
2. accessibility/usability pilot;
3. controlled pilot of immediate urge/pause outcome;
4. engagement evaluation of the recovery handoff;
5. only then, a larger preventive-effect study if approved.

Do not describe Pattern Interrupt as treatment, cure, or proven behavior change
until the relevant evidence exists. Association is not causation.

## Retention and engagement (`PKM-EVAL-004`)

The proposal names “retention rate” but does not define it. Before collection,
the product/research owner must specify:

- eligible cohort and index event;
- observation periods (for example D1/D7/D30, only if approved);
- qualifying privacy-safe activity;
- treatment of account deletion, consent withdrawal, offline use, and missing
  data;
- whether the metric is product engagement, protection continuity, recovery
  engagement, or study retention;
- minimum cohort size and suppression rules;
- why the measure is meaningful and not a proxy for compulsive app use.

Recommended supporting outcomes include recovery-handoff acceptance, module
completion, mission engagement, weekly-review completion, opt-out, and
qualitative usability—always aggregated and purpose-limited.

## Privacy and ethics gates

No evaluation may collect URL, DOM, browsing history, screenshots, or raw
per-page scores on the backend. Local test harnesses may process curated
research fixtures under the dataset protocol. Production aggregates must be
non-reconstructive and described in `privacy-security.md`.

Product consent, partner consent, and research consent are distinct. A user
must be able to use core protection without being silently enrolled in
research. Withdrawal must stop future research collection and follow the
approved deletion/retention policy.

## PKM evidence package

The final evidence bundle should connect each registered PKM requirement to:

- implementation/runtime version;
- model/rules/content version;
- protocol and dataset/device/cohort description;
- raw-to-summary analysis procedure;
- result with limitation and failure analysis;
- reviewer/owner/date;
- artifact path/hash and publication restriction;
- corresponding report section and demo step.

Required and additional PKM outputs should be recorded in the owning component
status document or approved PKM report: progress report, final report,
prototype, social-media account, usage documentation, educational video, and
scientific article.

The repository-controlled Phase 5 drafts, production packages, and fail-closed
acceptance manifest live under `deliverables/phase5/`; the governing status and
external gate are defined in `phases/05-finalization-reporting.md`.

## Decisions still required

- Original proposal restoration and complete phase plan.
- Dataset governance owner and labeling protocol.
- Numeric detection and FPR targets.
- Final latency percentile gate and Android/Windows device matrix.
- Retention definition.
- Ethical review route and Pattern Interrupt study design.
- Supported platform coverage and resilience pass criteria.
- Publication/redaction policy for datasets, model artifacts, and results.
