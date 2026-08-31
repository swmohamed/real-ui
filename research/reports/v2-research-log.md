# V2 Research Log (upgrade research — 2025-08)

Honest record of every fetch behind the V2 upgrade. Labels follow
SKILL.md source classes: OBSERVED / PLATFORM RULE / DESIGN PRINCIPLE.

## Official documentation (fetched OK → OBSERVED source)

| Source | URL | Status | Used in |
|---|---|---|---|
| Flutter — adaptive & responsive | docs.flutter.dev/ui/adaptive-responsive | 200, 132KB | platforms/flutter.md, responsive/adaptive-models.md |
| Flutter — layout | docs.flutter.dev/ui/layout | 200, 398KB | platforms/flutter.md (constraints rule) |
| Flutter — Material | docs.flutter.dev/ui/material | 200, 131KB (redirect target of ui/material-3) | flutter.md (useMaterial3, M2 deprecation) |
| Flutter — web | docs.flutter.dev/platform-integration/web | 200, 138KB | flutter.md web caveats |
| Android — adaptive layouts | developer.android.com/develop/ui/compose/layouts/adaptive | 200 (consent cookie flow), 364KB | jetpack-compose.md (NavigationSuiteScaffold, ListDetailPaneScaffold) |
| Android — large screens | developer.android.com/guide/topics/large-screens/support-different-screen-sizes | 200, 377KB | android.md (sw≥600dp), adaptive-models.md |
| Android — Material 3 Compose | developer.android.com/develop/ui/compose/designsystems/material3 | 200, 466KB | jetpack-compose.md (MaterialTheme, dynamic color, M3 Expressive) |
| React Native docs (official source repo react/react-native-website, main branch, docs/) | raw.githubusercontent.com — accessibility, intro-react-native-components, platform-specific-code, keyboard, keyboardavoidingview, pressable, optimizing-flatlist-configuration | 200 ×7 | platforms/react-native.md |

reactnative.dev itself: network-blocked from this machine (timeouts);
GitHub official source used instead — same content, authoritative.

## Blocked / JS-walled (facts labeled DESIGN PRINCIPLE, never OBSERVED)

| Source | Status | Handling |
|---|---|---|
| Apple HIG (layout, navigation, typography) | 200 but JS-only shell (155 visible chars) | swiftui.md / uikit.md use [DESIGN PRINCIPLE] labels; conventions cross-stable |
| m3.material.io adaptive pages | JS shell (51 chars) | window-class cutoffs cited as documented standard in jetpack-compose/adaptive-models |
| W3C WCAG 2.2 (w3.org/TR/WCAG22) | 403 bot-wall | WCAG facts cited as [PLATFORM RULE] with note; exact criterion texts verifiable via any mirror |
| web.archive.org fallbacks | 404/unreliable for JS pages | — |

## New-industry product research (pipeline: tools/fetch_analyze.py)

Raw: raw/v2_industry_products.json · batch: raw/v2_industries.json

| Site | Status | CSS bytes | Key evidence |
|---|---|---|---|
| quran.com | ok | 496,936 | UthmanicHafs + Kitab + Newsreader + Figtree; bp 768/1024 |
| islamicfinder.org | ok | 40,538 | Red Hat Display + Roboto + Noto Naskh Arabic |
| muslimpro.com | ok | 9,790 | WordPress utility framing |
| bayt.com | ok | 218,529 | Roboto + Vazirmatn bilingual stack; bp 1023/1024 |
| wuzzuf.net | ok | 49,371 | Open Sans + IBM Plex Sans Arabic; Bootstrap bp set |
| kraken.com | ok | 430,746 | IBM Plex Sans + Kraken Plex Mono + brand faces; bp 768/640 |
| coinbase.com | ok | 228,742 | --cds- tokens; bp 1280/1600 |
| bitoasis.net | ok | 450,450 | Bootstrap + Open Sans (MENA) |
| rain.bh | ok | 119,417 | Suisse Intl + Tiempos serif (→ rain.com redirect) |
| aramex.com | fetch_failed | 0 | bot-wall — logistics-delivery.md labeled honestly |
| dhl.com | fetch_failed | 0 | bot-wall — same |
| linkedin.com/jobs | ok, 0 CSS | 0 | login wall — not used as CSS evidence |

## Method integrity

- No knowledge written from model memory alone where a fetch was
  possible; blocked sources are labeled and confined to stable,
  verifiable conventions.
- Apple/M3/WCAG pages were NOT counted as observations anywhere.
- All industry DNA claims above trace to the JSON evidence files.
