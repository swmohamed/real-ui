# Screenshot Analysis (visual evidence, honestly)

Screenshots are EVIDENCE. Analyze them for what they show; never invent
what they can't. This skill is code-first — screenshots supplement code,
they don't replace it.

## What a screenshot CAN reveal (OBSERVED)

Layout structure · regions · navigation visible on screen · components ·
typography hierarchy (relative sizes/weights, never exact px) · color
language (approximate: dark canvas, warm surface — never fake hex) ·
spacing feel (tight/compact/moderate/spacious) · density · icon style ·
imagery treatment · visible states (loading/empty/error if captured) ·
language + direction (RTL/LTR) · platform clues (system bars, control
style) · device estimate · inconsistencies (mixed radii, icon styles).

## What a screenshot CANNOT reveal (say UNKNOWN, never guess)

Interactions & hover states · hidden navigation/routes · performance ·
real animation · accessibility compliance · backend · responsive
behavior not shown · exact measurements · exact fonts · the framework.

## Host vision tools (provider-agnostic rule)

If a vision-capable model/tool is available in the host environment, it
MAY be used to produce OBSERVATIONS. Rules:
- Vision tool = EYES (structured observations). real-ui = BRAIN (UX/UI
  reasoning, diagnosis, redesign decisions).
- Never hard-code a vision provider or API key into this skill. Use
  whatever the host offers, generically.
- Vision output is labeled `OBSERVED (vision)` — still subject to the
  no-hallucination list above.

## Analysis protocol

1. **Classify** image type (website/web app/mobile/tablet/dashboard/
   form/game), device, language, direction. Label uncertain items.
2. **Shared DNA first** (multi-screenshot): typography language, color
   system, component styles, nav language. THEN per-screen differences.
3. **Responsive inference** across differently-sized shots = INFERENCE
   with the differing evidence stated ("nav collapses from sidebar to
   hamburger between shot A and B → adaptive nav likely").
4. **Feed the diagnosis** — map observations into redesign/diagnosis.md
   checklist categories. Vision never outputs verdicts like "outdated"
   or "bad UX"; that reasoning is ours.
5. **Before/after evidence** — for redesign delivery, capture what
   changed vs the screenshot: region map (kept/moved/removed) + visual
   hierarchy shift, matching preservation.md's ledger.

## Evidence phrasing

GOOD: "Dark top bar, logo leading edge, four nav items, RTL order."
BAD: "The designer used dark nav to increase conversion." (speculation)
BAD: "Built with Tailwind." (invisible from a screenshot — UNKNOWN)
