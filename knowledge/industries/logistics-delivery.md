# Industry: Logistics, Delivery & Shipment Tracking

Evidence upgrades (v2.1, OBSERVED): bosta.net (Egyptian logistics
leader — fetched 2026-08: utility-first CSS, 640/550/990/860 bps,
sale-banner tokens) and splonline.com.sa (Saudi Post/SPL — app-shell,
minimal inline CSS, logged as thin evidence). Aramex/DHL remain
bot-blocked (see research/reports/v2.1-research-log.md); knowledge
below mixes OBSERVED (where marked) + corpus patterns + stable
conventions. Complements restaurants-food.md (food delivery) and
ecommerce-marketplace.md (shipping steps of checkout).

Apply `industries/README.md`. Distinguish public tracking, consumer shipping,
merchant operations, courier tooling, and a marketing site. Tracking, maps,
notifications, proof capture, addresses, COD, quoting, pickup, and driver
location are separate capabilities that require scope evidence.

## Conditional domain patterns and questions

1. **On a public tracking surface**, AWB/waybill search may be the
   primary function (like jobs' keyword search) — big, single-field,
   paste-friendly; sample-number hint; recent-track memory.
2. **When milestone event data exists**, a timeline is a strong candidate
   (Booked → Picked up → In transit hub(s) → Out for delivery →
   Delivered) with timestamps + location names; current step animated/
   highlighted; future steps ghosted but visible (progress honesty —
   ux/states.md).
3. A map may supplement—but should not replace—an accessible textual status
   history when live location is in scope; it is not required
   timeline (timeline works offline/poor network — mobile-states.md).
4. Status vocabulary human-first: "Arrived at Dubai hub" not
   "DEP-SCN-045 COMPLETED"; exception states (customs hold, address
   issue) with ACTION (what do I do now) — exceptions are the real UX
   test of a logistics product.
5. If notifications exist, cadence may follow milestone events (not every scan); quiet
   hours; delivery-day granularity (window picker where supported).
6. If proof of delivery exists: signature/photo/time-stamp receipt — success
   state = shareable artifact (ux/trust-conversion.md).
7. If address capture is in scope, MENA contexts may need pin-drop + landmark text + what3words-
   style helpers; "villa/apartment/office" selectors; saved addresses
   with labels; Arabic address entry (number-street patterns differ
   from Western) `[DESIGN PRINCIPLE - MENA]`.

## Possible multi-surface model (only when supplied)

Consumer tracking (above) + business shipping (quote → pickup booking
→ bulk print labels → invoices) — b2b-enterprise density for the shipper
portal, consumer clarity for the recipient page. Courier/driver app =
third surface: route list, proof capture (camera states), offline-first
(mobile-states.md).

## Key flows

- Track: enter AWB → timeline (+map) → share/copy status → notify-me.
- Ship (consumer): quote calculator (origin/dest/weight) → pickup
  booking → label/QR.
- Delivery-day: live driver view (ETA chip, delay honesty), delivery
  instructions edit until cutoff, reschedule affordance.

## MENA specifics

When COD is supported, its return/refusal flow needs explicit states. Public
bilingual tracking URLs can preserve locale when shared. Customs/return
certificate states, WhatsApp/SMS channels, and Ramadan/Eid peak handling are
conditional on route, market, product operations, and supplied evidence—not
regional defaults to invent.

## Don't

Marketing-site cosplay on the tracking page · spinners where a
timeline should be · jargon dumps · map-only tracking · dead links to
"contact support" as exception handling.

## Corpus observations (v7.1 growth: 11+ products SOURCE-OBSERVED 2026-09-03)

| Family (n) | Observed shape | Why it differs | When / when NOT |
|---|---|---|---|
| Consumer tracking hubs (17track, parcelsapp, aftership) | tracking widget is the hero; product marketing + API tiers below (9–10 h2) | anonymous visitor's #1 job: paste a number | multi-carrier tracking; NOT carrier sites |
| Carrier mega-sites (fedex, dpd, bring, postnl, aramex) | track + ship + support + business split; heavy nav | brand covers the full journey; enterprises AND consumers | carriers; NOT pure trackers |
| Freight/B2B platforms (maersk, flexport, freightos) | enterprise-lead surfaces, quote flows (freightos 14 inputs) | sales cycle, not self-serve clicks | B2B freight; NOT parcel UX |
| Developer APIs (easypost, shippo) | docs/pricing-first, code samples prominent | buyer = engineers | API products; NOT consumer surfaces |
| Regional last-mile (instabox, bosta, naqel, mylerz) | lean consumer pickup/delivery flows, local language | doorstep trust in-market | regional ops; NOT global platforms |

WHY: the payer splits the family (consumer time / shipper money /
developer integration / enterprise contract). Tracking-first surfaces must
survive with ZERO browsing intent — a number in, a status out. B2B freight
inverts everything: quote forms, relationship, sales assist.

## Corpus observations (v7.3 diversity, SOURCE-OBSERVED 2026-09-03)

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| National posts (correios Enviar / Receber / Comprar / Logistica / Atendimento, 3 forms / 15 inputs) | send, receive, and shop under one public brand | the post office is a counter + a shop | national postal operators | multi-carrier tracking hubs | a 17track paste-box on Correios hides counter services |
| Regional last-mile ecom (jtexpress Track / Merchant login / Locate points) | merchant + consumer track | last-mile brands serve shops first | SEA ecom couriers | freight quote tools | |

Ninjavan returned a thin shell — do not invent a network map from it.
