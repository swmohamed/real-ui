# Research Saturation & Confidence Ledger

When the knowledge base makes a claim, this file explains how well-evidenced
the underlying pattern is. Update via Deep Mode research (see SKILL.md).

## Confidence tiers

- **HIGH** — observed in 3+ diverse, high-traffic leaders across ≥2 regions or
  generations of the pattern. Safe to apply without justification.
- **MEDIUM** — observed in 1–2 major sites, or common in one region only.
  Apply when context matches; state the rationale.
- **EXPERIMENTAL** — single outlier or early-adopter pattern. Use deliberately,
  never as a default.

## Saturation record (2025 corpus, 156 sites)

| Pattern family | Saturation | Confidence | Why |
|---|---|---|---|
| 768/1024/1280 breakpoint spine | Saturated | HIGH | Thousands of media-query hits across all sectors and both directions |
| h1 = 1 per page | Saturated | HIGH | Corpus mean exactly 1.0; SEO + a11y converge |
| Small-radius institutional / medium-radius product split | Saturated | HIGH | Radius histograms split cleanly by sector (62 sites at 4px) |
| Inter as default product sans; system stack as fallback | Saturated | HIGH | 17 direct + variants; every sector |
| Inter+Tajawal/Almarai Arabic pairing family | Saturated (MENA) | MEDIUM→HIGH | Multiple leaders (Zid, FilGoal, Jarir, Almentor variants) |
| Tailwind utility grammar as delivery layer | Saturated | HIGH | 58% of corpus incl. BBC/gov.uk |
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

## Deep Mode triggers

Run fresh research when: new industry not covered; 12+ months since corpus
date; a client names specific competitors; a target market (e.g., GCC
government) is outside the confidence table.
