# Dynamic Matching Repair Complexity

This repository studies a narrow question in fully dynamic maximal matching:

> Can the structure induced by a maintained matching make maximality-violation discovery easier than generic dynamic set-intersection witness search?

## Research status

The generic neighborhood-witness primitive is **not novel by itself**. Dynamic set intersection already provides witness data structures and 3SUM-based square-root-type update/query lower bounds.

The surviving research target is matching-specific:

1. formalize which active-set updates and witness queries are actually induced by maximal-matching repair;
2. compare those constrained sequences with generic dynamic set intersection;
3. test whether matching structure permits lower repair-discovery cost;
4. if not, derive reductions/lower bounds explaining the current square-root-scale deterministic frontier.

The 2026 deterministic fully dynamic maximal-matching frontier is n^(1/2+o(1)) amortized update time.

## Implemented baselines

- Full recomputation after each update
- Local greedy repair after each update
- Eager free-neighbor counters
- Heavy/light witness maintenance
- Repair instrumentation: recourse, adjacency probes, propagation work, affected degree, violation discovery cost

## Experiments

- synthetic adversarial graphs
- Erdős-Rényi dynamic graphs
- Barabási-Albert-like hub graphs
- application-style resource-allocation graphs
- threshold sweeps for heavy/light maintenance

Run:

```bash
python experiments/run_benchmarks.py
python experiments/run_application_demo.py
python artifacts/generate_artifacts.py
```

Outputs are written to `results/` and `artifacts/output/`.

## Claim discipline

The code is an experimental research instrument. It does **not** claim a new asymptotic bound until a matching-specific theorem survives prior-art and proof checks.
