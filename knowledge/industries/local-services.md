# Industry: Local Services (Home, Trades, Beauty Booking)

Not jobs-recruitment (employment). Not restaurants-food (meals). Not
real-estate (property stock). The object is a local job or appointment
fulfilled by a person nearby.

Apply `industries/README.md`. This catalog never invents two-sided
marketplaces, reviews, maps, payments, or provider tools.

Label: REAL-WORLD OBSERVATION (SOURCE-OBSERVED 2026-09-03, waves 19+21)
plus DESIGN PRINCIPLE.

## Distinct problem space

Users: households booking help, and (when in scope) the trade/pro who
fulfils it. Jobs: describe the task, get quotes or a fixed price, pick a
vetted person, book a slot, pay, review. Trust is identity + reviews +
"satisfaction guaranteed" — different from a job board's CV. Density is
category search, not a feed. Platform: often app-led fulfilment with a
web booking door. Seeker vs provider may need two surfaces
(`ux/roles-surfaces.md`).

WHEN NOT jobs: the hire is a task, not a role. WHEN NOT food delivery:
there is no menu; the inventory is labor. WHEN NOT beauty ecommerce:
Fresha/Booksy sell time, not SKUs.

## Product families (never average)

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Task / trades marketplaces (taskrabbit Book trusted help; checkatrade find a tradesperson; mybuilder hire a tradesperson; bark Find the perfect professional, 26 inputs; hipages Connect with trusted tradies; getninjas 500 tipos de serviços; myhammer Handwerker; sulekha Connect with experts; sweepsouth Bookings/Placements/Nanny; housekeep local cleaners; get-handy cleaning & handyman; lawnstarter lawn from $19) | category or "post a job" as the home | the object is a one-off or recurring home task | home/trades | salon slot-booking or field-SaaS | Indeed-class job search on Taskrabbit hides the task; Fresha slot chrome on Checkatrade hides vetting |
| On-demand home super-apps (urbancompany Arabic H1 خدمات منزلية; justlife #1 Super app cleaning/salon/repair) | many home verticals under one book CTA | high-frequency urban chores share fulfilment | dense cities with mixed chores | a single-trade directory | Grab-class grids on a plumber directory fake breadth |
| Appointment marketplaces (fresha Book local selfcare, 34 inputs; treatwell beauty routine; booksy Find & book; bokadirekt Frisör/Massage/Naglar SV; styleseat stylists; vagaro salon/spa/fitness, 106 inputs) | slot search by treatment and neighbourhood | the object is a calendar slot | beauty/wellness booking | emergency plumbing or B2B field ops | Taskrabbit "post a job" on Fresha hides the chair-time inventory |
| Pro / field software (housecallpro quoting/scheduling/payments; jobber Quoting/Invoicing/Client Hub; mindbody More revenue for studios; houzz pros+homeowners) | ops suite marketing | the buyer is the trade, not the household | field-service SaaS | consumer booking homes | consumer "book now" on Jobber hides dispatch; Jobber mega-nav on Handy hides the household job |

ALTERNATIVES: post-a-job, category directory, slot marketplace, pro OS.
Never average them.

Contaminated / not this product: kaodim returned a betting-spam page —
do not count it as local-services evidence. porch.com is now home
insurance (see insurance.md). thumbtack/trademe/localsearch were JS
shells — count if fetch-ok, do not invent IA.

## Arabic / RTL / a11y

Urban Company served an Arabic H1 on an EN URL (locale serving).
Justlife exposes العربية. Mrsool was fetch-failed. When Arabic is in
scope: RTL category names, LTR phone fields, booking times in local
numerals. Provider photos are not a substitute for name+trade+price
in text (accessibility).

## Don't

Job-board filters on a cleaning booking · restaurant menu chrome ·
mandatory maps · copying Urban Company onto a single-trade joiner ·
field-SaaS dashboards for a consumer who only needs a slot.

V7.5: a team calendar or booking-*link* product is
`interface-families/temporal-workspace.md`. Fresha/Booksy remain
appointment *marketplaces* (labor inventory), not Teamup.
