# Personal Claude Code Defaults

- Load the project's `CLAUDE.md` and its imported canonical instructions.
- Preserve unrelated worktree changes and avoid destructive Git operations.
- Ask before production mutations, deploys, releases, pushes, secret changes,
  or new production dependencies.
- Keep changes small. Run only the repository-designated linter/analyzer by
  default and its context validator when context changes. Standalone
  typechecking, tests, builds, packaging, coverage, and E2E require the user's
  explicit request. Report only checks that actually ran.
- Follow repository conventions over these personal defaults when they differ.
