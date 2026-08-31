# Page Type: Article / Long-form Reading

The reading experience: typography IS the interface. Everything else is
furniture.

## Anatomy

1. Kicker/section label (linked) + headline (h1)
2. Standfirst/dek (1–2 sentences, larger muted body)
3. Byline block: author (linked), avatar optional, dual timestamps
   (published / updated — verification readers depend on them), reading
   time
4. Hero media (image/video/embed) + caption + credit
5. Body: measured column (65–75ch), structured with subheads (h2/h3),
   pull-quotes, inline media, fact boxes
6. Tags/topics; author bio card; related reading; newsletter/module gates
7. Progress indicator (top or inline) on long pieces

## Typography rules (the craft)

- Body 18–20px desktop / 17–18px mobile, line-height 1.6–1.7, paragraph
  spacing not indents (web convention)
- Serif body for quality-press register (NYT/Guardian class); sans for
  speed/utility register — both legitimate; commit fully
- Arabic body: Naskh (Noto Naskh/Lateef/Amiri class) 19–21px, line-height
  1.8–2.0 (Arabic ascenders/descenders need more), justify historically
  preferred but ragged-right (start-aligned) increasingly standard
- Headlines: one dramatic step from body (×1.8–2.5); subheads punctuate
  every 3–5 paragraphs
- Captions/credits: small, muted, but ≥12px and ≥4.5:1 — captions carry
  journalistic weight

## Interaction patterns

- Reading progress; text-size controls (quality-press convention)
- Sticky share rail (desktop left/start) / bottom share bar (mobile)
- Deep links on paragraphs (¶ anchors) for reference products
- Live-blog variant: reverse-chron entries with time chips, auto-update
  pill, anchor navigation
- Newsletter inline gates after N paragraphs (respect once-per-user
  frequency caps)
- Comments: on-article (community products) or delegated to social embeds
  (news norm now)

## Media discipline

- Lazy-load below-fold media; no layout shift (aspect-ratio boxes)
- Embeds (posts/video) width-capped to measure; click-to-load third-party
  embeds (performance + privacy)
- Figures numbered for reference (science/legal)

## RTL/Arabic specifics (OBSERVED conventions)

- Byline/dateline RTL with Western digits for dates common (١٥ أغسطس 2025
  or 15 أغسطس — choose per brand, be consistent)
- Quote marks and punctuation flip (Arabic quotes «» or „" usage varies —
  follow regional style guides; «» safest)
- Mixed Latin names inside Arabic text: wrap with dir="ltr" spans or rely
  on dir="auto" paragraphs
- Column width can run wider than Latin reading comfort (Arabic scripts
  scan longer lines acceptably) — still cap ~80ch-equivalent

## Anti-patterns

- Mid-paragraph popovers/interstitials
- Autoplay video with sound adjacent to reading
- Gray-on-gray body text
- Social buttons above the headline
- Removing timestamps (breaks trust for update-sensitive readers)
- Sticky elements covering >15% of mobile viewport while reading
