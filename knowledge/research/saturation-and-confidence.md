# Research Saturation & Confidence Ledger

When the knowledge base makes a claim, this file explains how well-evidenced
the underlying pattern is. Update through bounded current research or a
Deep/Audit evidence-base task as routed by `SKILL.md`.

## Confidence tiers

- **HIGH** — observed in 3+ diverse, high-traffic leaders across ≥2 regions or
  generations of the pattern. Strong evidence that the pattern exists; it
  still requires product-fit and scope justification.
- **MEDIUM** — observed in 1–2 major sites, or common in one region only.
  Apply when context matches; state the rationale.
- **EXPERIMENTAL** — single outlier or early-adopter pattern. Use deliberately,
  never as a default.

## Saturation record (2025 corpus, 156 sites)

| Pattern family | Saturation | Confidence | Why |
|---|---|---|---|
| 768/1024 breakpoint candidates | Common, not universal | HIGH (source presence) | Corrected per-site prevalence: 91/145 at 768 and 63/145 at 1024; declaration repetition is not site count |
| h1 = 1 per page | Saturated | HIGH | Corpus mean exactly 1.0; SEO + a11y converge |
| Small-radius institutional / medium-radius product split | Saturated | HIGH | Radius histograms split cleanly by sector (62 sites at 4px) |
| Inter as default product sans; system stack as fallback | Saturated | HIGH | 17 direct + variants; every sector |
| Inter+Tajawal/Almarai Arabic pairing family | Saturated (MENA) | MEDIUM→HIGH | Multiple leaders (Zid, FilGoal, Jarir, Almentor variants) |
| Tailwind utility grammar as delivery layer | UNVERIFIED | LOW pending regeneration | Legacy detector accepted generic `flex`/`grid` class names; repaired detector has not been run across the corpus |
| Token namespaces (`--cds-` style) | High | HIGH | Stripe, Coinbase, Kooora, Spotify, Property Finder |
| Dark-canvas streaming/gaming identity | Saturated | HIGH | Steam/Disney+/Shahid/Twitch converge |
| Sticky search in travel | Saturated | HIGH | 75% of travel/food corpus |
| `prefers-reduced-motion` as quality marker | Growing | MEDIUM | 40% adoption; leaders ship it |
| Container queries as layout backbone | Early | EXPERIMENTAL | 19%; Spotify/Coursera/gov.uk lead |
| `:dir(rtl)` selectors vs logical properties migration | In flux | MEDIUM | 21/31 RTL sites use dir selectors; PayPal/others use `rtl:` variants |
| Poster-scrim blur in entertainment | Saturated | HIGH | 83% of streaming |
| Native `<dialog>` | Early | EXPERIMENTAL | 6% |
| Icon systems: FA on real web / lucide+SVG on modern product web | Saturated | HIGH | FA 29% corpus-wide; lucide/octicon on GitHub/Zid-class sites |

## Known gaps (recorded honestly)

- Sites that blocked research (Akamai/Cloudflare bot walls): netflix.com,
  epicgames.com, noon.com, talabat.com, aljazeera.net (TLS-blocked from research
  host), alarabiya.net, reuters.com, tesla.com, mayoclinic.com, unsplash.com,
  etsy/ebay/zalando/asos. Claims about these sites in the reference DB are
  labeled INFERRED (from prior public knowledge) or omitted — never "analyzed".
- Screenshots/vision were not used for any finding. All findings are
  implementation-derived.
- Mobile-only behaviors (app-web hybrids like Talabat's) partially inferred
  from blocked-fetch status + known public behavior — labeled UNCERTAIN.

## Targeted documentary samples (2026-09-01)

These bounded samples use current first-party help, product, and design-system
documentation. They are **DOC-OBSERVED**, not SOURCE-, RUNTIME-, or
RENDER-OBSERVED. Full source ledgers and comparisons are in
`research/reports/v6-evidence-driven-expansion.md`.

| Decision area | Diverse documented products/systems | Pattern-existence confidence | Transfer confidence |
|---|---:|---|---|
| AI-assisted and agentic control | 12 core products, with additional pattern-system examples | HIGH: scope, review, provenance, interruption, and editability recur | MEDIUM: authority, stakes, and artifact type change the correct interaction |
| Collaboration and concurrency | 11 core products | HIGH: roles, attribution, history, conflict control, and attention recur | MEDIUM: direct edit, suggestion, branching, and approval differ by consequence |
| Long-running operations and recovery | 10 product systems | HIGH: durable state, progress honesty, logs, and recovery recur | MEDIUM: cancel, retry, resume, undo, and rollback have product-specific semantics |

The samples are global-technology heavy and English-documentation heavy. They
establish pattern families, not prevalence across all industries or regions,
and do not validate rendered quality, accessibility execution, or usability.

## Fresh-research signals (not a mode router)

An uncovered industry, a corpus older than the decision permits, a named
competitor, or a market outside this confidence table can justify bounded
project research. These signals do **not** make ordinary design or FULL
REDESIGN a repository-wide Deep/Audit task. Use only the research needed for
the product decision and keep evidence labels explicit.

Deep/Audit mode is reserved for comprehensive investigation: auditing,
upgrading, debugging, or repository/knowledge/evidence-wide validation of
REAL-UI itself, plus deep/exhaustive research explicitly requested by the
user. See the mode router in `SKILL.md`.
