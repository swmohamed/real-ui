# Redesign Originality (direction before components)

Generic AI redesigns assemble templates. Original redesigns derive a
direction. Direction comes from the product, never from a component
library's demo page.

## Derive the direction

```
PRODUCT (content, data, workflows)
+ INDUSTRY (conventions, trust bar, density norms — industries/*)
+ AUDIENCE (consumers? pros? Arabic-first?)
+ BUSINESS MODEL (subscription calm vs transactional urgency)
+ PLATFORM (native conventions — platforms/*)
+ EXISTING BRAND ASSETS (what survives — preservation.md)
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

## Output contract for a redesign direction

```
DIRECTION: <one sentence>
DRIVERS: product:<..> industry:<..> audience:<..> platform:<..> brand:<..>
DNA FAMILY: <visual-dna name> + <product-specific bend>
TOKENS: <type scale / color roles / radius / spacing / elevation deltas>
WHAT WE REFUSED: <banned moves considered and rejected, with reasons>
```
