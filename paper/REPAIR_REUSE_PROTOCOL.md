# Repair-Reuse Mining Protocol

## Question
Before constructing an index at vertex v, is there observable evidence that future repair scans at v will repay construction and maintenance?

## Trace fields
step, vertex, degree, scan_work, found, repair_number, inter_repair_gap.

## First diagnostic
For each repaired vertex, compute an optimistic oracle ratio:

R*(v,t) = future scan work after repair t / max(1, degree at t).

If even this optimistic ratio rarely exceeds 1, indexing has little opportunity before maintenance cost is considered. If it frequently exceeds 1 but the debt policy fails, the problem is prediction rather than opportunity.

## Required external analyses
1. fraction of repaired vertices repaired more than once;
2. fraction with R*>1;
3. concentration of avoidable scan work among those vertices;
4. distribution of inter-repair gaps;
5. same-degree comparison: do recurrence/history variables predict future work beyond degree?
6. only after these measurements, design a new online policy.

## Claim discipline
R* is an oracle diagnostic, not an implementable algorithm and not a performance result. It deliberately ignores maintenance cost, so it is an upper bound on index opportunity, not realized savings.
