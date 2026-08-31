# Redesign Workflow (the pipeline)

A redesign is NOT "make it modern." Understand first, change with
reasons, preserve what WORKS — and change composition when the product
model justifies it. First action: classify DEPTH (stage 0).
POLISH/REFRESH default to "the same product evolved"; REDESIGN/FULL
re-derive structure (they do NOT default to the old composition).

## Pipeline (stage gates — do not skip stages)

```
CURRENT PRODUCT → CURRENT UX → CURRENT UI → WHAT WORKS → WHAT FAILS →
WHY IT FAILS → KEEP/CHANGE/REMOVE/MERGE/ADD → NEW UX → NEW UI →
DESIGN SYSTEM → PLATFORM ADAPTATION → REALISM QA
```

### 0. Classify depth (redesign/depth.md — before anything else)
POLISH · REFRESH · REDESIGN · FULL REDESIGN, from explicit words +
scope signals (depth.md signals table). Depth sets every preservation
default downstream. FULL treats the old interface as evidence of
requirements (functionality, content, workflows, routes, constraints),
never as the required architecture.

### 1. Understand (inputs: code, screenshots, user description)
Read the real product — HTML/CSS for web (code-first), screenshots as
visual evidence (redesign/screenshot-analysis.md), live fetch if allowed.
Never redesign from imagination or a vague memory of the brand.

### 1.5 Extract (REDESIGN/FULL; before diagnosing)
For REDESIGN/FULL, use redesign/extraction.md to decompose the old product
into four layers: REQUIREMENTS ·
CAPABILITIES · WORKFLOWS · PRESENTATION. Build the capability ledger
(PRESERVE/TRANSFORM/MERGE/RELOCATE/REMOVE-WITH-JUSTIFICATION).
Presentation (layer D) is quarantined: it informs nothing downstream
except the diagnosis of what served which capability. Subtle
capabilities that live only visually (progression, resume,
personalization, history…) are enumerated HERE or they die silently.
POLISH/REFRESH keep structure locked and use a lighter current-state inventory;
they do not quarantine/re-derive the composition (redesign/depth.md).

### 2. Diagnose (redesign/diagnosis.md)
Run the full checklist. Classify each problem: IA problem · navigation
problem · visual problem · density problem · state problem · trust
problem · platform mismatch · consistency problem.

### 3. Value inventory (redesign/preservation.md)
List what MUST survive: brand personality, recognition assets, useful
workflows, terminology users know, information structure, muscle memory.
Also list what is safe to sacrifice and what actively harms.

### 3.5 Re-derive from the product model (REDESIGN/FULL only)
Model the product fresh (foundations/product-modeling.md), SEEDED by
the extracted layers (1.5): entities → top tasks → relationships →
volume → content/information priority → screen contracts → new IA skeleton.
Every ledger capability must LAND
somewhere in the skeleton (coverage matrix, extraction.md). The old
interface contributes A/B/C evidence — never composition (layer D).
Stage 4 verdicts then run on THIS skeleton — the old composition's
disposition comes from the ledger, not from habit.

### 4. Decide per element — not per page
| Verdict | Meaning | Bar |
|---|---|---|
| KEEP | works + users rely on it | POLISH/REFRESH: default for anything working. REDESIGN/FULL: re-earned — still correct after stage 3.5 ("it existed" is not a reason) |
| CHANGE | right idea, wrong execution | visual/interaction fix only |
| REMOVE | harmful or dead weight | requires a stated reason |
| MERGE | duplicated concepts | collapse, keep strongest name |
| ADD | missing required/supporting piece | ALL depths: scope gate — EXISTING capability · EXPLICIT request · NECESSARY supporting UX only. Industry convention alone is never a reason; suggest hypotheses separately |

Write the verdict table BEFORE designing. Every change maps to a
diagnosed problem — no orphan changes. In REDESIGN/FULL the table's
axis is the RE-DERIVED structure (3.5): each new element names the
capability/requirement it serves; dispositions of old elements come
from the capability ledger (1.5).

### 4.5 Prioritize + sequence (redesign/prioritization.md)
Score verdict rows (impact/frequency/risk/effort/reversibility);
order: UX-blockers → token unification → direction moves → polish;
choose rollout shape; define 2–3 success criteria BEFORE designing.
Evolution reasoning: redesign/evolution-cases.md (observation →
pattern → principle → application).

### 5. New UX first, then UI
Fix IA/navigation/flows as skeletons. Only then apply visual direction
(redesign/originality.md + visual-dna/dna-selector.md). UX problems are
never solved with decoration.

### 6. Design system pass
Consolidate tokens (design-systems/tokens.md) — typography scale, color
roles, spacing rhythm, radius, elevation, states. One system, no
one-offs. For multi-platform: design-systems/cross-platform.md.

### 7. Platform adaptation
Web/mobile/tablet/desktop each get NATIVE treatment (platforms/README.md)
— never a squeeze. Bottom nav on phone, rail on tablet, sidebar on
desktop, hover states only where a pointer exists.

### 8. Realism QA + Redesign QA (tests/v2-quality-gate.md)
Realism: does it look like a real product? Redesign: was the old product
understood, requirements preserved, changes justified, identity intact?
Three HARD gates (a FAIL returns work to stage 3.5 — validation must be
able to change the output, not just describe it):
- DEPTH (redesign/depth.md): style-blind structural diff old↔new
  matches the classified depth? FULL preserving nearly everything
  without justification = insufficient depth. Reclothe test.
- CAPABILITY LOSS (extraction.md): every ledger row lives somewhere in
  the result? Any silent disappearance = FAIL → restore/transform.
- SCOPE FIDELITY (extraction.md): every new element passes
  EXISTING/REQUESTED/SUPPORTING? Invented feature = FAIL → remove
  (suggest separately instead).
Run the existed-vs-correct audit for every structural KEEP.

### 9. Iterate (close the loop — V2.2)
Design ≠ ship-and-forget: after delivery (or staged rollout per
prioritization.md), MEASURE against the success criteria defined
upfront (task completion, tickets, activation…); feed learnings back
— keep/refine/revert by criteria, not pride (kill-switch honesty in
prioritization.md). Small loop: observe → diagnose (diagnosis.md) →
adjust. Evolution happens in measured steps (evolution-cases.md).

## Transformation mode (= FULL REDESIGN)
Explicit "complete transformation"/rebrand requests classify as FULL
(depth.md). Stages 1–3 still run (you must know what you are killing);
preservation targets requirements + brand, not composition; state what
is intentionally discarded and why. Never silently transform.
