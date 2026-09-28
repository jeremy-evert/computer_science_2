# Week 7 — Contract and Swap, built on the Week 6 kitchen world

**Week 7 target (`assignments/odyssey_gates/week-07.md`, "Contract and
Swap (S03/S08)"):** pick a real dependency from your own world's Weeks
4-6 growth, turn it into an explicit contract with `abc.ABC` +
`@abstractmethod`, implement two conforming concrete collaborators, write
one focused test that swaps them and proves the contract holds for
either, and explain the caller boundary in plain language. `typing.
Protocol` is an optional comparison only, never the graded mechanism.

This example is **one way to meet that bar, not a template to
copy-paste.** It picks a made-up world (the same kitchen from `week_06/
unit_testing_example/`) and a made-up dependency. Your own submission
should use your own real Weeks 4-6 dependency, not this one.

## Looking back across the kitchen's own Weeks 4-6

Week 6's example built `Oven` and `Grill` — two appliances that share one
operation, `cook(food)`, with meaningfully different behavior (earned
substitution, no shared base class needed). That world now has a growing
system: appliances that cook. What does it actually depend on right now
that hasn't been made explicit yet?

**Answer: it depends on some way to tell someone the order is ready.**
Today that's implicit — nothing in the kitchen world says *how* "ready"
gets announced. That's the real dependency this example turns into a
contract.

## Run it

From this directory:

```bash
python -m unittest -v
```

All 5 tests pass.

## The contract

```python
class OrderNotifier(ABC):
    @abstractmethod
    def notify(self, order_name: str) -> str:
        ...
```

The promise: **whatever answers `notify(order_name)` must return a
message that actually names the order.** That's the whole contract — not
"rings a bell," not "prints a ticket." The caller doesn't get to assume
either of those; it only gets to assume the order gets named.

## Two conforming, genuinely different collaborators

```python
class KitchenBell(OrderNotifier):
    def notify(self, order_name):
        return f"Ring! Order ready: {order_name}"

class TicketPrinter(OrderNotifier):
    def notify(self, order_name):
        return f"Printed ticket: {order_name} READY"
```

`KitchenBell` and `TicketPrinter` do nothing alike internally — one
"rings," one "prints" — but both satisfy the same promise. That's the
point: the contract is about the promise, not the mechanism.

## The caller boundary

```python
def announce_order_ready(notifier: OrderNotifier, order_name: str) -> str:
    return notifier.notify(order_name)
```

`announce_order_ready` never asks which kind of notifier it got. It only
knows it has *something* that can `notify`. That's the caller boundary:
the line past which the caller stops caring about the concrete type and
starts trusting the contract instead.

## The focused swap test — the actual graded evidence

```python
def test_announce_order_ready_holds_the_contract_for_either_collaborator(self):
    order_name = "table 4 burger"
    notifiers = [KitchenBell(), TicketPrinter()]

    for notifier in notifiers:
        with self.subTest(notifier=type(notifier).__name__):
            result = announce_order_ready(notifier, order_name)
            self.assertIn(order_name, result)
```

One caller, two different concrete collaborators, one loop, one
assertion that only checks what the contract actually promises (the
order name shows up) — not what any one implementation happens to say
("Ring!" vs. "Printed"). That is what "proves the contract holds for
either" means in practice: the test would fail if either collaborator
forgot to name the order, and it does not care how they announce it.

## Two more tests, because the shared operation alone doesn't earn the
## claim (same spirit as Week 6's guard test)

- `test_announce_order_ready_accepts_a_notifier_it_has_never_seen` hands
  `announce_order_ready` a brand-new `Pager` class, written after the
  function, that `announce_order_ready` never saw coming. If the caller
  had secretly special-cased `KitchenBell`/`TicketPrinter` (an
  `isinstance` check, say), this is the test that would catch it. It
  doesn't, so the substitution claim is earned, not assumed.
- `test_the_contract_is_enforced_not_just_documented` tries to build a
  `SilentSpeaker(OrderNotifier)` that never implements `notify` and
  checks that Python itself refuses (`TypeError`). This is the specific
  thing `abc.ABC` buys over a plain duck-typed class or `typing.
  Protocol`: the contract isn't just a comment or a type hint, it's
  enforced at construction time. A `Protocol` version would accept the
  incomplete collaborator silently and only fail later, wherever
  `.notify()` actually got called — which is exactly why the gate treats
  `Protocol` as optional comparison, not the graded mechanism.

## World Bible entry

The fictional student who built this would record, in their own World
Bible (`docs/course-ethos.md`'s "short living project record: charter,
current state, one line per week saying what changed/broke, known debt,
tests/evidence, and important design choices"):

> **Week 7.** The kitchen world's order-ready announcement was implicit
> through Weeks 4-6 -- nothing said *how* "ready" gets communicated, it
> just happened inline wherever cooking finished. Made that dependency
> explicit as an `OrderNotifier` contract (`abc.ABC` + `@abstractmethod
> notify`), with `KitchenBell` and `TicketPrinter` as two genuinely
> different conforming collaborators, and `announce_order_ready` as the
> caller that only trusts the contract, never the concrete type.
> Evidence: `test_announce_order_ready_holds_the_contract_for_either_
> collaborator` (the swap test) and
> `test_announce_order_ready_accepts_a_notifier_it_has_never_seen` (the
> guard against a caller that secretly knows too much) -- both pass, plus
> `test_the_contract_is_enforced_not_just_documented` showing the ABC
> actually blocks an incomplete collaborator at construction time, not
> just at call time. Remaining debt: no third real-world notifier channel
> exists yet (e.g. a text/SMS notifier); the contract is proven for two,
> not stress-tested for a genuinely async one. `typing.Protocol` was
> considered as an alternative and rejected for this gate specifically
> because it would not have caught `SilentSpeaker` at construction time —
> worth revisiting if a future week needs duck-typed collaborators from
> outside this codebase.

## What this is not

Not a second graded assignment. Not a hierarchy, recursion, queue, GUI,
or algorithm — the rubric explicitly warns against that kind of
artificial scope, and this example deliberately stays as small as real
student work should be: one contract, two collaborators, one caller, one
swap test. Pick your **own** real Weeks 4-6 dependency for your actual
submission; this kitchen world is illustration, not the assignment.
