# Validated experimental findings

## Repair-stress workload

A fixed sequence repeatedly deletes and reinserts edges from the same initial maximal matching, so every implementation sees the same update stream.

The principal observation is a **tail-work trade-off**, not a universal total-work speedup.

| n | Scan total work | Scan max/update | Heavy/light total work | Heavy/light max/update |
|---:|---:|---:|---:|---:|
|128|4,780|127|6,960|16|
|256|5,364|255|7,056|16|
|512|6,424|511|7,104|16|
|1,024|6,460|1,023|7,152|16|

In this hub family, scan has lower median work (4 versus 8) and often lower total work, but its worst observed repair grows linearly with n. Heavy/light caps the observed maximum at 16 over the tested sizes. This is empirical evidence only, not an asymptotic theorem.

## Resource-allocation application

The application graph has 500 requests, 500 resources, 25 compatibility edges per request, and 1,500 fixed compatibility updates.

| Algorithm | Total instrumented work | p95 work/update | max work/update | recourse | maximal |
|---|---:|---:|---:|---:|---|
|Recompute|37,498,500|25,000|25,000|38,530|yes|
|Scan|31,275|53|63|1,389|yes|
|Eager|69,522|99|163|1,396|yes|
|Heavy/light|33,847|55|59|1,389|yes|

Heavy/light is close to scan in total work and slightly improves the maximum observed repair work in this application stream. The result supports a latency-tail interpretation rather than a claim of universal throughput superiority.

## Measurement caveat

Wall-clock values include Python overhead and correctness checking and should not be interpreted as systems-level latency. The primary reproducible metric is instrumented work = adjacency probes + maintained-summary propagation operations.
