# research/ — Audit Trail

This directory contains the evidence base for the real-ui skill. The
knowledge in `knowledge/` is distilled from this research plus cited official
platform/standards sources. Source extraction is not render/runtime evidence;
see `knowledge/research/method.md` for the evidence-mode contract.

## Contents

- `tools/fetch_analyze.py` — code-first site analyzer (HTML + primary CSS
  fetch → structure/tokens/typography/breakpoints/RTL extraction → JSON report)
- `tools/retry_curl.py` — curl-based retry for bot-blocked hosts
- `tools/aggregate.py` — cross-corpus aggregation (the source of
  observed-findings.md §1–11)
- `tools/industry_signals.py` — per-industry DNA signal profiles +
  flagship deep dives
- `raw/*.json` — site batches attempted (17 batches, 200+ entries with
  URL variants)
- `reports/*.json` — per-site extraction reports (the raw evidence)
- `reports/aggregate-summary.txt` — corpus-wide statistics
- `reports/industry-signals.txt` — per-industry aggregates + deep dives

## Corpus summary (2025 run)

- 156 distinct sites fetched OK (145 with parsed CSS; ~31 MB production CSS)
- ~45 industries; global leaders + conventional + award-class
- MENA track: 39 Arabic/regional sites (31 full RTL evidence)
- Blocked/inaccessible hosts recorded honestly (see
  knowledge/research/saturation-and-confidence.md for the list)

## Reproducing / extending the evidence base (Deep / Audit mode)

Run these from the `research/` directory:

```
python tools/fetch_analyze.py raw/<batch>.json reports/<batch>.json   # urllib path
python tools/retry_curl.py raw/<batch>.json reports/<batch>.json      # curl path (blocked hosts)
python tools/aggregate.py                                             # refresh corpus stats
```

Label new findings SOURCE-OBSERVED/RUNTIME-OBSERVED/RENDER-OBSERVED/
INFERRED; respect robots/blocks; never
re-publish site content — extract patterns only.
