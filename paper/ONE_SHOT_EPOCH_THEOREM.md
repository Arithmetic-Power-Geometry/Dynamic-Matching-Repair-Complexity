# One-Shot Repair Epoch Theorem

## Construction
For integer r>=1, create:
- center v and protected partner p with edge vp;
- candidates x_1,...,x_r, each adjacent to v;
- for each candidate x_i, a private partner y_i with edge x_i y_i.

Initially M contains vp and every x_i y_i. Thus M is maximal and every candidate is matched.

During the hidden-update epoch, for an arbitrary subset S of candidates, the environment may perform local state-changing operations whose net effect is that exactly candidates in S are free immediately before the repair trigger, while v remains matched to p. We consider an explicit-summary information model in which each candidate's resulting free/nonfree state is either communicated to v's query-visible repair state (propagation) or remains unresolved there.

The repair trigger deletes vp. Now v is free and must either match a free candidate x_i or certify that none is free to restore maximality locally.

## Theorem (epoch discovery–propagation tradeoff)
Suppose r candidate statuses are independently admissible at trigger time within the epoch family, and P of those statuses have been communicated into v's exact query-visible state. For a deterministic exact repair procedure, worst-case candidate-status discovery D satisfies

    P + D >= r.

## Proof
Let U be the r-P candidates whose current status is not distinguished by the query-visible state. Assume the repair procedure probes fewer than |U| candidate statuses. Then some x in U is unprobed.

Consider two admissible epoch outcomes identical on:
- all propagated information;
- every candidate probed by the repair procedure;
- all other graph information observed by the procedure.

Set every probed/unpropagated candidate nonfree in both outcomes. In outcome A let x be nonfree and all of U be nonfree. In outcome B let x be the unique free candidate in U.

After deletion of vp, the procedure receives the same observations in A and B. In A it may correctly certify no free candidate (subject to propagated candidates also being nonfree); in B maximality requires v not remain free adjacent to free x, so a valid local repair must discover/match a free candidate. The identical transcript cannot be correct in both outcomes. Contradiction.

Therefore every unpropagated candidate status must be discoverable in the worst case, giving D>=r-P.

## Important realizability caveat
The theorem assumes the epoch family can realize the designated candidate free/nonfree statuses while preserving the stated graph/matching conditions. A concrete O(1)-update-per-candidate gadget must be supplied before calling this a graph-theoretic dynamic-matching lower bound.

With the simple private-partner gadget, making x_i free by deleting x_i y_i while edge vx_i remains present does NOT preserve maximality before the trigger because v is matched (so edge vx_i may have free x_i and matched v; that is allowed) — therefore x_i may indeed remain free while v is matched. However y_i also becomes free; since y_i has only x_i as neighbor and x_i is free, edge x_i y_i has been deleted, so no free-free edge remains. To restore x_i to matched/nonfree state within a reusable epoch would require reinsertion and algorithmic choice; one-shot realization needs only deletion from the all-matched initial state.

Thus arbitrary subsets S can be realized one-shot by deleting x_i y_i for i in S. Each such deletion frees x_i,y_i without violating maximality because their mutual edge is absent and v remains matched to p.

## Consequence
For this one-shot family, after deleting vp, exact local repair faces a genuine matching-induced uncertainty set of size r. If candidate state changes were not propagated into a repair summary, worst-case repair must discover them.

This is a matching-specific epoch lower bound in a restricted explicit-information model. It is not a cell-probe lower bound for arbitrary dynamic maximal-matching algorithms and does not establish a new asymptotic bound.
