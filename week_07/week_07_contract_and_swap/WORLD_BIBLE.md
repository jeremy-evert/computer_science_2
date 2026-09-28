# World Bible: Frontier Settlement
## Version 0.7 -- Contract and Swap

---

## 1. World Premise

The Frontier Settlement is a growing community on the edge of mapped territory.
Every week, the settlement needs to know whether it is actually growing -- not just
feel like it is growing. Two different kinds of observers answer that question using
different evidence: scouts who travel the trails, and towers who relay telegraph
messages. The settlement growth-tracking system depends on *any* observer that
can deliver a report, not on one specific kind.

---

## 2. The Cast

| Name | Role |
|---|---|
| `TrailScout` | Travels the territory; reports growth based on wagon and foot traffic observed firsthand |
| `SignalTower` | Relays telegraph messages; reports growth based on communication volume |
| `SettlementGrowthSystem` | Asks a reporter for growth evidence; uses the report to inform the settlement |
| `GrowthReporter` | The explicit contract that any growth reporter must satisfy |
| `ContractViolationError` | Raised when a collaborator breaks its contract promise |

---

## 3. One Real Flow

1. The settlement marshal asks the `SettlementGrowthSystem` whether Dry Creek is growing.
2. `check_growth("Dry Creek")` validates the location at the caller boundary.
3. The system passes the location to whichever `GrowthReporter` it holds.
4. The reporter (scout or tower) uses its own state and evidence to produce a report.
5. The system validates the report before returning it.
6. The marshal receives a readable, non-empty growth assessment.

---

## 4. Three Software Questions

1. Is a given location growing, based on the evidence this reporter has gathered?
2. Can the system work with a new kind of reporter without changing its own code?
3. What happens at the boundary when a reporter breaks its promise?

---

## 5. Known Unknowns

- **Location registry**: Should the system maintain a list of valid locations, or is any
  non-empty string acceptable? Right now any non-empty string passes. A later version
  might validate against a known list of settlements.
- **Structured reports**: `report_growth()` currently returns a plain string. A later
  version might return a structured object (`GrowthReport`) with fields for confidence
  level, evidence type, and timestamp.
- **Concurrency**: `TrailScout` and `SignalTower` both hold mutable state. If two threads
  ask for a report simultaneously, the state is not protected.

---

## 6. Object Prediction (updated each week)

| Candidate | Status |
|---|---|
| `TrailScout` | Confirmed -- carries visited-location state; behavior changes over time |
| `SignalTower` | Confirmed -- carries message-count state; behavior changes over time |
| `SettlementGrowthSystem` | Confirmed -- owns the caller boundary; delegates to a reporter |
| `GrowthReporter` | Confirmed -- explicit ABC contract, not a concrete object |
| `ContractViolationError` | Added this week -- named exception for broken contracts |

---

## 7. What Changed This Week (v0.6 to v0.7)

### The dependency became explicit

Week 5 introduced two collaborating objects that worked together to track settlement
growth. The dependency between the caller and its collaborators was implicit: both
happened to have a `report()` method, but nothing enforced that promise. This week
that implicit assumption became the explicit `GrowthReporter` ABC.

### The collaborators became real objects

The previous collaborators were stateless -- they returned the same string regardless
of what had happened before.

- `TrailScout` now carries a `_visited` set. A first visit produces a cautious report;
  a return visit produces a confident revision.
- `SignalTower` now carries `_message_counts`. Reports move through three stages
  (unknown, early signs, confirmed) as message volume accumulates.

Both collaborators now have state that justifies the class and earns the is-a
relationship.

### The caller boundary became real

`SettlementGrowthSystem.check_growth()` now has three explicit responsibilities:

1. **Input validation** -- location is checked before crossing the boundary.
2. **Return-type enforcement** -- the report is checked after crossing the boundary.
   A collaborator that returns `None` or an integer triggers `ContractViolationError`.
3. **Failure isolation** -- unexpected collaborator exceptions are caught and re-raised
   as `RuntimeError` with context.

### The tests became behavioral, not brittle

The old contract tests asserted exact strings. The new contract tests assert
properties: is the result a non-empty string? Does it mention the location? Does it
differ between collaborators? Collaborator-specific tests are in their own test class.

---

## 8. Evidence Used

35 tests across 4 test classes:

| Class | What it tests |
|---|---|
| `TestGrowthReporterContract` | Contract-level properties only; no concrete wording |
| `TestTrailScoutBehavior` | Scout state, first/return visit logic, input validation |
| `TestSignalTowerBehavior` | Tower state, volume thresholds, input validation |
| `TestCallerBoundary` | Input validation, return-type enforcement, failure handling |

Run: `python -m unittest -v`

Demonstration: `python demo.py`

---

## 9. Remaining Debt

| Item | Priority | Notes |
|---|---|---|
| `report_growth()` returns a plain string | Medium | A `GrowthReport` object would carry confidence level, evidence type, timestamp |
| Location validation is just "non-empty string" | Low | A future version could validate against a registry of known settlement locations |
| No thread-safety on mutable collaborator state | Low | Flag for when the system runs concurrently |
| `isinstance` guard blocks structural subtyping | Low | A `typing.Protocol` version would allow duck-typed conformance without inheritance |
