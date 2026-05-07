---
type: project
status: active
last_updated: 2026-05-06
sources:
  - /Users/kian/.codex/memories/MEMORY.md
repo: autoagent
cwd: /Users/kian/Code/autoagent
confidence: high
---

# autoagent

The reference shape for "AutoAgent-style" runtime that [[baseline]] is migrating toward.

## File / runtime distinction (load-bearing)

- `agent.py` — default harness under test
- `agent-claude.py` — separate Claude variant
- Harbor — outer wrapper
- OpenAI Agents SDK — inner runtime
- `program.md` — the agent's program description
