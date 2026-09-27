# Prior-art novelty gate — 2026-09-27

## NO-GO claims
Do **not** claim any of the following as new:
1. rent-versus-buy / accumulated-cost break-even logic — classical ski rental;
2. adaptive online index construction based on workload benefit — established database index-tuning literature;
3. heavy/light degree separation or special handling of high-degree vertices in dynamic matching — established;
4. lazy-versus-eager dynamic maximal-matching tradeoffs — Kashyop & Narayanaswamy (Information Processing Letters, 2020) already study these classes and conditional lower bounds;
5. sublinear/worst-case/amortized dynamic maximal matching itself — extensive literature including Baswana–Gupta–Sen, Bernstein et al. 2025, and Chuzhoy–Khanna–Song 2026.

## Candidate surviving contribution
The current evidence supports investigation of a narrower **repair-level workload characterization** for free-neighbor discovery in fully dynamic maximal matching.

For a repaired vertex v after time t:
Q(v,t)=FutureScan(v,t)/deg_t(v).

With future repairs i=1..k, scan intensity a_i=s_i/d_i and degree drift g_i=d_i/d_0:
Q = sum_i a_i g_i = k[A G + Cov(a,g)].
For stable degree, Q=kA.

External observations:
- recurrence is not equivalent to profitable auxiliary-state maintenance;
- Simple Wiki: 30.62% of repaired vertices repeat, but only 8.55% are oracle-indexable at some repair under the optimistic build-only diagnostic;
- CAIDA: 49.36% repeat, but only 4.52% are oracle-indexable;
- degree alone transfers surprisingly well for event-level optimistic indexability; repair history adds only modest cross-domain predictive gain;
- fixed Heavy/Light and debt-based adaptive indexing both lose to Scan on external streams.

## Current novelty status
**PROMISING BUT NOT YET PAPER-LEVEL PROVED NOVELTY.**
The exact Q decomposition is mathematically elementary accounting. Novelty, if any, must come from a nontrivial matching-specific theorem, lower bound, competitive characterization, or reproducible structural law that is not merely ski-rental or lazy/eager matching under new terminology.

## Next theorem target
Seek a matching-specific statement showing when any auxiliary free-neighbor summary can or cannot amortize its maintenance against direct scanning under endogenous free/matched-state changes. A useful theorem must explicitly include propagation cost caused by neighbors changing matched/free state; this coupling is what distinguishes the setting from classical fixed-rent ski rental.

Do not begin a full manuscript until this theorem target either succeeds or is replaced by a comparably strong structural result.
