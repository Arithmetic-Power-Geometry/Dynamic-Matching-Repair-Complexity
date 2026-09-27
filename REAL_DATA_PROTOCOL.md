# Real-Data Protocol

The real-data study uses three temporal graph traces:

1. KONECT Dynamic Simple Wiki.
2. A one-million-record prefix of Dynamic NL Wiki.
3. 122 weekly AS-CAIDA snapshots from SNAP.

## Frozen validation totals

| Dataset | Algorithm | Total work | p99 | Max |
|---|---|---:|---:|---:|
| Simple Wiki | Scan | 204,572 | 4 | 292 |
|  | Eager | 1,312,908 | 21 | 2,456 |
|  | Heavy/light | 518,440 | 6 | 317 |
| NL Wiki 1M | Scan | 66,194 | 1 | 236 |
|  | Eager | 922,549 | 13 | 3,221 |
|  | Heavy/light | 383,848 | 1 | 512 |
| AS-CAIDA | Scan | 72,544 | 4 | 42 |
|  | Eager | 591,973 | 18 | 4,684 |
|  | Heavy/light | 248,748 | 8 | 206 |

## CAIDA reconstruction gate

The reconstruction must produce exactly:
- 32,955 initial edges;
- 542,194 subsequent dynamic updates;
- 281,050 insertions;
- 261,144 deletions.

The event-level shadow experiment uses deterministic greedy initialization and is treated as a reproducible trajectory because maximal matching is noncanonical.

## Shadow characterization

The final CAIDA shadow trajectory contains 54,070 repair events and 74,407 discovery probes. The residual Spearman association between discovery and combined neighborhood change after degree control is 0.0287.

The workflows and result CSVs in this repository are the authoritative reproducibility artifacts for these reported values.
