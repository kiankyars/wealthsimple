---
type: project
status: active
last_updated: 2026-05-06
sources:
  - /Users/kian/.codex/memories/MEMORY.md
repo: siri
cwd: /Users/kian/Developer/siri
confidence: high
---

# siri

Voice-driven Obsidian routing system. Thin "agentic audio" layer that takes voice input, routes it into the right Obsidian note (réflexion, JL, monde, etc.).

## Conventions

- Default to "no changes" or smallest correctness fix in review rounds — "no slop"
- Prefer the exact renderer/config surface (`src/render_codex_audio_prompt.py`, `src/obsidian_audio_routing_endpoints.json`) over a broad refactor
- Remove duplicate instruction sources; validate by *rendering each endpoint*, not just compiling
- `cross_note_links` was removable because the renderer already says not to add backlinks
- Validate by confirming `monde` and `réflexion` each show only their own filename rule

## Wrappers

- Split launch agents are correct
- Wrappers touching the same daily note serialize on a shared `logs/run.lock`
- Validate shell wrappers with `bash -n` (not Python linters)
- `run_siri.sh`, `run_voice_memos_ingest.sh` are the entry points

## Boundaries

- Export-only routing vs agent-runner boundaries are deliberate — keep them separate
