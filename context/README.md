# Gamblock-AI Context Router

Context version: `2026-07-29.1`

This directory is the durable knowledge base for Gamblock-AI. It separates
academic intent, derived product decisions, technical design, and current
implementation evidence so a fresh developer or AI agent does not silently
turn an implementation detail into a PKM requirement.

## Source-of-truth hierarchy

Use this order when documents disagree:

1. `pkm_proposal.md` — primary authority for the problem, target users,
   mandatory PKM features, scientific rationale, evaluation goals, and PKM
   deliverables.
2. `proposal-requirements.md` — normalized, traceable requirement IDs derived
   only from text that is present in the proposal.
3. `project-overview.md` — product specification derived from the proposal;
   it may add supporting capabilities but may not remove or weaken a proposal
   requirement.
4. Domain documents (`architecture.md`, `website-product.md`,
   `ui-context.md`, `privacy-security.md`, `research-evaluation.md`) — explain
   how the product should satisfy the requirements.
5. Component `docs/ai/README.md` files — describe current implementation truth
   and evidence for each independently releasable repository.
6. ADRs under `decisions/` — record long-lived engineering decisions. An ADR
   may choose an implementation, but it may not rewrite the proposal's intent.

Code is evidence of current behavior, not permission to redefine the target.
When code and the proposal differ, record the gap in the affected component's
`docs/ai/README.md`.

## Proposal integrity warning

The current Markdown extraction of `pkm_proposal.md` is incomplete: content
for Fase 1–3 in section 3.2 is missing, an OCR/image fragment remains, and the
final Fase 5 paragraph is truncated. Do not invent the missing academic text.
Restore it from the team's original PDF/DOC source when available, then review
all derived documents and bump the context version if requirements change.

The proposal itself is protected source material. Do not rewrite it merely to
match current code or a new product idea. Academic edits require an explicit
request and a reliable source from the proposal owners.

## Reading routes

| Task | Required context |
|---|---|
| Any product or implementation change | `pkm_proposal.md` relevant section, `proposal-requirements.md`, `ai-workflow-rules.md`, affected component `docs/ai/README.md` |
| Product scope, actors, journeys, or priorities | `project-overview.md`, `glossary.md` |
| Detection, native client, API, storage, or cross-component design | `architecture.md`, `privacy-security.md`, `mobile-product.md` for client behavior |
| Website feature or route | `website-product.md`, `ui-context.md`, relevant component `AGENTS.md` |
| Visual or interaction design | `ui-context.md`, `website-product.md` when web-facing |
| Dataset, model, metric, experiment, or academic claim | `research-evaluation.md`, `proposal-requirements.md` |
| Implementation status or next work | affected component `docs/ai/README.md` |
| Multi-repository context tooling | `manifest.yaml`, `decisions/0001-multi-repo-context.md` |
| Product-governance conflict | `decisions/0002-proposal-first-governance.md` |

For a narrow task, read the proposal sections and requirement IDs that apply;
loading the entire repository is not required. The non-negotiable privacy,
passive-extension, and safe anti-tamper rules still apply to every task.

Capability and evidence labels are defined once in `glossary.md`. Use those
terms in every status document; do not invent a stronger synonym for partial
evidence.

## Ownership and update rules

| Change | Update first | Then update |
|---|---|---|
| Proposal requirement or academic claim | `pkm_proposal.md` only with owner/source authorization | `proposal-requirements.md`, affected domain docs, tracker |
| Derived product scope or supporting feature | `project-overview.md` or `website-product.md` | architecture/UI/privacy docs and tracker |
| Architecture or trust boundary | `architecture.md` / `privacy-security.md` | component snapshots and ADR when long-lived |
| Visual or behavioral UX | `ui-context.md` | website/client docs and tracker |
| Research method or metric definition | `research-evaluation.md` | traceability and tracker |
| Workflow or validation policy | `ai-workflow-rules.md` | root/component `AGENTS.md`, skills, manifests, templates |
| Current capability evidence | relevant component `docs/ai/README.md` | affected README or domain document when behavior/contract changed |

Meaningful scope, architecture, workflow, or shared-contract changes require a
`context_version` bump in `manifest.yaml` and every affected component
snapshot. Spelling-only changes do not.

Keep component status documents limited to current status, evidence, gaps,
blockers, and next work. Historical change and command logs belong in version
control or CI records.

## Default validation policy

During normal AI-assisted development, run only the relevant linter/analyzer
and, when context files changed, the context-integrity validator. Tests,
builds, packaging, coverage, and end-to-end suites run only when the user asks
for them explicitly in the current conversation. See
`ai-workflow-rules.md` for the exact command matrix.
