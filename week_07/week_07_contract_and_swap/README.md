# Week 7: Contract and Swap
## Frontier Settlement -- CS2 Reasoning Odyssey Gate

---

## What this project demonstrates

| Concept | Where to look |
|---|---|
| Explicit ABC contract | `GrowthReporter` in `settlement.py` |
| Stateful collaborators (earned is-a) | `TrailScout`, `SignalTower` in `settlement.py` |
| Caller boundary with 3 responsibilities | `SettlementGrowthSystem.check_growth()` in `settlement.py` |
| Focused contract tests (no concrete wording) | `TestGrowthReporterContract` in `test_settlement.py` |
| Collaborator-specific tests | `TestTrailScoutBehavior`, `TestSignalTowerBehavior` |
| Boundary tests (input, return type, failures) | `TestCallerBoundary` in `test_settlement.py` |
| Working demonstration | `demo.py` |
| Full six-part World Bible | `WORLD_BIBLE.md` |

---

## Files

```
week_07_contract_and_swap/
|-- settlement.py        contract, collaborators, and caller
|-- test_settlement.py   35 tests across 4 test classes
|-- demo.py              working demonstration of all concepts
|-- WORLD_BIBLE.md       full six-part design record
`-- README.md            this file
```

---

## Run the tests

```
python -m unittest -v
```

Expected: 35 tests, 0 failures, 0 errors.

---

## Run the demonstration

```
python demo.py
```

---

## Design summary

### The contract

```python
class GrowthReporter(ABC):
    @abstractmethod
    def report_growth(self, location: str) -> str:
        raise NotImplementedError
```

### The two conforming collaborators

**TrailScout** carries a set of visited locations. A first visit produces a cautious
report. A return visit produces a confident revision. The scout is a real object with
memory, not a string factory.

**SignalTower** carries a message-count dictionary. Reports move through three stages
(unknown, early signs, confirmed) as message volume accumulates.

### The caller boundary

`SettlementGrowthSystem.check_growth(location)` has three responsibilities:

1. Validate input before sending it across the boundary.
2. Validate the return value before accepting it from the collaborator.
3. Isolate collaborator failures and re-raise with context.

### The swap

```python
scout_system  = SettlementGrowthSystem(TrailScout())
tower_system  = SettlementGrowthSystem(SignalTower())
```

`SettlementGrowthSystem` itself does not change. Only the injected collaborator changes.

---

## Rubric alignment

| Criterion | Points | Evidence |
|---|---|---|
| Working contract and swap | 15 | `GrowthReporter`, `TrailScout`, `SignalTower`, `SettlementGrowthSystem` in `settlement.py` |
| Focused contract test | 10 | `TestGrowthReporterContract` -- 6 tests, zero concrete wording assertions |
| Caller-boundary reasoning | 10 | 9 boundary tests in `TestCallerBoundary`; boundary documented in code and World Bible |
| Demonstration, reflection, World Bible | 5 | `demo.py` runs; `WORLD_BIBLE.md` has all six parts |
