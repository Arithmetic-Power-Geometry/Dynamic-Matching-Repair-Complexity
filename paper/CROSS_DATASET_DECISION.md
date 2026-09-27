# Cross-dataset real validation

| Dataset | Scope | Scan total | HL total | Eager total | Scan p99 | HL p99 | Scan max | HL max |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Simple Wiki | full 1,514,719 updates | 204,572 | 518,440 | 1,312,908 | 4 | 6 | 292 | 317 |
| NL Wiki | first 1,000,000 raw records | 66,194 | 383,848 | 922,549 | 1 | 1 | 236 | 512 |
| AS-CAIDA | full 122-snapshot delta stream | 72,544 | 248,748 | 591,973 | 4 | 8 | 42 | 206 |

All reported implementations passed final maximality/invariant validation.

## Decision
Fixed-threshold heavy/light repair indexing is **NO-GO as a universal improvement**. It helped the deliberately hub-stressed synthetic family but lost to direct scan on three external validations spanning Wikipedia hyperlink dynamics and Internet AS topology.

The scientifically stronger next question is selective activation: can observable local state predict when paying index-maintenance cost will reduce future repair cost? Any adaptive policy must be evaluated against scan with the policy/feature overhead fully charged. No performance claim should be made until this policy beats scan out-of-sample on external streams.
