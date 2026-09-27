# Audited Multiphase Hardness Theorem

**Theorem (conditional, one-shot repair-preserving model).**
Let n be the Multiphase universe size and k=Theta(n^gamma), gamma>1, the number of preprocessed sets. Construct the TMMR graph with one candidate pair per universe element and one protected center per preprocessed set, with incidence edges representing set membership.

Suppose a TMMR data structure:
1. preprocesses the graph in P(n,k) time;
2. processes each Phase-II candidate-edge deletion in worst-case/amortized time u(n,k), as appropriate to the source model;
3. processes the single Phase-III trigger deletion and repair-disjointness decision in q(n,k) time.

Then it solves the Multiphase instance with
    tau = O(max{P(n,k)/(nk), u(n,k), q(n,k)})
provided the Phase-II sequence contains at most n candidate deletions.

Consequently, under Pătraşcu's Multiphase Conjecture, there exist constants gamma>1 and delta>0 such that for k=Theta(n^gamma),
    max{P/(nk), u, q} = Omega(n^delta).

Since |V|=Theta(n^gamma) in this regime, this may equivalently be written
    max{P/(nk), u, q} = Omega(|V|^{delta/gamma}).

No concrete value of delta/gamma is claimed.

**Scope.** This theorem applies to the one-shot inherited/output-stable Triggered Maximal-Matching Repair model defined in this project. It is not a lower bound for unrestricted fully dynamic maximal matching.

## Why this theorem is clean
- one Phase-II element insertion/state activation = one private-edge deletion;
- Phase II contains at most n such updates, matching O(n tau) source budget;
- Phase III = one trigger deletion + repair decision, matching O(tau);
- the source problem itself has only one Phase-III query, so no reset gadget is required.

## Why KPP is not used here
KPP's incremental SetIntersection lower bound is for a reusable dynamic data structure supporting a query sequence. The current TMMR gadget has not established reusable queries. Therefore its concrete Omega(N^{1/2-o(1)}) lower bound is not imported.
