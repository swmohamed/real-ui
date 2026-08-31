# Code-First Test — Operating Without Vision

Verifies the Skill reasons deeply about design using ONLY code-level
evidence. Assumption: THE MODEL CANNOT SEE IMAGES.

## Part A — Reading a site from source (given HTML/CSS excerpts)

For each snippet, state what can be OBSERVED/INFERRED and what design
decisions follow:

1. `<html lang="ar" dir="rtl">`, viewport standard, theme-color #0c9,
   fonts: `var(--font-shahid)` + fallback sans; radii: 16px, 9999px.
   → Expect: dark streaming identity, brand-green accent, Arabic-first
   product, media-card system with pill CTAs; infer entertainment DNA.

2. Breakpoint census {768: 543 uses, 1280: 311, 767: 244, 1024: 220}
   + `[dir="rtl"]` overrides 40+ + Tajawal @font-face weights 400/500/700.
   → Expect: RTL-primary product, desktop-first legacy strategy (767/799
   max-widths), real Arabic bold available.

3. `font-family: ui-monospace…` + tabular-nums on `.price` + `<table>`
   with sticky first column + sparkline SVGs with role="img" + aria-labels.
   → Expect: instrument/data product; a11y-aware data viz.

4. CSS vars: `--brand: #635BFF` family with `--surface-raised`,
   `--radius-sm: 4px` only two shadow tiers, `prefers-reduced-motion`
   present, container queries on `.card`.
   → Expect: modern tokenized product, restraint, component-level
   responsiveness; likely SaaS/dev class.

## Part B — Producing design without seeing anything

Task: "Design the article page for an Arabic quality-news site; you
cannot view any screenshots." Expected reasoning chain:
- pages/article.md + typography/arabic-typography.md + industries/news-media.md
- Structure: kicker→h1→standfirst→byline (dual timestamps)→hero w/ caption
  → body 19–21px Naskh, lh 1.8, measure ~75ch → subheads → related
- Specify: dir rtl, punctuation ، ؟, dir="auto" on mixed Latin names,
  tabs/accordion patterns for sections, reading progress, share rail
  start-side, sticky minimal header
- Perf/a11y: lazy figures, aspect boxes, reduced-motion, focus-visible

## Part C — Auditing code-only (given a CSS block, list violations)

Sample block intentionally containing: `maximum-scale=1` viewport,
`letter-spacing: .05em` on Arabic, `position: left` absolute in RTL
context, gradient text on h1, blur(30px) on scrolling container.
Expected findings (why + fix) — all discoverable from code alone.

## Acceptance

The Skill passes if every answer above can be derived WITHOUT images,
with correct OBSERVED/INFERRED labeling, and violations/fixes reference
the correct knowledge files. Vision would only decorate these answers,
never enable them.
