# CAIDA shadow characterization — final finding

## Frozen data gate
122 snapshots; 32,955 initial edges; 542,194 dynamic updates; 281,050 insertions; 261,144 deletions.

## Trajectory convention
The shadow run uses deterministic source-file-order greedy initialization of the initial maximal matching. The update stream is identical to the frozen CAIDA benchmark, but maximal matching is noncanonical; therefore these event-level results are reported as a reproducible shadow trajectory rather than claimed to be identical to the earlier aggregate Scan trajectory.

## Result
54,070 repair events; total discovery D=74,407; p99 D=9; max D=49.

Raw Spearman association with D: degree 0.8980, status change 0.1415, adjacency churn 0.3500, combined change/churn 0.3517. Approximately 49.85% of repair events have some status or adjacency change.

After removing the degree signal, Spearman association of residual discovery with combined change/churn is only 0.0287 (adjacency churn 0.0292; status change -0.1561). Exact-degree comparisons are not monotone: for many common degrees, changed neighborhoods have lower mean discovery than unchanged neighborhoods.

A chronological 70/30 test using a flexible gradient model shows a small incremental predictive signal: log-discovery R2 improves from 0.8041 using degree alone to 0.8270 with status/churn; full-scan AUC improves from 0.9358 to 0.9497.

## Decision
**NO-GO as a central empirical structural law:** status change/churn does not robustly explain repair discovery beyond degree on this CAIDA trajectory. The small predictive increment is suitable as a secondary/negative result, not as the headline novelty.

**GO for manuscript construction around the theoretical repair-complexity contribution**, with this experiment used to delimit what the theory does *not* imply. Do not claim that topological/status churn is the principal driver of repair discovery.
