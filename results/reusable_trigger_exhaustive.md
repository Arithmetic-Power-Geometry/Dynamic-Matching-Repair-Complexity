# Reusable-Trigger Exhaustive Audit

Exhaustive small-instance audit of reset strategies for the one-shot matching construction.

| Reset strategy | Correct/state-preserving | Rate |
|---|---:|---:|
| Naive protected-edge re-add | 1,330 / 11,934 | 11.14% |
| Explicit unmatch + protected restore | 11,934 / 11,934 | 100% |
| Fresh one-shot center | 11,934 / 11,934 | 100% |

A successful repair may match a center to an active candidate and thereby consume the free-state encoding. Re-adding the protected edge alone does not restore that encoding. Explicit restoration succeeds only by modifying matching state; fresh centers preserve one-shot semantics by using a new center.

This audit supports the paper's decision not to claim a reusable edge-update-only reduction.
