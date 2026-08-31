# Industry: Logistics, Delivery & Shipment Tracking

Evidence upgrades (v2.1, OBSERVED): bosta.net (Egyptian logistics
leader — fetched 2026-08: utility-first CSS, 640/550/990/860 bps,
sale-banner tokens) and splonline.com.sa (Saudi Post/SPL — app-shell,
minimal inline CSS, logged as thin evidence). Aramex/DHL remain
bot-blocked (see research/reports/v2.1-research-log.md); knowledge
below mixes OBSERVED (where marked) + corpus patterns + stable
conventions. Complements restaurants-food.md (food delivery) and
ecommerce-marketplace.md (shipping steps of checkout).

## DNA rules

1. **Tracking number is the hero**: AWB/waybill search = homepage's
   primary function (like jobs' keyword search) — big, single-field,
   paste-friendly; sample-number hint; recent-track memory.
2. **Timeline = the core component**: vertical milestone timeline
   (Booked → Picked up → In transit hub(s) → Out for delivery →
   Delivered) with timestamps + location names; current step animated/
   highlighted; future steps ghosted but visible (progress honesty —
   ux/states.md).
3. Map view = second citizen (driver pin, ETA), never replaces the
   timeline (timeline works offline/poor network — mobile-states.md).
4. Status vocabulary human-first: "Arrived at Dubai hub" not
   "DEP-SCN-045 COMPLETED"; exception states (customs hold, address
   issue) with ACTION (what do I do now) — exceptions are the real UX
   test of a logistics product.
5. Notifications cadence: milestone events (not every scan); quiet
   hours; delivery-day granularity (window picker where supported).
6. Proof of delivery: signature/photo/time-stamp receipt — success
   state = shareable artifact (ux/trust-conversion.md).
7. Address UX (MENA-critical): pin-drop + landmark text + what3words-
   style helpers; "villa/apartment/office" selectors; saved addresses
   with labels; Arabic address entry (number-street patterns differ
   from Western) `[DESIGN PRINCIPLE - MENA]`.

## Two-sided reality

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

COD (cash on delivery) as first-class payment everywhere (return-flow
UX matters — COD refusal rates shape flows); bilingual AR/EN tracking
pages (public URLs — share across languages); customs/RC (return
certificate) states for cross-border GCC; WhatsApp/SMS-first
notification habits over email; Ramadan/Eid peak-season load patterns
(quick-edit + SLA honesty under stress).

## Don't

Marketing-site cosplay on the tracking page · spinners where a
timeline should be · jargon dumps · map-only tracking · dead links to
"contact support" as exception handling.
