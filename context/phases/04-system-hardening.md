# Phase 4 — Integration and System Hardening

Status: `instrumented`; external evaluation runs remain required

Scope: PKM core `PKM-EVAL-001`, `PKM-EVAL-002`, `PKM-EVAL-003`,
`PKM-EVAL-004`, `PKM-EVAL-005`, `PKM-EVAL-006`, `PKM-ACC-004`,
`PKM-AI-005`, `PKM-AI-006`, `PKM-AI-007`, and `PKM-BLOCK-002`

## Authority and completion rule

Section 3.2.4 of the protected proposal explicitly defines Phase 4. Unlike the
derived product phases, this phase is complete only when the declared protocols
have actually run and their evidence has been reviewed. Code, fixtures, seeded
metrics, or an empty report template cannot be promoted to an evaluated result.

The repository-controlled target is:

```text
reproducible evaluator + local-only timing instrumentation
+ safe resilience harness + privacy-safe retention analyzer
+ evidence manifest that fails closed on missing proof
```

The external evidence target is:

```text
approved labeled dataset + real Android/Windows device matrix
+ executed kill/recovery scenarios + approved UTY cohort/ethics protocol
```

## Requirement matrix

| Requirement                    | Repository-controlled evidence                                                                                                                                                                | External evidence required                                                                               |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `PKM-EVAL-001`                 | Offline Hybrid-v2 evaluator calculates confusion matrix, Precision, Recall, F1, uncertainty, and ablations without emitting raw URL/DOM.                                                      | Approved dataset card, leakage-safe final split, reviewer, and frozen report.                            |
| `PKM-EVAL-002`                 | Evaluator reports FPR overall and for government/education/benign/camouflage slices with opaque failure IDs.                                                                                  | Representative governed samples, target decision, and reviewed error analysis.                           |
| `PKM-EVAL-003`                 | Android and Windows write bounded local evidence only when explicit evidence mode is enabled; summarizer reports p50/p95/p99/max.                                                             | Declared real-device matrix and executed warm/cold, online/offline, foreground/background runs.          |
| `PKM-EVAL-004`                 | Offline analyzer implements explicit D1/D7/D30-style windows, consent filtering, withdrawal policy, and cohort suppression.                                                                   | Approved definition, research consent, minimum cohort, study owner, and collected pseudonymous activity. |
| `PKM-EVAL-005` / `PKM-ACC-004` | Disposable-device/VM harnesses emit standardized ordinary process-kill results; the fail-closed summarizer requires every reviewed device/scenario cell without unsafe critical-process APIs. | Executed Android/Windows scenario matrix and reviewer sign-off.                                          |
| `PKM-EVAL-006`                 | Completed protocol input drives a suppressed aggregate pre/post analyzer; the final gate requires ethics, accessibility, adverse-event, study-result, and limitations records.                | Academic/ethical approval and an actually executed staged study.                                         |

## Privacy boundary

- Evaluation inputs containing URL or DOM text remain under
  `evaluation/phase4/private-data/` or another approved local research store.
- Model reports contain aggregate metrics and opaque sample IDs only.
- Native latency evidence contains durations, declared scenario labels, and
  artifact versions only. It contains no URL, domain, DOM, score, or history.
- Retention input is separately consented D6 research data. The committed
  analyzer emits suppressed cohort summaries and never participant rows.
- Pattern Interrupt study input requires separate research consent and a
  completed ethics-approved protocol; reports suppress small groups and omit
  participant rows, free text, and browsing/recovery content.
- No Phase 4 evidence is uploaded through the production backend.

## Evidence states

- `instrumented`: repository tooling and local capture points are wired.
- `pilot`: an approved preliminary dataset/device/cohort run exists.
- `evaluated`: every applicable evidence-manifest gate resolves to an existing,
  hashed, reviewed artifact from the declared final protocol.

The canonical machine check is:

```sh
python3 evaluation/phase4/verify_evidence.py \
  evaluation/phase4/results/evidence-manifest.json
```

The checker must return non-zero while any required external artifact or
approval is missing. That failure is an honest project status, not a tooling
failure.
