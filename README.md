# Dynamic Matching Repair Complexity

This repository studies the information cost of repairing a maximal matching after dynamic graph updates.

The central question is narrower than ordinary update-time analysis:

> When a matched edge disappears, how much information must have been maintained in advance, and how much must be rediscovered before maximality can be restored?

## Main results

### 1. Discovery--propagation tradeoff

For the exact explicit-summary model developed here, if `r` neighbor states may have changed during a repair epoch, `P` of those states are communicated into exact query-visible state, and `D` unresolved states are discovered at repair time, then

```
P + D >= r.
```

This is a restricted information-flow theorem. It is **not** claimed as a cell-probe lower bound for arbitrary fully dynamic matching algorithms.

### 2. One-shot conditional hardness

A one-shot Triggered Maximal-Matching Repair (TMMR) construction reduces Pătraşcu's Multiphase problem to matching repair. If preprocessing costs `P(n,k)`, Phase-II candidate deletions cost `u(n,k)`, and the single trigger/repair decision costs `q(n,k)`, the reduction gives

```
tau = O(max{ P/(nk), u, q }).
```

Under the Multiphase conjecture, this yields a conditional polynomial barrier in the stated one-shot inherited/output-stable model. No lower bound for unrestricted fully dynamic maximal matching is claimed.

### 3. Exact future repair-burden identity

For future repairs `i=1,...,k`, with scan intensity `a_i=s_i/d_i` and degree drift `g_i=d_i/d_0`,

```
Q = sum_i a_i g_i
  = k [ A G + Cov(a,g) ].
```

The identity explains why repair recurrence alone does not determine whether maintaining an index is worthwhile.

### 4. Reproducible empirical boundary

The repository includes synthetic stress tests, application-style workloads, KONECT Wikipedia traces, and the 122-snapshot SNAP AS-CAIDA sequence.

For the final deterministic AS-CAIDA shadow trajectory:

- 54,070 repair events
- 74,407 discovery probes
- p99 discovery = 9
- maximum discovery = 49
- raw Spearman `rho(D, degree) = 0.8980`
- raw `rho(D, combined change) = 0.3517`
- degree-controlled residual `rho = 0.0287`

Thus neighborhood change/churn is **not** promoted as the principal driver of repair discovery. It has only a modest incremental predictive contribution beyond degree on this trajectory.

## Implemented methods

- full recomputation
- local scan repair
- eager exact free-neighbor summaries
- heavy/light summary maintenance
- adaptive-debt diagnostic policy
- event-level repair tracing
- exact snapshot shadow instrumentation
- differential-validated dirty-shadow instrumentation

The optimized dirty-shadow tracker is validated event-by-event against the direct snapshot implementation on 650 deterministic streams of 300 updates each (195,000 updates total).

## Frozen real-trace results

| Dataset | Algorithm | Total charged work | p99 | Maximum |
| --- | --- | ---: | ---: | ---: |
| Simple Wiki | Scan | 204,572 | 4 | 292 |
| Simple Wiki | Eager | 1,312,908 | 21 | 2,456 |
| Simple Wiki | Heavy/light | 518,440 | 6 | 317 |
| NL Wiki 1M prefix | Scan | 66,194 | 1 | 236 |
| NL Wiki 1M prefix | Eager | 922,549 | 13 | 3,221 |
| NL Wiki 1M prefix | Heavy/light | 383,848 | 1 | 512 |
| AS-CAIDA | Scan | 72,544 | 4 | 42 |
| AS-CAIDA | Eager | 591,973 | 18 | 4,684 |
| AS-CAIDA | Heavy/light | 248,748 | 8 | 206 |

These results do not support a universal winner among maintenance strategies. Heavy/light maintenance can reduce tail repair cost on designed hub instances while still losing to scan in total work.

## Reproducibility

Install requirements and run the core experiment suite:

```bash
pip install -r requirements.txt
python experiments/run_benchmarks.py
python experiments/run_application_demo.py
python artifacts/generate_artifacts.py
```

The CAIDA full replay workflow:

1. downloads the authoritative SNAP archive;
2. reconstructs the 122-snapshot temporal stream;
3. enforces the frozen gate of 32,955 initial edges and 542,194 measured updates;
4. replays the validated dirty-shadow tracker;
5. produces discovery-profile and compact summary artifacts.

Current GitHub Actions checks cover the benchmark suite, CAIDA full replay, the shadow replay fixture, and the dirty-shadow differential gate.

## Data sources

- SNAP AS-CAIDA: https://snap.stanford.edu/data/as-Caida.html
- KONECT temporal network collection: http://konect.cc/

## Claim discipline

This repository does **not** claim:

- a new asymptotic update bound for unrestricted fully dynamic maximal matching;
- that generic dynamic set intersection is a new primitive;
- that fixed-threshold heavy/light maintenance universally improves total work;
- that repair recurrence alone implies profitable indexing;
- that raw neighborhood churn is the principal cause of repair-discovery difficulty.

The contribution is a repair-centered mathematical and experimental framework with explicit model boundaries, auditable reductions, and reproducible falsification tests.
