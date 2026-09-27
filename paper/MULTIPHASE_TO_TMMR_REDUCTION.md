# Reduction from Pătraşcu's Multiphase Problem to One-Shot Maximal-Matching Repair

## Source problem
Multiphase Set Disjointness:
Phase I: preprocess fixed sets T_1,...,T_q subseteq [r].
Phase II: receive S subseteq [r] and update the data structure.
Phase III: receive index j and decide whether S intersect T_j is empty (or return a witness).

This is an established dynamic-data-structure hardness core; do not claim the multiphase formulation as new.

## Target problem: Triggered Maximal-Matching Repair (TMMR)
Preprocess a graph G and an initial maximal matching M.
Phase II permits a one-shot batch of edge deletions encoding candidate-state changes while preserving maximality.
Phase III supplies a designated matched trigger edge e_j. Delete e_j and determine whether restoring maximality requires matching the newly free center to a candidate neighbor; optionally return such a witness.

## Reduction
Given T_1,...,T_q:
- create candidate x_i and private y_i for each universe item i;
- create center v_j and protected p_j for each set T_j;
- add x_i y_i for every i;
- add v_j p_j for every j;
- add incidence edge v_j x_i iff i in T_j.
Initial matching:
M_0={x_i y_i : i in [r]} union {v_j p_j : j in [q]}.
It is maximal because every x_i and every v_j is matched; y_i,p_j are their matched partners.

Phase II, input S:
delete x_i y_i for each i in S.
Then x_i and y_i become free. No maximality violation is created:
- x_i y_i is absent;
- y_i has no other edge;
- every center v_j adjacent to x_i remains matched to p_j.
Thus the inherited matching remains maximal after every Phase-II deletion.

Phase III, input j:
delete v_j p_j. Now v_j and p_j become free.
v_j has a free candidate neighbor iff there exists i in S with i in T_j.
Therefore:
S intersect T_j != empty
iff
after trigger deletion, the inherited matching is non-maximal
iff
a local maximality-restoring repair at v_j must use some free x_i in N(v_j).

If witness output is required, any x_i chosen to match v_j is an element of S intersect T_j.

## Parameter map
Vertices: 2r+2q.
Edges: r+q+sum_j |T_j|.
Phase-II graph updates: |S| edge deletions.
Phase-III graph updates: one trigger-edge deletion.
The incidence set system is represented explicitly in the preprocessed graph.

## Theorem (reduction)
Any data structure for TMMR with preprocessing P, Phase-II update cost U per candidate deletion (or total U_S), and Phase-III trigger/repair decision cost Q yields a data structure for the multiphase set-disjointness instance with corresponding preprocessing, |S| Phase-II updates, and one Phase-III query.

Hence any applicable lower bound/conjectured hardness for the multiphase problem transfers to TMMR under the same computational model and parameter accounting.

## Critical scope
This does NOT automatically lower-bound ordinary fully dynamic maximal-matching maintenance, because an ordinary matcher is only required to output/maintain some maximal matching; it may proactively rematch freed candidates during Phase II rather than preserve the inherited matching used by TMMR.

Therefore the reduction is immediately valid for:
- repair-oracle / inherited-matching maintenance models;
- algorithms constrained to preserve the current maximal matching until it becomes invalid;
- local repair models matching the behavior of Scan/Eager/HeavyLight prototypes.

To transfer hardness to unrestricted fully dynamic maximal matching, we would need a gadget forcing Phase-II candidate x_i to remain free despite the algorithm's freedom to rematch it. That forcing problem is exactly the earlier unresolved obstacle.

## Scientific consequence
The multiphase reduction gives a recognized hardness basis for the repair model, but also precisely exposes the gap between local repair complexity and unrestricted dynamic maximal matching.
