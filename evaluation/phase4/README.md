# Phase 4 Evidence Workbench

This directory provides privacy-preserving, reproducible tooling for the
proposal's integration and system-hardening phase. It is an evidence workbench,
not a claim that UTY evaluation has already happened.

## Local-only directories

- `private-data/` — governed labeled URL/DOM or pseudonymous research input;
- `results/` — generated reports, native timing exports, and signed reviews.

Both directories are ignored by Git. Do not copy raw browsing fixtures,
participant rows, device identifiers, tokens, or screenshots elsewhere in the
workspace.

## Model evaluation

Input is JSON Lines. Each row needs an opaque `id`, opaque `group_id`, `split`,
`label`, `slice`, and the local research fields `url`, `title`, `headings`, and
`anchor_texts`. Allowed labels are `gambling` and `benign`. Allowed slices are
`gambling`, `dynamic`, `camouflage`, `benign`, `government`, `education`, and
`other`.

```sh
python3 evaluation/phase4/evaluate_model.py \
  --dataset evaluation/phase4/private-data/final-test.jsonl \
  --dataset-card evaluation/phase4/private-data/dataset-card.json \
  --split-manifest evaluation/phase4/private-data/split-manifest.json \
  --model gamblock_ai_apps/assets/protection/gamblock-lr-v2.json \
  --rules gamblock_ai_apps/assets/protection/gamblock-rules-v2.json \
  --mode final \
  --output evaluation/phase4/results/model-report.json
```

The output contains aggregate metrics, hashes, and opaque failure IDs only.
The tool calculates Hybrid, model-only, and rule-only results. It deliberately
does not mark the model artifact itself as `evaluated`; reviewer approval and
the final evidence manifest own that decision.

## Latency

Enable native evidence mode only on an approved disposable device or VM. Use
the platform scripts documented in the Flutter repository, export their JSONL,
then summarize all declared scenarios:

```sh
python3 evaluation/phase4/summarize_latency.py \
  --input evaluation/phase4/results/android-latency.jsonl \
  --input evaluation/phase4/results/windows-latency.jsonl \
  --device-matrix evaluation/phase4/private-data/device-matrix.json \
  --target-percentile p95 \
  --output evaluation/phase4/results/latency-report.json
```

The proposal target is below 200 ms. The percentile used as the acceptance gate
must be an owner-approved protocol decision; the command requires it explicitly.
Following the approved evaluation definition, the gate uses
`input_to_visible_ms`: complete supported local input through the first
committed Pattern Interrupt frame. `scan_to_visible_ms` and component
durations remain diagnostic fields and do not replace the acceptance metric.

## Retention

Retention analysis accepts only separately consented pseudonymous research
rows. It never reads production browsing data.

```sh
python3 evaluation/phase4/analyze_retention.py \
  --input evaluation/phase4/private-data/retention.jsonl \
  --protocol evaluation/phase4/private-data/retention-protocol.json \
  --output evaluation/phase4/results/retention-report.json
```

## Pattern Interrupt study

Only run this analysis under a completed, ethics-approved protocol. Input rows
use opaque participant/cohort IDs, one of the two declared condition labels,
explicit consent/withdrawal/completion flags, bounded pre/post scores, and a
closed adverse-event category—never browsing data or free text.

```sh
python3 evaluation/phase4/analyze_pattern_interrupt.py \
  --input evaluation/phase4/private-data/pattern-interrupt.jsonl \
  --protocol evaluation/phase4/private-data/pattern-interrupt-protocol.json \
  --output evaluation/phase4/results/pattern-interrupt-report.json
```

The report is descriptive, suppresses undersized groups, and cannot establish
clinical or causal efficacy. Complete the adverse-event and limitations review
templates separately; an actual institutional ethics approval is required and
has no synthetic repository template.

## Resilience matrix

The native harnesses produce one unreviewed `ordinary_process_kill` result.
Use `resilience-run.template.json` for the remaining approved disposable-device
or VM scenarios, obtain review, and check the complete device/scenario grid:

```sh
python3 evaluation/phase4/summarize_resilience.py \
  --input evaluation/phase4/results/android-resilience.json \
  --input evaluation/phase4/results/windows-resilience.json \
  --matrix evaluation/phase4/private-data/resilience-matrix.json \
  --output evaluation/phase4/results/resilience-report.json
```

The command returns non-zero for missing/unreviewed cells or any failed safety
and recovery result.

## Final gate

Copy `evidence-manifest.example.json` into the ignored `results/` directory,
replace every placeholder with a reviewed artifact and SHA-256, then run:

```sh
python3 evaluation/phase4/verify_evidence.py \
  evaluation/phase4/results/evidence-manifest.json
```

The command fails closed until all Phase 4 requirements have real evidence.
That includes the approved device and resilience matrices plus an
ethics-reviewed Pattern Interrupt protocol, executed study report, adverse
event review, and limitations review; instrumentation alone cannot satisfy the
gate. Generated model, latency, resilience, retention, and Pattern Interrupt
reports start with `review.approved: false`; the accountable reviewer must add
their approval metadata before hashing the immutable final copy. The verifier
also rejects failed latency/resilience gates and suppressed/empty study output.
