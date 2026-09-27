# Reusable Trigger Audit

This experiment tests whether the one-shot TMMR center can be reset without corrupting the Phase-II encoded active set.

## Strategies
1. **Naive re-add:** after querying center v_j, simply re-add protected edge v_j p_j.
2. **Explicit restore:** if the query matched v_j to active candidate x_i, explicitly unmatch that edge, re-add v_j p_j, and rematch the protected pair.
3. **Fresh copy:** allocate a fresh protected center copy for each query occurrence.

## Correctness conditions
After every reset:
- graph/matching must be maximal;
- candidate free/matched statuses must encode exactly the original active set S;
- query answer must equal [S intersect T_j != empty].

## Expected structural comparison
Naive re-add cannot generally restore the encoding: when a successful query consumes free candidate x_i by matching it to v_j, x_i is no longer free. Re-adding v_j p_j alone leaves the encoded set changed.

Explicit restore can reconstruct the previous state in this controlled repair model, but only by directly undoing the query-created matching edge and restoring the protected edge. This costs matching recourse and assumes the algorithm is permitted to force the old matching state; it is not a free reusable query in ordinary dynamic maximal matching.

Fresh copies avoid reset but use graph space proportional to the number of queries and therefore do not provide an unbounded reusable dynamic reduction.

## Interpretation
A successful explicit-restore test would show *functional reusability with charged recourse*, not a constant-overhead reduction using ordinary edge updates alone. The distinction is essential for any attempted transfer of reusable dynamic SetIntersection lower bounds.
