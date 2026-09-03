# Device: Mobile (phones)

Mobile is a different design problem, not a small desktop. A phone app
must feel native — never a website squeezed into a phone.

## Physical ergonomics

- **Reach and posture**: lower regions are often easier one-handed, but grip,
  handedness, device size, task, keyboard, assistive technology, and platform
  chrome vary. Place frequent consequential actions where they remain visible,
  safe, and reachable; bottom anchoring is one candidate, not a rule.
- **Touch hit regions:** Apple HIG generally recommends at least 44×44pt
  (its accessibility guidance documents 44×44pt default and 28×28pt
  minimum); Android recommends at least 48×48dp. Visual size may be smaller
  with hit slop; adjacent targets need safe gaps `[PLATFORM GUIDANCE]`.
- Test one- and two-hand postures, switch access, screen readers, external
  keyboard/pointer, and interrupted use where the audience needs them.

## Structural rules

- Minimize steps for top tasks and keep a visible, predictable way back
  (system/platform back + in-app orientation). No universal screen-depth
  number substitutes for task testing.
- Choose bottom destinations, tabs, visible header navigation, drawer, rail,
  sheet, or full-screen task from hierarchy, count/label fit, window size, and
  platform. No fixed destination count replaces testing.
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

Compact but not cramped: select type and columns from font/script metrics,
content, touch targets, text scaling, and item minimums. Truncate only when
the content contract and an accessible full-value path permit it.

## Mobile realism checks

[ ] reach/posture tested [ ] platform-preferred targets [ ] keyboard flows
tested [ ] safe areas respected [ ] back works on every screen
[ ] states designed (offline/loading/error/empty) [ ] deep-linkable
screens survive cold start [ ] task survives relevant postures and inputs
[ ] no web idioms (hover, tiny links, breadcrumbs-for-nav)
