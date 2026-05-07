# Entity decisions

Audit log for entity-resolution decisions: alias merges, splits, "is this the same person?" judgments. Every decision the agent makes about identity gets one line here, so Kian can spot-check.

Format:
```
## YYYY-MM-DD
- **Decision**: merge | split | new
- **Canonical**: [[page-name]]
- **Aliases / variants seen**: ...
- **Source**: <where the agent saw the ambiguous reference>
- **Confidence**: high | medium | low
- **Reasoning**: one sentence
```

---

<!-- agent: append new entries above this line; oldest at bottom -->

## 2026-05-06 (bootstrap)
- **Decision**: new
- **Canonical**: [[people/kian]]
- **Aliases / variants seen**: kian, Kian Kyars, kiankyars
- **Source**: bootstrap from `~/.codex/memories/memory_summary.md` and home directory
- **Confidence**: high
- **Reasoning**: trivially the wiki owner
