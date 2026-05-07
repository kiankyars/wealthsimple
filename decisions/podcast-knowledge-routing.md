---
type: decision
decided_on: 2026-05-07
revisits: 2026-06-07
last_updated: 2026-05-07
sources:
  - this conversation
  - /Users/kian/.claude/projects/-Users-kian/af7ba4a7-0af0-4d4b-9b04-961ccdcdca93.jsonl
  - /Users/kian/.codex/memories/MEMORY.md
  - /Users/kian/obsidian/balados/dylan-patel.md
confidence: high
---

# Podcast knowledge routing

## Decision

Keep live podcast listening, talking, and messy note-taking in [[../people/kian]]'s Obsidian vault. Promote only distilled, durable facts and decisions into this wiki.

The wiki should not become a transcript mirror or a pile of listening notes. Its job is to compile: update the people, projects, orgs, concepts, and decisions touched by the episode.

## Default flow

1. **Capture in Obsidian.** During or right after listening, write rough notes in `~/obsidian/notes/YYYY-MM-DD.md` or a topic/person file under `~/obsidian/balados/`.
2. **Make a corpus only when the source recurs.** For a person/topic that becomes real research input, use the [[../projects/dylan]] pattern: `index.json` manifest, timestamped `transcripts/*.json`, and readable `transcripts/*.md`.
3. **Ingest from the wiki repo.** Ask an agent in `/Users/kian/wiki` to read the Obsidian note/transcript/corpus and update affected wiki pages.
4. **Log the promotion.** If the episode changes the wiki, update [[../log]] and any touched pages. If it was just reflection or scratch thinking, leave it in Obsidian.

## Promotion triggers

Promote podcast material into the wiki when it does at least one of these:

- Changes Kian's position on a [[../concepts/compile-dont-retrieve]]-level concept
- Adds or corrects load-bearing facts about a person, project, org, or decision
- Becomes evidence for an active bet, especially [[one-bet-rl-post-training]]
- Starts a recurring research thread that should be searchable by future agents

Do not promote:

- Raw transcript chunks
- Whole episode summaries that do not change an entity page
- Emotional reactions or daily self-command material
- Timestamp lists unless they support a claim worth revisiting

## Practical answer

Use Obsidian while listening. Use the wiki after listening, when there is something worth compiling.

For high-value episodes, the best mechanism is: Obsidian capture first, transcript/corpus if needed, wiki distillation last.

## Related

- [[wiki-architecture]] - the Obsidian/wiki boundary
- [[../projects/dylan]] - working transcript-corpus pattern
- [[../projects/siri]] - voice/audio routing boundary
- [[../concepts/compile-dont-retrieve]] - why raw source material stays out of pages
