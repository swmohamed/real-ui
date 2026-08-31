# REAL-UI rendered showcase

This directory is executable evidence, not a catalog of templates. Each surface starts from a product model and uses a composition chosen for its entities, tasks, platform, and content. Do not retrieve these layouts as universal industry answers.

## Eight greenfield products

| Domain | Product and primary task | Desktop | Mobile |
|---|---|---|---|
| Gaming | Night Shift — stage a private multiplayer round | [1440×900](greenfield/gaming/desktop.png) | [390×844](greenfield/gaming/mobile.png) |
| Editorial | Groundwork — read and inspect an evidence-backed investigation | [1440×900](greenfield/editorial/desktop.png) | [390×844](greenfield/editorial/mobile.png) |
| Sports | Full Time — monitor live scores, fixtures, and table state | [1440×900](greenfield/sports/desktop.png) | [390×844](greenfield/sports/mobile.png) |
| Ecommerce | Cedar & Loom — configure and order made-to-order furniture | [1440×900](greenfield/ecommerce/desktop.png) | [390×844](greenfield/ecommerce/mobile.png) |
| Finance | Till — reconcile cash, bills, and budgets | [1440×900](greenfield/finance/desktop.png) | [390×844](greenfield/finance/mobile.png) |
| Education | Field Notes — resume a guided lesson and practice | [1440×900](greenfield/education/desktop.png) | [390×844](greenfield/education/mobile.png) |
| Hospitality | Copper Fig — scan tonight's menu and reserve | [1440×900](greenfield/hospitality/desktop.png) | [390×844](greenfield/hospitality/mobile.png) |
| SaaS | Relay Desk — resolve a support conversation with context | [1440×900](greenfield/saas/desktop.png) | [390×844](greenfield/saas/mobile.png) |

## Four FULL redesign comparisons

| Domain | Before | After | Contract |
|---|---|---|---|
| Gaming | [desktop](redesign/gaming/before-desktop.png) | [desktop](redesign/gaming/after-desktop.png) | [case](redesign/gaming/case.json) · [validation](redesign/gaming/validation.md) |
| SaaS | [desktop](redesign/saas/before-desktop.png) | [desktop](redesign/saas/after-desktop.png) | [case](redesign/saas/case.json) · [validation](redesign/saas/validation.md) |
| Editorial | [desktop](redesign/editorial/before-desktop.png) | [desktop](redesign/editorial/after-desktop.png) | [case](redesign/editorial/case.json) · [validation](redesign/editorial/validation.md) |
| Ecommerce | [desktop](redesign/ecommerce/before-desktop.png) | [desktop](redesign/ecommerce/after-desktop.png) | [case](redesign/ecommerce/case.json) · [validation](redesign/ecommerce/validation.md) |

Each case also contains mobile before/after screenshots, DOM geometry snapshots, and raw axe results.

## Reproduce

```powershell
python scripts\render_showcase.py
python scripts\validate_redesign.py showcase\redesign\gaming\case.json --phase render
```

The renderer uses an isolated `agent-browser` Chrome session and writes `render-report.json`. A passing run checks exact viewport size, horizontal overflow, console errors, and axe violations. See [the rendered validation report](../research/reports/v5-rendered-validation.md) for the evidence boundary.
