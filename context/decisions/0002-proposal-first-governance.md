# ADR-0002: Proposal-First Product Governance

- Status: accepted
- Date: 2026-07-15
- Context version: `2026-07-15.2`

## Context

Gamblock-AI contains an academic PKM proposal, a growing multi-component
prototype, and supporting product features that go beyond the proposal. Older
context documents treated the product overview as the scope authority and
used unsupported `PRD` references. This made it possible for implementation
convenience or supporting website work to displace mandatory PKM outcomes.

The stored proposal extraction is also incomplete around section 3.2. A
derived document must therefore be explicit about what is quoted from the
available proposal and what is a later design decision.

## Decision

`context/pkm_proposal.md` is the primary authority for academic intent,
mandatory product capabilities, target users, evaluation objectives, and PKM
deliverables.

The repository uses three scope classes:

1. **PKM core** — directly required by the proposal. These requirements use a
   stable proposal-requirement identifier in `proposal-requirements.md` and
   cannot be dropped by a
   supporting decision.
2. **Supporting product** — improves usability, safety, recovery, supervision,
   or dissemination but is not stated as a core proposal requirement. These
   features use an exact supporting or domain-specific identifier.
3. **Operational** — administration, delivery, observability, content
   operations, and infrastructure needed to run the prototype responsibly.

Derived documents may clarify ambiguous implementation boundaries, especially
privacy and safe anti-tamper behavior, but must label those clarifications as
engineering decisions. Missing proposal text must not be reconstructed as if
it were verbatim source.

## Consequences

- Every product feature must state whether it is PKM core, supporting, or
  operational.
- Current code status remains separate from target requirements.
- Supporting website features may be numerous, but PKM core recovery features
  receive higher priority and explicit traceability.
- Academic novelty and effectiveness statements remain hypotheses until the
  evidence defined in `research-evaluation.md` exists.
- Restoring the original proposal's missing sections triggers a traceability
  review and, when requirements change, a context-version bump.
- Component snapshots carry the proposal requirement IDs relevant to that
  component so standalone clones retain the product rationale.
