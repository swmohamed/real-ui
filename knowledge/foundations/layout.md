# Layout Foundations — content, relationships, and space

Layout represents the product model. Corpus values in
`research/observed-findings.md` are plausible candidates—not a universal
container, grid, sidebar, or breakpoint system.

## Derive regions before columns

For each major region record:

`required content/action → user decision/task → relationship to other regions → persistence → representation → stress condition`

Then identify shared key lines, reading/scan order, text measure, alignment,
and what owns leftover space. A grid is useful when it expresses those
relationships; “12 columns” is not a design rationale.

Candidate organizations include linear narrative, aligned comparison,
master-detail, supporting pane, canvas + inspector, temporal lane, spatial
map, editorial lead/secondary hierarchy, and modular browse. Select from
content and interaction shape—not page or industry name.

## Width and measure

- Choose reading measure from font/script, size, language, content type, and
  testing. Character-count heuristics can seed a test but are not pass/fail.
- Cap or partition wide space when longer lines or detached controls reduce
  comprehension. Data, media, maps, timelines, and canvases may legitimately
  use more width than prose.
- Gutters and internal spacing respond to viewport, safe areas, input targets,
  text scaling, and density mode. Use a small token scale, not copied values.
- Distinguish component padding, inter-item rhythm, section separation, and
  shell gutters; equal numeric values do not mean equal semantic roles.

## Content-derived adaptation

Do not begin with a fixed device spine. Start with representative content and
find the widths or container sizes where:

- labels/actions collide or wrap ambiguously;
- reading measure becomes uncomfortable;
- comparison loses alignment;
- panes cannot preserve useful minimums;
- touch/keyboard targets or focus order fail;
- localization, 200% text, reflow, safe areas, or virtual keyboard obscure work;
- an extra pane/column adds genuine simultaneous context rather than filler.

Normalize resulting thresholds into the smallest coherent project set.
Platform window classes remain platform inputs; do not reinterpret them as web
standards. Test immediately on both sides of every threshold.

## Transformation ledger

For each window/container class state what remains, moves, condenses, changes
representation, becomes progressive disclosure, or is intentionally removed.
Examples are decisions to evaluate, not automatic transforms:

- navigation may remain visible, become a rail, drawer, sheet, search-first
  surface, or contextual navigation according to hierarchy and platform;
- a table may keep comparison through priority columns, sticky identifiers,
  horizontal scroll, row disclosure, or a different compact representation;
  cards are valid only when records remain independently intelligible;
- filters may stay inline, become a compact bar, overlay, sheet, or saved view;
- split media/text may stack, crop, move, or disappear when the content
  priority and narrative allow it;
- a footer may remain grouped, wrap, disclose, or shorten according to link
  hierarchy and legal/support needs.

State and task continuity must survive recomposition: selection, focus,
scroll/reading position, edits, media, drafts, and long-running operations.

## Layering and occlusion

Define semantic layers (content, sticky context, transient command surface,
modal task, notification, teaching overlay) and assign tokens. The number of
layers depends on the product. Sticky regions must not obscure focus or consume
the working viewport; overlays need dismissal, focus, scroll, and background
interaction contracts. Elevation explains ownership and overlap, not prestige.

## Layout QA

- [ ] style-blind regions trace to content/task relationships
- [ ] wide space has an owner; prose does not stretch by accident
- [ ] thresholds come from named stress failures or platform classes
- [ ] comparison, hierarchy, spatial, and temporal meaning survives adaptation
- [ ] focus, selection, drafts, scroll, and operation state survive recomposition
- [ ] long localized strings, mixed scripts, 200% text, 320 CSS px reflow, safe areas, and virtual keyboard are tested where applicable
- [ ] no transformation exists solely because a framework or genre usually uses it

Connects: foundations/{product-modeling,visual-hierarchy}.md ·
responsive/{breakpoints-adaptation,adaptive-models}.md · devices/* ·
accessibility/floor.md.
