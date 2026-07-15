# Personal Gemini CLI Defaults

- Load the repository's hierarchical context before changing files.
- Preserve unrelated worktree changes and request approval for destructive or
  externally mutating actions.
- Prefer focused changes with only the repository-designated linter/analyzer
  and context validator when context changes. Do not run standalone
  typechecking, tests, builds, packaging, coverage, or E2E unless the user
  explicitly requests them.
- Follow project-specific architecture and language rules over these defaults.
