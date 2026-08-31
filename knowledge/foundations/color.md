# Color Foundations — How Real Palettes Are Built

## A four-role palette model

Use these semantic roles as a compact starting model. Named token systems in
the corpus support role-based palettes, but not every site has exactly four
groups and the role names are RECOMMENDED rather than observed universals:

1. **Canvas** — page background(s): 1 light + optional 1 dark.
2. **Ink** — text ramp: 3–4 grays (primary 87–100% ink, secondary 60–70%,
   muted 45–55%, inverse).
3. **Brand** — 1 primary hue + optional 1 identity secondary.
4. **Semantic** — success / warning / danger / info, fixed by convention.

## Observed sector color behavior

- **Finance/banking:** institutional blues (#012169 PayPal, Chase/HSBC navy
  family), high contrast, semantic states everywhere; one warm accent for
  marketing moments only. Gradients = subtle 2-stop, never rainbow.
- **News samples:** paper/ink contrast with restrained signal or section
  colors. Several brands use red, while others use broader section systems;
  brand evidence decides the hue and count.
- **Gaming/browser-gaming:** saturated accent on dark or candy-light canvas
  (Poki theme-color #83ffe7 mint on white; CrazyGames #212233 navy + vivid
  accents; Steam #171a21 near-black). Accents carry energy: mint, lime,
  magenta, cyan.
- **Government/health samples:** compact, high-contrast palettes (gov.uk GDS
  blue, NHS blue family, UAE portal flag colors). Decoration must not compete
  with task or safety information.
- **Entertainment/streaming:** dark navy/charcoal canvases with poster art as
  the real color source; UI stays neutral so thumbnails pop (Disney+, Shahid).
- **Luxury/auto samples:** near-monochrome systems sometimes let photography
  carry most color and use a restrained accent; this is a positioning option,
  not a category requirement.
- **MENA corpus examples:** several sampled brands use saturated primaries
  (stc violet, Emirates NBD green, Al Rajhi blue, Aqarmap cyan). Treat these as
  individual brand evidence, not a regional default; derive saturation from
  supplied brand assets and market research.

## Building ramps (tokens)

- Build only the primitive steps the semantic roles/states need; numeric
  50–950 naming is one convention, not the system itself.
- Test neutral ramps both truly neutral and brand-tinted; choose from brand,
  legibility, and adjacent-surface needs rather than a “designed” look rule.
- Dark mode is not an automatic inversion: tune canvas, text, brand, and
  semantic pairs for contrast and glare; often brand hues need adjustment and
  shadows replaced by surface lightness steps + hairline borders.
- Pair every dark surface with border `rgba(255,255,255,.06–.12)` — real dark
  systems separate surfaces with lines, not shadows (OBSERVED Discord/Steam class).

## Contrast & states (non-negotiable)

- Body text ≥ 4.5:1, large text ≥ 3:1, UI components/icons ≥ 3:1 (WCAG AA).
- Interactive states must remain distinguishable: use perceptible
  surface/border/shape changes, a visible focus indicator, honest disabled
  semantics, and persistent selected treatment. Verify contrast instead of
  relying on fixed darkening/opacity percentages.
- Link styling in body copy: always distinguishable by more than color
  (underline on hover minimum, persistent underline in dense text).

## Gradients — the cost/benefit line

Gradients are legal when: brand systems genuinely use them (Stripe's camille
sweep), poster scrims (entertainment), subtle depth in finance CTAs.
Avoid by default when: purple→blue hero washes, gradient buttons in gov/health,
gradient text everywhere, gradients as compensation for weak typography.
Volume matters: Stripe ships ~3 gradient declarations; Disney+ ships 230 —
because its gradients ARE scrims behind content. Match your sector's ratio.

## Color independence

Never encode meaning in color alone: errors get icon+text, charts get patterns
+ labels, statuses get dot+label. Test designs in grayscale — if the hierarchy
survives, color is doing enhancement, not carrying structure.
