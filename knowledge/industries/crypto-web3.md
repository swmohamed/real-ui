# Industry: Crypto, Web3, Trading

Evidence: v2 product fetch 2025-08 `[OBSERVED]` — kraken.com, coinbase.com,
bitoasis.net (MENA), rain.bh (MENA→global). Complements finance-banking.md
(read it first: trust bars, numbers discipline).

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

## DNA rules

1. **Numbers are the interface**: tabular numerals / dedicated mono
   family for prices, P&L, hashes (Kraken's custom mono `[OBSERVED]`);
   consistent decimals; red/green never sole signal (accessibility/
   contrast-motion.md).
2. Dark canvas is the genre default (v1 corpus: crypto = terminal-dark
   family `[OBSERVED]`) but light-mode = trust for onboarding/finance-
   lite products (Coinbase started light) — match audience risk
   appetite.
3. Live data everywhere: mini sparklines in lists, price flash states
   (not full-page reloads), websocket-real feel (no stale tickers).
4. Trust ladder UX: educational tiering (learn→earn), transparent
   fees BEFORE confirm, license/regulatory badges per region (MENA:
   VARA/CBB/Bahrain badges `[OBSERVED - rain/bitoasis footers]`),
   status/transparency pages.
5. Security UX as product: 2FA/MFA flows designed (not bolted on),
   withdrawal address whitelisting, session/device lists — these are
   RETENTION surfaces, not settings backwaters.
6. Wallet patterns: seed-phrase onboarding with copy friction done
   RIGHT (verify-a-word tests), gas/fee explainers per action, pending
   states with explorer links.

## Key flows (design deep)

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
Arabic numerals choice per locale (rtl/cross-platform.md); Ramadan
period trading promos; local payment rails (Fawry, KNET, mada) shown
in deposit flows; regulatory trust = region-specific badges, not
generic "regulated" claims.

## Don't

Generic fintech-blue template · hidden fees · fake scarcity pressure
(countdown timers on non-expiring offers) · meme-coin energy in
serious-tier UI · rainbow gradients hiding data density.
