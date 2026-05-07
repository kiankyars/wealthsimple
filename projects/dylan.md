---
type: project
status: active
last_updated: 2026-05-06
sources:
  - /Users/kian/.codex/memories/MEMORY.md
  - /Users/kian/obsidian/balados/dylan-patel.md
repo: dylan
cwd: /Users/kian/Developer/dylan
confidence: high
---

# dylan

Local transcript corpus and analysis workspace for [[../people/dylan-patel]].

## Shape

Practical paired shape:
- `index.json` manifest
- canonical `transcripts/*.json` with timestamps
- `transcripts/*.md` as the clean retrieval view

## Operational rules

- Search the on-disk corpus with `rg` / `sed` before retrying live YouTube access
- If `youtube_transcript_api` starts failing after a burst, suspect rate limits or blocked captions and pivot to another transcript source rather than retry
- Preserve literal transcript tokens (e.g. `XA`) when Kian asks "what was literally said" — don't silently normalize ASR artifacts
- For transcript-backed note snippets: inspect target note, mirror its exact heading/bullet syntax (`## YYYY-MM-DD` + `- term:: definition`)
- If direct note editing is blocked, return one paste-ready block in that house style

## Wikipedia draft

- Articles for Creation flow
- Output: Wikitext + citations (not plain prose)
- Local podcast corpus is useful background but not enough by itself for biography notability
- If a prior run hit `context_window_exceeded`, recover the saved session from `~/.codex/history.jsonl` before restarting
