# Patterns: Recommendations, Related Content & Sticky Actions

## Recommendation rows/shelves

- **Placement map**: PDP → "similar" + "frequently bought together" +
  "recently viewed"; article → related by topic + read-next sequential;
  streaming → "because you watched" after continue row; dashboard →
  suggested actions
- **Anatomy**: labeled rail (h2 or rail header with "See all" link) +
  horizontal scroll cards (240–320px) with peek + arrows; 6–12 items;
  lazy-render below fold
- **Labeling honesty**: "Recommended for you" only when personalized;
  else "Popular in [context]" / "الأكثر مبيعاً" (best sellers — MENA
  marketplaces standard), "New arrivals"
- **Why-not logic**: show a "why this?" tooltip on rec cards where the
  algorithm allows (trust pattern, advanced)

## Related content lists

- Editorial: 3–5 link-lists with kicker+headline+time (no images needed);
  topic-tagged ("More in футбол/كرة القدم")
- Ecommerce bundle rows: "Complete the look/setup" with add-all CTA
- Docs: "Next steps" + "See also" (sequential + lateral, both)

## "Recently viewed" rails

- localStorage (privacy-friendly default, no login); 8–12 items;
  dismissible row; appears after ≥2 views (empty before that — no fake data)

## Sticky action patterns

- **Sticky mobile buy bar** (PDP): price + variant shortcut + primary CTA;
  appears after decision block scrolls out; 56–64px + safe-area
- **Sticky filter bar** (results): appears when top filter rail exits;
  shows applied chips + "Filters" button + result count
- **Sticky table header/column** (data): pure CSS position sticky
- **Sticky chat/WhatsApp bubble**: bottom-start corner, 56px target,
  delay appear (3–5s or scroll-depth), closeable + remembers dismissal
  (MENA: WhatsApp bubble is a conversion standard — visible number builds
  trust)
- **Scroll-to-top**: appears past 2 viewports; 40–44px target

## Sticky budget rules

- Mobile: one sticky system max (buy bar OR chat, not stacked layers);
  never cover >20% viewport; safe-area respected
- Desktop: header + one sub-nav OR header + sticky sidebar
- Every sticky element needs an exit (dismiss, scroll-top, or context end)

## Toast/inline confirmation for quick actions

- Add-to-cart: cart badge bump + toast with "View cart" (context stays)
- Save/wishlist: heart fill animation ≤300ms + accessible announcement

## RTL

- Rails scroll RTL (snap handles); arrows flip; sticky bars mirror CTA
  position; WhatsApp bubble sits bottom-start (left in RTL) — follow
  regional app conventions (most sit start-side)

## Anti-patterns

- "You may also like" with random items (label lies = trust dies)
- Sticky bars that cover content with no dismissal
- Rec rails above the primary content (cart before product!)
- Infinite related sections burying the footer (cap at 2–3)
- Chat bubbles that re-open on every page after dismissal
