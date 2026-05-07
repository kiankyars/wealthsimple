---
type: person
status: active
aliases: [Dylan, Dylan Patel]
last_updated: 2026-05-06
sources:
  - /Users/kian/obsidian/balados/dylan-patel.md
  - /Users/kian/Developer/dylan/transcripts/
  - /Users/kian/.codex/memories/MEMORY.md
confidence: medium
relationship: research subject (transcript corpus + Wikipedia draft)
---

# Dylan Patel

Founder of SemiAnalysis. Subject of an extensive local transcript corpus at `/Users/kian/Developer/dylan/transcripts/` and an in-progress Wikipedia draft.

## Why Kian tracks him

- Primary source for chip / datacenter / scaling-economics analysis
- Kian maintains a transcript corpus + a balados note at `/Users/kian/obsidian/balados/dylan-patel.md` in the house style `term:: definition`

## Active workstreams

- [[../projects/dylan]] — local transcript corpus, exact-excerpt lookup, balados note maintenance
- Wikipedia draft (Articles for Creation): Wikitext + citations, mining the local corpus for source material; podcast corpus is useful background but not enough for biography notability on its own

## Operational notes

- Search the on-disk corpus with `rg`/`sed` before retrying live YouTube access
- `youtube_transcript_api` rate-limits in bursts — pivot to another transcript source rather than retry loop
- Preserve literal transcript tokens (e.g. `XA`) when answering "what was literally said" — don't silently normalize ASR artifacts
