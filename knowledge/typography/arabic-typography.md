# Typography: Arabic Systems (the specialized craft)

Arabic is not "a font swap": different metrics, joining behavior, and
reading conventions. This file encodes real practice.

## The real Arabic web faces (observed + canon)

**Sans (UI/product):**
- **Tajawal** — geometric modern, pairs with Inter/Open Sans energy
  (Jarir, Zid OBSERVED)
- **Almarai** — clean contemporary sans, great UI legibility (FilGoal,
  4 Google-loads OBSERVED)
- **IBM Plex Sans Arabic** — engineered family, bilingual consistency
- **Noto Sans Arabic / Noto Sans Arabic UI** — coverage workhorse
  (Disney+, Almosafer fallback OBSERVED); UI variant has tighter metrics
- **Dubai Font** — UAE government/commerce identity face (Extra.com
  OBSERVED); carries institutional Gulf familiarity
- **Cairo** — ubiquitous in Egypt-market sites (verify current usage)

**Display/headers:**
- **Noto Kufi Arabic** — geometric Kufi energy; modern-tech headers
  (Almentor OBSERVED pairing with Inter)
- **Rubik Arabic / Baloo Bhaijaan** — rounded consumer/playful
- Custom Kufi logotypes for brands (identity tier)

**Naskh (reading/long-form):**
- **Noto Naskh Arabic** (2 loads OBSERVED), **Amiri** (classical, books/
  Quran-adjacent), **Lateef/Scheherazade** (SIL, long-form reading)
- News body class: Naskh for articles, sans for headlines/rails

**Diacritics-critical** (Quran, poetry, classical): Amiri/Scheherazade
class only — generic sans breaks harakat positioning. This is a
typographic hard requirement, not a taste call.

## Metrics reality (must handle)

- Arabic needs MORE vertical space: line-height 1.7–2.0 body (vs 1.5–1.7
  Latin) or diacritics/ascenders clip
- Font sizes run 1–2px larger than Latin equivalents for equal optical size
- Arabic doesn't have true italics (never synthesize skew); emphasis =
  weight or color
- Uppercase/lowercase doesn't exist — the small-caps "kicker" convention
  becomes: letter-spacing on Arabic (use sparingly, tracking harms joining
  legibility) OR use Latin kicker + Arabic headline, OR color/weight device
- Bold: check face actually HAS real bold (many Arabic webfonts fake it)
- Numbers inside Arabic text: choose Western (0-9) or Arabic-Indic (٠-٩)
  per product and stay consistent; Western digits dominate prices/data in
  the observed corpus

## Pairing systems (bilingual products)

| Register | Latin | Arabic | Seen in |
|---|---|---|---|
| Modern product | Inter | Tajawal / Almarai | Zid-class |
| Institutional Gulf | Source Sans-class | Dubai Font | Extra/gov adjacents |
| Video/consumer | Inter | Noto Kufi Arabic | Almentor |
| News | Franklin-class | Naskh body + sans heads | regional press |
| Coverage-safe | Open Sans/Roboto | Noto Sans Arabic | Almosafer-class |

Rules: match geometry (geometric↔geometric), match weights (both faces
need 400+700 real), define which script leads when sizes must differ
(optical-balance: Arabic often set 105–110% of Latin size).

## Line-break & shaping

- Never break lines mid-word (joining breaks meaning); `hyphens: none`
- Justified text: use `text-justify: inter-word` caution; prefer
  start-aligned (ragged) for UI, justify acceptable for long articles
  (regional convention)
- Mixed-script lines: Unicode bidi handles most; wrap volatile user
  content with `dir="auto"`; embed Latin runs with explicit spans when
  punctuation misbehaves (the classic "!" landing on the wrong side)

## Fallback stack template

```css
--font-arabic: "Tajawal", "Noto Sans Arabic", "Segoe UI Arabic", "Tahoma", sans-serif;
```
Tahoma = legacy but real Arabic-capable fallback (Windows); Segoe UI
Arabic covers modern Windows; always end sans-serif.

## Anti-patterns

- Latin-only line-height applied to Arabic (clipped dots/tails)
- Fake bold/skew; letter-spacing on Arabic body
- Naskh headlines at display sizes for tech products (wrong voice — Kufi/
  sans territory); Google-translate typography (auto font choices per
  script with no pairing decision)
- Mirrored question marks: Arabic question mark ؟ and comma ، — use the
  correct punctuation set in Arabic copy
