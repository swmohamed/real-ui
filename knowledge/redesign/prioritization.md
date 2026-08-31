# Redesign Prioritization (sequencing change, not just choosing it)

Extends redesign/workflow.md stage 4 (verdicts) with WHAT ORDER and
WHAT RISK. A verdict table without priorities produces big-bang
redesigns — the riskiest kind.

## Prioritize the verdict table

Score each KEEP/CHANGE/REMOVE/MERGE/ADD row on:

| Axis | Ask |
|---|---|
| User impact | Does this fix a top-3 task friction? (diagnosis.md P1s first) |
| Frequency | Daily-flow fix > annual-page polish |
| Risk | What breaks if wrong? (identity, muscle memory, data, trust) |
| Effort | Design + build + content + QA cost |
| Reversibility | Token-level change (easy back) vs IA change (expensive back) |

Pattern: **P1 UX-blockers first (diagnosis), P2 consistency/token
unification (cheap, wide effect), P3 identity/direction moves (big,
deliberate), P4 polish.** Never lead with visual refresh when
navigation is broken — decoration on a broken flow wastes the trust
you'll need for the real fix.

## Dependency ordering

1. IA/navigation changes BEFORE visual system (layout containers move
   first, then style them).
2. Token foundation BEFORE component redesign (tokens.md first, or
   every component redesign happens twice).
3. Shared components BEFORE one-off screens (fix the 20 screens that
   use the card, not 20 cards).
4. States (loading/empty/error — states.md, mobile-states.md) ride
   WITH their flows, not "later phase 3" (later = never).

## Rollout shapes

| Shape | When | Design-system consequence |
|---|---|---|
| Big-bang | rebrand/explicit transformation only | full token set day one |
| Staged by surface | default | new system ships per section; bridge tokens (old↔new) documented |
| Progressive/flagged | risky products (finance, government) | feature-flagged designs, A/B where possible |
| User-cohort staged | large user bases | cohort notes in regression ledger (redesign/preservation.md) |

Each stage must END shippable (no half-skinned surfaces live together
except through a documented bridge — two systems visible at once =
the inconsistency diagnosis.md flags).

## Success criteria (define BEFORE designing)

Pick 2–3: task completion rate / time-to-complete / support tickets
per flow / activation / return usage / brand-recognition check
(redesign/preservation.md tests). If a redesign can't name what improves, it's
aesthetic churn — cut it or justify as explicit rebrand.

## Kill-switch honesty

Any identity-level change (logo move, color-system change, nav-model
change) deserves a revert path: keep old tokens reachable for one
release; measure; keep or revert by criteria, not pride.

## Output

```
PRIORITIES:
- P1 [CHANGE] fix checkout nav (impact:high risk:low) — stage 1
- P2 [MERGE] unify card styles (impact:med risk:low) — stage 1
- P3 [CHANGE] typography system (impact:med risk:med) — stage 2
ROLLOUT: staged-by-surface; SUCCESS: checkout completion +15%, tickets -20%
```
