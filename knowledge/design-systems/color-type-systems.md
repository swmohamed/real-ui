# Design Systems: Color & Typography Systems

## Color system construction

### Building the scales
1. Pick brand hue(s) → generate 50–950 ramp (11 steps) with perceptually
   even lightness (OKLCH makes this trivial; HSL acceptable)
2. Build neutral ramp tinted toward brand (hue-matched grays)
3. Assign semantic roles (see tokens.md); the assignments are the system —
   the ramps are just inventory
4. Verify pairs programmatically: body/ink on canvas ≥4.5:1, actions
   ≥3:1 (automate in CI — leaders do)

### Observed real-system conventions
- Brand blues: PayPal #012169, Coursera #0056D2, Aqarmap #007dbe, GDS
  #1d70b8 — institutional blues cluster 210–225° hue
- Signal reds: TED #EB0028, BBC red family — reserved for live/breaking/
  brand-only usage
- Dark surfaces: #0a0e14–#171a21 range (Steam #171a21, Linear #08090a
  OBSERVED) with surface steps +10 L% apart + hairline borders
- Entertainment scrims: black gradients at 40–70% under text (Disney+
  OBSERVED)

### Theme strategy
- Light default + dark via class strategy (`.dark` on html — Tailwind
  convention OBSERVED across corpus) or `prefers-color-scheme` +
  manual override (respect stored choice)
- Multiple brands: swap primitive values only; semantic layer untouched

## Typography system construction

### Scale design (evidence-based)
- UI scale (corpus): 12, 13, 14, 15, 16, 18, 20, 24, 30, 36, 48, 60 —
  modular ~1.25 ratio with pragmatic clamps
- Display scale (marketing): extend to 64–96 via clamp(36px, 5vw, 72px)
- Line-height tokens: 1.1–1.2 display / 1.4–1.5 UI / 1.6–1.7 body /
  1.8–2.0 Arabic body
- Letter-spacing: -0.01 to -0.02em at display sizes; 0 body; +0.02–0.1em
  for uppercase labels (kickers/eyebrows)

### Font loading discipline
- `font-display: swap` (or optional/size-adjust with metric-compatible
  fallbacks to prevent swap-flash — modern standard: `ascent-override`
  tuned fallbacks, Inter-fallback class OBSERVED in Next.js corpus sites)
- Subset: latin + arabic subsets separately; preload the 1–2 weights
  actually used above fold (woff2, subset, ≤40KB each realistic)
- Variable fonts where multi-weight (1 file many weights) — OBSERVED
  adoption (Airbnb Cereal VF, sohne-var, Inter Var)

### Pairing slots
- **Single-family system**: one grotesk + weights (product UIs — Inter
  class; safest default)
- **Display+text system**: distinctive display (brand voice) + quiet text
  (reading) — SaaS marketing, editorial
- **Serif-body system**: editorial identity (news/quality press)
- **Three-slot system**: sans UI + serif editorial + mono technical
  (docs platforms, fintech — mono carries credibility)
- Arabic pairing: see `typography/arabic-typography.md` — Arabic slot is
  its own decision, not "same font Arabic version" automatically

### Numerals
- `font-variant-numeric: tabular-nums` for all tables/prices/counters;
  oldstyle figures only in editorial body if intentional

## Anti-patterns

- Two display fonts competing; 9 weights loaded for 3 used; per-page
  typography tweaks (the drift that kills systems); contrast "fixed in
  design tool" but broken by theme overlay; Arabic text styled with
  Latin-only line-heights (clipped diacritics)
