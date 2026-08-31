# Page Types: Pricing & Checkout (+ Payment Pages)

## Pricing page

Purpose: qualify + convert with transparency. Hidden pricing destroys more
trust than any design gains it.

### Anatomy

1. Header: plan-toggle (monthly/annual with "-20%" badge) + currency
   selector if international
2. Plan columns (3–4 max): name, price (largest number on page), billing
   note ("/user/mo, billed annually"), 1-line audience fit, feature list
   (checked, concrete), CTA; **"Most popular" badge on the target plan**
   (middle-right visual anchor — right column in LTR, start-side in RTL)
3. Feature comparison table below (dense, honest) for evaluators
4. Trust strip: payment methods, refunds, security, support SLA
5. FAQ: billing questions (what happens when I upgrade, refunds, limits)
6. Enterprise strip: "Need more? Contact sales" with a short form

### Rules

- CTA hierarchy per tier: free tier = ghost, popular = filled, enterprise =
  outline "Talk to sales" (ابدأ مجاناً / تحدث مع المبيعات in Arabic)
- Annual default toggle only with visible savings math
- Per-seat calculators for complex pricing (fintech/dev tools)
- Usage/pricing transparency = the differentiator vs "contact us" walls
- Show VAT handling for MENA/EU honestly (incl. vs excl. tax label)

### Mobile

- Plan columns → swipeable cards or stacked (popular first)
- Comparison table → horizontally scrollable with sticky first column, or
  per-plan accordion of features

## Checkout

Purpose: complete payment with zero anxiety. Every field is a chance to
leave; every reassurance is a chance to stay.

### Flow anatomy

1. Cart/review: items + editable quantities, promo field, order summary
   sticky (desktop right / mobile bottom sheet), edit links
2. Identity/contact (or login shortcut + guest checkout!)
3. Shipping/delivery method with dates + costs shown HERE
4. Payment: cards, wallets (Apple/Google Pay — one-tap above forms),
   regionals (mada, STC Pay, Fawry, COD for MENA; iDEAL/SEPA/BLIK for EU)
5. Review → confirm → **confirmation page** with reference number, next
   steps, receipt email note, tracking link when relevant

### Rules

- Show total (incl. shipping/tax/fees) from step 1 — surprise fees = #1
  abandonment
- Progress indicator (steps numbered); back never loses data
- Address autocomplete; correct field directions for mixed content
  (Arabic street + Latin company name → dir="auto" inputs)
- Error kindness: field-level, persistent, actionable ("Card number is
  missing 2 digits" not "Invalid input")
- Payment logos near CTA; security reassurance line under the pay button
- No account forced: guest checkout + post-purchase "save my info" convert
  better than forced registration
- RTL: order summary mirrors; card-number input stays LTR
  (dir="ltr" on number/CVC fields inside RTL page!) — numbers are
  left-to-right data
- COD (MENA): cash-amount preparation hint, exact-change note where
  culturally relevant

### Post-purchase

- Confirmation = reassurance page (what happens next, when, who contacts)
- Upsell only AFTER value is confirmed (post-purchase cross-sell in email,
  not blocking the confirmation)

## Anti-patterns

- Coupon fields that eclipse the CTA; surprise fees at final step
- Forced registration; logout on back-button
- Single-page checkouts that hide totals behind accordions
- Fake timers; removing edit-cart after payment step starts
- Dark "subscription traps" (pre-checked add-ons) — illegal in many markets
