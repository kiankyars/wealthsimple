---
type: decision
decided_on: 2026-05-06
revisits: 2026-08-06
last_updated: 2026-05-06
sources:
  - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
  - this conversation
confidence: high
---

# Wiki architecture

## Decision

Build an **agent-maintained** personal wiki at `/Users/kian/wiki/`, sibling to (not inside) `/Users/kian/obsidian/`. Markdown in git. Hybrid update model: scheduled nightly via launchd + on-demand via Claude Code session in the directory. Off-limits to manual editing of page bodies; Kian corrects via `_agent/corrections.md` and the agent rewrites.

## Why

- Karpathy + Farza paradigm holds: explicit, yours, file-over-app
- Kian's existing Obsidian vault is a **self-command system** (accountability, daily journal, plan, projection) — corrupting it with agent writes would destroy what makes it useful
- The right split: Obsidian = human-written self-command. Wiki = agent-written knowledge base. Agent reads Obsidian to ground itself, never writes there
- Existing high-signal corpora (`~/.codex/memories/`, Obsidian people/) make bootstrap cheap

## Stack chosen

- **Storage**: plain markdown in git (no DB, no embeddings as source of truth)
- **Runtime**: Claude Code with file tools (Read, Glob, Grep, Edit). No memory framework (Mem0/Letta/Zep/Cognee) — overkill at this scale and inverts file-over-app
- **Retrieval**: ripgrep + LLM rerank. Add LanceDB only when a specific query class fails
- **Entity resolution**: cascading matcher (deterministic alias rules → embedding similarity → LLM-as-judge), audited in `_agent/entity-decisions.md`
- **Scheduling**: launchd (not cron — deprecated on Sequoia, doesn't survive sleep)
- **Corrections**: `_agent/corrections.md`, loaded into every run prompt

## Stack rejected

- Memory frameworks (Mem0, Letta, Zep, Cognee) — invert file-over-app, want to own storage
- Vector DB (Chroma, Qdrant) — overhead at single-user scale
- Graph DB (Kuzu, Neo4j) — frontmatter + wikilinks are the graph
- Hosted background agents (Modal, Anthropic-hosted) — iMessage + filesystem signal forces local; cloud doubles leak surface
- Existing PKM products (Mem.ai, Reflect, Tana, Saner.ai, Capacities) — none are agent-maintained-not-just-agent-assisted; data ownership story is the whole point

## Bootstrap sources used (this commit)

- `/Users/kian/.codex/memories/memory_summary.md` (40 KB pre-distilled user profile)
- `/Users/kian/.codex/memories/MEMORY.md` (248 KB per-repo task summaries)
- `/Users/kian/obsidian/people/{molly,sam,nick,jacques,warren}.md` (5 hand-curated people notes)

## Open follow-ups

- Wire connectors (Gmail, Calendar, iMessage, Claude Code transcripts, Codex deltas, filesystem activity) — one at a time, drop into `inbox/`, let nightly agent triage
- Set up launchd plist
- Set up `/wiki` slash command for on-demand
- Skim `~/.codex/memories/memory_summary.md` and prune anything that shouldn't propagate

## Revisit conditions

- 3 months: review what worked, what rotted, what queries fail
- Earlier if: a query class consistently fails grep (→ add LanceDB), or wiki passes ~10k pages (→ revisit retrieval)
