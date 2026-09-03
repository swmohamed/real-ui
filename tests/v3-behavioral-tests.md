# V3 Reasoned Specification Scenarios (product modeling · variation · content design · cards · i18n)

Method: manually reason each scenario through the skill files and record
what the workflow would be expected to produce. This is not executable agent,
runtime, or render validation. PASS = a prior trace found the behavior forced
by an explicit instruction (not merely plausible). Each test names the
files that must fire.

## T1 — Niche product, no exact industry file (product modeling)

**Scenario:** "Design a web app for a dental clinic's front desk:
manage appointments, patient records, invoices. Staff-only tool."
**Must fire:** taxonomy (healthcare + b2b axes) → foundations/
product-modeling.md → MODEL step before any IA.
**PASS requires:**
- [ ] Entity list produced (patients, appointments, practitioners,
      invoices) BEFORE any layout talk
- [ ] Top task ranked ("run today's schedule") → home = schedule-first,
      NOT a marketing hero, NOT a generic dashboard
- [ ] Relationship 1→n → drill-down pattern chosen explicitly
- [ ] Volume 30–80/day → dense table/timeline, no decorative spacing
- [ ] Industry deviation logged with reason (no trust badges — internal tool)

## T2 — Same industry, different structures (variation dials)

**Scenario:** "Design (a) a retail consumer bank marketing site and
(b) a pro trading platform — same industry file."
**Must fire:** finance-banking.md + originality.md "Variation within
an industry" + product-modeling.
**PASS requires:**
- [ ] Five dials written for each product and DIFFERING (density airy↔
      dense; silhouette marketing↔app shell; nav top↔rail; rhythm
      editorial↔table; register warm↔technical)
- [ ] Difference justified by model (audience expertise + task verb),
      not randomness
- [ ] No color-swap-only differentiation

## T3 — Same model, same structure (legitimate similarity)

**Scenario:** two local restaurant ordering sites, same audience/task.
**PASS requires:** similar structure accepted WITH the originality.md
rule quoted — variation serves requirements, not novelty.

## T4 — Cards decision

**Scenario:** "Admin screen listing 5,000 shipments with 8 sortable
fields, status lifecycle, filters."
**Must fire:** ui/cards.md "When NOT to use a card" + data-display.
**PASS requires:** table/data grid chosen over cards with the content-
shape reason (dense/comparable/many attributes).

## T5 — Content design

**Scenario:** checkout fails: card declined. Arabic+English product.
**Must fire:** ux/content-design.md error formula + forms-validation.
**PASS requires:** what+why+fix copy in both languages; no "Oops!";
destructive-style clarity; field keeps user input.

## T6 — i18n beyond RTL

**Scenario:** German + English SaaS pricing page; French market dates.
**Must fire:** localization/i18n.md (+ NOT rtl/*).
**PASS requires:** +20–35% width survival stated; date format per
locale; plural templates not concatenation; one number system/surface.

## T7 — Regression: Arabic news site (V1 spine)

**Scenario:** Arabic-first news portal, mobile + desktop.
**PASS requires:** old routing intact — news-media + pages/homepage +
arabic-typography + rtl/* + visual-dna load path unchanged; finish gate
runs RTL + a11y + perf checks as before.

## T8 — Regression: redesign path

**Scenario:** redesign request with screenshot.
**PASS requires:** redesign/workflow.md branch still first; new
originality.md output contract now includes DIALS line; preservation
ledger unaffected.

## Historical manual trace record (re-run required after material changes)

- T1 PASS — MODEL step (SKILL.md step 3) forces entities→IA order;
  product-fit gate enforces task-#1 path.
- T2 PASS — dials table + worked bank pair force written, justified
  divergence; validated via finance-banking.md dual persona content.
- T3 PASS — explicit legitimate-similarity rule present.
- T4 PASS — decision table's dense/comparable row forces table.
- T5 PASS — error formula + bilingual section + destructive rules.
- T6 PASS — expansion table + formats table + QA checklist; routing
  row separates from rtl/*.
- T7 PASS — routing map rows untouched for old paths (grep diff of
  SKILL.md: only additions).
- T8 PASS — redesign branch untouched; contract extended additively.

Limitation (honest): these are reasoned-specification tests, not
executed rendering tests — the skill has no runtime harness. Static
integrity is covered by research/tools/verify_install.py.
