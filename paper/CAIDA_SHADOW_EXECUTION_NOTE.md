# CAIDA Shadow Replay Execution Note

The frozen AS-CAIDA reconstruction gate has been independently reproduced from the supplied archive:

- 122 snapshots
- 32,955 initial edges
- 542,194 derived dynamic updates
- 281,050 insertions
- 261,144 deletions

The first full local shadow replay exceeded the interactive runtime ceiling before completion. No partial statistics are promoted to results.

## Implementation audit discovered before result generation

1. The phase-aware replay script had undefined `initial` / `dynamic` variables.
2. The committed shadow matcher still treated the first observed neighborhood as churn.
3. Both were corrected before accepting any shadow result.
4. Initial edges now establish the starting graph and greedy maximal matching; metrics begin only at the first genuine dynamic update.

## Next execution optimization

The current exact shadow implementation copies the complete neighbor set/status map at each repair. This is scientifically clear but expensive for high-degree temporal graphs. Replace snapshot copying with exact versioned neighbor-status/change accounting, and validate the optimized tracker against the snapshot implementation exhaustively on small streams before using it on CAIDA.

**Gate:** optimized and snapshot trackers must produce identical event records on exhaustive/small randomized tests. Only then run the 542,194-update CAIDA stream.
