# Contributing to REAL-UI

Thanks for helping improve REAL-UI. This repository is a design-intelligence
skill: agents use it to design real products. Contributions should make that
reasoning better, not add generic UI kits.

Please follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Before you start

1. Search existing issues and pull requests.
2. Read `SKILL.md` and the files closest to your change (`knowledge/`,
   `knowledge/taxonomy.md`, `knowledge/research/method.md`).
3. Prefer extending an existing file over creating a new one.
4. Open an issue first for knowledge, research, or coverage proposals.

## Ways to contribute

| Kind | Typical files | What a good change does |
|---|---|---|
| Bug fix | `SKILL.md`, `scripts/`, `tests/`, routing/retrieval | Corrects incorrect behavior without changing the product-first model |
| UI/UX knowledge | `knowledge/` | Adds WHY / WHEN / WHEN NOT / TRADEOFF for a real design problem |
| Research / evidence | `research/reports/`, ledger tools | Adds traceable product evidence and honest labels |
| Coverage | industries, product types, interface families, platforms, regions | Fills a gap that current files do not already decide |
| Documentation | `README.md`, this guide, comments | Makes the skill easier to use or contribute to |
| Tests / tooling | `tests/`, `scripts/`, `research/tools/` | Catches regressions; does not invent product layouts |

## Contribution rules

- **No generic UI templates.** Do not add “the dashboard layout”, “the course
  page”, or any one-size design for an industry or product type.
- **Do not copy layouts from real products.** Real products are evidence.
  Extract decision logic (what the product is, why a pattern appears, when it
  fails). Never reproduce another product’s IA, chrome, or visual system.
- **Research-backed claims need traceable evidence.** Name the product, URL,
  and what was actually inspected.
- **Label evidence honestly.** Use SOURCE-OBSERVED, DOC-OBSERVED,
  RUNTIME-OBSERVED, RENDER-OBSERVED, INFERRED, RECOMMENDED, or UNCERTAIN.
  Do not call something analyzed if it was not inspected. Marketing/login
  shells are not in-app UI.
- **Preserve product-first reasoning.** Industry, page, and interface-family
  files suggest presentation options. They do not invent features, routes, or
  modules for a product that does not have them.
- **Avoid duplicate knowledge.** Search `knowledge/` before adding a family,
  page, or rule. If the decision already exists, tighten the existing file.
- **Update routing when knowledge changes.** If a new family or distinction
  should change retrieval, update `SKILL.md` and `knowledge/taxonomy.md` in
  the same change. Do not leave orphan files.
- **Do not mix evidence classes.** Production products and supporting sources
  (docs, guidelines, design systems, catalog names) stay separate.

## Research and coverage proposals

New categories, product types, and interface families need a distinct design
problem, not 20 variants of the same architecture. A proposal should say:

- the gap in current knowledge
- why existing files do not already cover it
- real production products (name + URL), not demos
- what decision logic would be stored (WHY / WHEN / WHEN NOT / TRADEOFF)

Thin sites, parked domains, and app-store shells may count as products if they
were actually fetched, but they must not become invented layout rules.

## What not to commit

Do not include:

- `research/raw/` dumps, corpus JSON, caches, or screenshots of live products
- secrets, tokens, `.env` files, or machine-specific paths
- OS junk (`nul`, `NUL`, `.DS_Store`, `__pycache__`)
- unrelated local experiments, validation HTML, or personal notes

Raw fetches are gitignored on purpose. Distill observations into knowledge
files and durable markdown reports under `research/reports/`.

## Tests to run

From the repository root:

```bash
python -m unittest discover -s tests -p "test_*.py"
python research/tools/verify_install.py
```

Knowledge and routing changes should leave retrieval map checks clean (no
ghosts, no orphans). Do not weaken tests to land a change.

## Pull requests

Use the pull request template. Keep the change reviewable: one problem, the
evidence for it, and the routing/test follow-through.

Security issues are not pull requests. See [SECURITY.md](SECURITY.md).
