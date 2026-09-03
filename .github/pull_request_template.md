## What changed

<!-- Summarize the change. Link the issue if there is one. -->

## Why

<!-- What product, skill, or contributor problem does this solve? -->

## Evidence / research

<!-- Name products, URLs, and evidence labels if this touches knowledge. Write "n/a" for pure docs/tooling. -->

## Checks

- [ ] No generic UI template, kit, or one-size layout
- [ ] No copied layout, IA, or visual system from a real product
- [ ] Existing knowledge searched; no duplicate family/rule
- [ ] Routing / retrieval updated if this change should affect it (`SKILL.md`, `taxonomy.md`)
- [ ] Observed evidence is labeled separately from inferred guidance
- [ ] `python -m unittest discover -s tests -p "test_*.py"` passed
- [ ] `python research/tools/verify_install.py` passed when install/knowledge files changed
- [ ] No raw fetches, screenshots, caches, secrets, temp files, or machine-specific paths
