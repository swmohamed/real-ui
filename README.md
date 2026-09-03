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
- **Models the experience and product before the page** (people, context,
  current journeys, entities, top tasks, outcomes, content priority,
  actors/authority, shared and operational state, scope, and screen contracts)
  so industry patterns cannot invent features
- **Retrieves only relevant knowledge** across dimensions automatically
- **Constrains with anti-AI-design rules** (banned-by-default list:
  purple gradients, glassmorphism-everywhere, bento-everything, glow borders…)
- **Synthesizes an original direction** before any pixel decision
- **Validates** with realism, industry, platform, a11y, RTL and
  anti-generic QA gates
- **Handles AI/automation, collaboration/concurrency, and long-running work**
  as control, provenance, permission, state, and recovery contracts—not as
  chat, avatar, progress, or card templates
- **Redesigns at the requested depth**: a full redesign preserves capabilities,
  data, routes, workflows, business logic, and required content while
  re-deriving IA, hierarchy, navigation, composition, and components

## What's inside

| Module | Coverage |
|---|---|
| `knowledge/` | **127 files** across 25 directories: 24 industry modules plus an authority contract · 9 platform guidance modules plus a router (web, Flutter, React Native, SwiftUI, UIKit, Jetpack Compose, Android, native desktop, cross-platform) · devices (phone/tablet/foldable/desktop/TV) · input models · redesign intelligence (10 files) · modern craft execution discipline · experience evidence and product/scope/content modeling · interaction control · AI/automation control · collaboration/concurrency · long-running operations/recovery · page-composition authority · forms, notifications, states, data-viz, theming, implementation, typography (Latin + Arabic), localization, RTL, accessibility, visual direction, and anti-patterns |
| `research/` | Reproducible code-first research pipeline (Python tools) + evidence logs. Built on a **156-site corpus** (~31MB fetched production CSS) + **39 MENA/RTL sites**, with additional 2026 official-platform and first-party product-documentation research. Source extraction and documented behavior are not runtime or render evidence. |
| `tests/` | Executable Python invariants for routing, evidence aggregation, scope/template/accessibility/platform contracts, plus behavioral tests that reject cosmetic-only FULL redesign plans and unauthorized scope |

### Evidence honesty (the core discipline)

Research claims distinguish **SOURCE-OBSERVED**, **RUNTIME-OBSERVED**,
**RENDER-OBSERVED**, **DOC-OBSERVED**, **INFERRED**, **RECOMMENDED**, and
**UNCERTAIN** evidence. Guidance separately classifies standards, platform
rules, official guidance, observations, principles, implementation guidance,
recommendations, and experimental ideas. Nothing is called analyzed unless it
was actually inspected; blocked sources are logged honestly, never fabricated.

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

- **Normal mode (default)**: uses the complete relevant design intelligence,
  including product modeling, accessibility, responsive/adaptive behavior,
  localization, platform guidance, targeted validation, and every redesign
  depth. A full redesign is normal use; it does not require Deep/Audit mode.
- **Deep / Audit mode**: reserved for auditing or upgrading REAL-UI itself,
  repository/knowledge/evidence-wide validation, architecture debugging, or
  explicitly requested deep research. It changes investigation breadth, not
  the quality available to normal design work.

Works without screenshots or vision (code-first: HTML/CSS/JS/DOM evidence),
and composes with your host's vision tools when present.

## Repository layout

```
real-ui/
├── SKILL.md                 # orchestrator (workflow + retrieval map)
├── knowledge/               # 127 modular knowledge files (25 directories)
├── research/
│   ├── README.md            # how to run/refresh the research pipeline
│   ├── tools/               # fetch_analyze, aggregate, verify + installer deps
│   └── reports/             # evidence & audit logs (V1→V7)
├── scripts/
│   ├── install.py           # install-everywhere + verify
│   └── validate_redesign.py # FULL redesign PLAN + RENDER gate
├── tests/                   # executable invariants + reasoned scenario specs
├── LICENSE                  # MIT
└── README.md
```

## Tests

```bash
python research/tools/verify_install.py   # integrity + sync + YAML safety
```

Executable repository checks:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

The Markdown suites in `tests/` are reasoned scenario specifications (gaming
redesign, Arabic ecommerce, Flutter food delivery, cross-platform products,
accessibility, dashboards, and more). They guide manual or future agent-harness
runs. They are not claims that every future agent run, native app, browser, or
production backend was executed.

## License

MIT © SwMohamed — see [LICENSE](LICENSE).

Research corpus consists of distilled, attributed observations about
public websites and official documentation; it contains no third-party
assets. Raw fetches are regenerable via `research/tools/` and are not
redistributed.
