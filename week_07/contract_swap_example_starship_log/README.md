# Week 7 — Contract and Swap, in the Starship Log world

**Note: pre-stateful-update illustration.** The Week 7 gate now requires
two genuinely *stateful* conforming collaborators (see
`assignments/odyssey_gates/week-07.md` and `week_07/week_07_contract_and_swap/`
for the current, stateful reference example built by Jeremy). The
collaborators below (`LegacySensorArray`, `NextGenSensorArray`) are
stateless -- written before that update. Still a valid illustration of
the contract/caller-boundary/swap-test shape, just superseded, not
broken; use `week_07/week_07_contract_and_swap/` as the primary
reference.

**Week 7 target (`assignments/odyssey_gates/week-07.md`, "Contract and
Swap (S03/S08)"):** pick a real dependency from your own world's Weeks
4-6 growth, turn it into an explicit contract with `abc.ABC` +
`@abstractmethod`, implement two conforming concrete collaborators, write
one focused test that swaps them and proves the contract holds for
either, and explain the caller boundary in plain language. `typing.
Protocol` is an optional comparison only, never the graded mechanism.

This is **one of four worked examples, not a template to copy-paste.**
It uses the course's own Starship Log world (the RSV Kestrel), one of
the four established Reasoning Odyssey worlds, and a made-up dependency
inside it. Your own submission should use your own real Weeks 4-6
dependency, in whichever world you're actually running (this one or your
own), not this one.

## The real dependency

By Week 7, the ship's log needs status readings from more than one
generation of sensor hardware -- an older legacy array that writes flat
log lines, and a newer array that reports structured readings. Nothing
today makes explicit that **both generations need to answer the same
promise**: report the subsystem's status, and say which subsystem it's
talking about.

## Run it

```bash
python -m unittest -v
```

All 5 tests pass.

## The contract

```python
class SubsystemReporter(ABC):
    @abstractmethod
    def report_status(self, subsystem_name: str) -> str:
        ...
```

The promise: whatever reports the status must return a message naming
the subsystem. Not the reading's own format -- just that.

## Two conforming, genuinely different collaborators

`LegacySensorArray` returns a flat `LOG :: name :: NOMINAL` line;
`NextGenSensorArray` returns a structured, dict-shaped reading. Both
satisfy the same promise, despite being built to genuinely different
interface standards.

## The caller boundary

```python
def log_subsystem_status(reporter: SubsystemReporter, subsystem_name: str) -> str:
    return reporter.report_status(subsystem_name)
```

`log_subsystem_status` never asks which generation of hardware produced
the reading. It only knows it has something that can `report_status`.
Past that line, the ship's log trusts the contract, not the hardware
era -- which matters here specifically because the Kestrel is too far
out for anyone to double-check a reading by hand.

## The focused swap test

```python
def test_log_subsystem_status_holds_the_contract_for_either_generation(self):
    subsystem_name = "life support"
    reporters = [LegacySensorArray(), NextGenSensorArray()]

    for reporter in reporters:
        with self.subTest(reporter=type(reporter).__name__):
            result = log_subsystem_status(reporter, subsystem_name)
            self.assertIn(subsystem_name, result)
```

One caller, two subsystems built to genuinely different interface
standards, one assertion that checks only what the contract promises
(the subsystem is named) -- never which generation's format won.

## Two more tests

- `test_log_subsystem_status_accepts_a_reporter_it_has_never_seen` hands
  the caller a brand-new `ExperimentalSensorPod` it never saw coming --
  proves the substitution is earned, not assumed.
- `test_the_contract_is_enforced_not_just_documented` tries to install an
  `UncalibratedArray(SubsystemReporter)` that never implements
  `report_status` and checks Python refuses (`TypeError`) -- exactly the
  failure mode the ship's log exists to prevent, and the concrete reason
  this gate treats `typing.Protocol` as optional comparison: a Protocol
  version wouldn't catch an uncalibrated array until the ship actually
  asked it for a reading, six weeks from the nearest relay.

## World Bible entry

> **Week 7.** The Kestrel's ship's log needed status from two sensor
> generations with different interface standards, and nothing made
> explicit that both owed the log the same promise. Made the dependency
> explicit as a `SubsystemReporter` contract (`abc.ABC` +
> `@abstractmethod report_status`), with `LegacySensorArray` and
> `NextGenSensorArray` as two genuinely different conforming generations,
> and `log_subsystem_status` as the caller that only trusts the contract.
> Evidence: the swap test and the guard test (a brand-new
> `ExperimentalSensorPod`), both pass, plus a test showing the ABC blocks
> an uncalibrated array at construction time. Remaining debt: no
> escalation path exists yet for when two subsystems' readings disagree
> about the same physical quantity -- a real problem for the mission,
> out of scope for this gate.

## What this is not

Not a second graded assignment. Not a hierarchy, recursion, queue, GUI,
or algorithm. One contract, two collaborators, one caller, one swap
test -- as small as real student work should be. Pick your **own** real
Weeks 4-6 dependency for your actual submission.
