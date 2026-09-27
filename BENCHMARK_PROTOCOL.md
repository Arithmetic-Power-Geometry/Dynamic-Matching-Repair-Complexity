# Benchmark Protocol

The benchmark suite compares repair and maintenance policies under a common charged-work accounting.

## Policies

- full recomputation
- local scan repair
- eager exact free-neighbor summaries
- heavy/light summary maintenance
- adaptive-debt policy as a falsification experiment

Charged work is reported as discovery probes plus propagation work. Recourse is recorded separately.

## Synthetic stress

The repair-stress family is designed to expose tail behavior. At n = 1024, scan reaches a maximum repair cost of 1023 probes while heavy/light reaches 16, a 63.9× reduction. Total scan work (6460) is nevertheless below heavy/light work (7152), so the result is not presented as universal dominance.

## Application-style workload

For the n = 1000 request/resource workload:

| Algorithm | Total work | Median | p95 | Max | Recourse |
|---|---:|---:|---:|---:|---:|
| Recompute | 37,498,500 | 24,999 | 25,000 | 25,000 | 38,530 |
| Scan | 31,275 | 0 | 53 | 63 | 1,389 |
| Eager | 69,522 | 49 | 99 | 163 | 1,396 |
| Heavy/light | 33,847 | 5 | 55 | 59 | 1,389 |

All reported runs maintain maximality.

## Interpretation

Benchmarks are used to distinguish aggregate work, tail repair cost, propagation cost, and recourse. They are not used to claim that one policy is universally superior.
