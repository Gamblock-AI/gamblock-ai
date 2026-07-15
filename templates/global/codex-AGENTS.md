# Personal Codex Defaults

- Read and follow repository and nested `AGENTS.md` files before editing.
- Inspect the worktree and preserve unrelated user changes.
- Ask before destructive actions, production mutations, releases, pushes,
  secret changes, or adding production dependencies.
- Prefer small changes. Run only the repository-designated linter/analyzer by
  default and its context validator when context changes. Run standalone
  typechecking, tests, builds, packaging, coverage, or E2E only when the user
  explicitly requests them in the current conversation.
- State assumptions and report exact commands for checks that passed or could
  not run.
- Respond in the user's language; follow the repository's language conventions
  for code and documentation.
