# Adaptive repair-index experiment

## Frozen hypothesis
A repair index should be activated only after observed local scan work has accumulated enough debt to pay its construction cost. No future event, dataset identity, or held-out result may enter the decision.

## Costs charged
- adjacency probes during scan
- full adjacency scan when an index is built
- propagation into active indexes after free/matched state changes
- index retirement is O(1) bookkeeping in the prototype

## Comparators
Scan is the primary baseline. Fixed Heavy/Light and Eager remain diagnostic baselines, not targets to beat selectively.

## Evaluation order
1. synthetic hub-stress: verify the policy can discover a regime where indexing helps;
2. Simple Wiki: full external stream;
3. AS-CAIDA: full snapshot-derived stream;
4. NL Wiki: frozen 1M prefix, then full stream only after a disk-backed converter exists.

Parameters build_factor and retire_factor must be selected on synthetic/training data and frozen before external test reporting. Do not tune separately per external dataset.

## Paper gate
Begin full manuscript drafting only if one of these occurs:
A. adaptive policy improves over Scan on at least two independent external datasets after all overhead is charged, without catastrophic regression on the third; or
B. experiments plus theory yield a clean break-even/competitive characterization explaining when indexing cannot pay.

Until then maintain only theorem notes, related-work notes, protocol, and result tables.
