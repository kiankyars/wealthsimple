---
type: decision
decided_on: 2026-05-09
revisits: 2026-06-09
last_updated: 2026-05-09
sources:
  - this conversation
  - /Users/kian/Developer/dylan/
  - /Users/kian/wiki/decisions/podcast-knowledge-routing.md
confidence: high
---

# Dylan corpus location

## Decision

Keep `/Users/kian/Developer/dylan/` as the transcript corpus. Do not merge the raw corpus under `/Users/kian/wiki/` yet.

The wiki should point to the corpus and compile durable takeaways from it. It should not own the raw transcript files.

## Why

- The Dylan directory is already a machine-usable corpus: `index.json`, timestamped `transcripts/*.json`, and readable `transcripts/*.md`.
- The wiki contract is [[podcast-knowledge-routing]]: capture/source material outside the wiki, then promote distilled facts and decisions into wiki pages.
- Raw transcripts would bloat the wiki and weaken the "compile, don't retrieve" boundary.
- `/Users/kian/Developer/dylan/` is a working research directory with scripts and generated artifacts. That is a better home for audio/transcript tooling than the agent-written wiki.

## Operating rule

When a new Dylan/SemiAnalysis episode matters:

1. Import it into `/Users/kian/Developer/dylan/`.
2. Use `index.json` and `transcripts/*.md` for lookup.
3. File only the resolved takeaways into wiki pages such as [[../projects/dylan]] or topic concepts.

## Revisit conditions

- If several transcript corpora become central, create a separate `~/corpora/` or `~/research-corpora/` parent and move `dylan/` there.
- If the wiki needs a local mirror for portability, mirror only manifests and distilled notes, not full raw transcripts.
