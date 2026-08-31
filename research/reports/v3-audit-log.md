# V3 Audit & Upgrade Log (historical, superseded)

This is a prior change record, not evidence of the current repository's
completeness or runtime behavior. Its Markdown “behavioral” results were
manual reasoned traces, and its file counts/sync status are historical. The
independent V4 audit re-verifies claims and supersedes current-status
conclusions without deleting this provenance.

Method per the V3 program: INSPECT → registry → prioritize → validate
existing → research only real gaps → implement → test → regression.
All findings below are INSPECTED (grep/read evidence recorded) — no
claims of unperformed work.

## AUDIT SCOPE (what was inspected)

- SKILL.md (full read) — workflow, retrieval map, dimension table,
  finish gate
- taxonomy.md (full) — classification axes
- Structural probes across knowledge/: file sizes (8,356 lines total);
  industry-file skeletons (H2 sets of gaming/finance/restaurants/
  education); IA-section content diff (finance vs restaurants);
  rtl/implementation.md + arabic-ux + cross-platform + global-vs-arabic
  (bidi/numerals/expansion coverage); states.md, originality.md,
  realism.md, desktop.md, cards.md headers; greps for microcopy,
  entities/data-model, same-industry variation, text expansion,
  currency/date formats.

## ISSUE REGISTRY (evidence-based)

| # | Issue | Sev | Evidence | Root cause | Fix | Validation |
|---|---|---|---|---|---|---|
| 1 | No product-modeling step; genre IA can substitute for product IA | CRITICAL | grep "entit\|data model" → 0 hits in 112 files; workflow step 3 was inventory-only | workflow skipped entity/task modeling between CLASSIFY and design | NEW foundations/product-modeling.md + SKILL.md step 3 "MODEL & CONSTRAIN" + map row + gate line | T1; ghost/orphan check |
| 2 | Same-industry variation guidance = 1 sentence | HIGH | originality.md had redesign-only rules; SKILL.md one differentiation line | variation system never built for fresh designs | originality.md "Variation within an industry" (5 dials + worked pair + legitimate similarity) + SKILL.md pointer | T2, T3 |
| 3 | No content-design system | HIGH | microcopy hits scattered across 6 files; no voice/CTA/error-copy rules | domain absent | NEW ux/content-design.md + map row + dimension row + gate copy-check | T5 |
| 4 | cards.md lacks when-not-to-use/alternatives | MEDIUM | headers: anatomy/variants/grids only | decision rule never written | cards.md decision table + cost ledger + dashboard case | T4 |
| 5 | i18n beyond RTL absent | MEDIUM | expansion/bidi hits only in rtl/* and industry snippets | RTL track absorbed all i18n | NEW localization/i18n.md (expansion table, formats, plurals, QA) + routing rows | T6 |
| 6 | SKILL.md header stale ("~45 industries", "websites") | LOW | read of line 10-13 | V2 growth outpaced prose | corrected to 24 modules / 9 platforms | read |
| 7 | Tests structural-only, not behavioral | MEDIUM (limitation) | tests are md specs | no runtime harness exists (by design) | v3 behavioral suite (reasoned) + honest limitation note | this file |

## EXISTING STRENGTHS VALIDATED (kept, untouched)

- Industry files share a SCHEMA but content differentiates deeply
  (finance IA: products→rates→security→regulation + logged-in
  dashboard-first split vs restaurants: brand-vs-platform dual IA +
  item-dialog signature) — genre knowledge changes IA/nav/density,
  not just colors. INSPECTED.
- RTL/bidi track strong (bidi survival kit, numerals policy, ship-gate
  checklist). A11y floor + WCAG 2.2 labels. States coverage complete.
  Realism ledger + per-stack contracts. Desktop keyboard-first
  differentiators. Routing map has zero orphan/ghost files
  (verify_install.py enforced since V1).

## RESEARCH (Phase 6)

No new external research required — all 7 issues are method/routing
gaps, not missing facts. New knowledge labeled RECOMMENDED (method) /
heuristic (i18n ratios) per evidence-honesty rules; no fabricated
sources; no corpus claims added.

## IMPLEMENTED (V3)

ADD: knowledge/foundations/product-modeling.md (model→IA derivation,
product-fit test, clinic worked example)
ADD: knowledge/ux/content-design.md (registers, labels, CTA verbs,
error formula, empty/loading/success copy, bilingual rules)
ADD: knowledge/localization/i18n.md (expansion table, layout survival,
locale formats, plurals, QA)
EXTEND: redesign/originality.md (retitled for all designs; 5 structural
dials; same-industry pair; legitimate similarity; DIALS in contract)
EXTEND: ui/cards.md (when-NOT-to-use decision table + cost ledger)
EXTEND: SKILL.md (7 edits: header correction, MODEL step, 2 map rows,
2 dimension rows, product-fit+copy gate lines, dials pointer)
ADD: tests/v3-behavioral-tests.md (T1–T8, all PASS reasoned)

Counts: knowledge 112 → 115 files; tests 8 → 9.

## REGRESSION

- verify_install.py: cross-refs, ghosts/orphans, compile, YAML — run
  after edits (results in session log).
- Old routing rows untouched (SKILL.md edits additive) — T7, T8 PASS.
- 18-destination sync + GitHub push performed after validation.
