# Discovery–Propagation Tradeoff: restricted exact-summary model

## Model
Fix a vertex v with neighborhood N(v) of size d. Each neighbor u has a dynamic bit f(u) in {0,1}, where f(u)=1 means u is currently free. A repair query at v must return some u with f(u)=1 or certify that none exists.

Consider an **exact explicit-summary algorithm** with two permitted ways to learn the current free status relevant to v:

1. **Propagation:** when f(u) changes, the update may write information into state associated with v (or a shared summary that the query for v reads without probing u);
2. **Discovery:** at query time, the algorithm probes current neighbor states f(u).

The query must be exact for every state sequence. We count one unit for each neighbor-state change propagated into query-visible summary information and one unit for each neighbor status probed during discovery.

This is deliberately a restricted information-flow model; it is not a cell-probe lower bound for arbitrary dynamic data structures.

## Lemma 1 — uncommunicated-change indistinguishability
Let S be a set of neighbors whose statuses may have changed since the last point at which the query-visible summary was known exact. If the update mechanism communicates no information distinguishing the current status of some x in S, then an exact query that does not probe x cannot, in general, distinguish two executions identical in all observed information but with f(x)=0 versus f(x)=1.

Proof sketch: choose the remaining neighbors to be nonfree. The two executions have identical summary state and identical answers to every other probe. One requires the answer NONE; the other permits/requires x as the only free witness. Therefore an exact algorithm must obtain information about x either during its update or during the query.

## Corollary 1 — per-epoch discovery–propagation accounting
Suppose r distinct neighbors of v have potentially changed free/nonfree status during an epoch, and the adversary may make any one of those r vertices the unique free neighbor at query time while all unchanged neighbors are nonfree. Let P be the number of those r neighbors whose new status is communicated into exact query-visible state before the repair query. Then, in the worst case, an exact deterministic query must inspect at least r-P of the remaining changed neighbors before it can certify absence / locate the adversarial witness.

Hence in this restricted model:
    P + D >= r,
where D is worst-case discovery probes among the changed neighbors.

## Interpretation for dynamic matching
A matched/free transition of a neighbor is exactly the event that can invalidate a cached free-neighbor summary. Thus an exact eager structure pays propagation as these transitions occur; a lazy structure can defer them, but unresolved transitions reappear as discovery uncertainty at repair time.

This formalizes a local conservation principle:
    information not propagated must remain discoverable.

## Limits / non-claims
- This does NOT prove a lower bound for arbitrary fully dynamic maximal-matching algorithms.
- It does NOT rule out compressed summaries, randomized sketches, word-level parallelism, shared structures, or algorithms exploiting correlations imposed by matching.
- P+D>=r is an information-flow statement for an explicit exact-summary model.
- A paper-level theorem requires either extension to a recognized computational model or a compelling structural/empirical theory built around the restricted model.

## Next extension target
Attempt a cell-probe / communication formulation for dynamic neighborhood emptiness or witness reporting under the matching-constrained free set. Determine whether known dynamic set-intersection / OMv lower bounds already subsume it. If they do, use the lemma only as exposition, not novelty.
