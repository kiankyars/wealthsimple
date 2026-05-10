---
type: project
status: active
last_updated: 2026-05-09
sources:
  - /Users/kian/.codex/memories/MEMORY.md
  - /Users/kian/obsidian/balados/dylan-patel.md
  - this conversation
  - /Users/kian/Developer/dylan/transcripts/2026-05-06-ep-011-gpt-5-5-vs-claude-4-7-openai-s-comeback-from-the-brink-tokenomics-semianalysis-weekly-ep011-2026-05-06.md
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

## Generalized podcast pattern

For one-off listening, keep notes in Obsidian. For recurring research input, make a local corpus in this shape, then let the wiki compile only the facts that change entity pages.

See [[../decisions/podcast-knowledge-routing]] for the general routing rule.

## SemiAnalysis Weekly Ep. 011 import

Imported 2026-05-06 SemiAnalysis Weekly Ep. 011 into the corpus from podcast audio using local MLX Whisper transcription.

Reference resolutions from the episode:
- `H126` means **H1 '26**: first half of 2026. The paired phrase was `H225`, meaning H2 '25. It was jokey time-period shorthand, not a chip/model code.
- `Google two weeks` means Dylan said Google and OpenAI were both expected to release in roughly two weeks from the 2026-05-05 recording, around 2026-05-19. OpenAI was framed as more pre-training + RL; Google as mostly a multimodal swap.
- `SOE` did not appear as such in the transcript. The closest local reference is `SSM`: state-space model, discussed in a joke about whether a fake-news model might be Mamba/SSM.

See [[../decisions/dylan-corpus-location]] for why the transcript stays in the corpus instead of moving under the wiki.

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
