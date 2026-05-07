---
type: project
status: active
last_updated: 2026-05-06
sources:
  - /Users/kian/.codex/memories/MEMORY.md
repo: rlvrbook
cwd: /Users/kian/Developer/rlvrbook
confidence: high
---

# rlvrbook

Manuscript + distribution work for an RLVR (Reinforcement Learning with Verifiable Rewards) book. Quarto-based.

## Editorial conventions

- Prefer one strong organizing example over framework survey sprawl
- Self-contained tables over prose scaffolding
- Shared stylesheet ownership (`book/styles/custom.css`) over inline markdown CSS
- Cited / step-by-step support for important claims or formulas
- Chapter-scoped action items + sentence-level edits over broad rhetorical rewrites

## Known specifics

- Chapter 6: best-of-N
- Chapter 7: Goodhart / Skalse footnote uses `a.`, `b.`, `c.` markers under `[^gh-possibilities]` — *not* `1 2 3`, *not* indented sub-bullets
- Chapter 8: `08-on-capabilities.md`, DeepSWE / R2E-Gym
- Chapter 9: harness reframing
- Appendix B: checklist-only compression

## Build notes

- Sequential renders are safer than parallel renders when `site_libs` or other shared output directories are in play
- If git writes blocked by `index.lock` / `Operation not permitted` / usage-limit rejection: keep the local edit and stop, don't invent a workaround

## Outreach

- `distribution/outreach_targets.csv`
- Gmail plugin or GWS only — never Mail.app
- `ACCESS_TOKEN_SCOPE_INSUFFICIENT` → fix connector OAuth, not retry. See [[../concepts/outreach-protocol]]
- `org_internal` GWS auth → OAuth project/client itself is the blocker
- Sends logged in `gws_send_results.jsonl`

## Site

- Homepage SEO/query-targeting: `book/_quarto.yml`, key term "What is RLVR?"

## Links

- [[../concepts/agent-harnessing]] (related domain)
- [[../orgs/judgment-labs]] (overlapping)
