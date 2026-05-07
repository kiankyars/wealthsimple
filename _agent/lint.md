# Lint spec

Run at the end of every ingest. Findings → `_agent/runs/YYYY-MM-DD.md`. Auto-fix what's safe; flag the rest.

## Hard checks (auto-fix where possible)

1. **Frontmatter validity** — every page has YAML frontmatter with at minimum `type`, `last_updated`. Auto-add missing `last_updated` from git mtime.
2. **Broken `[[wikilinks]]`** — every link points to an existing file (relative path or page slug). Auto-fix typos with high-confidence match; otherwise flag.
3. **Orphan pages** — any page with zero inbound links. Flag for review unless the page is `type: log` or in `_agent/`.
4. **Duplicate slugs** — two files that should arguably be one. Flag with both paths and a suggested merge.
5. **Stale `last_updated`** — page hasn't been touched in N days but its sources have. Flag for re-ingest.

## Soft checks (flag only, never auto-fix)

6. **Contradictions** — two pages making opposing claims about the same fact. Especially: `last_contact` for a person, `status` for a project, dated assertions in concepts.
7. **Stale claims** — sentences with absolute dates ("currently raising", "as of March") older than 60 days.
8. **Confidence drift** — page marked `confidence: high` but only one source. Flag for downgrade or for finding corroboration.
9. **Off-limits violations** — agent attempted to write to `~/obsidian/` or modify a `<!-- agent:user -->` block. Hard fail the run.
10. **Slop** — pages where >30% of the body is generic phrasing ("it's important to note", "in summary", "various aspects"). Flag with a prose-quality score.

## Report format

`_agent/runs/YYYY-MM-DD.md`:

```markdown
# Run YYYY-MM-DD HH:MM

## Ingested
- N inputs from <source>
- M pages updated, K pages created

## Auto-fixed
- ...

## Flagged for review
- ...

## Errors
- ...
```
