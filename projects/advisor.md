---
type: project
status: active
last_updated: 2026-05-06
sources:
  - /Users/kian/.codex/memories/MEMORY.md
repo: advisor
cwd: /Users/kian/Code/advisor
confidence: high
---

# advisor

Houses SWE-bench Verified GCP eval scaffolding + dashboard / artifact serving + the Advisor MCP migration. Part of the EvoForge workspace ecosystem along with [[subagents]] and `databasline`.

## Conventions

- Codex auth: `gpt-5-nano` works only via explicit `CODEX_API_KEY="$OPENAI_API_KEY"`; ChatGPT auth fails
- Dashboard (`prior-run-artifacts/serve_results.py`) needs a local markdown fallback for tables/quotes/rules
- GCP eval path is intentionally minimal; verify via real VM/artifact checks
- SWE-bench Verified GCP local-mode eval scaffolding lives in `run_swebench_verified_gcp_local.sh`

## EvoForge launcher discipline

- "Hardened launcher only" path for ablation recovery — do not call a score drop "regression" until the generation is fully finished and not externally confounded
- Prefer bounded `ps` / log / artifact checks over file-count watching
- Subagent authorization wording: narrow `if helpful`, not unconditional spawn
- Claude-only MCP + launcher-managed recovery became the stable path

## Links

- Sibling repos: [[../orgs/judgment-labs]] uses these together
- Related: [[../concepts/agent-harnessing]]
