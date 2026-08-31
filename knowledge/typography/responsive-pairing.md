# Typography: Responsive & Pairing Practice

## Responsive type rules

- Body: 16px minimum everywhere (14px only for dense UI metadata);
  articles 17–19 mobile
- Display: fluid via clamp — `clamp(2rem, 1.2rem + 4vw, 4.5rem)` — with
  min/max anchored to real design sizes
- Step rhythm at breakpoints: shift 1–2 steps, not full rescale (mobile
  h1 28–36px, desktop 48–72px product; editorial can exceed)
- Line-height inverse-scales with size: display 1.1, body 1.6
- Optical sizes: variable fonts with `opsz` axis honor display vs text
  cuts (real display cuts are drawn tighter)

## Hierarchy across viewports

- The ratio between h1 and body should INCREASE on mobile (fewer px, same
  hierarchy drama via weight/spacing)
- Kickers/eyebrows shrink-out on mobile if space-constrained (or stay —
  they're 1 line)

## Bilingual responsive reality (AR+EN products)

- Arabic runs larger + taller line-height → vertical rhythm tokens must
  accommodate BOTH scripts (define spacing in the system for the larger
  script; Latin reuses)
- clamp() values tested against Arabic string lengths: Arabic headlines
  are often 15–25% shorter character-wise but wrap differently — real QA
  with Arabic strings, not English + "it'll probably wrap fine"
- RTL line-clamp works; -webkit-line-clamp direction-safe

## Pairing checklist (any project)

- [ ] Two families max (+mono if technical)
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
