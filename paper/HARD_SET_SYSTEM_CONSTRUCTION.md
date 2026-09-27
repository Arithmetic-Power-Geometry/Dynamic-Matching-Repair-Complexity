# Hard Set-System Multi-Center Construction

## Graph family
Candidates: x_1,...,x_r, each initially matched to private y_i.
Centers: v_1,...,v_q, each initially matched to private p_j.
Choose a fixed set system T_1,...,T_q subseteq [r].
Add edge v_j x_i iff i in T_j.

Initially all candidates and centers are matched, so the matching is maximal.

Alice encodes S subseteq [r] one-shot by deleting x_i y_i for i in S. Candidate x_i becomes free. Since every center remains matched, these free candidates do not violate maximality.

Bob chooses query j and deletes v_j p_j. Then v_j is free.
There exists a free neighbor of v_j iff S intersect T_j is nonempty.
Therefore restoring maximality / reporting a repair witness computes static set-intersection emptiness/witness for S against the fixed query family {T_j}.

## Key validity check
Before Bob's trigger:
- free candidates may share matched center neighbors; maximality only forbids edges with two free endpoints, so this is legal;
- y_i is free when x_i y_i is deleted, but its only gadget edge to x_i is absent;
- all centers are matched to p_j.
After trigger:
- if S intersect T_j != empty, leaving v_j free would violate maximality because it has a free neighbor;
- if S intersect T_j = empty, v_j may remain free locally.

Thus the one-shot reduction is graph-theoretically valid.

## What this buys
The repair query is no longer a single addressed bit. It is:
    EMPTY/WITNESS(S intersect T_j).
With a hard fixed set system, this is a static set-disjointness / set-intersection data-structure problem embedded inside a maximal-matching repair epoch.

Any cell-probe lower bound imported from the static set-system problem must account for:
- space S_space of the maintained representation;
- word size w;
- preprocessing/initial graph containing all T_j incidences;
- update cost to encode candidate activation/free state;
- query/repair probes after trigger.

## Critical novelty warning
This construction may mean that the matching-specific repair problem simply **contains a known set-intersection data-structure problem**. If so, the lower bound is inherited rather than a new lower-bound technique. The contribution could still be a new reduction/lower bound for a carefully defined maximal-matching repair oracle, but it must be searched exhaustively before claiming novelty.

## Next exact task
Choose a recognized hard set system and state the strongest lower bound that transfers under its assumptions. Search:
- static set disjointness cell-probe lower bounds;
- lopsided set disjointness;
- multiphase problem / Pătraşcu;
- set intersection reporting data structures;
- dynamic set intersection 3SUM lower bounds.

Then determine whether the resulting transferred bound says anything nontrivial about standard fully dynamic maximal-matching maintenance, or only about an added repair-query oracle.
