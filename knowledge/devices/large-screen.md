# Device: Large Screens, TV, Wearables

## Large desktop / ultrawide (>1600px)

- Content bands hold (1120–1440) + secondary rails/panels absorb width
  (corpus OBSERVED — coinbase 1600 breakpoint as example).
- Power surfaces go full-bleed: editors, timelines, trading, dashboards.
- Danger: stretched type lines (>90ch), wallpaper dead zones, center-
  lonely content. Fix: rails, related content, denser grids.

## TV (10-foot UI)

- Distance viewing: min 24px body (think 2× web scale), high contrast,
  chunky focus states — navigation is FOCUS-DRIVEN (d-pad/remote):
  every element focusable in a sane 2D grid order.
- No hover, no precise pointing: focus replaces it (visible focus ring
  = the interaction star; overscan margins).
- Media-first layouts: poster walls, hero player, minimal text chrome.
  Android TV/XR are official Android targets `[OBSERVED - docs list]`.
- Simplified input flows (no forms if avoidable; OAuth codes on
  another device for login — real TV pattern).

## Wearables (watch)

- Glanceable seconds: single data point + one action per screen;
  complications = widget vocabulary.
- Tiny canvas: no scrolling walls of text; haptic + voice in/out;
  interactive complications deep-link to phone app (companion model:
  watch = extract, phone = full surface).
- Design honestly: only surface what survives a 2-second glance
  (timers, prayer next-time, price alerts, message triage).

## Shared rule

Unusual devices don't get "the website, smaller/larger" — they get the
subset/superset of the product that fits the device's glance/time/
input budget. Ask: what does a user do HERE in THIS context?
