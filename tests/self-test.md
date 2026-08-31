# Self-Test — 10 Industry Scenarios

Run each scenario through the Skill workflow mentally (or literally with
an agent). The acceptance test: **outputs must NOT resemble each other**
and each must satisfy its industry check. All reasoning is code-first —
no screenshots required.

## How to run
For each scenario: CLASSIFY → RETRIEVE (≤6 files) → direction statement →
token sheet sketch → key structural decisions. Then compare across
scenarios.

## 1. Browser gaming portal (Arabic-first, kids skew)
Must: gaming DNA, 16px tiles, hover-play, tag-chip browse, zero-friction
play, RTL shelves, Arabic titles with dir="auto", bright candy canvas.
Must NOT: SaaS hero, glass cards, dark-terminal default, form gates.

## 2. Arabic news site (quality-press positioning)
Must: Editorial DNA, serif-or-Naskh body + sans headlines, dense river,
live-blog capability, dual timestamps, RTL river with مباشر chips.
Must NOT: marketing gradients, sparse luxury whitespace, poster-hero
defaults.

## 3. Fashion ecommerce (luxury, Gulf)
Must: Premium Restraint, 0–4px radius, serif/spaced display, campaign
photography-first, modest-fashion categories, AED/SAR.
Must NOT: deal badges, countdown spam, playful radius, utility density.

## 4. SaaS dashboard (analytics tool)
Must: Instrument DNA, dense tables (40–48px rows), tabular numerals,
skeleton states, keyboard-first, left rail, 2–3 elevation tiers.
Must NOT: glassmorphism, gradient panels, marketing whitespace, blob
decoration.

## 5. Fintech consumer site (Egyptian mass market)
Must: warm-fintech or utility register, fee transparency surfaces,
Fawry/COD chips, Arabic-first with EN toggle, WhatsApp support visible,
EGP formatting.
Must NOT: crypto-terminal darkness, luxury restraint, hidden pricing.

## 6. Restaurant (single-location, upscale)
Must: appetite-led cinematic-lite, menu-as-content, reserve/CTA sticky,
story sections, hours/location prominent.
Must NOT: platform density, deal chips, utility grids.

## 7. Real estate portal (UAE, bilingual)
Must: search-first hero, map+list duality, icon-fact bars, agent cards
with WhatsApp, offplan payment plans, EN/AR parity.
Must NOT: cinematic-only luxury site (it's a portal), form-gates.

## 8. Travel booking (regional OTA)
Must: search widget as hero, free-cancellation badges, price calendars,
sticky summaries, BNPL display, bilingual.
Must NOT: inspiration-only hero for intent traffic, hidden totals.

## 9. Portfolio (senior product designer)
Must: work-first (no intro animation), Swiss or editorial DNA, case
study depth, contact ≤1 click, custom typography decision.
Must NOT: mystery nav, full-page WebGL before content, template feel.

## 10. Government services portal (bilingual, task-first)
Must: GDS DNA, task grid (verb-first), search-first, zero decoration,
full parity AR/EN, accessibility floor highest.
Must NOT: cinematic hero, gradients, marketing tone.

## Cross-scenario acceptance checks
- [ ] No two scenarios share the same token sheet (radius/type/density/
  accent all differ)
- [ ] Each cites ≥2 real reference classes as evidence
- [ ] Each passes the anti-AI banned list
- [ ] Arabic scenarios pass the RTL gate (dir, mirroring rules, bidi
  fields, Arabic type with real line-heights)
- [ ] Each states its one differentiation move

## Recorded expectations (for regression)
Token-sheet sketches per scenario should differ on ≥4 of 6 axes:
canvas (light/dark/candy), radius mode (0–4/4–8/8–16/16+), type pairing,
density (sparse/standard/dense/maximum), accent strategy, motion budget.
