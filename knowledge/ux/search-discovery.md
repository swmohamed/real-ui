# UX: Search & Discovery

## Search UX pipeline

1. **Entry**: prominent placement (header center for search-dominant;
   header icon expanding for content sites; hero-embedded for
   marketplaces/travel)
2. **Assist**: autocomplete (fast <100ms feel), thumbnails in suggestions,
   recent searches (localStorage), popular/trending when empty, category
   grouping (Products/Pages/Help)
3. **Execute**: tolerate typos (fuzzy), transliteration where expected
   (MENA: Arabic↔English brand names both hit), Enter = full results
4. **Results**: query echo + count; relevance default; mixed-type bands
5. **Recover**: zero-state rescue — did-you-mean, top categories, popular
   items; NEVER dead-end

## Facets & filters (see category-search page for UI detail)

The UX principles: counts on facets, applied-filter chips, never lose
state on reload, filters never require page 1 reset unless results shrink.

## Discovery vs known-item

- Known-item search: optimize precision — exact matches first, SKU/ID
  support, copyable URLs
- Discovery browse: optimize inspiration — editorial shelves, "because
  you viewed", mood tags, surprising-but-relevant adjacents
- Most real products serve BOTH: search bar (known) + shelves (discovery);
  don't force one paradigm

## Personalization honesty

- "Recommended for you" rows only when data justifies the label;
  otherwise "Popular in Cairo" (transparent context) beats fake personal
- Recently-viewed rows: opt-out-able, honest
- Cold-start: popularity-by-region/season beats empty personalization

## Search analytics loop (product maturity signal)

Track: zero-result queries (content gaps), first-result CTR, query
reformulation rate, filter usage. Design improvement comes from these
numbers, not vibes.

## Voice/visual search

- Voice input on mobile (search icon mic) — growing in AR/EN
- Visual search (image → similar products): fashion/home verticals;
  gate behind camera permission with clear purpose copy

## RTL/Arabic search specifics

- Placeholder and query direction: dir="auto" on input so Latin queries
  type LTR inside RTL UI; align field start
- Normalize: alef variants (أإآا), taa marbuta/haa (ة/ه), yaa (ي/ى) in
  matching — real Arabic search engines normalize; UI should not fight it
- Arabic numerals queries should match Western-digit data (normalize ٥→5)
- Bilingual catalogs: search both scripts, display both
  (شاهد Shahid pattern OBSERVED)

## Anti-patterns

- Search that requires login; search icon hidden behind hamburger
- Autocomplete that ignores input after focus (race conditions)
- Zero results with no suggestions
- Facets that filter to nothing silently
- Promoted results disguised as organic (label them — FTC/regional
  equivalents)
