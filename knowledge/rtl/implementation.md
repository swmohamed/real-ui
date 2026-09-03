# RTL Implementation (the engineering contract)

V2: non-web platforms (Flutter/Compose/RN/iOS) → rtl/cross-platform.md.

Corpus truth: 21/31 Arabic sites use explicit `[dir="rtl"]` selectors;
modern leaders use logical properties + `rtl:` utility variants (PayPal
`rtl:[--rotate:180deg]`, Arabian Oud `rtl:group-hover:-translate-x-2`
OBSERVED). Real bugs observed (missing dir attr with lang="ar", icon-font
arrows unmirrored) — encode the checklist below.

## Foundation (get these 100% right)

1. `<html lang="ar" dir="rtl">` — BOTH attributes, every page, both
   directions maintained per locale route (/ar/, /en/)
2. Build with **logical properties**: `margin-inline-start`,
   `padding-inline`, `inset-inline-end`, `text-align: start`,
   `border-inline-start` — 90% of mirroring happens automatically
3. Flexbox/Grid auto-mirror with direction — never use `left/right`
   absolute positioning for flow content
4. `[dir="rtl"]` overrides only for what logical properties can't do:
   transforms on directional icons, gradients with direction, background
   positions, pseudo-element arrows
5. Numbers/Latin data inside RTL: `dir="ltr"` spans or `dir="auto"` on
   user content (titles, search inputs, message bodies)

## Per-mechanism rules

| Mechanism | RTL handling |
|---|---|
| Chevrons/arrows (nav, next, breadcrumbs) | flip via scaleX(-1) class |
| Icons (see iconography flip list) | flip directional only |
| Progress/steppers | flow start→end (right→left); numbers stay |
| Carousels/rails | native scroll auto-RTL + snap; arrows flip |
| Tooltips/popovers | collision detection + start/end positioning |
| Shadows | symmetric or flip offset-side |
| Gradients/scrim | mostly direction-neutral; angled brand gradients flip |
| Range sliders | min at start (right) — native with dir |
| Charts | direction follows data meaning, domain convention, scale, and user expectation; labels and mixed values stay bidi-safe—pick and document |
| Video controls | unchanged (timeline semantics) |
| Maps | unchanged (geography) |

## Bidi text survival kit

- Punctuation drift ("Hello!" renders "!Hello"): wrap Latin runs in
  `<bdi>` or explicit `<span dir="ltr">`
- Mixed numerals with units: "٥٠٪" vs "50%" — set product policy;
  wrap if direction issues
- `unicode-bidi: plaintext` for user-generated lines; `dir="auto"` on
  comment/message containers
- Test strings: "iPhone 15 متاح الآن", "السعر: 1,299 SAR — شامل الضريبة",
  phone "+966 5X XXX XXXX" — all three are daily realities

## CSS architecture patterns (ranked)

1. Logical properties everywhere (best — one codebase)
2. Utility framework `rtl:` variants (Tailwind — OBSERVED mainstream)
3. `[dir="rtl"]` override blocks (legacy-compatible; keep selectors
   scoped, not page-wide rewrites)
4. Separate RTL stylesheet (worst — divergence guaranteed; legacy only)

## The QA checklist (ship gate for RTL)

- [ ] html lang+dir correct on every route
- [ ] No left/right positioning outside decorative absolutes
- [ ] Directional icons flipped; media controls NOT flipped
- [ ] Mixed-direction fields (phone, card, email) dir="ltr"
- [ ] Line-height/type tested with Arabic strings (diacritics don't clip)
- [ ] Sticky/absolute elements positioned with logical insets
- [ ] Toast/sheet placement and motion follow platform, reach, obstruction, and semantic direction—not automatic mirroring
- [ ] Filter/slider/math axes sensible; charts policy documented
- [ ] Font loaded includes Arabic subset with real bold
- [ ] Error/validation messages localize correctly (bidi-safe)

## Anti-patterns (observed in the wild — never repeat)

- `direction: rtl` on body only, children fighting with `text-align:left`
- Mirroring EVERYTHING including logos/media/play buttons (over-flip —
  as broken as under-flip)
- Direction set by JS after paint (flash of wrong direction — set
  server-side on html)
- Latin-only design reviewed, Arabic added post-hoc by "just flip it"
