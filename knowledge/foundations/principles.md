# Design Principles — The Skill's Core Doctrine

Ten principles that govern every output. These are not generic maxims; each is
tied to how the real web behaves (see `research/observed-findings.md`).

## 1. Context beats taste
Design decisions come from INDUSTRY + AUDIENCE + USER INTENT + CONTENT +
BUSINESS MODEL + BRAND + REGION + LANGUAGE. A bank at 4px radius and a game
portal at 16px are both correct. The wrong radius is the one imported from a
different context. Never open a project with aesthetics; open it with
classification.

## 2. Evidence over invention of facts
When reasoning about real sites: SOURCE-OBSERVED / RUNTIME-OBSERVED /
RENDER-OBSERVED / DOC-OBSERVED / INFERRED / RECOMMENDED / UNCERTAIN. Legacy OBSERVED labels
mean source presence unless a runtime/render state is named.
When designing: principles are reusable, pixels are not — never copy a site,
combine patterns from multiple references into an original result.

## 3. Content shapes layout
Content amount, shape, volatility, source, language, and decision value all
change the layout. Ask what exists, what must be compared or understood, and
what can be deferred before choosing a container. A genre may suggest density;
the actual product and task must justify it.

## 4. Hierarchy is allocation, not decoration
Every screen answers which outcome and decisions it supports. Some views have
one dominant action; monitoring, comparison, creation, and incident surfaces
may need several coordinated signals. Competition is wrong when priority and
relationship are unclear—not merely because two elements are salient.

## 5. Systems, not screens
Ship a scale, not a value: 2–3 radius steps, 3–4 elevation steps, 8–10 type
steps, one spacing rhythm. The corpus proof: leaders namespace tokens
(`--hds-`, `--cds-`, `--fco-`) and reuse them thousands of times.

## 6. The median web is mediocre — match the leaders
Observed median: `main` on 57% of homepages, reduced-motion 40%. The floor for
this Skill: semantic completeness, focus-visible, reduced-motion, contrast —
match gov.uk/GitHub/Stripe class, not the average.

## 7. Performance is a design material
Every visual effect has a cost line: blur on scroll, keyframes on low-end
Androids, 3 image variants per card in a 200-card grid. Budget effects to
where they earn value (hero scrim yes, every-card glow no).

## 8. Motion explains, never performs
Transitions communicate state change (open/close, add/remove, navigate).
If a motion doesn't answer "what just happened?", delete it. 40% of real
sites now ship reduced-motion respect — non-negotiable.

## 9. RTL is a first-class mode, not a mirror
Arabic UX differs in content density, font behavior, numerals, trust signals,
and reading rhythm — not just direction. Design both directions from the same
tokens using logical properties, and flip semantics, not just chevrons.

## 10. No generic AI aesthetics
The forbidden-by-default list (gratuitous purple gradients, glassmorphism,
bento-everything, glow borders, floating blobs, random 3D) is in
`anti-patterns/ai-aesthetics.md`. Each is allowed only with an explicit,
written justification tied to brand/context.

## The design decision framework (used at runtime)

For any decision, answer in order:
1. **Classify** — industry, product type, audience, intent, platform, language/region.
2. **Model and scope** — entities, tasks, capabilities, content priority, screen contracts.
3. **Retrieve** — load authority contracts before relevant page/industry catalogs.
4. **Constrain** — brand, technical limits, a11y, performance, locale, platform.
5. **Synthesize** — derive visual decision axes + adapt principles from multiple references (never one layout or preset).
6. **Tokenize** — express decisions as a small scale system before styling anything.
7. **Validate** — run scope/structure/state plus anti-AI, a11y, RTL,
   performance check, "does it feel like its industry?" check.
