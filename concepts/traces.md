---
type: concept
domain: technical
last_updated: 2026-05-06
sources:
  - /Users/kian/obsidian/people/nick.md
  - /Users/kian/.codex/memories/MEMORY.md
confidence: high
---

# Traces

Agent execution traces — the sequential, hierarchical record of an agent's calls, tool uses, and outputs. A first-class object that Judgment Labs and adjacent stacks treat as data, not just logs.

## Properties (per [[../people/nick]])

- Sequential, hierarchical, easy for default models to get distracted by — they latch onto the original task / train of thought
- Naturally graph-shaped, but graph methods get chunky at larger scales
- One trace expands into many thought / turn nodes — node counts balloon

## Approaches

### Trace-as-filesystem ([[../people/nick]])
- Break a trace into hierarchical text files
- Agents are good at operating over file trees
- Direct analog of how the wiki itself is structured

### Embedding + clustering
- Standard alternative: chunking, clustering over traces or raw JSON
- ReAct / agent-thought portions usually need heavy trimming first — otherwise they dominate and all traces look too similar

### Routing by agreement ([[../people/nick]])
- Multiple specialists / prompts / metrics
- Decide from combined outputs, not one metric alone
- Vision-model version: split into specialists in later layers vs end-to-end duplication

## Scaling

- GNN-based context-selection: ~1,000 traces / ~10,000 nodes to keep processing under ~1s
- Whether graph-based works depends heavily on how many traces fed in

## Operational practice (Judgment stack)

- `judgeval.Tracer` for capture
- `judgment traces search` for retrieval
- `judgment trace export` is separate from trace ingestion — failed export ≠ traces never arrived
- Validate live runs are actually traced before assuming pipeline works

## Open question (Nick)

- Could a separate model trained on traces beat general API models? Defaults get distracted; can start *following* the trace's reasoning instead of analyzing it.

## Related

- [[../projects/judgment-agent-harness]] — MailboxStore, BlackboardLedger, attempts.jsonl
- [[../projects/judgment-research]] — MST clustering pipeline (centroid decomposition over trace embeddings)
- [[../projects/self-improving-swe-bench-pro]] — local trace bundling
