# Cross-repository Testing and Evidence Context

If this document conflicts with `pkm_proposal.md`, the PKM proposal remains
the authority. This document defines engineering workflow and evidence
ownership; it is not a replacement for academic review or a completed study.

## Ownership

`gamblock-ai-testing/` is the canonical owner of cross-repository evaluation,
runtime evidence promotion, and per-technology testing reports. Product
repositories retain production code, component unit tests, lint configuration,
and source-specific fixtures.

Within the testing repository, system-specific tooling is separated into
`flutter/`, `golang/`, `next/`, and `browser-extention/`; model scope is
documented in `model/`. Cross-system checks live only under `docs/tools/`. This
keeps system-specific test assets from being mixed while preserving one ledger
per owning technology and one canonical report per technology.
Model replay evidence has a dedicated storage contract: permanent aggregate
JSON belongs under `gamblock-ai-testing/model/evidence/aggregate/` and charts
generated only from aggregate metrics belong under the exact allowlisted paths
in `gamblock-ai-testing/model/evidence/visuals/`. Raw prediction tables and other
sensitive replay inputs belong under ignored `gamblock-ai-testing/model/private/`.

The committed human-readable reports are:

```text
gamblock-ai-testing/flutter/report.md
gamblock-ai-testing/golang/report.md
gamblock-ai-testing/next/report.md
gamblock-ai-testing/browser-extention/report.md
gamblock-ai-testing/model/report.md
```

`docs/testing-index.md` only links to these reports and does not repeat their
results. JSONL files under a technology's `evidence/ledger/` are structured
source records for that technology's report. The umbrella stores context and
the pinned submodule commit only.

## Test execution handoff and receipt

### Audit versus execution

“Cek”, “periksa”, “review”, “audit”, dan “ringkas pengujian yang ada” adalah
permintaan audit read-only. Audit membaca source test, konfigurasi/workflow,
report/evidence yang sudah ada, status repository, dan runbook; audit tidak
menjalankan command test, membangun artifact, meregenerasi report, atau
melakukan prosedur Android/Windows/model. Status pada report yang sudah ada
harus disebut sebagai status tercatat karena mungkin bukan hasil terbaru.

Command hanya boleh dijalankan bila user meminta secara eksplisit untuk
menjalankan/menguji/validasi/evaluasi ulang atau merekam evidence baru. Jika
scope eksekusi disebutkan, jangan memperluasnya ke semua komponen. Test receipt
dan sinkronisasi report diwajibkan untuk eksekusi/evidence yang benar-benar
dijalankan, bukan untuk audit read-only.

An explicit test, evaluation, or re-evaluation request is not complete when a
component command merely succeeds. The agent must synchronize the relevant
technology report in `gamblock-ai-testing/` through the cross-system runner,
or record the exact reason that synchronization is `pending` or `blocked`.
Direct component commands remain useful for diagnosis, but they do not by
themselves publish project evidence.

Every completed test requires a final test receipt. The receipt is delivered
in the agent's handoff response and is not a second report. It must contain:

- run ID or sample label, technology, scope, command, status, and source
  repository commit(s);
- testing-repository public files added or modified and a short description of
  the aggregate-safe data in each file;
- private/local artifacts created, their location class (testing checkout,
  component checkout, or external temporary directory), contents at a safe
  level, and whether they were deleted or remain local;
- validator results, testing-repository commit status, and push status;
- `none` for any empty public or private category.

The agent must inspect both repositories' `git status` and `git diff` before
writing the receipt. Raw command output, screenshots, ADB traces, URLs,
domains, DOM, browsing history, serials, credentials, and participant data
must never be included in the receipt or public report. Hashes and aggregate
metrics are allowed only within the existing evidence contract.

The receipt format is maintained in
`gamblock-ai-testing/docs/ai/testing-run-receipt.md`. It is a response-level
handoff record, not a second committed result file.

## PKM progress-report traceability

`context/laporan-kemajuan.md` is the active proposal-facing progress-report
context. The status, limitation, and remaining-final-gate interpretation for
each claim is maintained in `context/progress-testing.md`, while target
definitions are maintained in `context/progress-targets.md`. The status file
may be updated as evidence changes, but neither it nor a component report may
silently redefine the current target contract.

## Evidence contract

Evidence must distinguish source-code checks, offline replay, and physical
runtime behavior. An unexecuted device/scenario cell is `pending`; a narrative
or old number without a validated export is not promoted to runtime evidence.

Android Research anti-uninstall evidence covers supported OS surfaces and
lifecycle recovery. The required OEM families and scenarios are versioned in
the testing repository's `flutter/config/device-matrix.json`.
The cross-OEM problem statement, Firebase Test Lab Android Device Streaming
context, and current device-status interpretation are maintained in
`gamblock-ai-testing/docs/ai/android-anti-uninstall-context.md`; detailed
validated scenario results remain in `flutter/report.md`.

The testing repository's `docs/config/targets.json` is the single active
machine-readable configuration. The runner uses it directly and does not
select among parallel report or target configurations.

Phase 4 latency has two named, separately rendered gates. `latency_feasibility`
is one homogeneous 30-sample group below the p95 200 ms target. The current
`progress_demo` checkpoint is intentionally narrower: the demonstrated Android
`researchRelease` APK, Chrome, and `warm_foreground_online`, with 30 successful
samples and no block/visibility failure. The former final-readiness latency
gate has been replaced by the cross-platform browser support regression. The
regression requires one Android device and treats the Windows browser matrix as
optional and non-gating. A debug measurement is diagnostic and cannot satisfy
the progress checkpoint.

The browser client-runtime evidence uses explicit
`<platform>/<browser>/<case>` folders under
`gamblock-ai-testing/flutter/evidence/client-runtime/`. Android cells are
required; Windows cells are optional when evidence is available. The active
target configuration and `docs/ai/client-runtime-evidence.md` define the exact
directory and aggregate-file contract.

## Public privacy boundary

The public ledger may contain only aggregate-safe labels and state:

- OEM family, Android API, build mode, product flavor, scenario, outcome, and recovery duration
- opaque run/sample labels
- allowlisted component status and output hashes
- local visual-evidence availability and a SHA-256 digest, when supplied

URLs, domains, DOM text, browsing history, keystrokes, screenshots, serial
numbers, credentials, participant data, raw ADB/logcat output, and local paths
must never be published. A screenshot digest does not authorize publishing the
image itself.
Model aggregate charts are not screenshots: they are permitted only when
generated from aggregate metrics and written to the exact allowlisted visual
paths by the testing runner; they must not contain sample-level or browsing
content.

Human-participant testing is separate from product consent. Identifiers, raw
responses, recordings, screenshots, consent forms, and raw task observations
stay outside the repository under the approved institutional process. Public
documentation may retain only approved aggregate counts, protocol version,
and aggregate outcomes.

## Firebase and device policy

Firebase Device Streaming, Android Studio Remote Devices, ADB lifecycle
actions, and Windows VM runs are explicit operator actions. Repository CI does
not reserve devices or execute cost-bearing cloud tests automatically. Review
the matrix and quota before starting a session, use disposable device state,
and promote results only through the testing repository validators.

Optional Firebase CLI MCP usage is limited to operator-configured inspection;
credentials and project configuration are never committed, and MCP does not
replace the interactive device workflow.

## Validation

From the umbrella:

```sh
./scripts/verify-ai-context.sh
python3 gamblock-ai-testing/docs/tools/verify_public_evidence.py
```

From the testing repository:

```sh
./docs/tools/verify-ai-context.sh
python3 docs/tools/verify_public_evidence.py
```

Device actions, builds, and full component test suites remain explicit checks.
