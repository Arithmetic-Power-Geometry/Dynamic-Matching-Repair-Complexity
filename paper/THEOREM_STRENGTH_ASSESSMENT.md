# Theorem-strength assessment

## PROVED in restricted model
For exact explicit-summary free-neighbor reporting at a fixed vertex, if r neighbor statuses are unresolved since the last exact summary point, update-time propagation P and worst-case query discovery D satisfy P + D >= r under the stated adversarial epoch model.

## Why this is not yet a standard-model lower bound
Known dynamic set-intersection/disjointness work studies update/query tradeoffs in standard data-structure models, often conditionally (e.g. 3SUM/OMv-style conjectures) or in cell-probe settings. Our free-neighbor primitive is a dynamic set-intersection witness query N(v) intersect Free, so generic lower-bound machinery is relevant. A matching-specific lower bound must exploit or survive the extra constraint that Free is an independent set generated endogenously by a maximal matching.

## Research fork
A. Standard-model theorem: reduce a recognized dynamic problem to matching-constrained free-neighbor reporting while preserving reusable updates/queries. This is difficult because maximal matching permits rerouting and earlier forcing gadgets failed.
B. Structural theorem: characterize the restricted model exactly and validate that real repair events expose the predicted unresolved-change burden; frame as instance-sensitive analysis rather than universal lower bound.

Route A is the stronger Q1 target. Route B may support a solid empirical/theory paper but should not be marketed as a general lower bound.
