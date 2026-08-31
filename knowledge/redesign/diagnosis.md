# Redesign Diagnosis (find the actual problem)

Identify the problem BEFORE choosing the solution. A visual problem gets
a visual solution; a UX problem gets an IA/interaction solution. "Don't
solve UX problems with decoration" is the #1 redesign rule.

## Diagnosis checklist

### Information architecture
- Is content grouped the way users think, or the way the org chart thinks?
- Are labels user language or internal jargon?
- Can a new user predict what each nav item leads to?

### Navigation
- Depth: key tasks reachable in ≤3 taps/clicks?
- Current location always visible (nav state, breadcrumbs)?
- Back/close behavior matches platform convention?

### Content & visual hierarchy
- What is the FIRST thing seen? Does it match the page's #1 job?
- Do competing primary actions exist (two "primary" buttons cancel out)?
- Is density right for the industry (see industries/* density norms)?
  A dashboard needs density; a luxury brand needs air.

### Discoverability & interaction cost
- Are key features findable without a tutorial?
- Count steps for the top 3 tasks. Every extra step is churn.
- Hidden-in-hamburger critical nav on desktop = smell.

### Consistency (component audit)
- Count radii, button styles, spacing values, icon styles in the
  CURRENT product. >3 of any = fragmentation diagnosis.
- Same action, different treatment on different pages?

### Typography / color / spacing
- Scale present or arbitrary sizes? (grab font-size census from CSS)
- Color doing semantic work or decoration?
- Spacing rhythm: consistent 4/8 base or random?

### States & feedback
- Loading/empty/error/success designed or default? (ux/states.md,
  ux/mobile-states.md)
- Destructive actions confirmed? Optimistic updates safe?

### Responsive & adaptive behavior
- Does mobile get a designed experience or a squeezed desktop?
- Nav model changing by size (bar→rail→sidebar) or just shrinking?
- Touch targets ≥44pt/48dp on mobile? Hover-only affordances on touch?

### Platform mismatch
- Web idioms in a mobile app (hover menus, tiny targets, URL thinking)?
- iOS app using Material back behavior or vice versa?
- Desktop app afraid of keyboard shortcuts / menus?

### Trust & branding (industries/* + ux/trust-conversion.md)
- Does trust signaling match industry bar (finance ≠ portfolio)?
- Brand assets preserved or replaced by generic?

## Symptom → cause → solution type

| Symptom | Likely real cause | Solution type |
|---|---|---|
| "Looks dated" | typography scale + spacing rhythm decay | visual system refresh |
| "Users can't find X" | IA/navigation problem | restructure, not restyle |
| "Feels cluttered" | hierarchy failure, not size failure | consolidate, group, cut |
| "Doesn't convert" | trust + friction on key flow | flow surgery + trust cues |
| "Mobile feels wrong" | web squeezed into phone | redesign mobile-native |
| "Inconsistent" | missing design system | tokens + component states |
| "Boring/generic" | no visual DNA | direction from product, not template |

## Output format (feeds workflow stage 4)

```
DIAGNOSIS:
- P1 [IA] ... (evidence: ...)
- P2 [NAVIGATION] ...
- P3 [CONSISTENCY] 5 radii, 3 button styles (evidence: CSS census)
WHAT WORKS: ... WHAT FAILS: ... WHY: ...
```
Label evidence OBSERVED (from code/screenshot) or INFERRED.
