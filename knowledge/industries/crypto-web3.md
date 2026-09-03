# Industry: Crypto, Web3, Trading

Evidence: v2 product fetch 2025-08 `[OBSERVED]` — kraken.com, coinbase.com,
bitoasis.net (MENA), rain.bh (MENA→global). Complements finance-banking.md
(read it first: trust bars, numbers discipline).

Apply `industries/README.md`: distinguish an exchange, wallet, market-data
tool, protocol site, custody product, and marketing site before adopting any
pattern below. This catalog never creates trading, KYC, wallet, account,
security, or payment capabilities.

## Observed design languages

- Kraken: IBM Plex Sans + **custom Kraken Plex Mono** (dedicated mono
  for data/numbers!) + custom brand display faces; heavy 768/640
  breakpoints `[OBSERVED]`.
- Coinbase: `--cds-` token system (v1 corpus confirmation), 1280/1600
  breakpoints `[OBSERVED]`.
- BitOasis (MENA): Bootstrap base + Open Sans; conventional
  marketing-site front, app behind login `[OBSERVED]`.
- Rain: editorial-luxury take — Suisse Intl + serif headlines
  (Tiempos) `[OBSERVED]` — proof crypto ≠ one aesthetic.

## Conditional domain patterns and questions

1. **Numbers are the interface**: tabular numerals / dedicated mono
   family for prices, P&L, hashes (Kraken's custom mono `[OBSERVED]`);
   consistent decimals; red/green never sole signal (accessibility/
   contrast-motion.md).
2. Dark canvases appear in the sampled genre, but are not a default. Choose
   mode from brand, audience, task, environment, and accessibility evidence.
3. When live market data is a KNOWN capability: mini sparklines in lists, price flash states
   (not full-page reloads), websocket-real feel (no stale tickers).
4. For regulated transactional products, trust may require transparent
   fees BEFORE confirm, license/regulatory badges per region (MENA:
   VARA/CBB/Bahrain badges `[OBSERVED - rain/bitoasis footers]`),
   status/transparency pages.
5. If accounts/custody exist, security UX may include 2FA/MFA flows,
   withdrawal address whitelisting, session/device lists — these are
   RETENTION surfaces, not settings backwaters.
6. If a self-custody wallet exists: seed-phrase onboarding with copy friction done
   RIGHT (verify-a-word tests), gas/fee explainers per action, pending
   states with explorer links.

## Candidate flows by product subtype (scope required)

- Trade pair view: orderbook depth + chart + order entry — desktop =
   multi-panel (devices/desktop.md), mobile = tabbed/chart-first.
- Buy/sell flow: preview (rate+fee+total) → confirm → receipt —
  never one-tap money movement.
- KYC tiers: progressive (trade limits per tier), document upload
   states (camera guidance, glare/poor-image errors), MENA: bilingual
   document names.
- Portfolio: allocation donut + P&L period switchers; hide-balance
   affordance (screenshot-safety habit).

## MENA specifics

Bilingual AR/EN with financial-terminology care (محفظة/محفظة رقمية);
Arabic numerals choice per locale (rtl/cross-platform.md). Seasonal campaigns,
local payment rails (Fawry, KNET, mada), and regulatory badges appear only
when the product, processor, jurisdiction, and supplied evidence support them;
never fabricate a payment method, promotion, or authorization.

## Don't

Generic fintech-blue template · hidden fees · fake scarcity pressure
(countdown timers on non-expiring offers) · meme-coin energy in
serious-tier UI · rainbow gradients hiding data density.

## Corpus observations (v7.1 growth: 13 products SOURCE-OBSERVED 2026-09-03)

| Family (n) | Observed shape | Why it differs | When / when NOT |
|---|---|---|---|
| Data terminals (coingecko, defillama) | dense sortable tables; defillama nav = Dashboards/Metrics/Tools/Chains | users monitor positions/TVL; scanning is the job | analytics; NOT onboarding surfaces |
| Explorers (etherscan: 3 forms/22 inputs; blockscout) | query machines: search boxes everywhere, hash/tx/address lookups | deep-link + exact-lookup traffic dominates | explorers; never style as marketing |
| Wallets (metamask, phantom, rainbow) | feature marketing (10 h2) or near-empty one-liner; download CTA is the page | conversion = install; product lives in extension | wallet landing; NOT trading surfaces |
| Exchanges (kraken, gemini, kucoin, bitoasis) | trust-first: regulation, security, tiers | money custody demands credibility before features | trading; NOT wallets/data |
| MENA regulated (rain.bh RTL, coinmENA, bitoasis) | bilingual/regional compliance framing | local licensing is the differentiator | regional exchanges |

WHY: consequence + audience. A trader's terminal optimizes density; a
first-time buyer needs trust and guidance; an engineer using an explorer
needs query speed. There is no unified "crypto aesthetic" in the corpus —
families share almost nothing structurally. Never import exchange trust
chrome onto a data terminal or vice versa.

## Corpus observations (v7.3 diversity, SOURCE-OBSERVED 2026-09-03)

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Regional exchanges (mercadobitcoin Quem somos / Seguranca / Ouvidoria, pt; wazirx India exchange; upbit ko shell) | local trust + ombudsman language | licensing and complaint paths are the differentiator | in-market exchanges | a DeFi terminal or a wallet landing | defillama density on Mercado Bitcoin hides ouvidoria |
