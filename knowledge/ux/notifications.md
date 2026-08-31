# UX: Notifications & Interruptive Messaging

Cross-platform notification UX. Extends ux/states.md (in-flow feedback)
and ux/mobile-states.md (lifecycle). A notification is a PRODUCT
SURFACE, not a system spam channel.

## Value contract (before asking for any permission)

Every notification must pass: RIGHT event · RIGHT moment · RIGHT
detail · clear action path. If a notification only says "come back,"
it trains users to ignore the channel (habituation = channel death).

## Permission UX (mobile) `[PLATFORM RULE]`

Ask in-context AFTER showing value (first useful moment), never at
cold launch; pre-permission priming screen (what + how often + example)
only when the system dialog alone would under-sell; denial path
designed: feature continues degraded, deep-link to settings when user
tries to enable later (ux/mobile-states.md permission rows).

## Notification anatomy (per message)

- **Title**: the event, not the app ("Order out for delivery" not
  "Bosta update").
- **Body**: the delta since last message (new status, new time, new
  info) — never repeat the previous notification.
- **Action buttons** where the platform allows (reply/track/snooze) —
  fewer than 3; deep-link EXACTLY to the relevant screen, never home.
- **Grouping/stacking**: per-thread/per-order threads (e.g., all
  messages about shipment 123 stack) `[PLATFORM CONVENTION]`.
- **Quiet hours + per-category prefs**: channels/categories are the
  user's contract (Android channels `[PLATFORM RULE]`; iOS categories);
  respect DND/schedules; time-sensitive exceptions used sparingly.

## Cadence design (per product type)

| Product | Notify on | Never notify on |
|---|---|---|
| Logistics (logistics-delivery.md) | status changes, driver-en-route, exceptions, delivered | every scan |
| Crypto/finance (crypto-web3.md) | price alerts (user-set), fills, security events | general market noise |
| Islamic apps (islamic-apps.md) | adhan (with per-prayer opt-in), Ramadan times | religious spam — reverence discipline |
| Jobs (jobs-recruitment.md) | application status changes, recruiter messages | "new jobs matching" floods (unless user-tuned) |
| Social | direct interactions | algorithmic engagement bait |

Digests > streams for non-urgent categories (daily summary); breaking
only for genuinely time-critical (security, delivery TODAY).

## Web/desktop notification differences

Web Push: opt-in is harder-earned (browser prompt distrust) — offer
in-site notification center first; email as fallback channel with
preference center. Desktop apps: badge + in-app inbox > OS toasts for
professional tools (attention economics — devices/desktop.md).

## States & recovery

- Tapped notification → deep-linked screen must hydrate context
  (cold-start safe — mobile-states.md).
- Dismissed ≠ done: state lives in the app's inbox/activity feed too.
- Failure to deliver (offline) → sync on reconnect, don't queue-flood.

## Anti-patterns

Pre-ticked boxes · fake notification dots (engagement bait) · vibrating
badge counts as growth hack · notification for content the user will
see in-app in seconds · asking permission at signup.
