# V7 Variance Stress Test & Stability Review

Date: 2026-09-03. Skill state: commit `7f6cdd8` (released V7). Method:
REAL-UI as the only design skill; isolated contexts under
`real-ui-v7-variance/` (outside the repository); normal user-style prompts
with no instructions to differentiate; browser tooling for render/inspection
only. Labels used honestly: RENDERED / RUNTIME / STRUCTURAL / REASONED-SPEC.

## Per-case metadata (required record)

All cases: REAL-UI V7 @ `7f6cdd8`, installed-copies identical (19/19).
Knowledge activated per case listed with results below. Render evidence:
every built page executed at 1280×800 and 390×844 (screenshots + DOM
checks); T4 cases also carry full verifier artifact sets.

## 1. Same product type (landing page) × 5 briefs — PASS (RENDERED)

Prompts (no differentiation hints): open-source error-tracking tool ·
family law practice · farm veg-box delivery · mechanical keyboard ·
university executive program. Routing: pages/landing.md authority +
per-brief industry modules (saas-dev, education read; others model-first
by contract). Each derived its own screen contract before composition.

Style-blind fingerprints (STRUCTURAL, extracted from implementations):

| Brief | Primary artifact | Section spine | Type | Geometry | Primary CTA |
|---|---|---|---|---|---|
| dev tool | live terminal proof | match → mechanism → proof → objections → final | sans + mono | 6–10px | Start free trial |
| law practice | free-consultation block | reassurance → areas → process timeline → people → fees → contact | serif | 4–6px | (phone-led, no button CTA) |
| veg-box | this week's harvest list | box contents → how → farm story → plans → FAQ | sans | 10–12px | Order/Start |
| keyboard | spec table + configurator | product hero → config → spec table → engineering → sound → buy | sans (dark) | 12–14px | Buy/Configure |
| university | at-a-glance facts panel | promise+facts → fit → 8 themes → faculty → cohort → apply steps | serif | 2–4px | Apply |

Verdict: zero shared hero, zero shared section order, zero shared primary
artifact, distinct registers and CTA verbs. The one recurring module class
(card-like groupings in 4/5) appears as different justified modules
(objections, plans, engineering reasons, practice areas) — bounded-entity
representation per product-modeling.md, not a card-grid default.

## 2. Same brief × 5 isolated runs — STABLE, with justified family resemblance (RENDERED)

Brief (open): "Design and build a homepage for an independent neighborhood
pharmacy that delivers." Five isolated runs, each re-derived through a
different legitimate model lens (task-rank / entry-context / audience-split /
trust-consequence / content-priority), none told to differ.

| Run | Primary surface | Structure spine | Register | Accent |
|---|---|---|---|---|
| 1 | refill form | promise + form + 3 tasks + ask strip | sans | teal |
| 2 | status strip + 4 channels | ways list + pharmacist aside + shelves + out-of-hours | serif | green/warm |
| 3 | two-door audience split | prescriptions vs shop + facts strip + people band | sans | blue |
| 4 | vows + counter cases | trust promises → 5 real conversations → delivery facts | serif | plum |
| 5 | live delivery tracker | tracker → shelf grid (8 cats) → counter services | sans | blue |

Collapse detection: no run shares the primary-surface type or section spine;
3 sans / 2 serif; 4 accent hues; radius 4–12. What DOES recur (pharmacist
presence, delivery facts, ordering path, opening-hours truth) is the
product's own entity/task set — justified content-level similarity, not a
memorized composition. Multi-run variance: no forced randomness observed or
needed; composition differences trace to documented model-lens choices.

## 3. Same industry (restaurants/food) × 3 products — PASS (2 RENDERED + 1 REASONED-SPEC)

- r1 fine-dining tasting room (RENDERED): menu-as-reading (7 courses with
  provenance lines), one-seating facts, deposit-honest reservation form,
  serif cream, geometry 3–4px. Top task: decide + reserve.
- r2 street-food pickup app (RENDERED): live order-status strip, item rows
  with modifiers, sold-out honesty, sticky thumb-zone cart bar, warm sans,
  geometry 9–12px. Top task: order in under a minute.
- r3 multi-branch ops console (REASONED-SPEC): shift queue by station,
  exception-first (late orders, stockouts), hands-busy targets, staff
  register; no consumer chrome.

Style-blind: opposite silhouettes (reading-form vs transaction-app vs ops
grid), different navigation, density, interaction model, and responsive
behavior — derived from audience/consequence, matching the module's own
"two modes" split. Prior healthcare pair (V7 behavioral record) shows the
same pattern in a second industry.

## 4. Full redesign variance × 2 real products — PASS (VERIFIER-EXECUTED)

Both: fetch (SOURCE-OBSERVED) → extraction → ledger → re-derivation →
instrumented before/after → `scripts/validate_redesign.py` → PLAN PASS →
RENDER PASS (9/9 style-blind dimensions each, viewport-exact screenshots,
DOM snapshots 0 console errors, structural a11y 0 violations).

**Hacker News** (34 KB fetched 2026-09-03): 8 capabilities preserved
(story-browse, voting, discussion, submission, sections, login, hide,
pagination — machine-checked markers). Scope gate rejected thumbnails /
infinite scroll / personalization (register and scope fidelity). Legitimate
structural keeps re-audited: rows (homogeneous ranked records) and high
density (feed product), with changed anatomy. Old-layout anchoring: none —
navigation/zones/sequence/grouping/interactions/responsive/silhouette all
re-derived; identity (orange-on-cream hue family, terse register) preserved
without rebrand.

**itch.io** (112 KB fetched 2026-09-03): 8 capabilities preserved (search,
tag-browse, category-browse, game-discovery, jam-participate, blog, login,
game-pages with real extracted game URLs). Games moved above the tag cloud;
featured gained lead/rail editorial hierarchy; jams became countdown cards;
scope gate rejected recommendations/cart-on-home/follows. Identity (red
family, italic wordmark) preserved.

## 5. Visual-DNA comparison (all 15 pages) — PASS

Typography: 4 serif voices, 10 sans, 1 mono-accented, 1 dark technical —
chosen by register (institutional serif / civic sans / enthusiast dark /
playful rounded). Geometry spans 2–14px tracking register, never uniform.
Surfaces: 13 light / 2 dark, each dark justified (kitchen context in V7
record; enthusiast hardware here). Motion: near-static across all; emphasis
via weight/color/position. Imagery role: none (no stock anywhere) — honest
limitation: static demos use typographic/color-block artifacts instead of
photography; real-content roles were specified in each model. No single
REAL-UI look emerged across unrelated products.

## 6. Template-gravity scan — no failures after repairs

Checked across all outputs: same hero (none), same card grid (no — card
modules differ per model), same dashboard shell (none in this set),
same sidebar (none), same section order (none within any test set),
same container language (radius varies by register), same spacing rhythm
(varied), same CTA pattern (verb + object differs per product), same
responsive transformation (varied: collapse/scroll/tablet-rail by content).

## Failures found → root-cause repairs (all implementation/tooling level; zero knowledge defects)

| # | Failure | Root cause | Repair | Retest |
|---|---|---|---|---|
| F0 | 19 installs content-drifted in 4 files (pre-test audit) | release-time sync ran before final whitespace fixes | re-ran install.py | 19/19 IDENTICAL |
| F1 | T4-HN plan FAIL: changed dims lacked decisions | verifier counts density/representations as changed (anatomy did change) — my intent labels were wrong | added 2 structural decisions (honest: anatomy changed, principle kept) | PLAN PASS |
| F2 | T4-itch case.json unreadable | missing opening quote in routes array | fixed JSON | PLAN PASS |
| F3 | T4 a11y violations: h1 missing (HN both, itch before), nav landmark missing (HN before) | real HN lacks h1/nav; reconstruction comparability baseline incomplete | added instrumented h1/nav (documented as comparability additions) | 0 violations |
| F4 | itch after overflowed at 390px | flexbox input min-width:auto (placeholder set intrinsic width) | `min-width:0` | no overflow |
| F5 | itch before overflowed at 390px | my reconstruction used fixed grids — unfaithful to real responsive product | added collapse breakpoints | no overflow |
| F6 | T4 both: RENDER FAIL on missing capability/feature markers | under-marked implementations | added exact markers | RENDER PASS |
| F7 | run3 double h1; r2 missing h1 | heading semantics slip | h1→h2 on second door; logo→h1 | PASS |
| F8 | run1.html vanished after creation (browser read error page; file absent) | file lost post-write (cause unconfirmed; likely tooling hiccup) | rewrote from derivation, verified on disk + fresh browser | PASS |

Knowledge→routing→reasoning chain held in every case: all failures were
implementation or instrumentation defects caught by the harness/verifier,
repaired at root, retested. No knowledge files modified (none implicated).

## Regression + state

- `python -m unittest discover`: 29/29 OK (unchanged knowledge, as expected).
- verify_install: 19/19 destinations IDENTICAL, no ghosts/orphans, compile,
  YAML — FINAL: ALL CHECKS PASS.
- Repository working tree: clean except this report (committed as the
  session's evidence record). No push performed (awaiting instruction).

## Honest limitations

- Multi-run variance is evidenced across 5 isolated runs of one brief by one
  agent configuration; cross-agent and repeated-sampling variance remain
  future work (matches the V7 record's stated limit).
- T4 game/story/jam content mixes verbatim extracted links with
  representative entries where the live page loads them via JS (labeled in
  both case files).
- a11y checks are DOM-structural (not axe-core); contrast not machine-measured.
- r3 (restaurant ops) is REASONED-SPEC; native app runtimes remain untested.
