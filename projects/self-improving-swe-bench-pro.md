---
type: project
status: active
last_updated: 2026-05-06
sources:
  - /Users/kian/.codex/memories/MEMORY.md
repo: self-improving-swe-bench-pro
cwd: /Users/kian/Code/self-improving-swe-bench-pro
confidence: high
---

# self-improving-swe-bench-pro

Meta-Harness for self-improving runs against SWE-bench Pro. Local trace bundling + Judgment upload boundaries.

## Boundaries (load-bearing)

- **Trace ingestion ≠ trace export.** A failed export does not prove traces never arrived.
- Candidate-local trace bundling: `judgment_traces.jsonl` + `judgment trace export`
- `score_results` upload to ClickHouse can return HTTP 400 on schema mismatch
- Guarded exception-path saves prevent dropping work on partial failures
- Seed-vs-iteration batch slicing: first batch only for the seed, not all batches
