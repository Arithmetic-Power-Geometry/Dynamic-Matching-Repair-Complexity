# Shadow Replay Readiness

## Completed
- Generic projected-stream replay: `artifacts/replay_shadow_epoch.py`
- Exact same-trajectory shadow instrumentation: `src/shadow_epoch.py`
- Deterministic fixture: `experiments/fixtures/shadow_small.csv`
- Invariant test and GitHub Actions workflow
- First-observation correction: initial neighborhood is a baseline, not between-repair churn.

## Full real-data inputs
The repository currently contains aggregate Simple Wiki / CAIDA results but not the projected raw `op,u,v` streams used to produce them. Therefore full shadow statistics cannot be regenerated from GitHub alone.

## Required input contract
For either existing dataset, provide/export the same benchmark projection as:
```
op,u,v
add,<node>,<node>
remove,<node>,<node>
...
```
The replay preserves first-appearance node remapping and ignores self-loops.

## Commands
```bash
python artifacts/replay_shadow_epoch.py data/simplewiki_projected.csv --out results/simplewiki_shadow_events.csv
python artifacts/analyze_discovery_profile.py results/simplewiki_shadow_events.csv --dataset KONECT_Dynamic_Simple_Wiki --out results/simplewiki_discovery_profile.csv
```
and analogously for CAIDA.

## Gate
Do not report real-data `r_changed`, churn, or discovery-intensity distributions until these projected streams are available and replayed.
