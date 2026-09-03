# Industry: SaaS, Dev Tools, AI Products, Productivity

## Characteristics
Sell software to evaluators and buyers. Users arrive skeptical, comparing
alternatives. Content must explain value → prove value (demo/trial) → remove
risk (pricing, security, docs). Modern standard: technical credibility with
product-real visuals, not stock abstraction.

## User intents
1. Understand what this does and for whom (10-second test)
2. Evaluate fit (features, integrations, pricing)
3. Verify credibility (customers, security, docs quality)
4. Start trial / book demo / read docs
5. Log in and use

## Business goals
Trial/demo starts, signups, PLG expansion, enterprise pipeline (demo CTA),
documentation as SEO + trust surface.

## Candidate information-architecture patterns (not a product sitemap)
- Home = positioning + social proof + feature proof + CTA
- Product/Features (per-module pages), Solutions (by role/industry),
  Pricing, Docs, Blog/Changelog, Customers, Security/Trust Center,
  Careers, About. Docs on separate path or subdomain for developers.
- App shell (dashboard) is a separate world from marketing site (see below).

## Navigation
- Persistent header: Product ▾, Solutions ▾, Resources ▾, Pricing + Sign in +
  primary CTA ("Get started"). Dropdown mega-menus with icons + descriptions
  (OBSERVED: Stripe, GitHub, Vercel pattern family).
- Docs get their own sidebar + search-first UX (docs search is the homepage).
- Version/changelog links signal engineering health.

## Candidate components observed in the genre
- Code blocks with syntax highlighting + copy button + tabs (bash/js/python) —
  the genre's trust object #1
- Terminal/IDE-styled demos; live interactive playgrounds
- Logo walls + quantified social proof ("used by 4M developers")
- Feature split sections (text + product screenshot)
- Pricing tables with monthly/annual toggle + feature matrix
- Integration grid, security badges (SOC2/GDPR), status page link
- Changelog timeline; changelog-rss for dev trust

## Visual characteristics
- The 2024–25 leader look (OBSERVED: Linear #08090a near-black, Vercel
  monochrome + geist, Stripe camille gradient accents): **dark or high-key
  minimal canvas, one accent hue, geometric grotesk (Inter/Söhne/geist),
  generous spacing, real product screenshots.**
- Inter + system mono (`var(--font-mono)`, ui-monospace) is the corpus
  default; monospace as identity accent for dev tools.
- Radius 6–12px, tight token scales (`--hds-`, `--cds-` namespaces OBSERVED).
- Subtle gradients legal (Stripe heritage) but restrained: 3–20 declarations,
  not 200.
- Micro-illustration / 3D accents on AI products (Anthropic's editorial warm
  minimalism is the counter-trend OBSERVED: serif body touches, calm palette).

## Interaction patterns
- Scroll-triggered reveals (IntersectionObserver, subtle 8–16px fade+rise)
- Tabbed feature demos, hover states on every interactive element
- Interactive pricing calculator; comparison table vs competitors
- Command palette (⌘K) on docs/apps — power-user credibility

## Mobile patterns
- Dropdown menus collapse to accordion sheets; CTAs stay visible
- Code blocks scroll horizontally, never wrap
- Pricing tables become swipeable/stacked cards

## Dashboard/app shell (productivity tools — Notion/Linear/Asana class)
- Left icon rail (56px) + contextual panel + content; dense lists 32–40px rows
- For expert/high-frequency tasks, provide scoped keyboard shortcuts and make
  them discoverable without placing shortcut chrome everywhere
- States matter more than styling: empty, loading skeletons, offline sync,
  permission-denied views
- OBSERVED: Notion ships doc-like typography inside app; Linear keeps
  13px UI text — app density ≠ marketing airiness

## Arabic/MENA considerations
- B2B Arabic SaaS exists (OBSERVED: Salla سلة, Zid زد — Arabic-first with
  Arabic display headlines, Inter+Arabic pairing on Salla, Suisse/Codec+Tajawal
  on Zid, pills 40–85px radius for playful commerce energy)
- RTL: dashboards flip fully (data tables RTL, charts keep LTR numbers),
  Arabic CTAs (أنشئ متجرك — OBSERVED on Zid)
- Trust differs: WhatsApp contact, local payment logos (mada, Fawry, COD),
  local customer logos, Arabic testimonials with real names/photos

## Conventions to evaluate (adopt only when model-supported)
Mega-menu + persistent CTA, code-with-copy, logo wall above fold, docs as
first-class product, changelog, status link, pricing honesty (no "contact us"
for core tiers), real screenshots > illustrations.

## Overused/anti-patterns
- Generic purple SaaS gradient hero + glassmorphism (the AI-slop signature)
- Fake dashboard screenshots with lorem numbers
- "Trusted by" with partner logos nobody recognizes
- Feature lists without proof artifacts (code, video, interactive demo)
-burying pricing

## Strong references
Stripe, Linear, Vercel, GitHub, Tailwind CSS, Supabase, Netlify, Cloudflare,
Framer, Notion, Anthropic (editorial counterpoint), OpenAI (container-query
adopter), GitLab, Salla + Zid (Arabic-first).

## Contextual decision prompts
Default: Inter/geist-class grotesk, dark-or-light single accent, real product
artifacts, 6–12px radii, generous but not empty spacing, code blocks that run.
For MENA B2B: Arabic-first copy with bilingual fonts, WhatsApp CTAs, local
trust marks. Justify any gradient/glass with brand system evidence.

## Corpus observations (v7.3 diversity, SOURCE-OBSERVED 2026-09-03)

SaaS is not only US developer tools.

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Regional suites (zoho served ar homepage, 10 h2; freshworks customer/employee service; lark Chat/Meetings/Docs/Projects superapp; naver-cloud) | suite or superapp nav; locale-first serving | the buyer is a company outside the US default stack | in-market productivity suites | Stripe-class single-API developer marketing | Inter+purple on Zoho/Lark is unearned; mega-nav is earned when the suite is real |
| Site builders (shopify Egypt RTL ar-EG Start/Sidekick; wix Website Builder) | locale homepage + builder promise | the product is a storefront the merchant will inhabit | merchant builders | internal admin SaaS | |

WHEN NOT: do not average GitHub docs-led density with Shopify locale
storefront marketing. Locale-first serving (Shopify ar-EG, Zoho ar) is a
product decision, not a skin.

## Corpus observations (v7.4 rejected accounting/legal-SaaS categories, SOURCE-OBSERVED 2026-09-03)

Accounting (6 fetch-ok) and law-firm practice tools did not earn categories.
They are SaaS families with different artifacts.

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Consumer tax filing (turbotax File your taxes / expert / desktop; taxact Get your maximum refund) | filing path + DIY vs expert | the artifact is a return | seasonal consumer tax | SME bookkeeping | Xero invoicing nav on TurboTax hides the refund job |
| SME accounting (xero Pricing / Invoices / Payments / Bills; freshbooks everyday small business; waveapps Accounting/Receipts/Payroll; zoho-books 32 inputs / 14 tables) | books + invoices + payroll as the suite | the buyer runs a small firm | bookkeeping SaaS | consumer 1040 wizards or banks | |
| Legal practice management (mycase case management + billing; smokeball people-law; filevine Legal AI that runs the firm) | matter + time + pay | the buyer is a firm | legal PM | public statute search (see government-public) | LII search chrome on MyCase hides dockets |
| Consumer legal documents (legalzoom business/family/IP; rocketlawyer Contract HQ; vakilsearch India legal services) | document or registration SKU | the visitor is forming an entity or a will | DIY legal docs | court databases or firm OS | |

V7.5: a helpdesk or issue tracker is a work-queue workspace, not a
SaaS marketing homepage (`interface-families/work-queue.md`). Product
docs are `interface-families/reference-docs.md`, not this file's hero.

ALTERNATIVES: tax wizard, books suite, matter OS, document SKU. Never a
unified "legal" or "accounting" template.
