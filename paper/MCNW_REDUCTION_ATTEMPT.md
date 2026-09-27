# Matching-Constrained Neighborhood Witness (MCNW): reduction attempt

## Primitive
Maintain a graph G together with a maximal matching M. A query at v asks for a free neighbor of v (a vertex u in N(v) with mate[u]=NONE), or NONE.

Unlike generic dynamic set intersection N(v) intersect F, the set F of free vertices is constrained:
1. F is an independent set in G;
2. F changes endogenously when M changes;
3. the algorithm may choose among multiple maximal matchings, so F is not uniquely controlled by the update sequence.

## Why the obvious generic reduction fails
To encode an arbitrary active bit for item x, one would like a vertex x to be free iff bit(x)=1. A private dummy x' with edge xx' appears to permit toggling:
- bit 0: keep xx' present and x matched;
- bit 1: remove xx' and make x free.

But after other matching edges are present, maximality does not force x to rematch to x' when xx' is reinserted. The dynamic matching algorithm may legally keep x matched elsewhere or reroute. Thus a reusable arbitrary-bit simulation is not obtained with O(1) updates.

This is not a technical nuisance: maximal matching specifies a property, not a canonical matching state.

## Restricted reduction that does work
If every item vertex x has no possible matching edge except its private dummy xx', and query vertices are not themselves part of the maintained matching graph (equivalently, query sets are external/read-only incidence lists), then arbitrary free bits can be represented exactly by deleting/inserting xx'. A query list S asks whether S intersects the free items.

But this is no longer ordinary graph-neighborhood witness inside one maximal-matching graph; it separates the query incidence structure from the matching graph. Therefore generic dynamic set-intersection lower bounds transfer only to this external-incidence variant, not automatically to MCNW.

## Structural obstruction
Internalizing a query edge vx into G changes the matching possibilities of x and v. Hence the very incidence relation used to ask the question can alter the state being queried. This feedback is absent from ordinary dynamic set intersection.

## Candidate research statement
The difficulty of reducing generic dynamic set intersection to MCNW comes from **state-query coupling**: query incidences are graph edges, and graph edges participate in the matching whose free set defines the query predicate.

This observation is potentially useful, but it is not a lower bound.

## Next route
Rather than force arbitrary bits, seek a lower bound directly on a restricted family where:
- a designated center v is kept matched to a protected partner;
- candidate neighbors x_i have controlled matched/free transitions using local gadgets;
- query is triggered only after deleting v's protected matched edge;
- after query, the construction need not be reusable (one-shot epoch).

A one-shot epoch can support an information lower bound without solving reusable reset. The target is an epoch theorem, not a full dynamic lower bound.
