# Content Design (labels, CTAs, microcopy)

Structure is half the interface; the words are the other half. Generic
copy ("Learn more", "Submit", "Oops! Something went wrong") marks output
as template-made faster than any gradient. Label: RECOMMENDED method.

## Voice & register (decide once per product)

| Register | Fits | Example |
|---|---|---|
| Institutional | finance, government, healthcare trust surfaces | "Your statement is ready." |
| Product-professional | B2B, SaaS, dev tools | "Deploy queued — ETA 40s." |
| Direct/warm | consumer, food, lifestyle | "Your order's on its way." |
| Playful | gaming, social, creative — ONLY where brand briefs it | "Boss defeated." |

Register follows the product model (foundations/product-modeling.md)
and industry trust bar — never the designer's mood. Arabic: register
maps to MSA vs dialect choice (rtl/arabic-ux.md) — default MSA for
product UI, dialect only for consumer-casual brands.

## Labels

- Navigation = nouns (Settings, Orders, مواعيد). Actions = verbs
  (Save order, احفظ الطلب). Never swap.
- Say the object: "Add payment method" > "Add". "Delete invoice" >
  "Delete". One-word labels only where context is physically adjacent.
- Buttons: verb + object, sentence case, ≤3 words. Not "Submit" —
  what happens? "Send invite" / أرسل الدعوة.
- Menu items parallel in grammar (all nouns or all verb-phrases).
- Truncate never at design time: write the real longest label
  (implementation: ellipsis + full text in title/tooltip).

## CTA verbs by intent (replace generic "Get started" everywhere)

| Intent | Verbs | Avoid |
|---|---|---|
| Signup/commitment | Create account · Start free · Book a demo | Submit · Continue |
| Transactional | Order · Book · Reserve · Donate | Get · Go |
| Content | Read · Watch · Listen · Explore | Learn more (only for genuine explainers) |
| Tool/app | Try the builder · Run analysis | Click here |
| Download/leave | Get the app · Open console | — |

Primary CTA = the product's ONE main verb (its top task). Secondary
actions get quieter verbs + quieter styling. Bilingual AR/EN: verify
the Arabic CTA is a real verb form, not a transliteration.

## Error copy (formula: what happened + why + the fix)

```
[What] couldn't [complete action].
[Why — one honest clause, no blame.]
[Fix: action to retry / link / auto-retry note.]
```
- "Payment failed. Your card was declined (code: do_not_honor). Try
  another card or contact your bank."
- Never: "Error 500", "Oops!", "Something went wrong" alone, jokes in
  error paths, or blame ("You entered").
- Field errors: say the fix — "Enter a phone number like 0100 123 4567",
  not "Invalid input". Keep the user's input.
- Destructive confirmations: name the object + consequence + undo path
  ("Delete invoice INV-204? This can't be undone." / Delete in red).

## Empty / loading / success copy

- Empty (ux/states.md): what is this + why empty + one action —
  "No invoices yet. Create your first invoice." لا توجد فواتير بعد.
- Loading: honest scope — "Loading today's schedule…" beats spinners
  with no text; skeletons for structure, text for time.
- Success: confirm the OUTCOME, not the click — "Your booking is
  confirmed for Tue 10:00" (email sent / reference code).

## Onboarding & instructional copy

- Value before account: one sentence of what the product does, in its
  register, using its top task verb.
- Steps: ≤5, each named by outcome ("Add your menu"), skip path visible.
- Tooltips/empty-state hints: one sentence, dismissible, shown at the
  moment of need — not tours that block the interface.

## Bilingual notes (with rtl/*)

- Design with real copy in every target language. When translations are not
  yet available, use the synthetic expansion budgets in localization/i18n.md
  to stress-test buttons and navigation, then replace them with real strings.
- Preserve the same capability and task coverage across languages; content
  order, grouping, examples, and emphasis may adapt when language research or
  local mental models justify it. Do not silently remove capabilities.
  Numerals policy per market (Western vs
  Arabic-Indic — rtl/global-vs-arabic.md).

## Anti-patterns

- "Learn more" as universal CTA · "Submit" everywhere · "Click here"
- Robot positivity ("Awesome! Your file was uploaded!!")
- Marketing voice inside app workflows (workspace ≠ landing page)
- ALL-CAPS long labels (readability + RTL never all-caps — Arabic has
  no case; use weight/color for emphasis instead)
- Transliterated UI terms where native equivalents exist
  (تنبيه not "نوتيفيكيشن")

Connects: ux/states.md (structural states) · ux/forms-validation.md
(field-level) · industries/* (terminology + trust register) ·
localization/i18n.md (length + formats).
