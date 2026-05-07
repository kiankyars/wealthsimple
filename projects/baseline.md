---
type: project
status: active
last_updated: 2026-05-06
sources:
  - /Users/kian/.codex/memories/MEMORY.md
repo: baseline
cwd: /Users/kian/Code/baseline
confidence: high
---

# baseline

Single-agent variant of [[parallel-ralph-lab]]. Sibling directory, not a mutation of the original. Preserves the three-held-out-datasets experiment but collapses manager/worker coordination into one agent.

## Architecture

- Outer runner preserved
- Mutable harness workspace: nested `agent/` git repo
- Direction: AutoAgent-style — `agent.py` + `program.md` for the inner runtime, with Harbor as outer wrapper
- See [[autoagent]] for the file/runtime distinction

## Why a sibling, not a fork

User explicitly: "do not mutate the original repo if I want to keep it". Build new directory; re-read live source before copying behavior.

## Run shape

- `runs/<run_id>/sessions/`
