# Color Foundations — How Real Palettes Are Built

## The four-role palette model

Every real site's palette resolves to four roles (OBSERVED across token
systems — Stripe `--hds-`, Coinbase `--cds-`, Kooora `--fco-`):

1. **Canvas** — page background(s): 1 light + optional 1 dark.
2. **Ink** — text ramp: 3–4 grays (primary 87–100% ink, secondary 60–70%,
   muted 45–55%, inverse).
3. **Brand** — 1 primary hue + optional 1 identity secondary.
4. **Semantic** — success / warning / danger / info, fixed by convention.

## Observed sector color behavior

- **Finance/banking:** institutional blues (#012169 PayPal, Chase/HSBC navy
  family), high contrast, semantic states everywhere; one warm accent for
  marketing moments only. Gradients = subtle 2-stop, never rainbow.
- **News:** paper whites + ink blacks + **exactly one signal red** (BBC, TED
  #EB0028, Sky News Arabia, CNN). Section color-coding on leaders (Guardian
  section pinks/blues) is a secondary system, applied to section labels only.
- **Gaming/browser-gaming:** saturated accent on dark or candy-light canvas
  (Poki theme-color #83ffe7 mint on white; CrazyGames #212233 navy + vivid
  accents; Steam #171a21 near-black). Accents carry energy: mint, lime,
  magenta, cyan.
- **Government/health:** 2–3 colors total. gov.uk GDS blue #1d70b8, NHS blue
  family, UAE portal flag-green + gold accents. Zero decoration color.
- **Entertainment/streaming:** dark navy/charcoal canvases with poster art as
  the real color source; UI stays neutral so thumbnails pop (Disney+, Shahid).
- **Luxury/auto:** near-monochrome + one metallic/champagne accent;
  full-bleed photography IS the palette (Porsche, Rolex class).
- **MENA mainstream:** deeper saturated primaries than Western equivalents —
  stc violet/purple, Emirates NBD green, Al Rajhi deep blue, Aqarmap cyan —
  with generous white space still expected in Gulf premium segment.

## Building ramps (tokens)

- Build 50–950 ramps (11 steps) per hue; use ~5 steps in practice.
- Neutral ramps should tint toward the brand hue slightly (warm-gray with
  warm brands) — the difference between "designed" and "default gray".
- Dark mode is not inverted light mode: dark canvases 8–12% lightness, ink
  becomes off-white (not #fff), brand hue lightened 1–2 steps for contrast,
  shadows replaced by surface lightness steps + hairline borders.
- Pair every dark surface with border `rgba(255,255,255,.06–.12)` — real dark
  systems separate surfaces with lines, not shadows (OBSERVED Discord/Steam class).

## Contrast & states (non-negotiable)

- Body text ≥ 4.5:1, large text ≥ 3:1, UI components/icons ≥ 3:1 (WCAG AA).
- Interactive states must differ by more than hue: hover (darken 8%),
  active (darken 12% or inset), focus (visible ring), disabled (40% ink +
  no shadow + `cursor: not-allowed`), selected (fill + check icon).
- Link styling in body copy: always distinguishable by more than color
  (underline on hover minimum, persistent underline in dense text).

## Gradients — the cost/benefit line

Gradients are legal when: brand systems genuinely use them (Stripe's camille
sweep), poster scrims (entertainment), subtle depth in finance CTAs.
Illegal by default when: purple→blue hero washes, gradient buttons in gov/health,
gradient text everywhere, gradients as compensation for weak typography.
Volume matters: Stripe ships ~3 gradient declarations; Disney+ ships 230 —
because its gradients ARE scrims behind content. Match your sector's ratio.

## Color independence

Never encode meaning in color alone: errors get icon+text, charts get patterns
+ labels, statuses get dot+label. Test designs in grayscale — if the hierarchy
survives, color is doing enhancement, not carrying structure.
