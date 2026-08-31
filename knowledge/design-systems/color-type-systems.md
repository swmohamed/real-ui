# Design Systems: Color & Typography Systems

## Color system construction

### Building the scales
1. Pick evidenced brand hue(s) → create only the primitive steps needed by
   semantic roles and states; 50–950 names are optional. Prefer a perceptual
   color space and verify real rendered pairs
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
- Choose light, dark, or system-following initial mode from product context;
  when both exist, support system preference plus an explicit stored override
- Multiple brands: swap primitive values only; semantic layer untouched

## Typography system construction

### Scale design (evidence-based)
- Common corpus values can seed a compact scale (12/14/16/18/20/24/32 are
  frequent), but choose steps from content hierarchy and selected typeface
- Display sizes use a bounded responsive range verified against real copy;
  no fixed 64–96 extension is required
- Line-height tokens: 1.1–1.2 display / 1.4–1.5 UI / 1.6–1.7 body /
  1.8–2.0 Arabic body
- Letter-spacing: -0.01 to -0.02em at display sizes; 0 body; +0.02–0.1em
  for uppercase labels (kickers/eyebrows)

### Font loading discipline
- `font-display: swap` (or optional/size-adjust with metric-compatible
  fallbacks to prevent swap-flash — modern standard: `ascent-override`
  tuned fallbacks, Inter-fallback class OBSERVED in Next.js corpus sites)
- Subset scripts carefully and preload only critical faces/weights; set a
  project font budget measured from the actual files rather than a universal
  per-file number
- Variable fonts where multi-weight (1 file many weights) — OBSERVED
  adoption (Airbnb Cereal VF, sohne-var, Inter Var)

### Pairing slots
- **Single-family system**: one suitable brand/system family + weights when a
  unified product UI hierarchy benefits from it
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
