# Multi-Center INDEX: Information-Transfer Lemma

## Gadget
For i=1,...,r create candidate x_i with private partner y_i.
For j=1,...,r create protected center v_j with private partner p_j.
Add candidate edge v_j x_j (singleton-query version).
Initially M contains every x_i y_i and every v_j p_j.

Alice receives z in {0,1}^r. For each i with z_i=1 she deletes x_i y_i. Because every v_i remains matched to p_i, x_i may remain free without violating maximality.

Bob receives j in [r] and deletes v_j p_j. Then:
- if z_j=1, v_j and x_j are adjacent and both free, so maximality forbids leaving both unmatched;
- if z_j=0, x_j remains matched to y_j, so v_j has no free candidate neighbor in this gadget.

Thus the post-trigger repair state reveals z_j.

## Lemma — retained-information requirement
Consider any one-shot dynamic maximal-matching representation whose state after Alice's update epoch is the only information about z available to Bob before he receives j. If Bob must answer/repair correctly with bounded error <1/2 for uniformly random z and j, then the persistent state that depends on Alice's epoch must contain Omega(r) bits of information in the standard one-way randomized INDEX sense.

This is an information/space statement, not a time lower bound.

## Proof route
The dynamic representation induces a one-way communication protocol:
1. Alice simulates the initialization and her deletions for z.
2. Alice sends the resulting persistent representation/state to Bob.
3. Bob receives j, simulates deletion of v_j p_j and the repair/query procedure.
4. From whether the repair matches v_j to x_j (or equivalently from the resulting local status) Bob recovers z_j.

Therefore a representation/message enabling bounded-error recovery for arbitrary j is a one-way protocol for INDEX_r. Standard randomized one-way INDEX requires Omega(r) communicated bits.

## Important model caveat
If the dynamic algorithm uses private randomness that Bob must continue consistently, the communicated state must include the necessary public/shared randomness convention or random seed/state. The reduction should be stated in the standard public-coin or state-transfer formulation.

## Why this does not contradict fast dynamic maximal matching
Omega(r) retained information is cheap when the graph itself has Theta(r) vertices/edges and the algorithm has linear or larger memory. It says nothing yet about update or query time. Existing fast maximal-matching algorithms may write information incrementally during Alice's r updates.

## Toward a time tradeoff
Partition Alice's epoch into update cells written W and Bob's repair cells read R. To derive a time lower bound, show that Bob's reads must recover enough information about z_j from cells whose contents depend on Alice's updates. A naive INDEX argument only yields total retained information Omega(r), not that a single query reads Omega(r) cells.

Indeed an array storing z_i in one word per candidate gives:
- O(1) writes per candidate update,
- O(1) read for Bob's chosen j,
while using Theta(r) total bits.
Therefore **the singleton-center INDEX gadget cannot prove a superconstant query-time lower bound.**

This is a second crucial NO-GO.

## What would be required for a nontrivial update/query lower bound
Bob's query must depend on many Alice bits in a way that cannot be answered by one addressed cell, e.g. a subset query T_j asking whether S intersects T_j. The query family must be sufficiently rich while represented compactly enough that graph size does not trivialize the bound.

Potential route:
- r candidate bits x_i;
- q protected centers v_j;
- neighborhoods T_j forming a hard set system;
- Alice frees S;
- Bob triggers v_j, computing witness/emptiness of S intersect T_j.

Then invoke static/dynamic set-disjointness or lopsided-disjointness lower bounds in an appropriate cell-probe model, while checking graph-size and preprocessing assumptions.

## Decision
Singleton INDEX embedding: useful information-space lemma, but **NO-GO for nontrivial repair-time lower bound**.
Next target: hard multi-center set system, not singleton centers.
