# Page Types: Pricing & Checkout (+ Payment Pages)

## Pricing page

This section applies only when plans/subscriptions or quoted pricing are
KNOWN/REQUESTED. It must not invent tiers, trials, annual billing, enterprise
sales, calculators, discounts, or currencies. Purpose: help the intended
buyer understand eligible offers and trade-offs with honest constraints.

### Candidate modules (select from real offer data)

1. Billing-period/currency controls only when the offer actually varies by
   those dimensions; savings claims come from supplied pricing data
2. Plan columns (3–4 max): name, price (largest number on page), billing
   note ("/user/mo, billed annually"), 1-line audience fit, feature list
   (checked, concrete), CTA; recommendation badges only when backed by a
   defined audience rule or real data
3. Feature comparison table below (dense, honest) for evaluators
4. Trust strip: payment methods, refunds, security, support SLA
5. FAQ: billing questions (what happens when I upgrade, refunds, limits)
6. Sales-assisted path only when it exists in scope

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

This section applies only when a transaction is KNOWN/REQUESTED. Do not add a
cart, account, shipping, promotion, payment method, tax claim, or tracking
capability because it appears in this catalog. Purpose: complete the real
transaction with clear totals, state continuity, and recoverable errors.

### Candidate flow stages (include only required stages)

1. Cart/review: items + editable quantities, promo field, order summary
   sticky (desktop right / mobile bottom sheet), edit links
2. Identity/contact (or login shortcut + guest checkout!)
3. Shipping/delivery method with dates + costs shown HERE
4. Payment: cards, wallets (Apple/Google Pay — one-tap above forms),
   regional methods only when supported by the merchant, processor, and market
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
