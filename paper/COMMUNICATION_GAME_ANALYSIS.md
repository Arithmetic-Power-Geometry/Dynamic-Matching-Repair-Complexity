# Communication-game route: what the one-shot gadget can and cannot prove

## Game G_epoch
Alice receives S subseteq [r]. Starting from the all-matched gadget, she deletes x_i y_i exactly for i in S. The resulting memory state of a dynamic matching data structure is passed to Bob. Bob performs the trigger deletion vp and must restore/report a maximal matching outcome.

If Bob's task is only "is there any free candidate?", then his query is whether S is empty. This is NOT Set Disjointness with two independent inputs; Bob has no independent subset T. Alice can communicate emptiness in one bit. Therefore the current one-center gadget cannot yield an Omega(r)-bit communication lower bound against arbitrary compression.

This is a crucial NO-GO result.

## Why explicit-summary P+D>=r nevertheless held
That theorem forbids joint compression by construction: unresolved candidate statuses must be learned individually. Once arbitrary compressed memory is allowed, Alice can summarize the only question needed by the fixed center v ("does any candidate exist?") with one bit, or store a witness with O(log r) bits.

Thus no linear information lower bound is possible for the fixed-neighborhood one-shot query.

## What a genuine communication reduction would need
Bob must possess an independent query input T subseteq [r], so the repair question computes:
    Is S intersect T nonempty?
or returns a witness in S intersect T.
Then randomized bounded-error communication is Omega(r) in the dense Set-Disjointness regime.

To realize this inside matching, Bob's T must select which candidates are adjacent/relevant to the triggered repair vertex without destroying the encoded free/nonfree state. This is exactly the state-query coupling problem.

## Candidate multi-center construction
Create many protected centers v_j, each with a fixed neighborhood T_j over candidate vertices x_i. Alice encodes S by freeing candidates. Bob chooses a center j and deletes its protected edge v_j p_j. The repair asks whether S intersects T_j.

This realizes a static family of query subsets T_j without Bob dynamically inserting query-incidence edges after Alice's encoding.

However:
- if the family {T_j} is explicitly stored in the graph, graph size may be Theta(r^2);
- a single chosen j is analogous to INDEX/membership for singleton T_j and may have only one-way INDEX hardness if all r singleton centers are represented;
- candidate x_i adjacent to multiple matched centers can remain free because those centers are matched, so Alice's one-shot encoding remains feasible;
- after trigger, a free x_i adjacent to v_j forces repair/maximality, so the query semantics work.

## Promising next theorem target
Use r centers with singleton neighborhoods T_j={j}. Alice encodes an r-bit vector S by deleting x_i y_i. Bob receives index j and triggers center v_j. Correct repair distinguishes whether j in S.

This embeds the one-way INDEX problem into a one-shot dynamic maximal-matching state-transfer problem.

If the data structure's persistent memory after Alice's updates is treated as Alice's one-way message and Bob has no access to Alice's update sequence except through that memory, randomized bounded-error INDEX requires Omega(r) bits of retained information.

Caveat: an ordinary data structure is allowed Theta(r) or more persistent memory anyway, so this proves a space/information requirement, not an update/query-time lower bound. To obtain a cell-probe time tradeoff, one must bound which cells written by Alice are read by Bob, requiring a standard information-transfer/cell-probe argument.

## Status
- Fixed-center communication lower bound: NO-GO (compressible to witness/emptiness).
- Multi-center INDEX embedding: graph construction appears valid one-shot.
- Omega(r) persistent-information consequence: plausible direct INDEX reduction.
- Cell-probe update/query tradeoff: NOT YET PROVED.
