# Patterns: Content Sections — Tabs, Accordions, Feature Splits, FAQs,
Timelines, Comparison

## Tabs
- **Purpose**: sibling content in same context without page jumps
- **Anatomy**: tab list (role=tablist) + panels; active indicator
  (underline or pill); arrow-key navigation; hash deep-links
- **Use**: PDP info groups (description/specs/reviews), dashboards,
  league pages (fixtures/table/stats OBSERVED on sports)
- **Watch-outs**: ≤6 tabs visible; overflow = scrollable rail not wrap;
  lazy panels; never tabs for sequential steps (use stepper)

## Accordions
- **Purpose**: progressive disclosure of scannable reference content
- **Use**: FAQs, syllabi, specs, policies, mobile filters/menus
- **Anatomy**: button header (aria-expanded) + content region; single-open
  (menu-like) vs multi-open (reference) — choose deliberately
- **Watch-outs**: chevron rotate 180 on open (flip in RTL); content
  searchable ideally (long FAQ); first item open by default only when
  truly representative

## Feature split sections
- **Purpose**: explain capability with alternating text/visual rhythm
- **Anatomy**: eyebrow label + h2 (24–32) + 1–2 line description + 3–4
  bullet proofs + visual (product shot/diagram); alternate sides with
  generous vertical rhythm 96–128px
- **Use**: SaaS/product pages (the canonical section)
- **Watch-outs**: 3 sections max before a proof break; visuals real;
  mobile: text→visual stacking consistent

## Feature grids
- 2×2/3×3 icon+title+line cards; icons from ONE system (see iconography);
  **use**: secondary capabilities after hero/splits; **watch-outs**: 9
  identical tiles = wall — vary emphasis or cut to 6

## FAQ sections
- Accordion + FAQPage schema (OBSERVED: Almosafer ships FAQPage JSON-LD);
  question-first phrasing users actually type; 5–8 items above fold of
  section; link to full help center

## Comparison sections
- Product tiers side-by-side, or us-vs-them tables (risky — frame as
  objective criteria, avoid competitor logos without legal review)
- Feature parity checklists; highlight column (target tier)
- Mobile: sticky first column horizontal scroll, or per-tier stacked cards

## Timelines / process sections
- "How it works" 3–4 steps: numbered markers + connecting rail + micro-copy
  per step (reduces perceived risk — conversion pattern)
- History timelines (about pages): year rails; changelog: reverse-chron
  with version tags + date

## Stats bands
- 3–5 big numbers inline row (value + label + context/date); tabular
  numerals; counters animate once; sources cited (trust)

## Testimonial sections
- Carousel testimonials: 1 visible, real name/role/photo/company, specific
  outcome quote; quote marks as typographic device not clipart
- Logo walls: 6–12 grayscale → color on hover (subtle), single row or 2
- Video testimonials: poster + duration + captions

## CTA bands (section closers)
- Solid brand color band, 2-line promise, single CTA; alternating contrast
  to reset the page rhythm; final one before footer on marketing pages

## RTL notes
- Tab rails scroll start→end; accordions chevron flip; timeline rails
  flip; numbered steps keep Western digits; comparison columns mirror
  (target tier emphasis start-side)

## Anti-patterns
- Accordions hiding content users must read (policies, pricing)
- Tabs with 1–2 items; carousels of testimonials without controls
- Feature walls of 12 tiles; stats without dates; process steps of 7
