# Mobile States (the full lifecycle, not just loading)

Mobile UIs live through interruptions. Every screen must define its
behavior in each state BEFORE polish. Extends ux/states.md (web states).

## App-level states

| State | Design contract |
|---|---|
| First launch / onboarding | value-first (1 screen of value before any ask); skippable; progress visible (ux/onboarding.md) |
| Permission requests | context-first: ask in-context with purpose, never cold on launch; denial path designed (feature degrades gracefully, settings deep-link) |
| Offline | honest indicator + cached content + queued actions visible ("will send when online") — never fake success |
| Poor network (2G/3G) | progressive load (structure→text→media), timeouts with retry, image downscales, skeletons not spinners |
| Background→foreground | restore exact state (scroll, input, media position); refresh quietly, don't reset |
| Interrupted interaction | call/app-switch mid-form/mid-payment: state survives; resume affordance |
| Update available / forced | non-blocking notice unless breaking |

## Screen-level states

- Loading: skeletons mirroring real layout; never blank.
- Loaded-empty: teach + first action (create/import/explore) — empty
  states are onboarding, not apologies.
- Error: what failed, why (human words), retry, support escape; forms
  keep user input on failure.
- Success: confirm + next step (receipt, continue, share) — success
  is a step, not a dead end (ux/trust-conversion.md).
- Partial degradation: feature flags, per-module offline/error.

## Mobile-specific mechanics

- Pull-to-refresh on list tops (with timestamp of last update where
  freshness matters — news/prices) `[PLATFORM CONVENTION]`.
- Keyboard open/closed: layout shifts sanely, submit reachable, error
  visible above keyboard, scroll-to-focused (platforms/react-native.md).
- Deep link / notification cold-start: ANY screen as entry — context
  (nav, back target) reconstructed, never orphan screens.
- Optimistic UI: like/save/reorder apply instantly, reconcile quietly;
  conflicts surface honestly (payment ≠ optimistic).
- Haptics as state feedback (success/error ticks) — subtle, not
  arcade.
- Learning-specific interruptions: restore playback position, current
  card, or live-class join; queued downloads must show progress and not
  fake completeness; camera/mic for scan or speech asks in context with
  a non-camera path (`industries/education.md`). Offline is common on
  LMS and catalog apps and rare on live-only tutor calls.
- Dual-role products: rider and driver (Uber vs Uber Driver listings),
  guest and host, shopper and seller often ship as **separate apps**,
  not a mode switch. Camera, GPS, and background location belong to the
  role that captures or navigates (`ux/roles-surfaces.md`). Files and
  chat listings claim offline, camera, backup, and calls — those are
  store claims, not in-app layout.

## State matrix exercise (do it per screen)

rows = states above, cols = screens → fill every cell. Empty cells are
bugs found before code, not after.

## QA

[ ] every state designed per screen [ ] offline path real [ ]
permission denials graceful [ ] interruption survival tested (form,
payment, media) [ ] cold-start into deep screens works [ ] PTR where
expected [ ] inputs survive errors
