# Responsive: Mobile UX Patterns (the phone is the primary context)

Mobile traffic is the majority in MENA (70–90% in many verticals) and near-
majority globally. Design phone-first as the real product, not a port.

## The mobile page contracts

- Viewport height lies: use svh/dvh units (URL bar); 100vh traps content
- Safe areas: notch + home-indicator insets on sticky elements
- One-hand zone: primary actions bottom 60% of screen; destructive/
  secondary top-right (hard to reach accidentally)
- Thumb targets: 44px min, 48–56 preferred; 8px+ separation

## Canonical mobile patterns by job

**Browse**: 2-col grids (commerce/games/media), swipe rails with peek,
pull-to-refresh on feeds
**Search**: sticky search field or persistent search tab; full-screen
keyboard states with search-in-suggestions; recent/saved chips above pad
**Decide**: sticky decision bar (price+CTA), image-first PDPs, specs in
accordions, bottom-sheet comparisons
**Convert**: single-column checkout, wallets above forms (Apple/Google Pay
one-tap), numeric keyboards for OTPs (inputmode), autofill tokens
**Navigate**: bottom tabs ≤5 + hamburger tree; section chips rails;
breadcrumb → back button + page title
**Consume**: article typography 17–18px, media full-bleed, sticky minimal
chrome, reading progress thin
**Operate** (dashboards): card-stacked KPIs, tables → card lists or
scroll+sticky-col, quick-action FAB, offline states visible

## Mobile-specific UX mechanics

- Bottom sheets: drag-handle, snap points (peek/half/full), scrim dismiss,
  Esc-equivalent (back gesture) closes
- Toasts above tab bars; snackbars with action ≤1
- Keyboard: field focus scrolls into view (fixed headers must not cover
  focused inputs — scroll-margin)
- Form UX: correct inputmodes, autocomplete, single-column, inline
  validation, submit button visible with keyboard open
- Performance floor: LCP <2.5s on 4G, tap-responsive <100ms, no
  layout jumps on image/font load

## Mobile RTL specifics

- Swipe directions mirror (carousel next = swipe left→right gesture
  pulls content rightward — native scroll handles automatically with
  RTL containers)
- Drawer opens from right/start; back-gesture still left-edge on iOS/
  Android (system) — don't fight OS gestures
- Numeric pads unaffected; Arabic text fields with LTR data fields
  (card numbers) need dir="ltr" + inputmode

## Anti-patterns

- Hover-dependent UI; tiny text links inline; interstitials before content
- Sticky layers stacking >20% viewport (ad + chat + cookie + CTA bar)
- Carousels without swipe; PDFs as mobile content
- Auto-zoom on input focus (font-size <16px iOS triggers — set 16px+)
