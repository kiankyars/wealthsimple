# wiki

Agent-maintained personal wiki for Kian. Sibling to `~/obsidian/`.

This repo is **agent-written**. I don't edit page bodies by hand. I correct the agent via `_agent/corrections.md`, and the agent rewrites.

If you're an agent: read [AGENTS.md](AGENTS.md) first.

If you're a human: read [index.md](index.md) for what's in here, [log.md](log.md) for what changed recently.

## Why

Following Karpathy's "Wiki LLM" gist and Farza's worked example (Farzapedia). The system replaces ad-hoc RAG with a persistent, incrementally-maintained wiki the agent compiles from raw sources (Codex/Claude transcripts, Gmail, Calendar, iMessage, Obsidian, git history).

Three Karpathy principles hold here: **explicit** (you can read what the AI thinks it knows), **yours** (local files), **file-over-app** (Unix toolkit works on it).

## How

- **Source of truth**: markdown in git. No DB, no embeddings as source.
- **Ingest**: scheduled nightly via launchd + on-demand via Claude Code session in this directory.
- **Retrieve**: ripgrep + LLM rerank. Add LanceDB only when a real query class fails.
- **Correct**: edit `_agent/corrections.md` directly (or tell the agent in chat — it'll update both the page and corrections).

## Bootstrap sources

This wiki was bootstrapped from:
- `~/.codex/memories/memory_summary.md` (40KB pre-distilled user profile)
- `~/.codex/memories/MEMORY.md` (248KB per-repo task summaries)
- `~/obsidian/people/*.md` (5 hand-curated people notes)

Subsequent updates come from connectors listed in [llms.txt](llms.txt).
