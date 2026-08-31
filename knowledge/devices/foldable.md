# Device: Foldables

Foldables are a size+posture problem. `developer.android.com` treats
foldables as first-class alongside phones/tablets `[OBSERVED - large-
screens docs]`; Flutter docs carry a dedicated "large screens &
foldables" adaptive section `[OBSERVED]`.

## The two states problem

Design for BOTH folded (compact/narrow, usually portrait) and unfolded
(expanded/tablet-class) as ONE continuous product:
- Layout continuity: same screen, reflowed — content position may
  change but task state NEVER resets on fold/unfold.
- Window class switching mid-use (compact↔expanded): nav morphs
  (bottom bar ↔ rail) per responsive/adaptive-models.md.

## Postures (the fold as an interface feature)

- **Book posture** (half-opened, vertical fold): split naturally at the
  hinge — content top, controls bottom (keyboard-like bottom zone).
- **Table-top / flex mode** (horizontal fold, like a laptop): video on
  top half, controls bottom half.
- **Cover screen** (external display): compact glanceable surface
  (notifications, quick actions) — minimal but real product surface.

Android exposes hinge/fold posture + display features to layout
`[PLATFORM RULE]`; NavigationSuiteScaffold already reacts to posture
`[OBSERVED]`.

## Design rules

1. Nothing important ON the hinge line: split zones AT it, content
   away from it (avoid text/images straddling the fold).
2. Hinge = natural divider (master-detail, media+controls, form+preview).
3. Aspect-ratio jumps (unfolding): fluid layouts, no fixed pixel
   assumptions; test ultra-tall (folded 21:9-ish) AND squarish unfolded.
4. Continuity tests: fold mid-video (player survives), mid-form
   (input state survives), mid-game (state survives).
5. Don't over-fold-design: 90% of foldable UX = correct adaptive
   layout + continuity; posture-specific layouts are bonus delight.

## Foldable QA

[ ] folded + unfolded both designed [ ] state survives fold/unfold
[ ] hinge-aware splits (nothing straddles) [ ] postures used where they
help (book/table-top) [ ] nav morphs by class [ ] aspect extremes safe
