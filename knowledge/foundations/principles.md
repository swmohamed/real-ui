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
When reasoning about real sites: OBSERVED / INFERRED / RECOMMENDED / UNCERTAIN.
When designing: principles are reusable, pixels are not — never copy a site,
combine patterns from multiple references into an original result.

## 3. Content shapes layout
Real homepages average exactly one h1 and 60–600 links depending on sector.
Density is a design decision: news grids are dense because scanning IS the
product; luxury is sparse because scarcity IS the message. Ask "how much
content exists?" before "how should it look?"

## 4. Hierarchy is allocation, not decoration
Every screen answers: what is the ONE job of this view? Everything else is
subordinate by size, weight, color, or position. If two elements compete,
one is wrong.

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
1. **Classify** — industry, sub-industry, audience, intent, page type, language/region.
2. **Retrieve** — load the matching industry file, page file, DNA, patterns.
3. **Constrain** — content inventory, brand input, technical limits, a11y floor.
4. **Synthesize** — pick a Visual DNA + adapt 2–4 reference patterns (never one).
5. **Tokenize** — express decisions as a small scale system before styling anything.
6. **Validate** — run the finish gate: anti-AI check, a11y check, RTL check,
   performance check, "does it feel like its industry?" check.
