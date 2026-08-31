# Originality (direction before components)

Generic AI design assembles templates. Original design derives a
direction. Direction comes from the product, never from a component
library's demo page. (Redesigns additionally follow the rules below.)

## Derive the direction

```
PRODUCT (content, data, workflows)
+ INDUSTRY (conventions, trust bar, density norms — industries/*)
+ AUDIENCE (consumers? pros? Arabic-first?)
+ BUSINESS MODEL (subscription calm vs transactional urgency)
+ PLATFORM (native conventions — platforms/*)
+ EXISTING BRAND ASSETS (what survives — redesign/preservation.md)
= VISUAL DIRECTION → then tokens → then components
```

Use visual-dna/dna-selector.md to pick a DNA family; then bend it with
the product's specifics (its content rhythm, its brand color, its
industry's density).

## Banned auto-moves (anti-patterns/ai-aesthetics.md — enforced harder in redesigns)

Never reach for these by default:
- excessive rounded cards everywhere · random gradients
- glassmorphism panels · huge generic hero sections
- generic SaaS dashboard layout for non-dashboard products
- repeated identical card grids for everything
- shadow stacks · whitespace inflation (density ≠ bad)
- purple/blue AI gradient identity · floating decorative blobs
- arbitrary animations · purposeless floating elements

Each of these is allowed ONLY with an explicit product-specific reason.

## Redesign-specific originality rules

1. **One idea, carried everywhere.** A redesign needs one strong,
   nameable idea ("mushaf-inspired calm reading surface", "terminal-
   density trading skin") — not five weak ones.
2. **Rescue before replace.** Often the original product's best visual
   idea is underused — amplifying it beats importing a stranger.
3. **Contrast with old ≠ opposite of old.** Fix decay, don't invert the
   brand (dark→light swaps usually break recognition).
4. **Components follow direction.** Pick radius/elevation/type ONLY
   after direction exists. Banned order: components → direction.
5. **Industry reality check.** Direction must clear the industry's
   trust/density bar (a bank cannot go brutalist-poster; a game site
   cannot go bank-formal — unless briefed).
6. **Density is a design decision.** Don't "clean up" a data product
   into air. Match industries/* density norms.
7. **Name it.** If the direction can't be stated in one sentence, it
   doesn't exist yet.

## Variation within an industry (same genre, different products)

Two products in one industry must not share a structure by default —
nor differ randomly. Difference traces to the product model
(foundations/product-modeling.md): positioning, audience expertise,
top task, volume. Color/logo swaps are NOT differentiation.

Five structural dials (choose deliberately per product, write the choice):

| Dial | Range | Set by |
|---|---|---|
| Density | airy editorial ↔ dense operational | task verb (browse vs monitor) + audience expertise |
| Nav model | top bar ↔ side rail ↔ bottom tabs ↔ command palette | platform + task count + power-user share |
| Silhouette | marketing hero-first ↔ app shell-first ↔ catalog grid-first ↔ editorial feed | product type + where task #1 lives |
| Rhythm | uniform card grid ↔ mixed editorial sections ↔ table-dominant | content homogeneity (homogeneous→grid; mixed→editorial) |
| Register | formal/institutional ↔ casual/direct | audience + trust bar (industries/*) |

Worked pair (same industry file, different dials): retail consumer bank
= marketing-first, airy, warm photography, top nav, hero product story
vs trading platform = app shell, dark option default, table/chart-
dominant, rail nav, keyboard shortcuts, dense. Same genre knowledge,
opposite structures — each justified by its model.

Same-brand families: shared tokens + component library, varied dials
per product (a bank's marketing site ≠ its trading app ≠ its admin
console — one system, three silhouettes).

Legitimate similarity: when two products' models genuinely match
(same audience, task, volume), similar structure is CORRECT — do not
invent difference. Variation serves requirements, not novelty
(finish-gate "originality" check reads this file).

## Output contract for a direction (any design or redesign)

```
DIRECTION: <one sentence>
DRIVERS: product:<..> industry:<..> audience:<..> platform:<..> brand:<..>
DNA FAMILY: <visual-dna name> + <product-specific bend>
DIALS: density <..> · nav <..> · silhouette <..> · rhythm <..> · register <..>
TOKENS: <type scale / color roles / radius / spacing / elevation deltas>
WHAT WE REFUSED: <banned moves considered and rejected, with reasons>
```
