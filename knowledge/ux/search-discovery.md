# UX: Search & Discovery

## Search contract (before the search box)

Model the retrieval system before selecting its presentation:

- **Corpus and scope:** which entities, fields, workspaces, connected sources,
  dates, languages, and permission boundaries are searched?
- **Intent:** known-item lookup, discovery, comparison, command, or answer
  synthesis? These may need different result structures.
- **Freshness:** live, indexed, cached, or delayed; when does stale information
  change a decision?
- **Ranking:** exactness, recency, popularity, personalization, business rules,
  or semantic similarity; make consequential promotion or personalization
  understandable.
- **Grounding:** distinguish retrieved records from generated summaries. When
  synthesis affects a decision, preserve source, authorship, and freshness.
- **Recovery:** no permission, unavailable source, stale index, partial source,
  no match, and query failure are different states.

If search includes generated answers, recommendations, or actions, also apply
`ai-automation.md`; a synthesized answer does not erase the result set or its
source boundaries.

## Search UX pipeline

1. **Entry**: place search according to task frequency, not page genre; name
   or expose scope when users can search multiple corpora.
2. **Assist**: use autocomplete, recent queries, examples, filters, or grouped
   suggestions only when available data and user intent support them.
3. **Execute**: tolerate typos where safe; support transliteration where the
   catalog and audience require it (MENA: Arabic↔English brand names).
4. **Results**: echo query and scope; expose count or completeness only when
   reliable; group mixed entities when that improves comparison or action.
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

Learning products are not one discovery shape. A skill library may be
search + trending shelves; a private academy may be path/career nav; a
tutor product is a people index; open courseware is a packet/explorer; a
classroom LMS is a class list / join code; a habit app is a next-action
queue. Cards are one option (`industries/education.md`). Do not default
a course-card grid because the industry is education.

File libraries search names, types, and people. Messengers search
threads and messages. Comparison products search then align attributes
(`ui/data-display.md`). Do not give all three a product-card grid.

## Personalization honesty

- "Recommended for you" rows only when data justifies the label;
  otherwise "Popular in Cairo" (transparent context) beats fake personal
- Recently-viewed rows: opt-out-able, honest
- Cold-start: popularity-by-region/season beats empty personalization

## Search analytics loop (product maturity signal)

Track: zero-result queries (content gaps), first-result CTR, query
reformulation rate, filter usage. Design improvement comes from these
numbers, not vibes.

## Voice/visual input (conditional capability)

- Do not add voice or visual search because a product is mobile, regional,
  retail, or fashionable. It must be KNOWN, REQUESTED, or proven necessary
  support UX for an existing input capability.
- For voice, show recording state, stop/cancel, editable transcription,
  language handling, permission purpose, error recovery, and a non-voice path.
- For visual input, show capture/upload choice where supported, permission and
  data-use purpose, processing state, editable query/refinement, and a
  non-camera path.

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
- Generated summaries with hidden corpus, permissions, freshness, or sources
