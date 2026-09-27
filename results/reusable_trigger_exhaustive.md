# Reusable Trigger — Exhaustive Small-Instance Results

Date: 2026-09-27

## Test space
Exhaustive set systems for universe sizes r=1,2,3,4; query-family size up to 3; every active subset S.
Total configurations checked: **11,934**.

## Results

| Strategy | Correct / state-preserving cases | Rate | Meaning |
|---|---:|---:|---|
| Naive protected-edge re-add | 1,330 / 11,934 | 11.14% | Fails whenever successful queries consume encoded free candidates |
| Explicit unmatch + protected restore | 11,934 / 11,934 | 100% | Functionally reusable, but requires direct matching-state restoration / charged recourse |
| Fresh one-shot center | 11,934 / 11,934 | 100% for tested one-query-per-center schedule | Correct but space grows with query copies |

## Structural conclusion
A successful query may match center v_j to active candidate x_i. The active-set encoding represents i by x_i being free. Therefore the query itself consumes one encoded bit/witness. Merely re-adding v_j p_j does not free x_i again.

The only tested constant-local reset that restores the encoding explicitly undoes the query-created matching edge and reinstates v_j p_j. This is a matching-state operation, not merely an ordinary graph-edge update handled by an unrestricted dynamic maximal-matching algorithm.

Thus:

**PROVED COMPUTATIONALLY for exhaustive small instances:** naive edge-only reset is not a valid general reusable encoding.

**CONSTRUCTION:** explicit restore is functionally reusable with charged recourse/state control.

**NO-GO for current route:** these tests do not supply the edge-update-only reusable gadget needed to import reusable dynamic SetIntersection lower bounds into unrestricted dynamic maximal matching.

## Research decision
Do not spend more time tuning reset variants of this same center/candidate gadget. Keep the audited one-shot Multiphase theorem as the valid hardness result.

The next useful empirical task is to instrument the existing Simple Wiki and CAIDA traces for discovery-versus-propagation quantities tied to the proven repair model, rather than adding a new dataset.
