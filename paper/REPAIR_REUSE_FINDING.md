# Repair-reuse finding

| Dataset | Repair events | Repaired vertices | Repeated vertices | Repeated % | Oracle R*>1 vertices | Oracle % | Scan work in oracle-indexable vertices |
|---|---:|---:|---:|---:|---:|---:|---:|
| Simple Wiki | 59,780 | 39,901 | 12,218 | 30.62% | 3,412 | 8.55% | 17.77% |
| AS-CAIDA | 40,373 | 14,901 | 7,355 | 49.36% | 673 | 4.52% | 8.32% |

R* is deliberately optimistic: future scan work divided only by build degree, ignoring maintenance. Therefore R*>1 is an upper-bound opportunity diagnostic, not an implementable decision rule.

## Finding
Repair recurrence is not equivalent to indexability. CAIDA has substantially more recurrent repaired vertices, yet roughly half the oracle-indexable fraction and less than half the concentration of potentially avoidable scan work seen in Simple Wiki.

This explains why a policy based on accumulated historical repair/scan debt can fail: repeated repairs can remain individually cheap, sparse in useful future scan work, or expensive to maintain.

## Next test
Do not design Algorithm #3 yet. Test whether any observable pre-activation features predict R*>1 out of sample:
- current degree;
- repair count so far;
- cumulative scan work so far;
- previous scan work;
- recent inter-repair gaps;
- degree change since prior repair.

Train only on synthetic + one external dataset, then evaluate classification/ranking on the other external dataset. Compare against degree-only and repair-count-only baselines. If no predictor transfers, adaptive indexing is likely a dead end for this mechanism.
