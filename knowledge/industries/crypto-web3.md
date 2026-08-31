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
