# Patterns: Footers

The most underdesigned, most-scanned region. Footer = navigation +
trust + legal + brand close.

## Standard footer anatomy (top→bottom)

1. **Brand block**: logo, one-line description, social icons (real links
   only), contact quick info (phone/email/address), newsletter form
2. **Link columns** (3–5): Product/Company/Resources/Legal + market-specific
   (Support, Branches/الفروع for MENA service businesses)
3. **Trust strip**: payment methods (visa/mc/mada/stcpay/cod chips for
   MENA commerce), certifications, regulator references, security badges
4. **Legal bar**: © year Company · Terms · Privacy · Cookies ·
   sitemap · language/currency switcher (when not in header)
5. Optional: back-to-top, app badges (consumer apps), careers CTA

## Column content rules

- 4–7 links per column; verbs where possible; group by user task not
  org chart
- Same hierarchy as body links (not 10px gray-on-black — footers still
  need 4.5:1)
- Mobile: columns become accordions (standard) OR 2-col wrap with
  shortened lists; legal bar stays flat

## Mega-footers (portals/enterprise)

- 30–100 links acceptable when genuinely a sitemap (gov, banks, telcos —
  OBSERVED: stc-class sites use footer as full service tree); organize
  with group headers + 2–3 tiers; provide footer search for very large ones

## Trust furniture details

- Payment chips: 24–32px height, grayscale acceptable, hover color;
  COD chip in MENA (الدفع عند الاستلام) — it converts
- Government/consortium logos only when current member (expired badges =
  liability)
- Newsletter: single email field + button + privacy microcopy; success
  inline (no page reload)

## RTL/Arabic footers

- Columns mirror; social icons keep LTR order (brand marks); legal
  bar: "© 2025 الشركة — جميع الحقوق محفوظة" pattern; Hijri year optional
  alongside (منذ التأسيس contexts)
- Contact block: phone LTR spans, WhatsApp number visible

## Accessibility & perf

- Footer is in tab order: no aria-hidden dumping grounds; forms labeled
- Lazy-render below fold; massive footers shouldn't block LCP (render
  after interaction/idle)

## Anti-patterns

- 8-column footers on 4-page sites; dead social icons
- Contact info ONLY in footer (should be header/page-level too on service
  sites)
- Cookie-banner stacking on footer on mobile (double bar chrome)
- Contrast-dumped gray links (illegible = useless)
