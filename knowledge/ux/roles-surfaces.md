# Roles and Surfaces

Roles are not hidden buttons. When two actor classes have incompatible
jobs, density, risk, or launch context, the product often needs two
surfaces — or two apps — not one chrome with a permission flag.

Label: DESIGN PRINCIPLE + REAL-WORLD OBSERVATION (SOURCE-OBSERVED
2026-09-03, waves 33–34 and 36). Most public URLs are marketing. They
prove that host/guest, driver/rider, seller/buyer, creator/audience,
and merchant/customer are named as different jobs. They do not
authorize invented operator consoles. YouTube Studio redirected to
Google sign-in — do not invent Studio IA from that URL.

Actors already live in `foundations/product-modeling.md`. This file
stores WHEN one surface is enough and WHEN it is not.

## Distinct problem

A rider opening Uber Egypt sees Ride / Drive / Business / Uber Eats as
**jobs to pick**, not as admin toggles. Airbnb's guest homepage
("Vacation Rentals…") is a different page from `/host/homes` ("Your
home could make money"). Grab's nav names Consumer / Driver / Merchant
/ Enterprise as peer audiences. Fiverr puts **Become a Seller** next to
the freelancer marketplace. Vinted's title is "Sell and buy". OLX
resolved to Dubizzle Egypt (`lang=ar dir=rtl`) — a classifieds product
where listing and browsing are both first-class.

Hiding "Host" in a settings menu does not make a guest product into a
host product.

## Patterns (never average)

| Pattern | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Two-sided marketplace, one brand (vinted sell and buy; fiverr Become a Seller; olx/dubizzle RTL classifieds; mercadolibre country picker; etsy-sell "How to sell on Etsy Egypt") | buy and sell (or hire and work) as peer jobs | both sides must succeed or the market dies | classifieds, freelance, resale | a single-vendor store | Operator density on the buyer home hides shopping; storefront chrome on the seller tools hides inventory risk |
| Separate apps per role (uber vs uberdriver Play listings; airbnb listing vs host page; grab.com/driver vs consumer home) | different install or different site | jobs, notifications, and maps diverge enough that one IA would lie | driver/rider, host/guest, captain/passenger | a CMS where "admin" is only extra fields on the same object | One app with a mode switch is cheaper and easier to lose the wrong user in. Two apps cost install friction |
| Super-app audience switcher (grab Consumer/Driver/Merchant/Enterprise; gojek super app; careem "everything app" Go/Eat/Get/Pay; bolt Ride vs Earn money; rappi Únete) | named audiences, not features | the company sells several jobs under one brand | multi-sided local platforms | a single kitchen or a single airline PNR | A four-audience grid on a one-job product is costume (`foundations/modern-craft.md`) |
| Creator / audience split (patreon creator communities; substack; twitch Creator Camp; youtube audience home vs Studio sign-in) | watch/read vs publish/analytics | creation tools would wreck the watch surface | media and membership | a private notes app | Putting Studio analytics on the YouTube watch home hides the video. Do not invent YouTube Studio from a login URL |
| Merchant platform vs customer (shopify commerce platform marketing; stripe infrastructure vs register; booking Partner Hub "Register your property") | builder/operator tools vs the resulting customer product | the merchant product is not the storefront | platforms that mint other UIs | a simple restaurant site | Shopify admin on a brand storefront hides the goods; a consumer checkout as the Stripe home hides financial ops |
| Hire vs seek (linkedin Jobs vs People vs Learning; teacheron Find teachers / Teaching Jobs; coursera For Individuals / Business / Universities) | two searchers, two detail pages | the query and the proof differ | jobs, tutoring, B2B education | a single-learner habit app | Recruiter filters on a candidate profile hide the person |

ALTERNATIVES: one surface + permission-aware actions · mode switch in
one app · two apps · two sites under one brand · super-app switcher.
Pick from how far the jobs, notifications, maps, and risk diverge.

## When one surface is enough

Keep one IA when:

- the same objects and tasks serve every actor (a shared doc with
  comment vs edit — `ux/collaboration-concurrency.md`);
- the difference is a field or a button, not a launch job;
- volume is low and role changes are rare.

Permission-denied, view-only, and approval states are still required.
They are not a second product.

## When two surfaces are required

Split when:

- launch context differs (open the app to ride vs to earn);
- home objects differ (listings vs reservations; inbox vs catalog);
- notification grammar differs (trip request vs order confirmation);
- maps/sensors differ (driver navigation vs passenger ETA);
- risk differs (payouts, KYC, inventory vs browsing).

Then write **two product models**, two scope ledgers, and two screen
contracts. Shared brand is not shared layout
(`redesign/preservation.md`).

## Mobile

Play listings for Uber and Uber Driver are **different apps**, not a
toggle. Airbnb, Grab, Careem, Etsy, Vinted listings are role-aware.
Do not learn DESKTOP ADMIN → SHRINK → MOBILE SELLER. Camera, GPS, and
background location belong to the role that actually captures or
navigates (`ux/mobile-states.md`).

## Don't

A single "dashboard" with role dropdown as the design · averaging
Airbnb host tools with Uber Driver and Shopify admin · inventing
seller analytics because Fiverr has a seller CTA · treating "admin"
as an industry · copying Grab's four-audience nav onto a bakery site.
