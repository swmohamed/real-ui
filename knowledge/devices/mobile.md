# Device: Mobile (phones)

Mobile is a different design problem, not a small desktop. A phone app
must feel native — never a website squeezed into a phone.

## Physical ergonomics

- **Thumb zone**: bottom of screen = easiest reach. Primary actions
  bottom-anchored (bottom nav, thumb-reach CTAs, FABs). Top corners =
  worst zone (large phones) — nothing critical there.
- **Touch hit regions:** Apple HIG generally recommends at least 44×44pt
  (its accessibility guidance documents 44×44pt default and 28×28pt
  minimum); Android recommends at least 48×48dp. Visual size may be smaller
  with hit slop; adjacent targets need safe gaps `[PLATFORM GUIDANCE]`.
- One-hand use: navigation + primary actions within thumb arc;
  two-hand patterns (keyboards, carousels) acceptable for input tasks.

## Structural rules

- Minimize steps for top tasks and keep a visible, predictable way back
  (system/platform back + in-app orientation). No universal screen-depth
  number substitutes for task testing.
- Bottom nav (3–5) for top-level modes; tabs for sibling content;
  sheets for focused tasks; full-screen for immersive only.
- Content scrolls; chrome (header/nav) stable or purposefully reactive
  (collapse-on-scroll with return affordance).
- Avoid hover-dependent anything; large hit areas; gesture
  discoverability (visual handles, hints, first-run coaching).

## System realities (design for all of them)

Safe areas/notches/home indicators · status bar legibility · keyboard
opens (layout shifts, input visibility, dismiss paths — see
ux/mobile-states.md) · orientation changes (portrait default; landscape
supported or deliberately locked with reason) · permissions (context-
first requests) · notifications & deep links (cold-start into any
screen) · app lifecycle (interruptions: calls, switcher, background —
state must restore) · offline & poor network · battery/haptics.

## Density & type

Compact but not cramped: 16px body baseline common (corpus mobile
patterns — responsive/mobile-patterns.md); fewer columns (1–2);
truncate with intent; Arabic mobile type ≥ Latin (Arabic needs slightly
larger sizes for equal legibility — typography/arabic-typography.md).

## Mobile realism checks

[ ] thumb-reach primary actions [ ] 44/48 targets [ ] keyboard flows
tested [ ] safe areas respected [ ] back works on every screen
[ ] states designed (offline/loading/error/empty) [ ] deep-linkable
screens survive cold start [ ] one-hand navigation possible
[ ] no web idioms (hover, tiny links, breadcrumbs-for-nav)
