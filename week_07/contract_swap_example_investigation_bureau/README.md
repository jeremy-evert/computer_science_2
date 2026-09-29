# Week 7 — Contract and Swap, in the Investigation Bureau world

**Week 7 target (`assignments/odyssey_gates/week-07.md`, "Contract and
Swap (S03/S08)"):** pick a real dependency from your own world's Weeks
4-6 growth, turn it into an explicit contract with `abc.ABC` +
`@abstractmethod`, implement two conforming concrete collaborators, write
one focused test that swaps them and proves the contract holds for
either, and explain the caller boundary in plain language. `typing.
Protocol` is an optional comparison only, never the graded mechanism.

This is **one of four worked examples, not a template to copy-paste.**
It uses the course's own Investigation Bureau world (Meridian Case
Bureau), one of the four established Reasoning Odyssey worlds, and a
made-up dependency inside it. Your own submission should use your own
real Weeks 4-6 dependency, in whichever world you're actually running
(this one or your own), not this one.

## The real dependency

By Week 7, evidence can arrive two ways -- logged directly by Case
Records Division, or submitted from the field by an investigator, in a
rougher format that's "pending records review." Nothing today makes
explicit that **both intake paths need to answer the same promise**: log
the item, name it and describe it.

## Run it

```bash
python -m unittest -v
```

All 5 tests pass.

## The contract

```python
class EvidenceLogger(ABC):
    @abstractmethod
    def log_intake(self, item_id: str, description: str) -> str:
        ...
```

The promise: whatever logs the item must return a message naming the
item id and the description. Not the log's own formatting conventions --
just that.

## Two conforming, genuinely different collaborators

`RecordsDivisionLogger` writes a formal case-records line; `FieldUnitLogger`
writes a rougher, "pending review" field format. Both satisfy the same
promise, in a way that reflects the real institutional difference between
the two (see `investigation_bureau.md` section 3: "Field Reports ...
need to reconcile with what's already on file").

## The caller boundary

```python
def intake_evidence(logger: EvidenceLogger, item_id: str, description: str) -> str:
    return logger.log_intake(item_id, description)
```

`intake_evidence` never asks which division wrote the log. It only knows
it has something that can `log_intake`. Past that line, the caller trusts
the contract, not the format.

## The focused swap test

```python
def test_intake_evidence_holds_the_contract_for_either_logger(self):
    item_id = "EV-104"
    description = "sealed envelope, unopened"
    loggers = [RecordsDivisionLogger(), FieldUnitLogger()]

    for logger in loggers:
        with self.subTest(logger=type(logger).__name__):
            result = intake_evidence(logger, item_id, description)
            self.assertIn(item_id, result)
            self.assertIn(description, result)
```

One caller, two genuinely different record formats, one assertion that
checks only what the contract promises (item id + description appear) --
never which division's format won.

## Two more tests

- `test_intake_evidence_accepts_a_logger_it_has_never_seen` hands the
  caller a brand-new `NightShiftLogger` it never saw coming -- proves the
  substitution is earned, not assumed.
- `test_the_contract_is_enforced_not_just_documented` tries to construct
  an `UnverifiedDivision(EvidenceLogger)` that never implements
  `log_intake` and checks Python refuses (`TypeError`) -- exactly the
  kind of gap the Bureau's own premise ("disagreement between two records
  is itself the crime scene") can't afford, and the concrete reason this
  gate treats `typing.Protocol` as optional comparison: a Protocol
  version wouldn't catch an incomplete logger until the case actually
  needed it.

## World Bible entry

> **Week 7.** Evidence at Meridian could arrive through Case Records
> Division or straight from the field, and nothing made explicit that
> both paths owed the same promise to the case file. Made the dependency
> explicit as an `EvidenceLogger` contract (`abc.ABC` + `@abstractmethod
> log_intake`), with `RecordsDivisionLogger` and `FieldUnitLogger` as two
> genuinely different conforming intake paths, and `intake_evidence` as
> the caller that only trusts the contract. Evidence: the swap test and
> the guard test (a brand-new `NightShiftLogger`), both pass, plus a test
> showing the ABC blocks an unverified division at construction time.
> Remaining debt: no reconciliation logic exists yet for what happens
> when Records and a field report disagree about the same item -- a real
> problem for the Bureau, out of scope for this gate.

## What this is not

Not a second graded assignment. Not a hierarchy, recursion, queue, GUI,
or algorithm. One contract, two collaborators, one caller, one swap
test -- as small as real student work should be. Pick your **own** real
Weeks 4-6 dependency for your actual submission.
