# External Baselines and Context

The empirical study uses internal implementations of full recomputation, scan repair, eager exact summaries, and heavy/light maintenance. External dynamic-matching literature is used for context rather than to claim a direct implementation-level speed comparison.

The manuscript explicitly distinguishes its scoped results from unrestricted fully dynamic maximal-matching update-time results. In particular, the one-shot TMMR reduction is not presented as a reusable lower bound for unrestricted dynamic maximal matching.

Dataset sources used by the real-data workflows are SNAP AS-CAIDA and KONECT dynamic Wikipedia traces. Reconstruction scripts and frozen validation counts are included in this repository.
