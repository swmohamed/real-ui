# Full Time product brief

Full Time is a live football match center. Users scan live scores, change the date, open a match, check the live table, and reach a highlight. Match, competition, fixture, team, table row, and media clip drive the screen. Desktop uses a scoreboard ribbon and utility table; phone narrows the ribbon to one live match and keeps fixtures and standings task-oriented. Editorial article browsing and fan social features are outside the fixture.

- Research used: [BBC GEL data tables](https://bbc.github.io/gel/components/data-tables/) for scannable aligned data and [WCAG target size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) for date and match controls.
- REAL-UI knowledge used: `industries/sports-fitness.md`, `ui/data-display.md`, `devices/mobile.md`, and `input/touch.md`.
- Major decision: use match state, date, and standings as the visible hierarchy rather than treating sports as an article-card homepage.
