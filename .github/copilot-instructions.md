# Gamblock-AI Copilot Instructions

Read and follow `AGENTS.md` before proposing or changing code. Use
`context/README.md` to select the relevant product context, then read the
closest component `AGENTS.md` and `docs/ai/README.md` before working in a
component.

Non-negotiable rules:

- Keep all gambling-content classification on-device; never send raw DOM,
  URLs, domains, screenshots, or browsing history to the backend.
- Keep the browser extension passive. It does not classify, block, redirect,
  close tabs, or render Pattern Interrupt.
- Never use critical-process APIs for anti-tamper.
- Treat `context/pkm_proposal.md` as the primary product authority and label
  supporting additions separately.
- Preserve unrelated worktree changes. Run only the relevant linter/analyzer
  and context validator by default; tests/builds/packages/e2e require the
  user's explicit request.
- Keep implementation status distinct from target architecture and stubs.
