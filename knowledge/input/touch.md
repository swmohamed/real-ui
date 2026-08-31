# Input: Touch

Touch is imprecise-but-direct: design fat targets, obvious affordances,
forgiving gestures.

## Targets & spacing

- Prefer ≥44×44pt hit regions on Apple platforms (HIG guidance; Apple
  accessibility documentation distinguishes 44×44pt default from 28×28pt
  minimum) and ≥48×48dp on Android. Visual bounds may be smaller with hit
  slop; gaps between targets prevent mis-taps `[PLATFORM GUIDANCE]`.
- WCAG 2.2 adds a 24×24 CSS px minimum target-size criterion with
  exceptions (spacing, inline links, equivalent control, user-agent sizing,
  essential presentation) `[PLATFORM RULE — WCAG 2.2 official Understanding
  page checked 2026-08]`.
- Thumb ergonomics (devices/mobile.md): primary actions low; deadly
  corners = top-left/right (large phones).

## Press states & feedback

- Design applicable default / pressed / disabled / focused states. React
  Native Pressable's current `style` callback directly supplies `pressed`;
  other states come from callbacks or surrounding component state.
- Instant visual response on press (<100ms feel); ripple/Material or
  scale/opacity — pick per platform dialect.
- Long-press = power gesture (context menus, multi-select) — always
  paired with a visible alternative path (discoverability).

## Gestures (vocabulary + discoverability)

Standard set: tap, long-press, swipe (list actions / paging / back-edge
— platform-consistent), pull-to-refresh (list tops), drag (reorder —
with handles), pinch (zoom media/maps), double-tap (like/zoom).
- Every gesture needs a non-gesture twin (button, menu item).
- First-run hints OK; persistent coach-marks = smell.
- Edge gestures must not collide with system gestures (Android back
  edge, iOS home indicator).

## Form input on touch

- Right keyboard per field (email/numeric/tel input modes) — OS-level
  contract `[PLATFORM RULE]`.
- One-hand reach for submit; inline validation near field; error
  visible above keyboard; autocomplete where possible.

## Touch QA

[ ] platform target guidance and WCAG web floor checked [ ] states designed [ ] gestures have button
twins [ ] edge-gesture collisions checked [ ] keyboards correct per
field [ ] press feedback instant
