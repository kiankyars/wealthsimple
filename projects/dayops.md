---
type: project
status: active
last_updated: 2026-05-06
sources:
  - /Users/kian/.codex/memories/MEMORY.md
repo: dayops
cwd: /Users/kian/Developer/dayops
confidence: medium
---

# dayops

Day-planning system. Cloud Run deployed via Akash; uses an OAuth shim for Google.

## Architecture

- Auth shape: `oauth_shim` after migration to shim-only Google OAuth flow (`/auth/google/bootstrap`)
- Common error: `redirect_uri_mismatch`, "Missing code verifier"
- Planner / app contract endpoints: `/plan`, `/revise`, `/rollback`
- Behavior boundaries around: duplicate events, locations, rollback history, image-publish loops
- Deploy config: `akash-deploy.yaml`

## Why it exists

[[../people/molly]] mentioned she has trouble planning her day — dayops is partly aimed at that user shape.
