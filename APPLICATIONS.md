# Applications

## 1. Dynamic request-resource allocation
Vertices represent requests and resources; compatibility is an edge. Edge insertion/deletion models changing eligibility, capacity compatibility, locality, or service availability. A maximal matching provides a locally saturated conflict-free allocation, not necessarily a maximum-cardinality or utility-optimal allocation.

## 2. Communication link pairing
Vertices represent endpoints eligible for pairwise communication. Link changes represent changing reachability/interference constraints. Repair-tail latency matters when a high-degree endpoint loses its current pair and a replacement must be found quickly.

## Why repair-tail latency matters
The experimental hypothesis is not that every update becomes cheaper. It is that witness summaries can cap expensive neighborhood scans around high-degree vertices, trading small background propagation cost for lower extreme repair cost.

## Non-claims
This prototype does not model fairness, weights, capacities greater than one, kidney-exchange cycles, or globally optimal assignments.
