# V5 rendered validation report

Generated on 2026-08-31 from `showcase/render-report.json`.

## Result

- 16 implemented surfaces rendered in Chromium: 8 greenfield pages plus 4 redesign cases in before and after states.
- 32 exact viewport screenshots: desktop 1440×900 and mobile 390×844.
- 4/4 FULL redesign cases passed the executable PLAN and RENDER phases.
- Every redesign changed 9/9 style-blind dimensions and covered its complete declared capability ledger.
- All 32 renders had zero axe violations, zero console errors, and no horizontal page overflow.
- Axe marked 16 renders `incomplete` for automatic color-contrast calculation where text or symbols intersect CSS gradients, clipped scroll regions, or generated art. Those targets were inspected in the rendered screenshots; this is manual visual review, not an automated contrast claim.

## Manual checks

- Gaming before/after: the after-state no longer has the hero → ad → rail → card-grid composition and keeps play/resume first on phone.
- SaaS before/after: the after-state is a triage workbench, not a restyled overview dashboard.
- Editorial before/after: the after-state is edition/chronology-led, not a restyled lead-and-card homepage.
- Ecommerce before/after: the after-state is a technical selection workbench, not a restyled campaign storefront.
- Editorial versus sports: article/evidence navigation and live score/date/table navigation have distinct composition, density, and interaction.
- Greenfield set: all eight surfaces use different domain entities, task verbs, content representations, and responsive priorities.

## Evidence limits

Automated axe checks are useful but do not replace screen-reader, switch-control, browser-matrix, localization, or usability testing. The static pages exercise semantic structure, local interactions, reflow, and visual composition; they do not provide production backends, persistence, networking, checkout, game engines, or live data.
