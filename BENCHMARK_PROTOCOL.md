# Benchmark protocol

## Goal
Measure where heavy/light witness maintenance helps and where it hurts. Runtime alone is insufficient; report probes, propagation, total instrumented work, median, p95, maximum update work, recourse, and maximality.

## Algorithms
1. Full greedy recomputation.
2. Local scan repair.
3. Eager free-neighbor maintenance.
4. Heavy/light witness maintenance with threshold T.

These are reproducible baselines implemented in this repository. We do not claim to implement the STOC 2025 or STOC 2026 theoretical algorithms.

## Workloads
- Erdos-Renyi sparse/medium/dense.
- Hub-dominated synthetic graphs.
- Matched-edge deletion/reinsertion repair stress.
- Request-resource compatibility application.
- Threshold sweep: T in {2,4,8,16,32,64,sqrt(n),2sqrt(n)}.
- Multiple seeds for stochastic workloads.

## Primary endpoint
Maximum and p95 instrumented work per update. Secondary endpoints: total work, wall-clock time, recourse.

## Correctness
After every update, verify that no edge has two free endpoints. A run is invalid if maximality fails.

## Interpretation rule
A heavy/light advantage is a tail-latency result unless it also lowers total work and runtime. Synthetic stress results must not be presented as general real-world speedups.

## External comparison
DynMatch (ESA 2020) is the appropriate established implementation framework for later native-code comparison. It implements several fully dynamic matching algorithms including random-walk, Neiman-Solomon and Baswana-Gupta-Sen. Cross-language wall-clock comparisons require a controlled machine/build and are not inferred from this Python prototype.
