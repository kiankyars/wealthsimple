---
type: person
status: active
aliases: [Nick]
last_updated: 2026-05-06
sources:
  - /Users/kian/obsidian/people/nick.md
confidence: high
last_contact: 2026-03-18
relationship: technical peer (traces / agent eval)
---

# Nick

Trace-analysis and knowledge-graph specialist. Strong technical depth; "the person others recommend talking to" on traces, agent eval, graph methods, and extraction pipelines. Worth keeping warm long-term.

## Background

- Master's in analytics + MBA. Analytics master's done part-time, paid by employer. MBA via startup-focused program that covered tuition for founders (he founded a startup during it).
- Studied at Georgia Tech and CMU.
- View: graduate school often doesn't need to be self-funded if you're doing interesting enough work.

## Technical depth

- Trace analysis, meta-learning, knowledge-graph extraction, GNNs, SQL agents, tracing infrastructure
- LangChain + LangSmith-style tracing hooks; finds they miss intermediate events
- Overrides default model behavior + inserts corrective passes into the hot path
- Uses smaller "watcher" model to catch typos / imports / simple code problems before letting full agent continue. Caught ~30% of SQL-agent errors, especially on complex SQL where the model got lazy about imports/tabs/syntax.

## Trace / model takes (see [[../concepts/traces]])

- Traces are unusual inputs: sequential, hierarchical, easy for default models to get distracted by because they latch onto the original task
- Heavily trims ReAct / agent-thought portions before clustering — otherwise they dominate and traces look too similar
- **Trace-as-filesystem**: break trace into hierarchical text files because agents are good at file trees
- Standard alternative: embeddings + chunking + clustering over traces or raw JSON
- **Routing by agreement**: multiple specialists / prompts / metrics, decide from combined outputs, not one metric. Vision-model version splits into specialists in later layers rather than end-to-end duplication. Has used analogous multi-expert idea for text extraction.
- Real case for a separate model trained on traces vs general API models — defaults get distracted, can start following the trace's reasoning instead of analyzing it.

## Knowledge graph / extraction takes

- Token-level extraction labeling (nothing/subject/predicate/object) is expensive; speculative decoding might help in parts of the pipeline
- Built custom noisy dataset because clean academic triple datasets aren't what production wants
- His model is supervised on real triples; doesn't imply perfect prediction accuracy
- Sees traces as naturally graph-shaped, but graph methods get chunky at larger scales

## Scaling notes

- GNN-based context-selection: ~1,000 traces / ~10,000 nodes to keep processing under ~1s
- Node counts balloon because one trace expands into many thought/turn nodes
- Whether graph-based works depends heavily on how many traces fed in

## MTEB

- Embedding-model benchmark, 8 tasks. MMTEB is the multilingual version.

## Open follow-ups

- Send him the article with embedding learnings distilled from someone's PhD
- He's looking into whether a graph-based clustering method fits this problem
- Stay warm specifically on: traces, agent evaluation, graph methods, extraction pipelines
