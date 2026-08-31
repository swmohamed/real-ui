# Code-First Research Method

How to deeply understand any real website **without vision**, using only public
implementation. This is the Skill's primary research mode. Screenshots are
supplementary, never required.

## Evidence labels (mandatory)

Every research claim must carry one label:

- **OBSERVED** — directly extracted from fetched HTML/CSS/JS/headers of the site.
- **INFERRED** — reasoned from observed artifacts + known conventions; not directly measured.
- **RECOMMENDED** — our design guidance; not a claim about the site.
- **UNCERTAIN** — plausible but unverifiable (e.g., CDN served different markup).

Never say "I analyzed their CSS" unless CSS was actually fetched and read.
Never invent breakpoints, tokens, fonts, or behavior. If a site is inaccessible,
record it as inaccessible.

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
2. **Linked CSS** (fetch the 2–4 largest same-origin stylesheets)
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
4. Infer UX architecture: map components → jobs (orientation, search, selection,
   detail, conversion, retention).
5. Compare against industry baseline in `knowledge/industries/`.
6. Distill to patterns/principles with labels. Store the reusable form:

   WEAK: "Site X uses 12px-radius cards."
   STRONG: "Consumer game-discovery surfaces use moderate radii (12–16px) to
   soften density; fintech dashboards stay at 4–8px to signal precision."

## Reading a site without rendering it (heuristic table)

| Question | Code evidence |
|---|---|
| Is it dark or light? | theme-color, body background, color pairs near `#0/1/2…` vs `#f/ff…` |
| Dense or airy? | padding/margin values, font-size distribution, link count per nav |
| Mobile strategy? | breakpoint count, hidden/shown patterns, separate m. domain |
| Is there a design system? | token namespaces, `var(--…)` density, utility framework |
| Conversion priority? | sticky elements, CTA words, form placement above fold |
| RTL quality? | logical properties vs `[dir=rtl]` overrides vs nothing |
| Motion language? | transition/animation counts, keyframe names, transform usage |

## Saturation rule

Research a category until new references stop yielding new patterns — then stop.
Classify findings: HIGH CONFIDENCE (seen in 3+ diverse leaders), MEDIUM (1–2
sites or one region), EXPERIMENTAL (single outlier, possibly trend-driven).
