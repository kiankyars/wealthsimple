---
type: concept
domain: philosophical
last_updated: 2026-05-06
sources:
  - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
  - https://x.com/FarzaTV/status/2040563939797504467
confidence: high
---

# Compile, don't retrieve

The organizing principle of this wiki, taken from Karpathy's "Wiki LLM" gist.

## The shift

- **Old (RAG)**: keep raw documents; at query time, retrieve chunks; compose an answer fresh each query.
- **New (Wiki LLM)**: compile raw documents into a curated, cross-linked wiki *once* (and incrementally update it). Future queries hit the wiki, not the raw pile.

Karpathy: *"The LLM doesn't just index it for later retrieval... it reads it, extracts key info, and integrates it into the existing wiki."*

## Why it wins

1. **Lower hallucination risk.** The wiki is the agent's working memory, already verified once. Less re-derivation.
2. **Compounding.** Each query that requires synthesis becomes a new page. The wiki gets denser over time.
3. **Inspectable.** You can read what the agent thinks it knows and edit it. RAG's "knowledge" is implicit in retrieval scores.
4. **Cheaper at query time.** No fresh chunk-retrieval-and-rerank loop on every question.

## Implications for this wiki

- The agent does **not** paste raw email bodies / Codex transcripts / iMessage threads into pages. It reads them, extracts the load-bearing facts, integrates into existing pages.
- New input ≠ new page. Most inputs update 1–3 existing pages. New pages are created only when a genuinely new entity or theme appears.
- Query results that required real synthesis get filed back as new or updated pages (workflow B in [[../AGENTS]]).
- Sources stay in the `sources:` frontmatter so the agent can re-fetch, but the body is distillation.

## Related

- [[../AGENTS]] — the operationalization of this principle
- Farzapedia ([[../people/farza]]) — worked example: 2,500 inputs → 400 backlinked articles, no embeddings
