# Typography: Latin Systems & Real-World Practice

## What the real web loads (observed 2025 corpus)

- **Tier 1 default**: Inter (17 sites + Inter Display/Tight variants) and
  system stacks (`-apple-system…`, `ui-sans-serif`) — the modern baseline
- **Tier 2 utility**: Open Sans, Roboto, Helvetica Neue — everywhere,
  invisible
- **Tier 3 identity**: proprietary/restricted faces — Söhne (Stripe), SF
  Pro (Apple), Airbnb Cereal VF, BBC Reith, NYT Cheltenham/Franklin,
  MoMA Sans, UberMove, Porsche Next, GDS Transport, Torus (Poki), Roobert
  (Twitch), GitLab Sans, ABC Ginto (Discord)
- **Mono as identity**: ui-monospace/SF Mono/Source Code Pro for dev/fin
  products — Stripe, GitHub-class

## Choosing a Latin face (decision table)

| Register | Face class | Examples |
|---|---|---|
| Neutral product | Geometric/humanist grotesk | Inter, Söhne, Untitled Sans |
| Technical credibility | Grotesk + mono pairing | Inter+JetBrains, Söhne+SourceCode |
| Editorial quality | Serif display / serif body | Cheltenham, Guardian Egyptian, Tiempos |
| Warm consumer | Rounded geometric | Nunito, Cereal-class, Baloo (kids) |
| Luxury | Didone/high-contrast serif | Didot, Canela-class |
| Institutional | Humanist sans | Frutiger/GDS Transport class |
| Brutalist/system | Monospace-forward | IBM Plex Mono accents, Carbon's Plex family |

## Practical rules

- 2 families max + mono optional; 3 weights loaded typically (400/600/700
  or 400/500/700); variable font when more
- Fallback stack with metric tuning: `Inter, "Inter Fallback", system-ui…`
  (OBSERVED pattern on Next.js sites using size-adjust overrides to kill
  layout shift on swap)
- Line-length discipline: 45–75ch content; UI labels exempt
- Type hierarchy from ONE scale (see design-systems); don't hand-tune
  per section
- Display tightening: -1 to -2% tracking above 40px; never tighten body
- Sentence case for UI (Title Case only for proper nouns/marketing H1s
  where brand voice says so); ALL-CAPS = labels/eyebrows only, with
  tracking

## Common mistakes

- Inter for everything as identity (Inter is invisible — identity needs
  either display-weight Inter craftsmanship or a second voice)
- 300-weight body on white (thin + small = illegible)
- Letter-spacing body text; fake small-caps via CSS on wrong fonts
- Loading 6 weights "just in case"
- Roboto as "brand" (Roboto = non-statement)

## Self-check question per project

"Could this typography appear on any competitor's site unchanged?" If
yes → the type system hasn't made a decision. Fix with weight contrast,
a display voice, or scale drama — not with a novelty font alone.
