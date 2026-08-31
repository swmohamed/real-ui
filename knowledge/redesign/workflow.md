# Redesign Workflow (the pipeline)

A redesign is NOT "make it modern." Understand first, change with
reasons, preserve what works. Default outcome: **the same product
evolved** — not a stranger wearing its logo.

## Pipeline (stage gates — do not skip stages)

```
CURRENT PRODUCT → CURRENT UX → CURRENT UI → WHAT WORKS → WHAT FAILS →
WHY IT FAILS → KEEP/CHANGE/REMOVE/MERGE/ADD → NEW UX → NEW UI →
DESIGN SYSTEM → PLATFORM ADAPTATION → REALISM QA
```

### 1. Understand (inputs: code, screenshots, user description)
Read the real product — HTML/CSS for web (code-first), screenshots as
visual evidence (redesign/screenshot-analysis.md), live fetch if allowed.
Never redesign from imagination or a vague memory of the brand.

### 2. Diagnose (redesign/diagnosis.md)
Run the full checklist. Classify each problem: IA problem · navigation
problem · visual problem · density problem · state problem · trust
problem · platform mismatch · consistency problem.

### 3. Value inventory (redesign/preservation.md)
List what MUST survive: brand personality, recognition assets, useful
workflows, terminology users know, information structure, muscle memory.
Also list what is safe to sacrifice and what actively harms.

### 4. Decide per element — not per page
| Verdict | Meaning | Bar |
|---|---|---|
| KEEP | works + users rely on it | default for anything working |
| CHANGE | right idea, wrong execution | visual/interaction fix only |
| REMOVE | harmful or dead weight | requires a stated reason |
| MERGE | duplicated concepts | collapse, keep strongest name |
| ADD | missing table-stakes pieces | industry convention gaps |

Write the verdict table BEFORE designing. Every change maps to a
diagnosed problem — no orphan changes.

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
understood, strengths preserved, changes justified, identity intact?

### 9. Iterate (close the loop — V2.2)
Design ≠ ship-and-forget: after delivery (or staged rollout per
prioritization.md), MEASURE against the success criteria defined
upfront (task completion, tickets, activation…); feed learnings back
— keep/refine/revert by criteria, not pride (kill-switch honesty in
prioritization.md). Small loop: observe → diagnose (diagnosis.md) →
adjust. Evolution happens in measured steps (evolution-cases.md).

## Transformation mode (only when explicitly requested)

User asks for complete transformation → stages 1–3 still run (you must
know what you are killing), but preservation rules relax; state what is
intentionally discarded and why. Never silently transform.
