# NL Wikipedia external validation

The uploaded KONECT Dynamic NL Wikipedia archive reports 1,039,252 vertices and 20,070,561 temporal records. Because a full in-memory directed-to-undirected projection exceeded the validation environment memory budget, the frozen protocol was applied to the first 1,000,000 raw records in chronological order.

Projection: 978,945 undirected updates = 583,381 insertions + 395,564 genuine deletions; 2,139 self-loops removed; zero duplicate additions and zero orphan removals.

Corrected implementations all passed final maximality/invariant validation.

Result: Scan again beats eager and heavy/light. This independently supports the conclusion that proactive heavy summaries are not universally advantageous on Wikipedia hyperlink dynamics. It does not substitute for a full 20M-record run; that requires streaming/disk-backed projection.

Next validation should change graph domain rather than add another Wikipedia network.
