# CORRECTION — Lower-Bound Transfer Audit (2026-09-27)

## Correction to TRANSFERRED_TMMR_HARDNESS.md
The previously stated direct transfer of the Kopelowitz–Pettie–Porat incremental SetIntersection Omega(N^{1/2-o(1)}) conditional lower bound to the current TMMR gadget is **NOT YET ESTABLISHED**.

### What maps cleanly
Let S be a dynamic set initially empty and T_j fixed preprocessed sets.
Insertion of element i into S maps to ONE graph update:
    delete x_i y_i.
Thus there is no intrinsic |S|-batch mismatch for incremental insertions.

A single intersection query "is S intersect T_j empty?" maps to ONE trigger deletion:
    delete v_j p_j,
followed by the repair/emptiness decision.

### The unresolved issue
The current graph gadget is one-shot per center/query. After v_j p_j is deleted and repair occurs, the center's state is consumed. KPP's dynamic lower bound concerns a data structure supporting an online sequence of updates and queries. We have not shown how to reset/reuse a queried center, or otherwise simulate the source query sequence with constant overhead while preserving the encoded S.

Therefore the full dynamic KPP lower bound cannot yet be cited as a theorem for TMMR.

## What remains valid
1. Pătraşcu's Multiphase problem is inherently one-shot in Phase III: preprocess sets; process Phase-II set T; receive one index i; answer disjointness. Our one-shot TMMR construction matches this shape directly.
2. The reduction Multiphase -> one-shot TMMR remains valid, with parameter accounting:
   - Phase I incidence graph preprocessing;
   - Phase II up to |T| private-edge deletions;
   - Phase III one protected-edge deletion plus repair decision.
3. Any hardness statement expressed in Pătraşcu's multiphase parameter tau can transfer if Phase-II total time and Phase-III time satisfy the same budgets.

## Pătraşcu parameter map
Source:
- universe size n;
- k=Theta(n^gamma) fixed sets;
- Phase I budget O(nk * tau);
- Phase II budget O(n * tau);
- Phase III budget O(tau);
- conjecture: tau=Omega(n^delta) for constants gamma>1, delta>0.

TMMR graph:
- r=n candidates;
- q=k centers;
- |V|=2n+2k=Theta(k) when gamma>1;
- incidence edges <= nk, plus n+k private/protected edges;
- Phase II has at most n candidate-edge deletions. If per-edge update time is u, total Phase-II time <= n*u;
- Phase III one trigger deletion/repair decision of time q_rep.

Hence if preprocessing is O(nk*tau), u=O(tau), and q_rep=O(tau), the TMMR structure yields a Multiphase solution with parameter tau=max{preprocess/(nk), u, q_rep} up to constants.

Under Pătraşcu's Multiphase Conjecture, for k=Theta(n^gamma):
    max{ normalized preprocessing, per-candidate update, trigger-repair time } = Omega(n^delta).
In graph-vertex terms n=Theta(|V|^{1/gamma}), giving only:
    Omega(|V|^{delta/gamma})
for the relevant maximum, not a square-root bound.

This is a polynomial conditional barrier, but delta and gamma are conjectural constants; do not present a concrete exponent.

## Status
- Multiphase -> one-shot TMMR: VALID.
- Polynomial conditional barrier under Multiphase Conjecture: VALID subject to exact source assumptions.
- KPP square-root dynamic SetIntersection -> current one-shot TMMR: NOT PROVED.
- Concrete Omega(sqrt(N)) TMMR theorem: RETRACTED / NO-GO until reusable queries are constructed.

## Next theorem target
Try to make queries reusable with constant/polylog overhead WITHOUT losing Alice's encoded dynamic set S. If impossible, accept the Multiphase-Conjecture polynomial barrier as the correct theorem and judge paper strength accordingly.
