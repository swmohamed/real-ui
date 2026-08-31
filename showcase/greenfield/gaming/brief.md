# Night Shift product brief

Night Shift is a private multiplayer party-game room for friends coordinating a four-round session. The primary tasks are sharing the room code, confirming the round order, seeing player readiness, and starting the next match. Room, round, squad, and player are the core entities. Desktop keeps preparation, arena context, and squad state in one cockpit; phone prioritizes the active round and moves room tasks into labeled destinations. Voice chat and public matchmaking are outside this fixture.

- Research used: [Xbox Accessibility Guideline 112](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/112) for predictable digital-input navigation; it did not prescribe the composition.
- REAL-UI knowledge used: `foundations/product-modeling.md`, `industries/gaming.md`, `devices/desktop.md`, and `responsive/adaptive-models.md`.
- Major decision: model the screen as match preparation around room and squad state, not as a game-discovery storefront.
