# Input: Touch

Touch is imprecise-but-direct: design fat targets, obvious affordances,
forgiving gestures.

## Targets & spacing

- ≥44pt (iOS) / 48dp (Android) hit areas `[PLATFORM RULE]`; visual
  smaller is fine (hit slop); gaps between targets prevent mis-taps.
- WCAG 2.2 adds a 24×24 CSS px minimum target-size criterion with
  exceptions (inline links, equivalents) `[PLATFORM RULE - WCAG 2.2,
  page blocked from network — standard text]`.
- Thumb ergonomics (devices/mobile.md): primary actions low; deadly
  corners = top-left/right (large phones).

## Press states & feedback

- Design 4 states minimum: default / pressed / disabled / focused
  (RN Pressable ships exactly these `[OBSERVED]`).
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

[ ] all targets ≥44/48 [ ] states designed [ ] gestures have button
twins [ ] edge-gesture collisions checked [ ] keyboards correct per
field [ ] press feedback instant
