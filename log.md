---
type: log
last_updated: 2026-05-09
sources:
  - this conversation
confidence: high
---

# Log

Append-only chronological stream of changes. One line per significant event. Format: `YYYY-MM-DD: <what changed> ([[page1]], [[page2]])`.

---

<!-- agent: append new entries above this line; oldest at bottom -->

## 2026-05-09

- Imported SemiAnalysis Weekly Ep. 011 into the Dylan corpus and resolved Kian's three references (`H126`, Google two weeks, `SOE`/`SSM`). Decided not to merge raw Dylan transcripts under the wiki; keep the corpus external and compile takeaways here. ([[projects/dylan]], [[decisions/dylan-corpus-location]])

## 2026-05-08

- Added Lambert / Interconnects takeaway on Chinese LLM lab culture: the claim is a coordination and incentive-design edge for today's model-building game, not a generic "no ego" claim. ([[concepts/chinese-llm-lab-culture]])

## 2026-05-07

- Decided podcast knowledge routing: capture live listening in Obsidian, use a transcript corpus only for recurring research input, and promote only distilled durable facts into the wiki. ([[decisions/podcast-knowledge-routing]], [[projects/dylan]], [[projects/siri]])

## 2026-05-06

- Audit pass: read `~/obsidian/agency.md`, `projection.md`, `commitment-to-one-goal.md`. Validated [[people/kian]] tensions (correct). Sharpened the "one bet" section with explicit RL post-training target. Added [[decisions/one-bet-rl-post-training]] and [[concepts/the-one-bet-rule]]. Deliberately kept depressive/biographical content from projection.md OUT of the wiki — Obsidian is the right place. ([[people/kian]], [[decisions/one-bet-rl-post-training]], [[concepts/the-one-bet-rule]])
- Bootstrap commit. Wiki structure created at `/Users/kian/wiki/`. Schema defined in [[AGENTS]]. Seeded from `~/.codex/memories/memory_summary.md`, `~/.codex/memories/MEMORY.md`, and `~/obsidian/people/*.md`. Pages created: 7 people, 13 projects, 6 orgs, 5 concepts, 1 decision. ([[decisions/wiki-architecture]], [[index]])
