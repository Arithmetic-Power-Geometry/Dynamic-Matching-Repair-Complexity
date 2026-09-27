# Frozen Real-Data Reconstruction Gates

## AS-CAIDA
Authoritative source: SNAP AS-CAIDA collection, 122 snapshots from January 2004 to November 2007.

The reconstruction is accepted only if all frozen benchmark counts reproduce exactly:

| quantity | frozen value |
|---|---:|
| snapshots | 122 |
| initial edges | 32,955 |
| derived updates after initial snapshot | 542,194 |
| derived insertions | 281,050 |
| derived deletions | 261,144 |

The projected replay CSV includes initial-edge additions followed by symmetric-difference updates. Shadow analysis must distinguish initialization from the 542,194 dynamic updates when comparing to the frozen benchmark.

If any count differs: **GATE FAIL — no scientific comparison permitted.**

## Dynamic Simple Wiki
Frozen projection counts:
- valid projected updates: 1,514,719
- insertions: 1,106,716
- genuine deletions: 408,003
- self-loops excluded: 3,664
- duplicate additions: 0
- orphan removals: 0
- nodes: 100,312

Do not add a downloader until the original KONECT artifact URL/format is independently verified. A candidate reconstruction must reproduce these counts exactly before use.
