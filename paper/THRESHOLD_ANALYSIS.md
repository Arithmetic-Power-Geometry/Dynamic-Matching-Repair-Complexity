# Threshold law and testable hypotheses

Let T be the heavy/light threshold.

For a light repair vertex v, degree(v) <= T, so a direct free-neighbor scan costs at most T adjacency probes.

For a heavy repair vertex h, the prototype maintains a free-neighbor witness set, so lookup is O(1) at query time. A matched/free state change of x propagates only to heavy neighbors of x. Define

    H(x) = |{ y in N(x) : y is currently classified heavy }|.

Then the directly instrumented state-change cost is O(H(x)); it is not automatically O(n/T) for arbitrary graphs.

Accordingly, a single local repair event involving endpoints u and v has prototype work bounded in terms of

    O(T + H(u) + H(v) + propagation caused by any newly matched witness).

This is an instance-structural bound, not a universal sqrt(n) theorem.

## Hypothesis H1 — tail suppression
On degree-skewed graphs where repair frequently touches high-degree vertices but each state-changing vertex has relatively few heavy neighbors, heavy/light maintenance reduces maximum repair work relative to direct scan.

## Hypothesis H2 — no universal dominance
On low-degree or homogeneous graphs, direct scan can have lower total work because witness propagation overhead is unnecessary.

## Hypothesis H3 — threshold is workload dependent
The T minimizing total work need not minimize maximum work. Report both objectives and the Pareto curve.

## Required theorem work
A publishable theoretical contribution requires either:
1. a formally defined graph/update class with a nontrivial bound on H(x) or a related structural parameter, or
2. a new data structure that controls propagation without assuming such a bound.

Do not replace H(x) by n/T without an additional incidence/degree argument.
