# Validation Status

## Mathematical scope checks

- **P + D ≥ r:** retained only for the exact explicit-summary model.
- **TMMR conditional hardness:** retained only for the one-shot inherited/output-stable model.
- **Future-burden decomposition:** retained as an exact accounting identity.
- **Reusable SetIntersection transfer:** not claimed.

## Software validation

The optimized dirty-shadow tracker was compared event-by-event with the direct snapshot implementation on 650 deterministic streams × 300 updates = **195,000 updates**. Checked fields include step, vertex, degree, discovery, found/not-found, status changes, additions, removals, and combined churn.

The reusable-trigger audit covers **11,934** small set-system configurations:
- naive protected-edge re-add: 1,330 / 11,934 correct/state-preserving (11.14%);
- explicit unmatch + protected restore: 11,934 / 11,934 (100%);
- fresh one-shot center: 11,934 / 11,934 (100%).

## Empirical interpretation

The real traces do not support universal superiority of eager or fixed-threshold heavy/light maintenance. On the frozen AS-CAIDA shadow trajectory, degree explains most of the apparent discovery/churn association.

The repository's CI workflows encode the current reproducibility gates.
