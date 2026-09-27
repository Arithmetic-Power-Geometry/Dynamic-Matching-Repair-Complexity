# Research Gate After Multiphase Reduction

## Established
1. Exact workload identity:
   Q(v,t)=k[A G + Cov(a,g)].
2. External empirical result:
   repair recurrence is not equivalent to profitable indexing.
3. Negative algorithmic results:
   fixed Heavy/Light and debt-triggered indexing lose to Scan on multiple external streams.
4. Restricted explicit-information theorem:
   P+D>=r.
5. Graph-realizable one-shot repair gadget.
6. Reduction:
   Multiphase Set Disjointness -> Triggered Maximal-Matching Repair (TMMR), for an inherited/output-stable repair model.

## Prior-art boundary
- Multiphase set disjointness is established (Pătraşcu STOC 2010).
- Dynamic set intersection has known expected upper bounds and conditional 3SUM lower bounds (Kopelowitz–Pettie–Porat).
- Communication/set-disjointness lower bounds exist for matching in streaming/distributed models.
- No novelty should be claimed for the hardness source or generic set-intersection tradeoff.
- Candidate novelty is the reduction/connection to local maximal-matching repair plus the empirical characterization of when repair indexing actually pays.

## Central limitation
The reduction does not cover unrestricted fully dynamic maximal matching because such an algorithm may proactively alter the matching during Phase II. TMMR assumes inherited/output-stable behavior: while the current matching remains maximal, it is preserved.

## Paper-level decision
Do NOT market this as a lower bound for fully dynamic maximal matching.
A defensible paper could instead explicitly study:
"output-stable dynamic maximal-matching repair" or
"triggered maximal-matching repair,"
provided that:
A. the model is motivated by practical/local repair algorithms and recourse/stability requirements;
B. the multiphase reduction yields a formally stated conditional lower bound/tradeoff by importing exact source assumptions;
C. real traces demonstrate that the model captures observed repair work;
D. comparisons include unrestricted dynamic matching literature and explain the model gap.

## Q1 gate
Current status: BORDERLINE / NOT YET Q1-READY.
The next decisive step is to instantiate an exact theorem from a published multiphase/dynamic-set-intersection hardness result with parameters mapped to TMMR. If the transferred theorem is nontrivial and clean, begin manuscript. If it becomes weak/artificial after parameter mapping, stop this lower-bound route rather than inflate it.
