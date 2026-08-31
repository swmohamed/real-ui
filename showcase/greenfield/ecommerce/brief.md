# Cedar & Loom product brief

Cedar & Loom sells made-to-order furniture through configuration rather than catalog filtering. Users inspect a room view, choose size, upholstery and finish, understand delivery, then add the exact configuration. Model, size, material, finish, delivery window, and configured order are the core entities. Desktop keeps the room and configuration panel together; phone sequences preview, material, delivery, and order tasks. Product recommendations and financing are deliberately absent.

- Research used: [WCAG target size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) for material choices and [WCAG reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) for the phone transaction path.
- REAL-UI knowledge used: `industries/ecommerce-marketplace.md`, `pages/product-detail.md`, `ux/content-design.md`, and `accessibility/floor.md`.
- Major decision: represent the product as a configured order with an explicit delivery promise, not as a catalog card grid.
