# Transferred Hardness Theorem for Triggered Maximal-Matching Repair (TMMR)

## Source facts
Pătraşcu (STOC 2010) defines the Multiphase problem, a dynamic set-disjointness problem, and uses it as a modular hardness core. The paper relates sufficiently fast Multiphase data structures to strongly subquadratic 3SUM algorithms.

Ko and Weinstein (FOCS 2020) prove a ~Omega(sqrt(n)) cell-probe lower bound for a Multiphase setting with general adaptive updates and layered-adaptive queries; their result is model-restricted and should not be quoted as an unrestricted lower bound.

Kopelowitz, Pettie and Porat (WADS 2015/full version) prove, conditioned on Integer3SUM, that for incremental set-intersection emptiness either update or query time is Omega(N^{1/2-o(1)}), where N is total set-family size.

## TMMR reduction recap
For fixed query sets T_1,...,T_q subseteq [r], construct:
- candidates x_i--y_i;
- protected centers v_j--p_j;
- incidence v_j--x_i iff i in T_j.
The inherited matching contains all private/protected edges.
Phase-II input S is encoded by deleting x_i y_i for i in S; inherited matching stays maximal.
Phase-III index j deletes v_j p_j.
Then a repair is necessary at v_j iff S intersect T_j is nonempty, and a repair witness gives an intersection witness.

## Safe conditional theorem
**Theorem (conditional transfer, repair-preserving model).**
Any TMMR data structure in the same computational model that, after preprocessing the incidence graph, supports the Phase-II candidate deletions and the Phase-III trigger/emptiness decision with costs that would violate the corresponding published Multiphase / incremental SetIntersection lower bound would yield the forbidden faster source-problem data structure through the reduction above.

In particular, when instantiated through an incremental SetIntersection family of total incidence size N for which the Kopelowitz--Pettie--Porat Integer3SUM lower bound applies, the corresponding TMMR instance inherits the conditional statement that update and repair-query costs cannot both be N^{1/2-o(1)}-smaller: at least one is Omega(N^{1/2-o(1)}) under the Integer3SUM conjecture, subject to the same source-model and parameter assumptions.

## Parameter caution
Our graph size is:
|V|=2r+2q,
|E|=r+q+N, where N=sum_j |T_j|.
Thus the transferred lower bound is naturally expressed in terms of incidence size N (and hence O(|E|)), not automatically as sqrt(|V|). Dense set systems may have N=Theta(rq).

Phase-II input S is represented by |S| candidate-edge deletions. Therefore distinguish:
- per-candidate graph-update time u;
- total Phase-II time |S|u;
- Phase-III trigger/repair-query time q.
Do not silently equate a source problem's one Phase-II operation with one graph-edge deletion if its model treats the whole set S as one update phase.

## What we may claim
- A reduction from set-disjointness/multiphase-style queries to TMMR.
- Conditional hardness inherited under explicitly matched source assumptions.
- For suitable incremental SetIntersection parameterizations, a square-root incidence-size update/query barrier transfers to the repair-preserving TMMR formulation.

## What we may NOT claim
- Omega(sqrt(m)) for unrestricted fully dynamic maximal matching.
- Omega(sqrt(n_vertices)) without a parameter conversion for the chosen hard family.
- An unconditional polynomial lower bound.
- Ko--Weinstein's restricted-model result as an unrestricted TMMR theorem.
- The 2026 Boolean Inner-Product Multiphase lower bound for our SetDisjointness predicate without a new reduction.

## Manuscript consequence
This is now a legitimate theorem route, but the final paper theorem must choose ONE source lower bound, reproduce its exact assumptions, construct the corresponding hard set family, and map N,r,q,|S|, graph vertices/edges, update cost, and repair-query cost explicitly.
