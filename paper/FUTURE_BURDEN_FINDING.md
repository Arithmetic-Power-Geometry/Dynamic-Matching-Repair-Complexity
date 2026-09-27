# Future-burden decomposition: external finding

The exact identity Q = k[A G + Cov(a,g)] was numerically verified on all repair events (maximum reconstruction error < 1.5e-14).

| Dataset | Repair events | Q>1 events | Rate | Median k among Q>1 | Median A among Q>1 | Median G among Q>1 |
|---|---:|---:|---:|---:|---:|---:|
| Simple Wiki | 59,780 | 3,449 | 5.77% | 3 | 0.3824 | 1.0 |
| AS-CAIDA | 40,373 | 1,180 | 2.92% | 4 | 0.3333 | 1.0 |

For the median break-even event in both domains, mean degree drift is 1.0. Thus degree growth is not the central explanation at the median. Break-even events instead combine multiple future repairs with nontrivial scan intensity.

This also clarifies why raw recurrence failed: k can be large while A is tiny. Conversely, one expensive historical scan does not establish future k or future A.

The decomposition is exact accounting, not by itself a novelty claim. The next research target is an observable proxy for the product of future persistence and future normalized scan intensity. Before naming or claiming a theory, search prior work on ski-rental/rent-or-buy indexing, adaptive data structures, dynamic graph maintenance, and instance-sensitive dynamic matching.
