# Evidence-First Research Method

How to understand real products without overstating what the available
evidence proves. Public implementation remains the primary mode for website
source research; current first-party product documentation, runtime exercise,
and rendered inspection answer different questions and keep distinct labels.

## Evidence labels (mandatory)

Every research claim must carry an evidence-mode label and an interpretation
label when appropriate:

- **SOURCE-OBSERVED** — directly extracted from fetched HTML/CSS/JS/headers.
  This proves source presence only: a media query, hidden node, or selector may
  be unused on the sampled route.
- **RUNTIME-OBSERVED** — exercised in a browser/app and observed in a named
  state, viewport, input mode, and route.
- **RENDER-OBSERVED** — visually inspected from a named screenshot/render at
  a stated viewport/state.
- **DOC-OBSERVED** — explicitly documented in a current, named first-party
  product/help/design-system source, with access date. It proves documented
  behavior or intent, not that a feature was exercised, rendered well, is
  available to every account/region, or is effective in use.
- **INFERRED** — reasoned from observed artifacts + known conventions; not directly measured.
- **RECOMMENDED** — our design guidance; not a claim about the site.
- **UNCERTAIN** — plausible but unverifiable (e.g., CDN served different markup).

Legacy `OBSERVED` labels mean SOURCE-OBSERVED unless the claim explicitly
records runtime/render evidence. Never infer actual visibility, order,
interaction success, animation quality, or performance from source presence
alone.

Never say "I analyzed their CSS" unless CSS was actually fetched and read.
Never invent breakpoints, tokens, fonts, or behavior. If a site is inaccessible,
record it as inaccessible.

Evidence mode is orthogonal to knowledge class. Classify reusable knowledge as
one or more of: **STANDARD REQUIREMENT**, **PLATFORM RULE**, **OFFICIAL
GUIDANCE**, **REAL-WORLD OBSERVATION**, **DESIGN PRINCIPLE**, **IMPLEMENTATION
GUIDANCE**, **RECOMMENDATION**, or **EXPERIMENTAL IDEA**. A DOC-OBSERVED product
feature remains an observation; it does not become a standard or default.

## What to fetch (in order of value)

1. **HTML of the page** (view-source equivalent)
   - `<html lang dir>`, `<meta viewport>`, `<meta theme-color>`, `<title>`, description
   - Semantic skeleton: header/nav/main/section/article/aside/footer counts
   - Heading hierarchy: h1 count (discipline check), h2/h3 structure
   - Forms: labels, placeholders, required, aria-, autocomplete, input types
   - Links & buttons: counts, CTA wording, hreflang alternates
   - Inline `<style>` blocks and CSS custom properties on :root/body
   - JSON-LD `@type` list → reveals page archetype + entity model
   - Icon classes (`fa-`, `material-icons`, `lucide-`, `octicon-`, custom `icon-*`)
   - Framework fingerprints: `__NEXT_DATA__`, `wp-block`, Tailwind class grammar,
     Bootstrap grid classes, `data-v-` hashes, Webflow classes
2. **Linked CSS** (fetch up to three first-party stylesheets in document
   order, within caps, plus inline style blocks; record the fetched URLs)
   - `@font-face` blocks: family, weights, variable axes, `font-display`
   - `font-family` stacks: brand font → fallback chain (the chain encodes intent)
   - Media queries: min/max-width distribution → the real breakpoint system
   - Container queries (`@container`) → component-driven responsiveness
   - Custom properties: token namespaces (`--hds-`, `--cds-`, `--fco-`, `--sk-`)
   - Color frequency: brand hues, neutral ramps, dark-mode pairs
   - Radius scale, shadow tiers, z-index scale, max-width/container values
   - `:focus-visible`, `prefers-reduced-motion`, `prefers-color-scheme` presence
   - RTL handling: `[dir="rtl"]`, `:dir(rtl)`, `:lang(ar)`, logical properties
3. **JS behavior** (when bundles are readable; usually infer from markup)
   - Data attributes that drive components (`data-carousel`, `data-tab`)
   - `noscript` content → SSR vs CSR and fallback content
   - Event-visible state hooks (`.is-open`, `.collapsed`, `aria-expanded` in markup)
4. **URLs and routing** — path grammar reveals IA (`/category/`, `/p/`, `/ar/`, `?dir=`)
5. **Metadata & i18n** — hreflang, og:, apple-web-app, alternate links
6. **Public behavior** — redirects, geo-localized variants (e.g., a global payments
   site serving `lang="ar-EG" dir="rtl"` from Egypt — OBSERVED in our corpus)

## Analysis procedure

1. Fetch → record status. Blocked = "inaccessible", not a gap to invent over.
2. Extract skeleton metrics (tag counts, headings, links).
3. Extract CSS metrics (typography, tokens, breakpoints, states).
4. Infer possible UX architecture: map source components → likely jobs
   (orientation, search, selection,
   detail, conversion, retention).
5. If rendered/runtime access exists, verify high-impact inferences at named
   widths and states; otherwise label them INFERRED/UNVERIFIED.
6. Compare against the product model first, then the industry evidence catalog
   under `knowledge/industries/README.md`.
7. Distill to patterns/principles with labels. Store the reusable form:

   WEAK: "Site X uses 12px-radius cards."
   STRONG: "When content is bounded, media-forward, and browsed rather than
   compared, cards may aid item recognition; test density, hierarchy, and
   brand register before selecting their shape."

## Cross-product comparison protocol

Use comparison when learning a product pattern rather than verifying one
named implementation:

1. Define the decision question and sampling axes before collecting examples
   (task, stakes, platform, audience, region, maturity, and business model).
2. Prefer current first-party sources; record product, feature, URL, access
   date, evidence mode, state/viewport where applicable, and access limits.
3. Compare at least three materially different products before calling a
   behavior cross-product. Seek a counterexample instead of counting only
   convergence.
4. Separate **common mechanism**, **meaningful differences**, and **conditions
   that explain the difference**. Do not average incompatible workflows.
5. Extract the underlying user/system problem and decision variables, not the
   visible shell. A side panel, chat composer, card grid, avatar stack, or
   sparkle treatment is not transferable knowledge by itself.
6. Classify confidence in two parts: confidence that the pattern exists, and
   confidence that it transfers to the target product.
7. Reject observations that are one-product branding, plan/region gated,
   inaccessible, stale, unsupported by the named evidence mode, or likely to
   create scope by imitation.

**Template-gravity gate:** if the proposed lesson can be copied as a layout
without knowing the target's entities, tasks, actors, authority, consequence,
or content shape, it is not yet a reusable principle.

## Reading a site without rendering it (heuristic table)

| Question | Code evidence |
|---|---|
| Is it dark or light? | theme-color, body background, color pairs near `#0/1/2…` vs `#f/ff…` |
| Dense or airy? | padding/margin values, font-size distribution, link count per nav |
| Mobile strategy candidate? | breakpoint presence, hidden/shown selectors, separate m. domain; runtime needed to confirm |
| Is there a design system? | token namespaces, `var(--…)` density, utility framework |
| Conversion priority candidate? | sticky selectors, CTA words, source order; render/runtime needed to confirm visibility/above-fold position |
| RTL quality? | logical properties vs `[dir=rtl]` overrides vs nothing |
| Motion language? | transition/animation counts, keyframe names, transform usage |

## Saturation rule

Research a category until new references stop yielding new patterns — then stop.
Classify findings: HIGH CONFIDENCE (seen in 3+ diverse leaders), MEDIUM (1–2
sites or one region), EXPERIMENTAL (single outlier, possibly trend-driven).
