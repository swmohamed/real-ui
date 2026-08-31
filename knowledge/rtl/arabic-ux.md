# Arabic UX: Cultural & Regional Conventions (beyond direction)

Arabic/MENA UX differs in content, trust, commerce, and rhythm — not just
mirroring. Grounded in observed regional products + market conventions.

## Content & language

- **MSA (فصحى) for UI copy** — formal register is the interface norm;
  dialect (مصري، خليجي، شامي) for marketing warmth/social voice — pick
  per brand, consistently
- **Bilingual hierarchy**: decide lead language per market (Saudi-first,
  Egypt-first, or EN-first for expat-heavy UAE segments); language toggle
  ع/EN must be ≤2 taps and preserve current page
- **Copy length**: Arabic runs shorter in characters but allocate similar
  or +1 line-height space; buttons sized for Arabic labels (سجل الآن)
- **Punctuation**: Arabic comma (،), question mark (؟), semicolon (؛) —
  localize, don't transliterate
- **Numerals policy**: Western digits dominate prices/data/scores in the
  observed corpus; Arabic-Indic (٠-٩) in Egypt-consumer contexts and
  formal government content; be consistent within a product

## Numbers, dates, currency

- Currency: SAR ر.س / AED د.إ / EGP ج.م / KWD د.ك — with correct decimal
  conventions (KWD/BHD 3 decimals!)
- Placement: commonly after amount (129 ر.س) — match per-market leader
  convention
- Dates: Gregorian + optional Hijri side-by-side for official/religious
  contexts; Arabic month names (يناير/كانون الثاني varies by country —
  target-market style); relative time منذ ساعتين
- Phones: +966/+971/+20/+974/+965/+962 formats; LTR fields; WhatsApp-
  deep links standard (wa.me)

## Commerce conventions

- **COD (الدفع عند الاستلام)** remains a major payment method — chip it
- Local wallets/cards: mada (KSA), STC Pay, Fawry (EG), Benefit (BH),
  KNET (KW); BNPL (Tabby/Tamara) shown pre-checkout
- Installments/تقسيط display on high-ticket items
- Delivery expectations fast + time-slotted; district-level addressing
  (no postal-code culture in much of the region — free-text areas +
  map pins)
- Returns: generous + Arabic-clear policy near price

## Trust & social conventions

- WhatsApp as primary support channel (number visible = trust)
- Family/group plans, multiple-line cart items common in telecom
- Religious calendar moments: Ramadan (night-peak traffic — schedule
  promo timing!), Eid gifting hubs, Hajj seasons — IA and theming events
- Formality: honorifics in support copy, formal plural addressing
  (أنتم-register) for brand voice in conservative segments
- Government/regulator references: licenses, ministry logos where real
- Modesty conventions in imagery per market (Gulf stricter; Lebanon/Egypt
  more relaxed) — respect in stock-photo selection (driving side, dress,
  prayer-room facility lists in venues)

## Regional market notes

- **KSA**: largest e-commerce momentum; Vision-2030-adjacent brands lean
  modern-bold; Founding Day/Flag Day theming; Absher-class app-first
  government UX expectations
- **UAE**: most bilingual-expat market (EN+AR parity essential); Dubai
  Font institutional presence; premium design expectations highest
- **Egypt**: price-sensitive mass market; COD critical; Fawry ubiquity;
  dialect-friendly voice performs
- **Qatar/Kuwait**: high ARPU; bilingual; KNET/Benefit payment specifics
- **Jordan/Levant**: strong dev-community products (Edraak-class);
  cost-conscious but quality-tolerant

## SEO/IA regional notes

- Arabic URLs: translated slugs (/ألعاب/) vs transliterated
  (/al3ab/) vs Latin (/games/ar/) — translated ranks better for Arabic
  queries; transliteration legacy survives in gaming (al3ab = "games"
  search term itself!)
- hreflang pairs ar/en (+ ar-XA variants if market-differentiated)
- Search normalization expectation: users type with/without diacritics,
  alef variants — server-side normalization is UX

## Anti-patterns

- English UI machine-translated to Arabic with broken plurals (Arabic
  has broken plurals — professional copy is non-negotiable)
- Direction flipped but iconography/semantics unflipped
- Ramadan theme skin that breaks contrast (festive ≠ illegible)
- Treating "MENA" as one market (KSA ≠ Egypt ≠ UAE in payment, tone,
  imagery, price display)
- Gregorian-only calendars for religious-season products
