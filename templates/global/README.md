# Optional Personal Agent Defaults

These files are templates for user-level preferences that apply across
repositories. They intentionally contain no Gamblock-AI product rules; project
rules must travel with each repository.

Nothing in this directory is installed automatically. Review and copy only the
template for the tool you use:

| Tool | Template | Typical destination |
|---|---|---|
| Codex | `codex-AGENTS.md` | `~/.codex/AGENTS.md` |
| Claude Code | `claude-CLAUDE.md` | `~/.claude/CLAUDE.md` |
| Gemini CLI | `gemini-GEMINI.md` | `~/.gemini/GEMINI.md` |
| GitHub Copilot CLI | `copilot-instructions.md` | `~/.copilot/copilot-instructions.md` when supported |
| Cursor | `cursor-user-rules.txt` | Cursor Settings -> Rules -> User Rules |

Repository instructions take precedence in intent. If a personal preference
conflicts with a safety or architecture rule in a repository, follow the
repository rule.

These defaults intentionally limit local AI validation to the
repository-designated linter/analyzer plus a context validator when context
changes. Standalone typechecking, tests, builds, packaging, coverage, and E2E
are opt-in when explicitly requested by the user; repository CI may still run
its own automatic quality gates.
