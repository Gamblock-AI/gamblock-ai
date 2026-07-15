# ADR-0001: Versioned AI Context for Independent Repositories

- Status: accepted
- Date: 2026-07-15
- Context version: `2026-07-15.2`

## Decision

Keep the backend, website, Flutter client, browser extension, and
infrastructure as independent repositories. Add a sixth umbrella repository
that owns shared product context, the component composition, bootstrap tools,
and cross-repository validation.

Each component repository must remain safe and understandable when cloned by
itself. It therefore carries:

- a self-contained root `AGENTS.md`;
- a concise product/component snapshot under `docs/ai/`;
- native entry points for supported agents;
- a local context-integrity check; and
- the shared `context_version` marker.

The umbrella repository pins component revisions as Git submodules and runs
cross-repository checks. Shared context is intentionally summarized in each
component rather than referenced through `../` paths that disappear in a
standalone clone.

## Rationale

The components already have separate release histories and GitHub remotes.
Converting them into one monorepo would require a history and release migration
unrelated to the context-loss problem. Parent-only instructions are not
portable, while copying all academic and UI context into every repository
would waste context and create unnecessary drift. A versioned minimal snapshot
balances standalone safety with centralized governance.

## Consequences

- Shared invariant changes require a context-version bump and snapshot update.
- Proposal-derived requirement changes require the same snapshot review so a
  standalone component retains the rationale relevant to its responsibility.
- Cross-repository validation runs from the umbrella checkout.
- A standalone component clone cannot enforce another repository's pending
  change; its handoff must name the related repository and contract.
- User-level agent preferences stay outside product rules. Version-controlled
  templates may be provided, but installation is always explicit.
