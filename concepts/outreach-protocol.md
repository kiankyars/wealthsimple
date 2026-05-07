---
type: concept
domain: operational
last_updated: 2026-05-06
sources:
  - /Users/kian/.codex/memories/MEMORY.md
confidence: high
---

# Outreach protocol

Kian's rules for outbound email and outreach work. Repeated correction-derived rules; treat as hard constraints.

## Channel

- Gmail plugin **or** GWS only when constrained
- **Never** fall back to Mail.app
- Gmail read access does not imply send access
- `ACCESS_TOKEN_SCOPE_INSUFFICIENT` → fix connector OAuth, do not retry

## GWS send sequence (when Gmail send fails)

1. `gws auth status`
2. `gws auth login --scopes https://www.googleapis.com/auth/gmail.send`
3. `gws gmail users messages send`

## Auth diagnosis

- `org_internal` GWS auth response → the OAuth project/client itself is the blocker, not the scope

## Bounce protocol

- Guessed aliases are provisional
- Verify bounces (`550 5.1.1` etc.) before calling the send step complete
- After alias bounces: public-page lookup before retry, ask before reusing a shared routing inbox for multiple people
- **Hard stop**: after a routing mistake (e.g. duplicate routing to one generic inbox), stop outbound sends until Kian re-confirms

## Drafts

- Keep drafts in the relevant note (e.g. `people/<name>.md` in Obsidian or this wiki) rather than detached
- Embed blunt drafts in markdown for review
- Privacy-safe by default

## Logging

- For `rlvrbook` outreach: results go to `gws_send_results.jsonl`
