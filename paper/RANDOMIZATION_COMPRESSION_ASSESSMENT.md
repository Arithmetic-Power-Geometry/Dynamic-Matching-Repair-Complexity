# Randomization and Compression Assessment for the One-Shot Repair Epoch

## 1. Deterministic exact
For the one-shot epoch family with r independently realizable candidate statuses, if P candidate statuses are encoded/communicated into query-visible state and the repair procedure obtains no information about the remaining r-P statuses except by inspecting them, then worst-case discovery D >= r-P.

## 2. Randomized zero-error (Las Vegas)
Fix the random coins. Conditioned on any coin outcome, a zero-error algorithm must be correct on every admissible epoch outcome. The deterministic indistinguishability argument therefore applies to that fixed execution. Hence the same worst-case statement survives:
    P + D >= r
for every coin fixing under the same explicit-information model.
Randomization may change expected probe order, but cannot permit an exact NONE certificate while leaving an unresolved candidate completely unaccounted for.

## 3. Bounded-error (Monte Carlo)
The linear P+D>=r statement does NOT automatically survive. A compressed randomized summary can encode information about many candidate statuses jointly, and a bounded-error query may distinguish aggregate cases without learning every bit individually. Any lower bound here must count bits/cell probes and use communication/information complexity (e.g. set disjointness), not the per-candidate explicit-accounting proof.

Therefore do not claim P+D>=r for arbitrary randomized compressed summaries.

## 4. Compression
The phrase "P candidate statuses propagated" is representation-dependent. One memory word can encode multiple status bits. Consequently P+D>=r is meaningful only when P counts resolved candidate information in the explicit-summary model, not arbitrary RAM/cell-probe writes.

A standard-model theorem must replace P by an information or cell-probe quantity. Candidate routes:
- communication complexity across the update/query epoch boundary;
- cell-probe chronogram/information-transfer arguments;
- reduction from lopsided set disjointness or a dynamic multiphase problem.

## 5. Why direct transfer is nontrivial
Generic dynamic set-intersection witness has known randomized upper bounds and conditional/communication-based lower-bound machinery. MCNW adds matching-induced state-query coupling and a noncanonical maximal matching. A paper-level lower bound must show that these constraints preserve hardness rather than merely restate set intersection.

## 6. Safe theorem status
PROVED: deterministic exact + zero-error randomized, restricted explicit-information epoch model.
NOT PROVED: arbitrary compressed RAM summaries; bounded-error randomized algorithms; general cell-probe lower bound; general fully dynamic maximal matching lower bound.

## Next best step
Formulate the one-shot epoch as a two-party communication game:
- Alice receives hidden subset S and processes candidate-edge deletions;
- memory/message crossing the epoch boundary is the propagated information;
- Bob receives the trigger and must output a witness or EMPTY using limited probes/communication.
Then identify whether the game is exactly INDEX, DISJOINTNESS, or a weaker promise problem. This will determine whether a standard information lower bound is available without inventing a new conjecture.
