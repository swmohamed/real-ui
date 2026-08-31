# Night Shift validation

- RENDER-OBSERVED on 2026-08-31 in Chromium via `scripts/render_showcase.py`.
- Screenshots: `desktop.png` at 1440×900 and `mobile.png` at 390×844.
- Automated evidence: zero axe violations, zero console errors, and no horizontal page overflow in both viewports.
- Manual review: match staging remains primary on both sizes; the mobile layout does not squeeze the three-column room.
- Boundary: the fixture demonstrates UI behavior and local controls, not a networked game server.
