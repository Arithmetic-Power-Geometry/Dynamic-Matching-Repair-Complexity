# Discovery Profile: Exact Observable Metrics

The current real-data RepairTrace logs record repair-time degree d and actual Scan discovery work D (neighbor probes). They do **not** record the exact epoch-specific number r of candidate statuses that changed, nor propagation P for an alternative indexed algorithm on the identical matching trajectory.

Therefore this analysis deliberately does not report P+D-r or claim an empirical test of the restricted P+D>=r theorem.

It reports the exact observable ratio

    scan intensity a = D/d

for d>0, plus:
- full-neighborhood-scan fraction;
- successful-witness vs NONE repairs;
- first vs repeated repairs;
- logarithmic degree bands;
- discovery-work quantiles.

This directly complements the future-burden identity Q=sum a_i g_i by measuring its a_i component on the real traces.

## Next instrumentation needed for theorem-slack measurement
Replay a raw update stream while recording, for each repair epoch and vertex:
1. statuses of its neighbors at the previous repair;
2. which candidate statuses changed since then (exact r);
3. Scan discovery D;
4. a shadow exact-summary strategy's propagated candidate-status changes P, without allowing the shadow strategy to alter the Scan matching trajectory.

Only that shadow replay can legitimately compute P+D-r event by event.
