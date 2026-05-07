---
type: org
status: active
aliases: [Judgment Labs, JL, Judgment]
last_updated: 2026-05-06
sources:
  - /Users/kian/.codex/memories/MEMORY.md
  - /Users/kian/obsidian/jl/
kind: startup
confidence: high
---

# Judgment Labs

Kian's primary work context. Houses the agent-harness lab, advisor / SWE-bench Verified GCP eval, EvoForge, the meta-harness, and the Judgment CLI / tracing stack.

## Repos

- [[../projects/parallel-ralph-lab]]
- [[../projects/advisor]]
- [[../projects/baseline]]
- [[../projects/autoagent]]
- [[../projects/judgment-agent-harness]]
- [[../projects/self-improving-swe-bench-pro]]
- subagents, databasline, EvoForge (workspace)
- judgment-research (MST clustering pipeline)

## Operational

- Local `.env` at `/Users/kian/Code/.env` for shared keys
- Judgment CLI: `judgment status`, `JUDGMENT_BASE_URL`, `judgeval.Tracer`, `judgment traces search`
- Validate live runs are actually traced before assuming the pipeline works
- Authenticate the installed Judgment CLI from `/Users/kian/Code/.env`
- For Judgment MCP auth docs: keep live secret out of `config.toml`; prefer `bearer_token_env_var` plus a separate export step

## Common gotchas

- Cheap checks can pass while runtime contract is wrong; verify with real artifacts
- ClickHouse HTTP 400 on `score_results` upload usually means schema mismatch, not auth
- Distinguish trace ingestion from trace export — failed export ≠ traces never arrived
