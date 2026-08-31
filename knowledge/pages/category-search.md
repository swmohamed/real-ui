# Page Types: Category & Search Results

The workhorse pages of discovery. Category = curated tree browse;
Search = intent-driven query. Both live or die by **filter/sort ergonomics**
and **result-card scannability**.

## Category page

Purpose: browse a taxonomy with confidence ("show me everything in X, help
me narrow").

Structure:
- Breadcrumb (Home / Category / Sub) — orientation + SEO
- H1 + result count + optional description paragraph (SEO, collapsible)
- Filter rail (desktop left / mobile bottom sheet) + sort bar + view
  toggles (grid/list) where volume justifies
- Results grid (faceted) + pagination or infinite scroll
- Empty/edge states: no-results with guidance, filtered-empty with
  "clear filters" chip row

Category tile cards vs results cards: same component family; category tiles
can be image-led (no price).

## Search results page

Purpose: resolve a query. Differences from category:
- Query echo + result count ("12 results for 'nike air'")
- Corrections/suggestions ("Did you mean…", zero-result rescue with
  spell-tolerant search)
- Mixed-type results (products + categories + content) on marketplaces —
  grouped bands, not shuffled
- Recent searches + popular searches when empty-focused

## Filter system rules (the core craft)

- Facet types: single-select (category), multi-select (brand), range
  (price slider with min/max inputs), rating (threshold), boolean chips
  (in-stock, free-cancellation, RTL-friendly)
- Show facet counts (Adidas (14)) — counts guide and prevent dead-ends
- Applied filters render as removable chips above results — always
- Sort options: relevance (default for search), newest, price ↑↓, rating —
  persist across pagination
- Mobile: "Filters (3)" button opens sheet + sticky "Show 87 results" apply
  CTA (the marketplace standard, observed across ecommerce class)
- Filters update via AJAX with skeletons, never full reloads; URL reflects
  state (deep-linkable facets — SEO + shareability)

## Result card anatomy (by vertical)

- Ecommerce: image, title 2-line, price(+compare), rating, delivery/stock
  chip, badges
- Games: thumb, title, tags, rating, NEW/HOT flag
- Real estate: carousel thumb, price, icon-facts, location, agent
- Jobs: role, company, location/remote chips, salary, posted-date, apply
- Content/news: thumb, kicker, headline, timestamp

## Pagination vs infinite

- Infinite scroll: browse/mood verticals (games, fashion, social) — add
  sentinel + "back to top"; preserve position on back
- Pagination: task/compare verticals (search with page-1 expectations,
  flights, jobs) — footer crawl + countability
- Hybrid: load-more button after 2 auto-loads (respects both)

## RTL/Arabic

- Facet rail flips right; sort dropdown native RTL; price sliders flip
  (low on right)
- Result counts/dates: Western digits common in marketplaces; relative
  time in Arabic words (منذ ٣ ساعات / منذ 3 ساعات)
- Zero-result copy: helpful, not blank ("لا توجد نتائج لـ X — جرّب Y")

## Anti-patterns

- Filters that reload and lose scroll position
- Facets with zero counts shown (dead ends)
- Hidden sort; relevance-only with no alternative
- Fake result counts
- Filters that don't deep-link (refresh loses everything)
