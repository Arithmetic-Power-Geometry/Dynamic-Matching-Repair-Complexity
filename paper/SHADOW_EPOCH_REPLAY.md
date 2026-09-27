# Shadow Epoch Replay

`src/shadow_epoch.py` adds exact event-level instrumentation without changing Scan repair decisions.

For every repaired vertex it records:
- `D`: actual Scan neighbor probes;
- `d`: current degree;
- `r_changed_common`: neighbors present at both consecutive repairs whose free/nonfree status changed;
- adjacency additions/removals between repair snapshots;
- `changed_plus_churn`: a conservative observable change count;
- `D/d`: scan intensity.

### Why shadow?
An Eager/HeavyLight algorithm can choose a different matching, so directly comparing its P to Scan's D mixes **strategy cost** with **different state trajectories**. Shadow instrumentation holds the Scan trajectory fixed and measures information changes on that same trajectory.

### Interpretation boundary
`r_changed_common` is an empirical repair-epoch change count, not automatically the theorem's adversarial `r`. Edge churn changes the candidate universe itself, so results must report both status changes and adjacency churn.

### Required replay
Run the already-used Simple Wiki and CAIDA raw update streams through `ShadowEpochMatcher` using exactly the same projection/preprocessing as the published DMRC benchmark. Export event CSVs, then run `artifacts/analyze_discovery_profile.py`.

Do not compare theorem slack until these event CSVs exist.
