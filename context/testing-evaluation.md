# Cross-repository Testing and Evidence Context

If this document conflicts with `pkm_proposal.md`, the PKM proposal remains
the authority. This document defines engineering workflow and evidence
ownership; it is not a replacement for academic review or a completed study.

## Ownership

`gamblock-ai-testing/` is the canonical owner of cross-repository evaluation,
runtime evidence promotion, and the public testing summary. Product
repositories retain production code, component unit tests, lint configuration,
and source-specific fixtures.

The only committed human-readable cross-repository summary is:

```text
gamblock-ai-testing/reports/testing-summary.md
```

The JSONL files in the testing repository's `evidence/ledger/` are structured
source records for that summary, not alternate summaries. The umbrella stores
context and the pinned submodule commit only.

## Evidence contract

Evidence must distinguish source-code checks, offline replay, and physical
runtime behavior. An unexecuted device/scenario cell is `pending`; a narrative
or old number without a validated export is not promoted to runtime evidence.

Android Research anti-uninstall evidence covers supported OS surfaces and
lifecycle recovery. The required OEM families and scenarios are versioned in
the testing repository's `config/device-matrix.json`.

## Public privacy boundary

The public ledger may contain only aggregate-safe labels and state:

- OEM family, Android API, build mode, scenario, outcome, and recovery duration
- opaque run/sample labels
- allowlisted component status and output hashes
- local visual-evidence availability and a SHA-256 digest, when supplied

URLs, domains, DOM text, browsing history, keystrokes, screenshots, serial
numbers, credentials, participant data, raw ADB/logcat output, and local paths
must never be published. A screenshot digest does not authorize publishing the
image itself.

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
python3 gamblock-ai-testing/scripts/verify_public_evidence.py
```

From the testing repository:

```sh
./scripts/verify-ai-context.sh
python3 scripts/verify_public_evidence.py
```

Device actions, builds, and full component test suites remain explicit checks.
