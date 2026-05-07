# AGENTS.md

The contract for any agent that writes to this wiki.

## What this wiki is

A compounding markdown artifact about Kian — people he knows, projects he runs, orgs he engages with, concepts he's working through, decisions he's made. Source of truth is the markdown in this repo. Git is the audit log.

This wiki is **agent-written, human-read**. Kian does not edit the body of pages. He corrects the agent (see `_agent/corrections.md`) and the agent re-writes.

Companion to `~/obsidian/`, which is human-written self-command (daily notes, plan, projection). The agent **reads** Obsidian, **never writes** to it.

## Five principles

1. **Compile, don't retrieve.** Do not paste raw source material into the wiki. Read the source, extract the load-bearing facts, integrate them into the existing pages. The wiki is a distillation of sources, not a mirror of them.
2. **File over app.** Markdown + git. No DBs, no embeddings as source of truth. Every page must be readable in `cat`, editable in `vim`, diffable in `git`.
3. **Explicit, not implicit.** Anything the wiki "knows" must live in a file Kian can open. If the agent infers something, write it down. If the agent isn't sure, say so in the page.
4. **Multi-update on ingest.** When new input arrives (an email, a meeting, a Codex session), update every page it touches — usually 1–3 existing pages, occasionally a new page. Do not append to one page and forget the rest.
5. **Lint, don't accumulate.** Every run includes a lint pass: contradictions, orphans, stale claims, broken links. Do not let the wiki rot.

## Four workflows

### A. Ingest (scheduled nightly + on-demand)

For each new input since the last run:
1. Triage: what entities does it touch? (people, projects, orgs, concepts)
2. For each affected page: rewrite the relevant section in place. Do not append-and-grow.
3. If a new entity is introduced, create the page. If an existing entity's alias is used, resolve via `_agent/entity-decisions.md`.
4. Append a one-line entry to `log.md` with `YYYY-MM-DD: <what changed> ([[page1]], [[page2]])`.
5. Update `index.md` if a new page was created.

### B. File-back (after every query Kian asks)

When Kian asks the wiki a substantive question that required real synthesis (not a lookup), write the answer into the wiki as a new or updated page before responding. The query becomes durable. Examples that file-back: "what should I do about X?", "compare Y vs Z", "what's my position on W?". Examples that don't: "when did I last meet Molly?".

### C. Correct (whenever Kian objects)

If Kian says "wrong" / "not quite" / corrects a fact:
1. Edit the offending page immediately.
2. Append the lesson to `_agent/corrections.md` with date and one-line "what I had wrong, what's right, why". Future runs read this file at startup.
3. If the correction implies a structural rule, also update this AGENTS.md.

### D. Lint (end of every run, plus on-demand `lint`)

Run the checks in `_agent/lint.md`. Write findings to `_agent/runs/YYYY-MM-DD.md`. Fix what's safe to fix automatically (broken links, missing frontmatter); flag the rest for Kian.

## Frontmatter schema

Every page starts with YAML frontmatter. Required fields per type:

```yaml
---
type: person | project | org | concept | decision | log
status: active | dormant | archived       # for project, person, org
aliases: [list]                             # for person, org — feeds entity resolution
last_updated: YYYY-MM-DD
sources: [list of file paths or URLs]       # what the agent read to write this
confidence: high | medium | low             # how sure is the agent
---
```

Type-specific extras:
- **person**: `org`, `last_contact`, `relationship` (one phrase)
- **project**: `repo`, `cwd`, `started`
- **org**: `kind` (lab, startup, fund, vendor)
- **concept**: `domain` (technical, philosophical, operational)
- **decision**: `decided_on`, `revisits` (date or `null`)

## Writing rules

- **One file = one entity.** No combined pages. If two things are different enough to confuse, they're different pages.
- **Atomic over essay.** Short sections under headings beat long paragraphs. Agents (and Kian) skim.
- **Backlink aggressively.** `[[wiki links]]` everywhere a named entity appears. Density is the point — Farza's wiki works because it's crawlable.
- **English only.** Obsidian can stay polyglot; the wiki is for the agent.
- **Cite sources in frontmatter, not inline.** Inline citations bloat. Frontmatter `sources:` lets the agent re-fetch.
- **No slop.** Direct prose. No "it's important to note that". No section that exists only to look complete. If a page has nothing to say, delete it.
- **House voice.** Concise, casual, factual. Match the tone of the Obsidian people files. Active voice. Short sentences when possible.

## Off-limits

- The agent **never writes** to `~/obsidian/`.
- The agent **never writes** to `~/.codex/` or `~/.claude/`.
- Sections marked with `<!-- agent:user -->` ... `<!-- /agent:user -->` are user-only. Read but never edit.
- Files under `_agent/` are agent-managed; Kian can read and edit `corrections.md` directly to teach the agent.

## Layout

```
~/wiki/
├── AGENTS.md                # this file
├── llms.txt                 # top-level catalog for agent navigation
├── README.md                # for humans
├── index.md                 # flat catalog of every page (for fast LLM nav)
├── log.md                   # append-only chronological stream of changes
├── people/                  # one .md per person
├── projects/                # one .md per active or notable project
├── orgs/                    # companies, labs, podcasts, vendors
├── concepts/                # technical/philosophical/operational ideas
├── decisions/               # explicit decisions Kian has made + why
├── inbox/                   # raw connector dumps awaiting triage
└── _agent/
    ├── corrections.md       # accumulated lessons; load into every run prompt
    ├── entity-decisions.md  # alias merges, auditable
    ├── lint.md              # the lint spec
    └── runs/YYYY-MM-DD.md   # nightly run logs
```
