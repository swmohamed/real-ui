# real-ui

**Real-world web + mobile UI/UX design intelligence for AI coding agents.**
Grounded in live research on real products — not generic design theory, not
template aesthetics.

> Designed, not generated · Real, not demo-like · Original, not copied ·
> Product-aware, not template-driven · Native, not forced · Implementable,
> not just pretty.

---

## What it does

When your agent designs, redesigns, reviews, or builds any interface — for
any industry or region, including Arabic/MENA/RTL — this skill makes it
behave like a senior product designer instead of a template assembler:

- **Classifies the task** (industry × platform × device × audience × language)
- **Retrieves only relevant knowledge** across dimensions automatically
- **Constrains with anti-AI-design rules** (banned-by-default list:
  purple gradients, glassmorphism-everywhere, bento-everything, glow borders…)
- **Synthesizes an original direction** before any pixel decision
- **Validates** with realism, industry, platform, a11y, RTL and
  anti-generic QA gates
- **Redesigns like a professional**: understand → diagnose → prioritize →
  preserve → change selectively → design → validate → **iterate**

## What's inside

| Module | Coverage |
|---|---|
| `knowledge/` | **112 files**: 24 industries · 9 platforms (web, Flutter, React Native, SwiftUI, UIKit, Jetpack Compose, Android, cross-platform) · devices (phone/tablet/foldable/desktop/TV) · input models · redesign intelligence (7 files) · forms & validation · notifications · states · data-viz · dark-mode theming · implementation realism · typography (Latin + Arabic) · RTL cross-platform · accessibility (WCAG 2.2 official criteria) · visual DNA catalog · anti-patterns |
| `research/` | Live code-first research pipeline (Python tools) + evidence logs. Built on a **156-site corpus** (~31MB production CSS analyzed) + **39 MENA/RTL sites**, refreshed with 2026 fetches: Apple DocC/WWDC, Android/Material official repos, React Native official source, MDN, W3C GitHub, NN/g, and real product evidence (quran.com, Kraken, Coinbase, Bayt, Wuzzuf, flynas, Bosta…) |
| `tests/` | Self-tests, quality gates, behavioral + adversarial test suites (V1 → V2.2) |

### Evidence honesty (the core discipline)

Every claim carries a source class: **OBSERVED** (corpus/product evidence) ·
**PLATFORM RULE** (official docs) · **APPLE OFFICIAL** · **DESIGN PRINCIPLE**
(stable convention) · **RECOMMENDED**. Nothing is called "analyzed" unless
it was actually fetched; blocked sources are logged honestly in the
research logs, never fabricated.

---

## Install

### One-liner (skills CLI — recommended)

```bash
npx skills add swmohamed/real-ui
```

Works with the standard agent-skills CLI (skills.sh): installs into the
universal `~/.agents/skills` hub (or the current project's) and wires up
every agent it detects (Claude Code, Codex, Cursor, Gemini CLI, Copilot,
and more). Local pre-publish testing works too:
`npx skills add /path/to/real-ui`.

### Zero-Node alternative (installs to EVERY agent on the machine)

```bash
git clone https://github.com/swmohamed/real-ui.git
cd real-ui
python scripts/install.py
```

This installer auto-detects **every** agent skills folder on the machine
(pi, Claude Code, Codex, Cursor, Gemini CLI, OpenCode, Windsurf, Continue,
Roo, Factory, Qoder, Trae, Kilo Code, CodeBuddy, Warp, Augment, Codewhale,
and any other `~/.<agent>/skills` convention), installs real **copies**
into each (no symlinks), and verifies every copy is identical.

Verify anytime:

```bash
python scripts/install.py --verify
```

### Manual install

1. Clone or download this repo.
2. Copy the whole folder into your agent's skills directory, renamed to
   `real-ui`:

| Agent | Destination |
|---|---|
| pi | `~/.pi/agent/skills/real-ui` |
| Claude Code | `~/.claude/skills/real-ui` |
| Codex | `~/.codex/skills/real-ui` |
| Cursor | `~/.cursor/skills/real-ui` |
| Gemini CLI | `~/.gemini/skills/real-ui` |
| OpenCode | `~/.opencode/skills/real-ui` |
| Windsurf | `~/.windsurf/skills/real-ui` |
| Continue | `~/.continue/skills/real-ui` |
| Roo / Factory / Qoder / Trae / Kilo / CodeBuddy / Warp / Augment / Codewhale | `~/.<agent>/skills/real-ui` |
| Universal hub | `~/.agents/skills/real-ui` |

3. Restart your agent.

> **Note:** raw fetched evidence (`research/raw/` + corpus JSONs) is **not
> included** in the repo (third-party content). All tools to regenerate it
> are included — see `research/README.md`.

## Usage

Just ask naturally — the skill auto-activates on design work:

```
"Use real-ui: build me a full website for an Egyptian fintech
startup, Arabic-first RTL, 5 pages"

"Use real-ui: redesign this dashboard"   (+ attach screenshot/URL)

"Review my Flutter app's UI for iPad + accessibility"
```

- **Fast mode (default)**: uses the prebuilt knowledge base — fast, no
  research.
- **Deep mode**: triggered by new industries, major redesigns, or
  explicit research requests — fetches fresh evidence with the included
  pipeline, labeled honestly.

Works without screenshots or vision (code-first: HTML/CSS/JS/DOM evidence),
and composes with your host's vision tools when present.

## Repository layout

```
real-ui/
├── SKILL.md                 # orchestrator (workflow + retrieval map)
├── knowledge/               # 112 modular knowledge files (18 domains)
├── research/
│   ├── README.md            # how to run/refresh the research pipeline
│   ├── tools/               # fetch_analyze, aggregate, verify + installer deps
│   └── reports/             # evidence & research logs (V1→V2.2)
├── tests/                   # quality gates, behavioral & adversarial tests
├── scripts/install.py       # install-everywhere + verify
├── LICENSE                  # MIT
└── README.md
```

## Tests

```bash
python research/tools/verify_install.py   # integrity + sync + YAML safety
```

Behavioral/adversarial suites (reasoned scenarios: gaming redesign, Arabic
ecommerce, Flutter food delivery, iOS+Android productivity, crypto,
logistics, Islamic apps + Hijri, foldables, a11y-heavy, cross-platform
design systems, dashboards, dark mode) live in `tests/`.

## License

MIT © SwMohamed — see [LICENSE](LICENSE).

Research corpus consists of distilled, attributed observations about
public websites and official documentation; it contains no third-party
assets. Raw fetches are regenerable via `research/tools/` and are not
redistributed.
