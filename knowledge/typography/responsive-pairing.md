# Typography: Responsive & Pairing Practice

## Responsive type rules

- Select body/support/display sizes from platform defaults, font/script
  metrics, viewing distance, density, user settings, and real-content tests;
  fixed pixel ranges are candidates, not roles.
- Fluid type (`clamp`) is useful only when its min/preferred/max values and
  wrapping behavior are tested at content-derived boundaries.
- Type roles can shift nonlinearly across windows; preserve hierarchy and
  measure rather than forcing every role down the same number of steps.
- Line height usually changes with size and script, but each font/content role
  needs diacritic, multiline, and text-scaling tests.
- Optical sizes: variable fonts with `opsz` axis honor display vs text
  cuts (real display cuts are drawn tighter)

## Hierarchy across viewports

- Preserve meaningful hierarchy with the available channels; mobile does not
  require a larger heading/body ratio.
- Remove or defer kickers/eyebrows only when their content is redundant; space
  pressure alone does not erase source, status, or category meaning.

## Bilingual responsive reality (AR+EN products)

- Arabic runs larger + taller line-height → vertical rhythm tokens must
  accommodate BOTH scripts (define spacing in the system for the larger
  script; Latin reuses)
- Test responsive values against real Arabic and Latin strings. Character
  counts do not predict width, wrap, diacritics, or vertical metrics.
- RTL line-clamp works; -webkit-line-clamp direction-safe

## Pairing checklist (any project)

- [ ] Every family/weight has a role and performance/license/script rationale
- [ ] Both scripts chosen deliberately (if bilingual)
- [ ] Weights: only what's loaded
- [ ] One type scale documented (all sizes = scale steps)
- [ ] Line-height + tracking tokens per size step
- [ ] Numerals policy set (tabular where data; digit style per market)
- [ ] Fallback stacks metric-tuned (size-adjust/ascent-override)
- [ ] FOUT/swap flash audited on slow 3G

## Editorial vs UI type (the two modes)

- **UI mode**: 13–16px, tight leading, sentence labels, tabular data —
  optimized for scanning; changes rarely
- **Editorial mode**: 17–21px body, generous leading, display hierarchy,
  pull-quotes — optimized for immersion; per-section rhythm
- Products mix both (SaaS = UI+marketing editorial; news = editorial+
  UI rails) — define which mode governs which template explicitly
