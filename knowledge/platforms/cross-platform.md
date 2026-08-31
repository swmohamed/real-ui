# Cross-Platform Products (one product, native everywhere)

Rule: **CONSISTENT BRAND + NATIVE EXPERIENCE** — never pixel-identical
clones, never one generic design everywhere.

## Shared product language (must be identical)

Color roles · type ramp (families may vary slightly per platform for
text rendering, hierarchy must match) · spacing scale · radius family ·
elevation philosophy · iconography style · motion personality ·
component SEMANTICS (a "card" means the same thing everywhere) · brand
voice/microcopy · information architecture (same tasks, same order).

## Platform-specific expression (must be native)

| Concern | Web | iOS | Android |
|---|---|---|---|
| Primary nav | header nav / sidebar | tab bar (2–5) | bottom nav / drawer / rail |
| Secondary screen | route/page | sheet or push | sheet or destination |
| Back | browser back | nav-back chevron+swipe | system back (gesture/button) |
| Row actions | visible controls | swipe actions | long-press/checkbox + snackbar undo |
| Primary action | button in flow | nav-bar trailing button / FAB-no | FAB or bar button |
| Feedback | toasts/alerts | alert/sheet | snackbar/banners |
| Hover | designed (web.md) | none (pointer on iPadOS exists — progressive) | none (desktop-Android: progressive) |
| Keyboard | shortcuts expected | hardware rare | hardware rare |
| Density | high ceiling | low-medium | low-medium (+large screens higher) |

## Decision procedure

1. Define the product's semantic components + tokens ONCE
   (design-systems/cross-platform.md).
2. Map each component to native idioms per platform (table above +
   platforms/*).
3. Where idioms conflict with brand irreconcilably → brand wins for
   look, platform wins for behavior (users can't unlearn system back,
   but they can accept a brand-colored FAB).
4. Test the "traveler test": a user switching phone OS should feel
   "same product, local accent" — not "different product" nor
   "clearly an Android app on my iPhone."

## Failure modes to catch in QA (tests/v2-quality-gate.md)

- Web page squeezed into phone · Android UI on iOS (back chevron
  misuse, Material shadows on iOS) · iOS UI on Android (center modals
  everywhere, no back support) · desktop squeezed into mobile · one
  generic design everywhere · brand drift (two products, same team).
