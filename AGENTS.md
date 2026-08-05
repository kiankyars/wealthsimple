# Shared agent context contract

This repository holds durable context that is useful across multiple agents and has no better canonical home. It is not a second Obsidian vault, a project encyclopedia, or a transcript archive.

The old `people/`, `projects/`, `orgs/`, `concepts/`, `decisions/`, `_agent/`, `index.md`, `llms.txt`, and `log.md` system is retired historical material. Do not read it for current context or update it.

## Read

1. Read `context.md` only when a task depends on Kian's preferences, current cross-project priorities, or where information belongs.
2. Read only the relevant section of `notes.md` when the task touches one of its topics.
3. Treat explicit user instructions and live local evidence as authoritative. Treat this repository as a routing hint, never proof of mutable state.
4. Respect `verified_at` and `review_after`. Reverify expired or changeable claims before using them.

## Write

Update this repository only when Kian explicitly asks an agent to remember something across tools, or when a completed task creates a durable cross-project decision with no canonical project file.

- Put terse current rules, preferences, and canonical-location pointers in `context.md`.
- Put durable explanatory synthesis that needs rationale, caveats, or sources in `notes.md`.
- Revise existing text in place; do not append session summaries.
- Record the source and verification date beside each mutable claim.
- Keep project facts in that project's `AGENTS.md`, README, or docs.
- Keep daily notes, reflection, planning, and personal records in Obsidian.
- Keep raw research, transcripts, and generated artifacts with their source project.
- Do not copy Codex memory into this repository.
- Do not revive people/org pages, manual indexes, ingest logs, run reports, or nightly jobs.

## Safety

- Never let stale context override the user's current statement.
- Verify paths, employment, active projects, deadlines, account state, and tool availability live.
- Preserve user-written Obsidian content unless the user explicitly asks for an edit.
- If a fact is useful only to one task or one repository, it does not belong here.
