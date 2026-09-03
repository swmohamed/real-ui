# V4 Reasoned Regression and Negative Scenarios

Classification: **REASONED-SPEC**. Manually traced on 2026-08-31 against the
current routing and authority contracts. This is not an executed agent,
runtime, browser, native-app, or render test. Executable repository safeguards
for these rules live in `test_skill_invariants.py`.

For every scenario, the trace must begin with CLASSIFY → MODEL/SCOPE and load
page/industry authority contracts before catalogs. “Satisfied” below means the
current instructions force the required reasoning artifact; it does not prove
a future model will comply.

| # | Scenario / attempted failure | Required trace | Manual result |
|---|---|---|---|
| 1 | Unknown niche: dental-clinic staff tool | entities + today's-schedule top task + content priority → schedule/timeline; no marketing hero | SATISFIED by product-modeling + page authority |
| 2 | Same industry: retail bank vs pro trading terminal | shared trust constraints; different tasks/volume/representation/density; difference justified, not randomized | SATISFIED by product model + originality dials |
| 3 | Similar local restaurant products | similar structures allowed when tasks/content/brand evidence align | SATISFIED by legitimate-similarity guard |
| 4 | Dense shipment admin list | 5,000 comparable rows → table/grid; card default rejected | SATISFIED by representation matrix + cards decision table |
| 5 | Greenfield gaming portal; prompt does not mention ads/accounts | ads, monetization, progression, accounts remain HYPOTHESES/OUT OF SCOPE | SATISFIED by all-design scope ledger + industry contract |
| 6 | Ecommerce page; prompt does not mention subscription | page/industry catalog cannot create subscriptions, loyalty, reviews, recommendations, or account | SATISFIED by scope and pricing/PDP contracts |
| 7 | Gaming FULL REDESIGN with resume/progression | extract capabilities, quarantine presentation, re-derive IA; close ledger; fail on silent loss or shallow restyle | SATISFIED by depth/extraction/workflow hard gates |
| 8 | “Polish spacing” request | classify POLISH; composition locked; no extraction/re-derivation churn | SATISFIED by depth precedence and conditional stage 1.5 |
| 9 | Mobile analytics workspace | preserve top task and comparison; state what moves/condenses/transforms; no stack-everything rule | SATISFIED by page/responsive authority + finish gate |
| 10 | Arabic bilingual results with SKUs/emails | direction and navigation adapt; mixed data stays bidi-isolated; no blind mirroring or heuristic-only sizing | SATISFIED by RTL + i18n evidence labels |
| 11 | Android desktop-sized window | use dynamic width/height classes including large/extra-large; not device-name checks | SATISFIED by current platform rules |
| 12 | Accessible compact toolbar | distinguish WCAG AA 24px-or-exception from 44px enhanced/platform guidance; nonmodal popover does not trap focus | SATISFIED by corrected accessibility/component rules |
| 13 | Paid landing page without testimonials/security claims | catalog cannot fabricate proof, logos, metrics, or integrations; message match remains | SATISFIED by landing scope warning |
| 14 | Search results on server-rendered site | URL/state/focus continuity required; AJAX not mandated | SATISFIED by corrected page guidance |
| 15 | `Design a new ecommerce website` | NORMAL; full product/domain/design workflow, no repository audit | SATISFIED by mode router |
| 16 | `Full redesign this existing gaming website` | NORMAL; FULL depth + extraction/re-derivation, no Deep/Audit dependency | SATISFIED by mode router + redesign depth contract |
| 17 | `Design a Flutter finance app` | NORMAL; platform/domain/mobile/a11y knowledge remains available | SATISFIED by mode router |
| 18 | `Audit the entire REAL-UI knowledge base` | DEEP/AUDIT; repository-wide validation is in scope | SATISFIED by mode router |
| 19 | `Validate all REAL-UI research and repair unsupported claims` | DEEP/AUDIT; evidence-wide research audit is in scope | SATISFIED by mode router |

## Negative gate expectations

The following outcomes are explicit FAIL conditions that return work to
reasoning rather than merely producing warnings:

- FULL REDESIGN whose style-blind structure remains a restyle without
  product/UX justification;
- any old capability missing from the new coverage matrix;
- any new capability lacking KNOWN/REQUESTED/NECESSARY SUPPORT UX evidence;
- inaccessible semantics/focus/contrast/reflow in the delivered surface;
- mobile adaptation that only shrinks/stacks without preserving task and
  information priority.

Runtime/render result: **UNVERIFIED — no isolated agent execution or product
render harness is available in this repository.**
