# Future Repair Burden Decomposition

Fix a vertex v immediately after a repair at time t. Let future repairs of v occur at t_1,...,t_k. Write:
- d_0 = degree of v at activation time t;
- d_i = degree immediately before future repair i;
- s_i = adjacency probes used by Scan at future repair i;
- a_i = s_i/d_i when d_i>0, and 0 otherwise (scan intensity);
- g_i = d_i/d_0 when d_0>0 (degree drift factor).

Define the optimistic future repair burden relative to one current index-build scan:
Q(v,t) = (sum_i s_i)/d_0.

For d_0>0, the following is an exact identity:
Q(v,t) = sum_i a_i g_i
       = k * mean_i(a_i g_i).

Equivalently, if A = mean_i a_i, G = mean_i g_i, and Cov_k(a,g) denotes the population covariance across the k future repairs,
Q = k [ A G + Cov_k(a,g) ].

Thus optimistic break-even Q>1 cannot be inferred from recurrence k alone. It depends exactly on:
1. future repair persistence k;
2. normalized scan intensity a_i;
3. degree drift g_i;
4. their within-vertex interaction/covariance.

Special stable-degree case: if d_i=d_0 for every future repair, then g_i=1 and
Q = sum_i a_i = k A.
Hence break-even is exactly k A > 1.

Bounds: because 0 <= s_i <= d_i for ordinary adjacency scan,
0 <= a_i <= 1,
so
Q <= sum_i g_i <= k * max_i g_i.
If degree never increases after activation, Q <= k. Therefore Q>1 requires at least two future repairs unless a later degree exceeds the activation degree enough to make the normalized burden exceed one.

This is an accounting identity/bound, not yet a novel theorem claim. Prior-art novelty must be checked before manuscript use.
