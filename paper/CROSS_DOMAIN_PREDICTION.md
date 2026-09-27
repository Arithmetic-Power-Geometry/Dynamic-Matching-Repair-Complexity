# Cross-domain indexability prediction

The label is optimistic future indexability at a repair event: future scan work at the same vertex exceeds current degree (one-time build proxy). Features are leakage-safe and available by the current repair.

| Train -> Test | Model | ROC-AUC | AP |
|---|---|---:|---:|
| Simple Wiki -> CAIDA | degree only | 0.8509 | 0.1287 |
|  | repair count only | 0.6861 | 0.0559 |
|  | full history | 0.8569 | 0.1431 |
| CAIDA -> Simple Wiki | degree only | 0.8221 | 0.2402 |
|  | repair count only | 0.7038 | 0.1194 |
|  | full history | 0.8324 | 0.2581 |

Positive prevalence is 2.92% in CAIDA repair events and 5.77% in Simple Wiki repair events.

## Decision
There is transferable ranking signal, but degree alone captures most of it. Full repair history adds only +0.0060 AUC (Wiki->CAIDA) and +0.0103 AUC (CAIDA->Wiki). This is not sufficient evidence for a novel history-based adaptive algorithm.

## Next theorem/mining question
The oracle condition is FutureScan(v,t) > degree(v,t). Since a single scan is upper bounded by degree, crossing break-even necessarily requires enough future repair opportunity and/or repeated near-full scans. Study normalized future burden:
Q(v,t)=FutureScan(v,t)/degree(v,t)
and decompose it into future repair count times mean scan fraction of degree. Seek a deterministic identity/bound and then test which factor transfers beyond degree.

Do not write the full manuscript yet. Start it only if this decomposition yields a nontrivial structural law or a degree-controlled predictor with substantial out-of-domain gain.
