# Week 7 — Contract and Swap, in the Frontier Settlement world

**Week 7 target (`assignments/odyssey_gates/week-07.md`, "Contract and
Swap (S03/S08)"):** pick a real dependency from your own world's Weeks
4-6 growth, turn it into an explicit contract with `abc.ABC` +
`@abstractmethod`, implement two conforming concrete collaborators, write
one focused test that swaps them and proves the contract holds for
either, and explain the caller boundary in plain language. `typing.
Protocol` is an optional comparison only, never the graded mechanism.

This is **one of four worked examples, not a template to copy-paste.**
It uses the course's own Frontier Settlement world (Docket Creek --
`sidecar/worlds/frontier_settlement.md`), one of the four established
Reasoning Odyssey worlds, and a made-up dependency inside it. Your own
submission should use your own real Weeks 4-6 dependency, in whichever
world you're actually running (this one or your own), not this one.

## The real dependency

Docket Creek's own world bible names this exact problem under "Contracts
/interfaces": *"two neighboring claims merging their separate,
incompatible ledger formats into one."* By Week 7, the town has more than
one office that can receive a new well-claim -- the Well Board keeps its
own ledger, and the Trade Post logs claims through its barter-credit
system. Nothing today makes explicit that **both offices need to answer
the same promise**: file the claim, confirm who filed it and how much.

## Run it

```bash
python -m unittest -v
```

All 5 tests pass.

## The contract

```python
class ClaimIntake(ABC):
    @abstractmethod
    def file_claim(self, claimant: str, gallons_per_day: int) -> str:
        ...
```

The promise: whatever files the claim must return a confirmation that
names the claimant and the amount. Not "how the office keeps its own
books" -- just that.

## Two conforming, genuinely different collaborators

`WellBoardIntake` returns a Well Board-style record line; `TradePostIntake`
returns a Trade Post ledger entry in a completely different format (barter
economy, not water-rights language). Both satisfy the same promise.

## The caller boundary

```python
def register_claim(intake: ClaimIntake, claimant: str, gallons_per_day: int) -> str:
    return intake.file_claim(claimant, gallons_per_day)
```

`register_claim` never asks which office it's talking to. It only knows
it has something that can `file_claim`. That's the boundary: past this
line, the caller trusts the contract, not the office.

## The focused swap test

```python
def test_register_claim_holds_the_contract_for_either_office(self):
    claimant = "Merrow"
    gallons_per_day = 40
    intakes = [WellBoardIntake(), TradePostIntake()]

    for intake in intakes:
        with self.subTest(intake=type(intake).__name__):
            result = register_claim(intake, claimant, gallons_per_day)
            self.assertIn(claimant, result)
            self.assertIn(str(gallons_per_day), result)
```

One caller, two offices with genuinely different record formats, one
assertion that checks only what the contract promises (claimant + amount
appear) -- never which office's wording won.

## Two more tests

- `test_register_claim_accepts_an_office_it_has_never_seen` hands the
  caller a brand-new `RoadDispatchIntake` it never saw coming -- proves
  the substitution is earned, not assumed (no hidden `isinstance` check
  on `WellBoardIntake`/`TradePostIntake`).
- `test_the_contract_is_enforced_not_just_documented` tries to open an
  `UnstaffedOffice(ClaimIntake)` that never implements `file_claim` and
  checks Python refuses (`TypeError`) -- the concrete reason this gate
  treats `typing.Protocol` as optional comparison, not the graded
  mechanism: a Protocol version would not catch this until the office
  was actually asked to file a claim, possibly mid-dispute.

## World Bible entry

> **Week 7.** Docket Creek had two places a new well-claim could land --
> the Well Board and the Trade Post -- and no shared promise between
> them. Made the dependency explicit as a `ClaimIntake` contract (`abc.
> ABC` + `@abstractmethod file_claim`), with `WellBoardIntake` and
> `TradePostIntake` as two genuinely different conforming offices, and
> `register_claim` as the caller that only trusts the contract. Evidence:
> the swap test and the guard test (a brand-new `RoadDispatchIntake`
> office), both pass, plus a test showing the ABC blocks an unstaffed
> office at construction time. Remaining debt: no reconciliation path
> exists yet for the same claimant filing at both offices for the same
> water source -- that's a real Docket Creek problem (see the world
> bible's "seeds" section on Old Tobin's paper ledger disagreeing with
> the digital one) but out of scope for this gate.

## What this is not

Not a second graded assignment. Not a hierarchy, recursion, queue, GUI,
or algorithm. One contract, two collaborators, one caller, one swap
test -- as small as real student work should be. Pick your **own** real
Weeks 4-6 dependency for your actual submission.
