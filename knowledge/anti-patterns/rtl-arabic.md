# Anti-Patterns: RTL & Arabic-Specific Failures

Bugs observed in production MENA sites + classic failure classes. Each:
symptom → cause → fix.

## Direction basics
- **`dir` missing while `lang="ar"`** (OBSERVED: a major Saudi bank) →
  mixed layout → always `<html lang="ar" dir="rtl">`
- **`direction: rtl` on body + children `text-align: left` patches** →
  whack-a-mole alignment → logical properties + text-align: start
- **JS sets direction after paint** → flash of LTR → server-rendered
  attributes on html
- **Over-flipping**: mirroring play buttons, logos, clocks, charts →
  as broken as not flipping → follow the flip/never-flip table
  (rtl/implementation.md)

## Typography
- **Latin line-heights on Arabic** → clipped dots/diacritics → 1.7–2.0
  body line-height, larger sizes
- **Fake bold** (browser-synthesized) → mushy letterforms → faces with
  real 700
- **Letter-spacing on Arabic** → breaks joining legibility → spacing
  reserved for Latin kickers only
- **Naskh at display sizes for tech products** → wrong voice → Kufi/sans
  display
- **English punctuation in Arabic copy** (, . ? !) → typographic
  illiteracy signal → ، ؟ ؛ …

## Numbers & mixed content
- **Bidi scrambles** ("!Hello" tails, phone "+966…" fragments) →
  unisolated runs → dir="ltr" spans / bdi / dir="auto" on user content
- **Arabic-Indic digits in prices on mass ecommerce** → scanning
  friction where Western expected → per-market policy, consistent
- **Currency placement drift** (129 SAR / SAR 129 / ر.س 129 mixed) →
  pick per-market convention, tokenize
- **Hijri-only dates on commercial pages** → confusion → Gregorian
  primary (+Hijri secondary where relevant)

## Forms & commerce
- **LTR page fields in RTL flow without dir="ltr"** (email/card/URL) →
  typing chaos → explicit field direction
- **Untranslated error messages** (developer strings) → users blocked
  at failure moments → localized validation copy
- **Address forms demanding postal codes** → much of region uses
  districts not codes → district dropdowns + map pin + free text
- **COD not offered/shown** → measurable conversion loss in EG/SA mass
  market → payment chips pre-checkout

## Trust & content
- **Machine-translated UI** (broken plurals, wrong register) → instant
  credibility drop → professional Arabic copy (this is not optional)
- **Ramadan skin breaking contrast** (gold on green patterns) →
  illegible festive → theming within contrast tokens
- **EN-first IA with AR bolted on** (English categories, Arabic labels) →
  taxonomy mismatch (categories must be natively Arabic where users
  think in Arabic: سيارات not "Cars")
- **One "MENA" variant for all markets** → KSA≠EG≠UAE (payments, tone,
  numerals, dress in imagery) → market-tier localization
