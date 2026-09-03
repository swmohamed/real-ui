# Industry: Finance, Banking, Fintech, Insurance, Investment, Crypto

V2 depth: dedicated crypto/web3/wallet/trading UX → crypto-web3.md.
V7.4: consumer/takaful/aggregator insurance UX → insurance.md. Keep
banking, remittance, neobank, and payments families here. Do not design
an insurer as a bank dashboard.

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

## Candidate information-architecture patterns (not a product sitemap)
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

## Candidate components observed in the genre
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

## Conventions to evaluate (adopt only when model-supported)
Persistent login CTA, rates/fees visible not "contact us", calculator
objects, regulator/protection trust strip, wizard forms with resume,
product previews on marketing pages only when real/supplied; use tabular
numerals where aligned numeric comparison benefits from them.

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

## Contextual decision prompts
Pick the register: institutional (legacy bank) vs fintech-warm (Monzo/Wise)
vs terminal-dark (crypto). All three share: tokenized numerals, honest fee
surfaces, calm interaction, error-kindness. MENA adds regulator/Islamic
trust marks + RTL-mirrored everything.

## Corpus observations (v7.2 knowledge integration, SOURCE-OBSERVED 2026-09-03)

Fetched remittance / neobank / business-bank / MENA-payments products showed
that "finance site" is not one IA. Corridor, plan, and suite are different jobs.

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Remittance corridors (remitly Personal/Business + Help; worldremit converter + app; westernunion Send/Receive/Track/Find locations, Egypt-localized; paysend infrastructure framing) | from/to/amount (or send/receive/track) as the page; help and locations as utilities | the job is moving a sum along a corridor, not opening an account | money-transfer products | consumer banks and spend platforms | rate/fee honesty in the widget beats brand hero; a plan-comparison nav hides the corridor |
| Consumer neobank (n26: Standard/Smart/Go/Metal + Business plan tree, 10 h2) | plan comparison is the public IA | conversion is picking a tier | consumer banking with packaged plans | remittance or SME spend | feature matrices read commercial; corridor widgets on a bank hide deposits/cards |
| Business banking / spend (mercury: Checking, Loans, Treasury, Credit, Spend, demo dashboard; tide: company registration + secretary + virtual office; brex: Customers/Pricing/demo) | suite of money-ops products + demo/sign-in | buyer is a company; the product is operating spend | startups/SME finance | consumer remittance | demo-gated dashboards are legitimate; consumer get-the-app CTAs undersell ops |
| MENA payments (fawry corporate: Company/About/What we do; valu Egypt: Personal product tree U/ShopIT/Flip/Sha2labaz/Cards) | corporate-group site vs BNPL product family | Fawry-class is a payments network; Valu-class is consumer credit SKUs | match the legal entity | importing Revolut-warm onto a bill-payment grid | Arabic-first bill grids (existing Fawry observation) stay valid for consumer pay; they are the wrong chrome for a corporate IR site |

ALTERNATIVES: corridor widget, plan matrix, spend-suite mega-nav, bill-category
grid. Pick from who sends money and whether the product is a transfer, an
account, or a network.

## Corpus observations (v7.3 diversity, SOURCE-OBSERVED 2026-09-03)

Mobile-money and national UPI/wallet super-apps are not neobanks.

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Mobile money / agent networks (mpesa: About / Legal / Journey, 6 forms / 20 inputs; wave Personal/Business) | education + legal + agent-trust, not a plan matrix | the product is a cash-in/cash-out network; the web explains and onboards | MNO wallets, agent cash-out | consumer neobanks (n26-class plans) | a Metal/Go plan tree on M-PESA hides agent and legal; a corridor widget on a wallet hides bills/airtime |
| National payment super-apps (paytm: Flights / Bus / Trains beside UPI; gcash #1 Finance Super App Services/Partners; touchngo) | pay + recharge + travel in one nav | high-frequency bill/QR pay expands into adjacent trips | wallet-first markets | remittance corridors or SME spend-suites | travel tabs on a bank homepage fake a super-app |
| African payment processors (paystack Why/Success Rates/Demo For Entrepreneurs/Corporates; flutterwave business possibilities) | docs + success-rate proof + demo | buyer is a merchant integrating payments | processor marketing | consumer wallets | |
| Regional neobank (nubank pt-BR) | sparse Portuguese consumer home | local-language consumer bank, not a US fintech clone | in-market consumer credit | English-only plan matrices in BR/ID | |

ALTERNATIVES: agent-network explainer, QR/UPI super-app, processor demo,
consumer neobank. Pick from cash-in method and who holds the balance.

## Corpus observations (v7.4 category split, SOURCE-OBSERVED 2026-09-03)

Consumer quote / takaful / aggregator insurance is now `insurance.md`.
Do not keep designing an insurer as a bank. AXA/Prudential-class group IR
that was fetched as `insurance` moves with that module; remittance,
neobank, and payments stay here.
