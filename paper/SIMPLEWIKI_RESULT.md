# Dynamic Simple Wiki: corrected real-data result

Source: KONECT Dynamic Simple Wiki. Raw directed +/- temporal records were projected to undirected matching edges by ignoring self-loops and keeping a projected edge active while either directed arc was active.

Projection integrity:
- raw records: 1,627,472
- self-loops removed: 3,664
- projected updates: 1,514,719
- insertions: 1,106,716
- genuine deletions: 408,003
- duplicate additions: 0
- orphan removals: 0

Corrected heavy/light implementation includes edge-summary maintenance and degree-threshold reclassification.

Result: Scan outperformed heavy/light on both total instrumented work and repair tail on this dataset. Heavy/light therefore has no universal tail advantage. The synthetic hub result should be treated as a structural-regime result, not a general performance claim.

This is a local reference execution; reproduce in CI/native external baselines before manuscript-level runtime claims.
