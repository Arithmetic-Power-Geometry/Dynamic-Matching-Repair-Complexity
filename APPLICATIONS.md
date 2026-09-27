# Illustrative Application Domains

The paper studies repair complexity in fully dynamic maximal matching. The following domains are **illustrative matching interpretations**, not claims that every domain was empirically evaluated.

## Ride allocation

Passengers and drivers can be represented as two vertex classes, feasible assignments as edges, and active assignments as matching edges. When an assigned driver becomes unavailable, the passenger requires repair: the system can either maintain availability information continuously or discover a replacement when needed.

## Request–resource assignment

The repository includes an application-style request/resource workload. Requests and resources form the two sides of a matching instance, while changing compatibility edges trigger reassignment and repair.

## Other interpretations

Task–server assignment, communication-link pairing, recommendation/pairing, and changing resource allocation can exhibit the same abstract repair question when feasible pairings change over time.

These examples motivate the information-allocation perspective; they do not extend the paper's theorems beyond their stated models.
