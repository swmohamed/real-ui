# Cross-Platform Design Systems (one system, native expression)

Companion to design-systems/tokens.md (web tokens). Goal:
CONSISTENT BRAND + NATIVE EXPERIENCE (platforms/cross-platform.md).

## Layer 1 — Shared product tokens (identical everywhere)

| Token group | Shared definition |
|---|---|
| Color roles | canvas, surface, primary text, secondary text, accent, action, success/warn/danger — role names stable; VALUES may shift slightly for platform text rendering/dark mode, hierarchy must not |
| Type ramp | display/headline/title/body/caption/mono steps with hierarchy ratios fixed; families can differ per platform (SF vs Roboto vs brand font) if ratios/weights parallel |
| Spacing scale | 4pt base (4/8/12/16/24/32/48/64) |
| Radius family | same steps (e.g., 4/8/16/24 + pill), mapped to component classes identically |
| Elevation philosophy | levels + WHEN to elevate (same semantics); visual execution per platform (web shadow / iOS no-shadow-layering / Android tonal elevation) |
| Motion | durations + easing personality shared; curves may match platform defaults (iOS spring vs Android emphasized) |
| Iconography | one set, one style; directional handling per rtl/cross-platform.md |

## Layer 2 — Semantic components (parity with native accent)

Define each component ONCE semantically (a Button has: label, action,
size, emphasis, state set) then map per platform:
- Button: web `<button>` variants · iOS bordered/filled (UIKit
  configuration / SwiftUI buttonStyle) · Android FilledButton (M3)
- List row: web table/list · iOS List row (chevron, swipe actions) ·
  Android LazyColumn row (long-press, checkbox state)
- Sheet: web dialog/drawer · iOS sheet with detents · Android bottom
  sheet with peek
- Feedback: web toast/banner · iOS alert/snackbar-equivalent ·
  Android snackbar + FAB synergy
- Selection: web checkbox/radio · iOS UISwitch/SwiftUI Toggle ·
  Android Switch (M3) — SWITCH SEMANTICS stay, look native.

## Layer 3 — Platform divergence (deliberate, documented)

Divergences allowed ONLY for: platform interaction law (system back,
gesture nav, Dynamic Type, edge-to-edge), or a platform-native pattern
that beats parity (snackbar-undo vs confirm dialogs on Android).
Document divergence in the system's "platform deltas" page — future
agents/designers must know it's intentional, not drift.

## Governance rules

1. Tokens are code (theme files), not wiki tables — single source per
   platform generated from one spec.
2. Component naming shared (semantics), file naming per platform
   conventions.
3. New component enters ALL platforms or is marked platform-specific
   with reason (e.g., iOS-only context menu).
4. QA per platform after token changes (tests/v2-quality-gate.md
   cross-platform realism).

## Multi-platform token QA

[ ] one spec, N implementations [ ] type hierarchy parallel across
platforms [ ] color roles semantically identical [ ] radius/spacing
scales exact [ ] elevation semantics equal [ ] motion personality
consistent [ ] divergences documented + intentional
