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

## Information architecture
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

## Components that define the genre
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
- Keyboard-first: shortcuts everywhere, visible in tooltips
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

## Conventions (follow)
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

## Decision guidance
Default: Inter/geist-class grotesk, dark-or-light single accent, real product
artifacts, 6–12px radii, generous but not empty spacing, code blocks that run.
For MENA B2B: Arabic-first copy with bilingual fonts, WhatsApp CTAs, local
trust marks. Justify any gradient/glass with brand system evidence.
