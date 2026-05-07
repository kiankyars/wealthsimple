---
type: concept
domain: technical
last_updated: 2026-05-06
sources:
  - /Users/kian/obsidian/people/molly.md
  - /Users/kian/.codex/memories/MEMORY.md
confidence: high
---

# Agent harnessing

The harness — the scaffolding around an LLM call (file tools, retries, evaluators, trace capture, prompt routing) — is what defines whether an agentic system works. The model is interchangeable; the harness is the durable IP.

## Why it matters

- [[../people/molly]]: "Agent harnessing matters a lot; the harness is what defines success."
- [[../people/molly]] is bearish on many-agent swarms (32 agents in parallel). Even in 2021 hackathons she did 2 people max — the analog being that coordination cost dominates.

## Where Kian works on this

- [[../projects/parallel-ralph-lab]] — primary harness lab
- [[../projects/advisor]] — eval + dashboard around harness runs
- [[../projects/baseline]] — collapsing manager/worker into single agent
- [[../projects/autoagent]] — reference shape (`agent.py` + `program.md`, Harbor outer wrapper, OpenAI Agents inner runtime)
- [[../projects/self-improving-swe-bench-pro]] — meta-harness for self-improving runs

## Practical heuristics from MEMORY.md

- Cheap checks (`unittest`, `py_compile`) can pass while runtime contract is still wrong — never treat them as proof of execution readiness
- Distinguish older `runner.py` live-harness path from newer `loop.py` + `evaluators/` path in [[../projects/parallel-ralph-lab]]
- Both `templates/harness` and `templates/harness.bundle` matter; refresh both when seed contents change
- Repo-local seeded files/skills > plugin-only or cloud-specific logic when system must work across builders
- Empty prior traces/scores/messages = normal bootstrap state, not a bug
- Hardened launcher only for ablation recovery; do not call score drops "regression" until the generation is fully finished
- Subagent authorization wording: narrow `if helpful`, not unconditional spawn
