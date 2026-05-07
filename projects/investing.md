---
type: project
status: active
last_updated: 2026-05-06
sources:
  - /Users/kian/.codex/memories/MEMORY.md
repo: investing
cwd: /Users/kian/Developer/investing
confidence: high
---

# investing

Personal / corporate investing data room. **File-first research workspace**, not a dashboard.

## Shape (accepted v1)

- Data room with reusable prompts
- Optional cron analysis
- Curated dossier under `00_RELEVANT_FINANCIAL_DOSSIER/` (preserves the original archive non-destructively)
- Published privately to `kiankyars/investing` on GitHub

## Domain context

- Corporate vehicle: Parveen Jahandar Professional Corporation
- Recurring concepts: Wealthsimple (3% match, self-directed), capital dividend, estate freeze
- Workflow goal: planning-relevant finance context, not raw document triage

## Operational notes

- Archive was non-git; bulk delete was safety-blocked. Right cleanup deliverable: a curated copy, not a destructive prune.
- For large `00_RELEVANT_FINANCIAL_DOSSIER/` rebuilds: simplify massively, verify `gh auth status` before publish, watch for "token invalid"

## Off-limits

- The agent does **not** draft outbound financial communications. Drafts of advisor / institution emails stay with Kian unless explicitly authorized.
