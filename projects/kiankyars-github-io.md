---
type: project
status: active
last_updated: 2026-05-06
sources:
  - /Users/kian/.codex/memories/MEMORY.md
repo: kiankyars.github.io
cwd: /Users/kian/Developer/kiankyars.github.io
confidence: high
---

# kiankyars.github.io

Kian's Jekyll blog. Two streams: long-form blog posts in `_posts/blog/`, weekly recall scaffolds in `_posts/weekly-victories/`.

## Conventions

- Quote YAML titles containing punctuation
- Add explicit `date` / `permalink` when rendered URL or date behavior matters
- Mobile readability: stacked bullet structures over wide tables in markdown-heavy posts
- Weekly victories: lightweight recall scaffolds sourced from `/Users/kian/obsidian/notes/`, not polished essays
- Short dated explainers: very short, preserve Kian's framing, name the standard source/theory plainly if there is one
- "No need to correct" → don't widen a requested edit into unrelated fact-checking or cleanup

## Recovery patterns

- If repo diverges from a prior Claude session, recovery surface is: the exact transcript + `~/.claude/file-history/...`, then a live filesystem check
- Use `git revert` for rollback; remove temporary stashes after the revert
- If `git push --force-with-lease` fails with `stale info` → fetch first so lease check sees current refs

## Specific posts

- `_posts/blog/2026-02-04-biomaxing.md` — Polar-table workflow with footnotes and manual placeholders
- `_posts/blog/2026-04-21-situational-awareness-lp.md`
- `_posts/blog/2026-04-24-diffusion.md` — short explainer (Fick's law, Brownian motion)

## Helpers

- `misc/update_biomaxing.py` — empty-cell-only updater so it doesn't overwrite manual `n/a` cells
- Use `python3 /Users/kian/obsidian/scripts/polar_accesslink.py ...` for Polar pulls
