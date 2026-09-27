# Adaptive debt policy decision

Parameters alpha=0.5, rho=1.0 were selected exclusively on repeated synthetic hub-repair training and frozen before external evaluation.

| Dataset | Scan total | Adaptive total | Adaptive / Scan | Scan p99 | Adaptive p99 | Scan max | Adaptive max |
|---|---:|---:|---:|---:|---:|---:|---:|
| Simple Wiki full | 204,572 | 1,281,698 | 6.27x | 4 | 17 | 292 | 2,135 |
| AS-CAIDA full | 72,544 | 436,953 | 6.02x | 4 | 11 | 42 | 4,664 |

Both adaptive runs passed final validity checks.

## Decision: NO-GO
Accumulated historical scan debt is not sufficient evidence that an index will be reused enough to amortize its construction and maintenance on these external streams. Do not retune alpha/rho on these datasets.

## Next falsifiable question
Measure vertex-level repair recurrence and temporal persistence directly:
- number of repair queries per vertex;
- inter-repair distance/time;
- cumulative scan work;
- degree at repair;
- whether a hypothetical index would still be useful at the next repair;
- realized break-even ratio: future scan cost avoided / index build+maintenance cost.

Only design another policy if external traces reveal a stable observable predictor available before activation.

## Manuscript gate
Do not draft the full paper from this adaptive algorithm. A paper becomes justified after either (1) an out-of-sample policy succeeds on independent external data with all costs charged, or (2) a theorem/empirical characterization of the search-vs-maintenance break-even boundary is strong enough to stand alone.
