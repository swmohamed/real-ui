# Apple Evidence Recovery Tests (run 2026-08)

Validates the Apple recovery pass: Apple-specific conventions used
appropriately, no generic-web iOS, no Android-on-Apple, no unsupported
"Apple requirements", cross-platform principles intact.

## Scenarios (10)

### 1. iOS application
Retrieval: platforms/{swiftui,uikit} + devices/mobile + a11y/mobile.
Reasoning trace: NavigationStack/detents/large-titles cited as APPLE
OFFICIAL; tab count stays DESIGN PRINCIPLE (not claimed as rule);
bottom sheets over center modals. **PASS** — iOS DNA, no web idioms.

### 2. iPadOS application
NavigationSplitView official two/three-column quote applied; devices/
tablet.md panes-not-stretching + density upgrade; iPad split ≠
stretched phone. **PASS**

### 3. SwiftUI application
sheet→fullScreenCover ladder with detents vocabulary (official);
Form/List official containers for data entry/settings; toolbar actions
not floating web buttons. **PASS**

### 4. UIKit application
UINavigationController stack + prefersLargeTitles; UITabBarController
multiselection (official); UISheetPresentationController detents;
UIFontMetrics for brand fonts. **PASS**

### 5. iOS accessibility
Dynamic Type via dynamicTypeSize/UIFontMetrics (official) to
accessibility sizes; VoiceOver traits/actions vocabulary (WWDC23
official); isReduceMotionEnabled gating motion (official). **PASS**

### 6. iPad adaptive layout
NavigationSplitView leading-column→subsequent-column semantics
(official) + window-class reasoning (adaptive-models.md). **PASS**

### 7. Apple navigation patterns
Push (stack) vs tabs vs split vs sheet — each with official anchor or
explicit DESIGN PRINCIPLE label; back = chevron+swipe stays principle
(not fake-ruled). **PASS**

### 8. Apple + RTL
semanticContentAttribute official (flip-decision mechanism); .playback
official case = media controls stay LTR; SwiftUI LayoutDirection
official; directional-vs-semantic table (rtl/cross-platform.md) intact. **PASS**

### 9. Apple + Dynamic Type
Scaling through accessibility sizes; truncation policy per class;
contrast pairs ≥4.5:1 kept; never global clamp. **PASS**

### 10. Apple + cross-platform design system
SwiftUI/UIKit files slot into design-systems/cross-platform.md layer
model; platform-behavior law (back, sheets, Dynamic Type) overrides
pixel-parity; traveler test intact. **PASS**

## Guard checks

| Check | Result |
|---|---|
| iOS ≠ generic web UI (sheet/detent/stack idioms enforced) | PASS |
| No Android conventions forced onto Apple (Material chips/FAB/snackbar absent from Apple files) | PASS |
| No unsupported "Apple requirement" claims (Apple-prose items stay DESIGN PRINCIPLE, listed in research log) | PASS |
| Apple facts traceable to DocC/WWDC evidence files | PASS (raw/apple/, 19 JSONs + transcript) |
| Cross-platform shared principles preserved | PASS |
| Unrelated V2.1 knowledge untouched | PASS (only 6 files extended) |

## Verdict

APPLE EVIDENCE RECOVERY COMPLETE (pending final reinstall verify — see
run log below).
