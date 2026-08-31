# Industry: Finance, Banking, Fintech, Insurance, Investment, Crypto

V2 depth: dedicated crypto/web3/wallet/trading UX → crypto-web3.md.

## Characteristics
Trust-first products handling money. Users split into: consumers choosing a
bank/card/app, investors moving money, and existing customers servicing
accounts. Regulatory gravity (disclosures, KYC) shapes flows. Risk perception
is managed through design: calm, precise, evidenced.

## User intents
1. Is my money safe here? (trust sweep: regulation, protection schemes, history)
2. What does it cost? (fees, FX rates, APR — transparency = conversion)
3. Can I do X? (feature verification: send, invest, insure)
4. Open account / apply (the conversion funnel, KYC-heavy)
5. Log in and operate (daily banking: balances, transfers, statements)

## Business goals
Account/card opens, deposits (fintech), policy quotes (insurance), AUM
(investment), cross-sell (cards → loans → insurance).

## Information architecture
- Public: Home (value prop + trust) → Products (accounts/cards/loans) →
  Rates/Fees → Security → About/Regulation → Help/FAQ
- Insurance adds: quote wizard (multi-step form) + claims flow
- Investment adds: markets/dashboard teaser, fee calculator, fund pages
- Crypto adds: live prices table, earn/learn pages, status/transparency pages
- Logged-in: dashboard-first app (separate design system from marketing)

## Navigation
- Consumer banks: Personal/Business top split + product dropdowns + "Log in"
  persistent right + usually a utility bar (rates, locator, contact)
- Fintech (Monzo/Revolut/Wise OBSERVED): single-audience nav, 5–7 items,
  bold type, illustration-forward, "Get the app" CTA replacing "Sign up"
- Arabic banks OBSERVED: dense utility headers (Emirates NBD 481 links on
  home!), promo sliders, rates widgets; Al Rajhi ships DaisyUI-class tokens
  (`--rounded-btn`, `--rounded-box` OBSERVED) + heavy Tailwind

## Components that define the genre
- Rate/fee tables and calculators (savings, mortgage, FX) — the honest-object
- Card visualizers (card art rotating on hover)
- Trust strips: regulator logos, deposit-protection scheme, security badges
- Quote wizards with progress + save-and-resume
- Live market tables/mini-charts (crypto/investment)
- KYC step flows (ID → selfie → verify) with clear state feedback
- Dashboard: balance hierarchy, recent transactions, quick actions,
  insights/spending donuts

## Visual characteristics (OBSERVED)
- Banking legacy: institutional blue (PayPal #012169, Chase/HSBC navy),
  serif or neutral sans, 3–5px radius, dense utility
- Modern fintech: vivid brand color (Monzo hotcoral family tokens OBSERVED:
  `--corner-radius-medium/large` token discipline), illustration systems,
  friendly tone, 8–12px radius, rounded-but-precise
- Crypto: dark canvases + data-dense tables (Coinbase `--cds-` tokens,
  Binance), mono numerals, status greens/reds
- Insurance: calm corporate blue/green, quote forms hero-positioned
  (Prudential/AXA OBSERVED heavy CSS with token systems)
- Numbers use tabular-nums; monospace accents for IDs/addresses

## Interaction patterns
- Multi-step forms with progress, inline validation, no dead ends
- Calculators with live-updating outputs (slider → monthly payment)
- Price tables with sortable columns, sparklines
- Transfer flows: double confirmation, receipts, undo windows where possible
- Error handling is the product: clear reason + next action + support path

## Mobile patterns
- App-first fintechs: the site sells the app (store badges, QR)
- Banking: biometric login, bottom tab actions, camera-based check deposit
- Sticky "Open account" CTA on long marketing pages

## Arabic/MENA considerations (heavily OBSERVED)
- Banks serve /ar with full RTL; Emirates NBD Arabic ships icon-font arrows
  that must be mirrored (their CTA extracted as "-->" — a real mirrored-icon
  bug class to avoid)
- Arabic banking density is higher (more links, more promos) — Gulf users
  expect full self-service trees in headers
- Trust marks: central bank logos, Islamic finance markers (حلال/المرابحة
  badges, Sharia board), branch/ATM locators
- Numbers/dates in banking UIs: Western digits standard; Hijri dates shown
  alongside Gregorian for statements on leaders (INFERRED convention)
- Fintech Arabic (Fawry OBSERVED): Arabic-first with instant-en; bill payment
  grids by category (كهرباء، مياه، إنترنت) — utility-bill IA is MENA-specific
- STCPay/Neo-class (INFERRED): app-store-first funnels

## Conventions (follow)
Persistent login CTA, rates/fees visible not "contact us", calculator
objects, regulator/protection trust strip, wizard forms with resume,
dashboard previews on marketing pages, tabular numerals everywhere.

## Overused/anti-patterns
- Rocket-ship growth gradients + casual tone on a bank (trust mismatch)
- Hidden fees until step 4
- Dark-pattern countdowns on financial products (regulatory + trust risk)
- Generic glassmorphism cards for a banking dashboard ( illegible numbers)
- 12-step KYC without progress or save-resume

## Strong references
Monzo, Wise, Revolut, PayPal (ar-EG geo-localized OBSERVED), Coinbase,
Binance, Vanguard, HSBC, Emirates NBD (AR), Al Rajhi (AR), STC Pay (INFERRED),
Fawry (AR), AXA, Prudential, Mubasher (AR finance media hybrid).

## Decision guidance
Pick the register: institutional (legacy bank) vs fintech-warm (Monzo/Wise)
vs terminal-dark (crypto). All three share: tokenized numerals, honest fee
surfaces, calm interaction, error-kindness. MENA adds regulator/Islamic
trust marks + RTL-mirrored everything.
