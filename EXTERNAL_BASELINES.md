# External baselines and literature

## Theory frontier
Chuzhoy, Khanna and Song, STOC 2026: deterministic fully dynamic maximal matching with n^(1/2+o(1)) amortized update time. Their subgraph-system framework is designed for verification and maintenance of maximality.

Bernstein, Bhattacharya, Kiss and Saranurak, STOC 2025: first deterministic sublinear fully dynamic maximal matching, with ~O(n^(8/9)) amortized update time.

## Practical baseline
Henzinger, Khan, Paul and Schulz, ESA 2020, Dynamic Matching Algorithms in Practice. Their DynMatch implementation includes several fully dynamic algorithms and is the appropriate native-code external benchmark for a later controlled-machine comparison.

## Comparison policy
The Python experiments in this repository compare only algorithms implemented under the same instrumentation. Published asymptotic bounds are reported separately. We do not compare Python wall-clock numbers with published C++ timings or claim superiority over STOC algorithms without implementing/running them under a common protocol.
