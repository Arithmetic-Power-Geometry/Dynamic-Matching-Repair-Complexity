# Repair Complexity in Fully Dynamic Maximal Matching

**Discovery–Propagation Tradeoffs, Conditional Hardness, and Reproducible Real-Data Evidence**

This repository contains the software, experiment drivers, reconstruction scripts, workflows, and machine-readable result artifacts accompanying the study by Mohammad Amir Khusru Akhtar (2026).

## Research question

When a matched edge disappears in a fully dynamic graph, what information must already have been maintained, and what must be discovered during repair before maximality can be restored?

The study separates **propagation** (information maintained before repair) from **discovery** (neighbor-state probes performed during repair).

## Main results

- **Exact explicit-summary tradeoff:** in the stated restricted model, if (r) neighbor states may have changed, (P) are communicated into exact query-visible state, and (D) are resolved by discovery, then **P + D ≥ r**.
- **One-shot conditional hardness:** a Triggered Maximal-Matching Repair (TMMR) construction encodes Multiphase set disjointness, yielding a conditional polynomial barrier for the stated one-shot output-stable model. This is not claimed as a lower bound for unrestricted fully dynamic maximal matching.
- **Exact future-burden identity:** **Q = k[AG + Cov(a,g)]**, separating recurrence, scan intensity, degree evolution, and their interaction.
- **Empirical boundary:** on the frozen AS-CAIDA shadow trajectory, raw neighborhood-change associations largely disappear after controlling for degree; the residual combined-change association is **0.0287**.
- **Reproducibility:** the optimized dirty-shadow tracker was differentially checked against the direct snapshot implementation on **195,000 updates**.

## Real-trace totals

| Dataset | Scan | Eager | Heavy/light |
|---|---:|---:|---:|
| Simple Wiki | 204,572 | 1,312,908 | 518,440 |
| NL Wiki 1M | 66,194 | 922,549 | 383,848 |
| AS-CAIDA | 72,544 | 591,973 | 248,748 |

These are charged-work totals. No single maintenance policy is claimed to dominate universally.

## Repository map

- `src/` — matching implementations and instrumentation
- `experiments/` — benchmark, application, audit, and differential-test drivers
- `artifacts/` — reconstruction and analysis scripts
- `results/` — frozen machine-readable outputs
- `datasets/` — dataset conversion/download helpers
- `.github/workflows/` — reproducibility and validation workflows

## Reproduce

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the general suite:

```bash
bash run_all.sh
```

The dedicated GitHub Actions workflows cover benchmark execution, real-data validation, CAIDA reconstruction/shadow replay, reusable-trigger auditing, and dirty-shadow differential validation.

## Scope

The theorem **P + D ≥ r** applies only to the exact explicit-summary model. The Multiphase reduction applies to a one-shot inherited/output-stable repair model. The future-burden decomposition is an exact accounting identity, not a new complexity lower bound. Empirical results are tied to frozen deterministic trajectories and the reported datasets.

## Citation

Akhtar, M. A. K. (2026). *Repair Complexity in Fully Dynamic Maximal Matching: Discovery–Propagation Tradeoffs, Conditional Hardness, and Reproducible Real-Data Evidence* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.22997728

Machine-readable citation metadata are provided in `CITATION.cff`.
