# Results template

This file is intentionally claim-conservative. Populate numeric fields only from committed experiment outputs.

## R1. Recourse–discovery separation

On the star-of-pairs family with k peripheral matched pairs, deletion of the center's matched edge changes only O(1) matching edges. The scan baseline must inspect up to k candidate neighbors in the negative-witness instance.

Report:
- n
- k
- recourse
- probes
- propagation work
- total instrumented work

Interpretation: this demonstrates a separation between output recourse and naive witness-discovery work. It does **not** by itself prove a lower bound for arbitrary dynamic maximal-matching data structures.

## R2. Eager–lazy tradeoff

Compare scan repair with eager free-neighbor maintenance:
- scan pays at witness-query time;
- eager maintenance pays when free/matched state changes propagate through neighborhoods.

The experiment measures where work is paid, not a new asymptotic lower bound.

## R3. Heavy/light intermediate strategy

Evaluate threshold T on sparse, dense, hub-dominated and application-style graphs. Report:
- median work/update
- p95 work/update
- adjacency probes
- propagation work
- recourse
- correctness (maximality after every update)

## R4. Application demo

Use the bipartite request–resource compatibility stream only as an application illustration. Maximal matching represents a conflict-free locally saturated allocation; it is not necessarily maximum-cardinality or utility-optimal allocation.
