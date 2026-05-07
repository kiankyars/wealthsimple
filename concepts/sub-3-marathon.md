---
type: concept
domain: operational
last_updated: 2026-05-06
sources:
  - /Users/kian/.codex/memories/MEMORY.md
  - /Users/kian/obsidian/running/marathon.md
  - /Users/kian/obsidian/running/README.md
confidence: high
---

# Sub-3 marathon

Kian's running goal: marathon under 3 hours. Goal pace ~4:15/km. Active training plan documented in `/Users/kian/obsidian/running/`.

## Hard constraints (Kian's own rules)

- **Mileage floor: 100 km/week.** Never below unless explicit taper authorized.
- Goal pace explicit at ~4:15/km
- Strava is the system of record for completed workouts
- Polar is the enrichment layer (HR, biomaxing). Do not let Polar replace Strava unless Kian explicitly chooses to.

## Workflow

- Live Strava pulls preferred over generic coaching when data is available
- One canonical running hub at `/Users/kian/obsidian/running/` (don't fragment)
- HR-grounded coaching cues from Polar
- Strava activity titles get renamed via API: format like "Sub3M W2D5 Recovery"
- `running/marathon.md` updated with actual stats (distance, pace, HR) post-run
- `python3 scripts/strava_analyze_runs.py --days 14` updates `running/README.md`

## Skill integration

- `~/obsidian/.agents/strava-daily-sync/SKILL.md` — Strava activity title updates + marathon.md stats sync
- Uses `STRAVA_ACCESS_TOKEN` from `.env`

## Off-limits

The agent does not modify Kian's training plan or generate workouts unprompted. Kian directs; the agent records and analyzes.
