# Odyssey Gate — Week 13: Find it, order it, count the cost

**Concept:** searching, sorting, and Big-O intuition (Deitel, §§11.6–11.14). **Arc:** 3 — Worlds That Think About Their State. **Instrument:** Quick Check (pass/fail) — see `docs/curriculum/judgment_toolkit.md` §1.

## The gate (do this first)

Use your world data to trace one search and one ordering operation. Explain the search's worst-case growth in plain language, including why binary search would require ordered data if you choose to compare it with linear search.

## Quick Check (pass/fail)

- [ ] A search finds (or correctly reports absent) a key in a real world-data collection, with a short trace of inspected items/indices.
- [ ] A sort orders that collection by one meaningful key and the before/after result is demonstrated.
- [ ] The student labels the traced linear search as **O(n)** worst case and explains one consequence as the collection grows; any binary-search claim notes its sorted-data precondition.

## Suggested textbook problem (optional scaffolding)

- **Frontier Settlement:** find a colonist/resource record and sort a roster by food need.
- **Investigation Bureau:** find a case ID and sort leads by priority.
- **Starship Log:** find an alert ID and sort events by timestamp/severity.
- **Small Business:** find a SKU and sort inventory by stock or sales.

## Then: open continuation (light Build, holistic)

Compare linear and binary search only on a sorted copy of the same data; do not claim timing alone proves Big O.

## World Bible

One line: what key you searched/sorted, what growth cost you noticed.

## Looking ahead

Week 14 integrates the recursive world operation and the visualization into Checkpoint 3.
