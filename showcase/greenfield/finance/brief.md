# Till product brief

Till is a cash-control ledger for a small studio. The primary tasks are checking available cash, reconciling recent transactions, reviewing committed bills, and watching category budgets. Account, transaction, bill, budget, and transfer are the core entities. Desktop balances a dense ledger with near-term obligations; phone preserves the balance and transaction scan while moving secondary analysis into destinations. Investments, credit scoring, and financial advice are outside scope.

- Research used: [WCAG reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) for the compact ledger and [WCAG target size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) for transactional controls.
- REAL-UI knowledge used: `industries/finance-banking.md`, `pages/dashboard.md`, `ui/data-display.md`, and `foundations/visual-hierarchy.md`.
- Major decision: make the reconciled transaction ledger authoritative and keep summaries subordinate to cash decisions.
