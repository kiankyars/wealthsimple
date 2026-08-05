# Shared agent context

A tiny, vendor-neutral context layer for Kian's local agents.

The original May 2026 LLM wiki tried to maintain people, projects, organizations, concepts, decisions, indexes, logs, and nightly ingest. It was used for one task, never wired into agent discovery, and became stale. Those files remain in place as retired historical material and in Git history at commit `25c9341`; agents are instructed not to use them as current context.

The replacement has three active documents:

- `AGENTS.md` — when agents may read or write here
- `context.md` — current cross-project routing and durable preferences
- `notes.md` — the few unique syntheses preserved from the old wiki

Agents discover this repository through the shared `use-agent-context` skill. There is no ingestion daemon, database, generated index, or requirement to file every answer back. If this stays small and occasionally prevents a real mistake, it is working.

Background: [Karpathy's original X post](https://x.com/karpathy/status/2039805659525644595) and [canonical LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
