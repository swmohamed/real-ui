# Industry: Islamic Apps (Prayer, Quran, Ramadan, Hijri)

A PRIMARY MENA industry, not a niche. Evidence: v2 fetch 2025-08
`[OBSERVED]` — quran.com (gold standard), islamicfinder.org,
muslimpro.com.

## Observed design languages

- Quran.com: **dedicated mushaf typography** — UthmanicHafs script for
  Quranic text + Kitab + Newsreader (serif reading) + Figtree (UI);
  768/1024 breakpoints `[OBSERVED]`. Role-split fonts = the whole
  design lesson: scripture ≠ UI text.
- IslamicFinder: Red Hat Display + Roboto + Noto Naskh Arabic fallback
  `[OBSERVED]` — utility-first scheduling face.
- MuslimPro: conventional utility app framing, WordPress-era site
  `[OBSERVED]`.

## DNA rules

1. **Quranic text is sacred content class**: dedicated script
   (Uthmanic/Amiri/Noto Naskh/Mushaf fonts), generous line-height,
   justify per mushaf tradition, ayah-end markers, surah headers as
   ornaments. NEVER generic sans for Quranic text.
2. **Time is the hero**: prayer-times widget = homepage's primary
   content (next prayer countdown, not a dashboard) `[OBSERVED - all
   three leaders]`; location-first UX; times in BOTH Arabic-Indic and
   Latin digits option.
3. Hijri calendar co-present with Gregorian (home + date pickers);
   Ramadan mode = seasonal IA shift ( fasting timer, iftar/imsak
   schedules, tarawih content) `[OBSERVED - seasonal nav on leaders]`.
4. Qibla = sensor-experience: compass screens designed for calibration
   states (device flat提示, magnetic interference warning), map fallback.
5. Audio (recitation): player with reciter picker, per-ayah repeat
   (learning loop), background play + lock-screen controls (mobile
   states — ux/mobile-states.md).
6. Calm, respectful motion; adhkar/dhikr counters (tap haptics);
   content accuracy trust (Quran text verified, translations credited
   — source attribution visible `[OBSERVED - quran.com credits]`).

## Key flows

- Home = prayer card + next-prayer progress ring + hijri date + verse-
  of-day + quick tiles (quran/qibla/adhkar).
- Quran reader: surah list → reading view (mushaf page mode vs list
  mode `[OBSERVED - both exist on quran.com]`), tajweed coloring
  toggle, translation side-by-side, bookmark/last-read resume (state
  survival — mobile lifecycle).
- Prayer details: calculation method + juristic setting (these change
  times! — expose honestly), notifications per prayer (silent vs
  adhan modes), location management (travel mode).

## MENA/global notes

Arabic-first with English UI for global ummah; Tajik/Urdu/French/
Indonesian translations = content, not just locale; mosque finder
(nearby + prayer times + juma times); dua/adhkar collections with
category browsing; no imagery of animate beings in decorative art —
geometric/calligraphic ornament vocabulary (cultural design literacy).
