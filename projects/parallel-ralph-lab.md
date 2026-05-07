---
type: project
status: active
last_updated: 2026-05-06
sources:
  - /Users/kian/.codex/memories/MEMORY.md
repo: parallel-ralph-lab
cwd: /Users/kian/Code/parallel-ralph-lab
confidence: high
---

# parallel-ralph-lab

Agent harness lab. Two distinct paths matter:
- Older `runner.py` live-harness path
- Newer root-level `loop.py` + `evaluators/` plan implementation path

Both `templates/harness` and `templates/harness.bundle` are load-bearing — refresh both when seed contents change.

## Operational notes

- `MODEL` lives in a committed `.env`
- Prefer `Path(sys.executable).with_name("harbor")` before falling back to `harbor` on `PATH`
- `w0` is the canonical sync workspace
- Run tests via `python3 -B -m unittest discover -s tests` (this repo documents `unittest`, not `pytest`)
- Cheap checks (`unittest`, `py_compile`) can pass while runtime contract is still wrong — don't treat them as proof of execution readiness

## Known failure modes

- `JSONDecodeError: Extra data` → suspect generated workspace harness parser, not the benchmark task
- `swe-bench-verified` exact-count checks were brittle
- TCC / Full Disk Access can make the same path look empty under launchd vs manual run

## Conventions

- Prefer repo-local seeded files/skills over plugin-only or cloud-specific logic when the system must work across builders
- Trim `tests/test_registry_loading.py` without widening the assertion surface
- Empty prior traces/scores/messages are normal bootstrap state
- "One problem, one fix" summary style fits this workflow

## Links

- Sibling: [[baseline]] (single-agent variant, doesn't mutate this repo)
- Related: [[../concepts/agent-harnessing]]
- Org: [[../orgs/judgment-labs]]
