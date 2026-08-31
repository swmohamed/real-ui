# SEO-Aware Design (structure that search engines + users both reward)

SEO is a supporting discipline here: it constrains structure and content
architecture, never overrides UX.

## Structural fundamentals

- One h1 per page (matches the corpus's real discipline); logical h2/h3
  outline (screen readers + crawlers read the same tree)
- Landmarks + semantic HTML (SEO and a11y share this skeleton)
- Clean URL grammar: /category/sub/item-slug; translated slugs for Arabic
  (ranks for Arabic queries); avoid parameter chaos
- Breadcrumbs + BreadcrumbList schema (OBSERVED: NBA, beIN ship it)
- Internal linking: related-content rails, tag/topic pages, footer trees
  — crawl paths are UX paths

## Content architecture

- Page-per-intent: category pages target browse queries ("ألعاب سيارات"),
  PDPs target product queries, guides target informational queries
- Unique meta: title (≤60ch, front-load keyword naturally) + description
  (≤155ch, benefit + CTA) per page — templates for scale with dynamic
  fields
- Pagination vs infinite: paginated with rel canonical chain for crawl;
  or load-more with static page 1 content in DOM
- Faceted navigation: crawlable canonical + noindex thin combos;
  filter URLs canonicalized

## Structured data (JSON-LD — the observed leader set)

- Organization + WebSite (+SearchAction sitelinks box — OBSERVED on
  Apple/Almosafer)
- Product (+Offer, AggregateRating) on PDPs; Article/NewsArticle with
  dates on editorial; FAQPage where real FAQs; BreadcrumbList; LocalBusiness
  for physical (restaurants/branches — MENA branch pages matter);
  Event for events; VideoObject with thumbnail
- Validate: Rich Results Test; mark only visible content

## Media & speed (SEO is CWV now)

- Image alt informative (also image-search entry); descriptive filenames
  (red-nike-air-max.avif); video transcripts/captions
- CWV targets (performance file) — ranking input
- No content behind JS-only walls for critical text (SSR/SSG for
  content pages; OBSERVED corpus majority server-renders)

## International/multilingual (the MENA reality)

- hreflang pairs (ar, en, ar-SA/ar-EG if market-differentiated) +
  x-default; self-referencing canonicals
- Language versions: full parity, not machine stubs (thin translations
  rank poorly + convert worse)
- ccTLD vs /ar/ paths vs subdomains: pick one, hreflink consistently;
  observed leaders use path segments (amazon.eg/-/ar/ class)
- Local search signals: Arabic NAP consistency, Google Business Profile
  for branches, regional schema (LocalBusiness with openingHours incl.
  prayer-time breaks where culturally relevant)

## Design decisions with SEO consequences

- Hero text as image = invisible promise (also a11y fail)
- Infinite scroll without static first-screen content = crawl gaps
- Modal-gated pricing/docs = invisible pricing/docs
- One-page JS sites = one URL to rank; content sites need real pages
- Internal search results = noindex (Google guidance) but make them
  GREAT for users

## Anti-patterns

- Keyword-stuffed copy (write for users; structure for machines);
  cloaked text/links; doorway pages per city with spun content; buying
  link networks; schema spam (marking invisible content)
