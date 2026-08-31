# Visual Hierarchy — How Real Sites Direct Attention

## The allocation model

A screen has a finite attention budget. Use this ordering as a diagnostic,
then adapt it to the screen contract:

1. **Primary signal or task group**: the hero headline, the product name, the
   search field, the checkout total. Biggest type or biggest surface.
2. **Action layer**: emphasize actions by task priority, not a fixed count.
3. **Scan layer**: section headings, card titles, prices. Built from weight
   and size steps, not new colors.
4. **Support layer**: metadata, timestamps, helper text. Muted color, smaller
   size, but never below readable minimums.
5. **Ambient layer**: backgrounds, textures, decoration. Must lose to everything.

## Size discipline (from corpus type scales)

- Real UI bodies live at 14–16px; support text 12–13px (61+68 sites declare
  14px and 12px). Below 12px is anti-pattern territory.
- Headline steps that read as "designed": ×1.25 ratio between adjacent levels
  (16 → 20 → 25 → 31 → 39 → 49). Editorial/display can go ×1.33+ for drama.
- One dramatic jump (h1 vs h2) beats five timid ones.

## Weight and color steps

- Common weight candidates are 400 body, 500–600 emphasis, and 700 headlines;
  use only weights the selected font actually supplies and the hierarchy needs.
- Keep neutral roles intentionally small; the semantic role count matters more
  than how many primitive ramp steps exist.
- Keep identity accents restrained enough that semantic colors retain meaning.
  News samples use varied brand/section systems; red is not a universal rule.

## Position and flow

- Reading/scan behavior follows content, script, task, and layout. Use prose
  flow for reading, aligned comparison for data, and grid scanning for
  genuinely browsable visual sets; do not impose named F/Z templates.
- RTL flips the F and Z **and** the implied "forward" of progress — a stepper
  moves right-to-left in Arabic (see `rtl/arabic-ux.md`).
- The initial viewport should expose the highest-priority message/task and a
  credible next step; routing or comparison surfaces may legitimately expose
  several coordinated options.

## Density as hierarchy

- Card padding is a signal: 12–16px = dense functional grid (news, games
  portal); 24–40px = premium browse (luxury, hotels).
- Row height carries meaning in data UIs: 40–48px interactive rows, 32px
  compact tables, 56px+ mobile touch rows.
- Whitespace volume maps to price positioning (OBSERVED: Ounass/luxury class
  vs Jumia density — same region, opposite whitespace).

## Common failure modes

- Competing actions with equal emphasis and no task rationale → establish a
  clearer priority or explain the intentional choice.
- Decorative layer competing with content (gradient hero behind gradient
  cards) → mute the ambient layer until it stops winning.
- Everything bold → nothing bold. Emphasis by promotion, not proliferation.
- Color used as the only differentiator (fails ~8% of males with color
  vision deficiency) → pair color with icon/text/shape.
