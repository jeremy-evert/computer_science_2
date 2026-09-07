# Week 4 — Collaborating Objects: composition and invariants

Week 4 is a refactor week. Reopen the cohesive object you built in Week 3,
find one thing it needs from another object, and make that collaboration
explicit. The goal is a small, meaningful design change—not a framework,
inheritance hierarchy, or new feature pile.

## Learning targets

By the end of this lesson, you should be able to:

- name the responsibility and boundary of each collaborating object;
- use composition by giving one object a useful collaborator;
- state one invariant in plain language and protect it with a focused test;
- compare composition with inheritance without inventing an `is-a` story; and
- use the AI Fluency habit **decompose the task**: turn a large refactor into
  small claims, inspect the proposed diff, and accept or reject it from
  independent evidence.

## Monday bridge: decompose the task

There is no Monday class this week because of Labor Day. Before Wednesday,
write four short lines in your notes:

1. **Existing object:** what state and behavior already belong together?
2. **Collaborator:** what other object does the real flow need?
3. **Invariant:** what must never be false after a public operation?
4. **Smallest proof:** what one test would catch a violation?

This is the Week 4 use of AI Fluency's *Decompose the Task* connection. It is
not a second assignment and does not ask you to use an AI tool.

## Wednesday — refactor the real flow

Start from the object and flow you submitted for the Week 3 gate. Draw a tiny
object map before changing code:

```text
Order  ──has-a──> Inventory
  |                 |
  |                 └─ knows available quantity
  └─ requests reservation and tracks status
```

The arrows describe ownership or collaboration, not inheritance. A useful
first pass is:

1. Describe the flow in one sentence, from request to outcome.
2. Circle the new decision or state relationship that needs a collaborator.
3. Give the collaborator one narrow responsibility and one public operation.
4. State the invariant before writing the test.
5. Make the smallest refactor that lets the objects collaborate.

### Worked example: a small-business order

Suppose the real flow is “customer requests two notebooks → inventory checks
stock → order reserves them.” `Order` should not own every inventory count.
`Inventory` owns quantities; `Order` owns its status and requested lines.

```python
class Inventory:
    def __init__(self, quantities):
        self.quantities = dict(quantities)

    def reserve(self, item, quantity):
        if self.quantities.get(item, 0) < quantity:
            return False
        self.quantities[item] -= quantity
        return True


class Order:
    def __init__(self, inventory, item, quantity):
        self.inventory = inventory       # composition: Order collaborates with Inventory
        self.item = item
        self.quantity = quantity
        self.status = "pending"

    def reserve(self):
        if self.inventory.reserve(self.item, self.quantity):
            self.status = "reserved"
            return True
        return False
```

The invariant is: **an order is `reserved` only when inventory has actually
reserved the requested quantity**. The focused test exercises the behavior
and checks the state change:

```python
import unittest


class OrderTest(unittest.TestCase):
    def test_reservation_cannot_overdraw_inventory(self):
        inventory = Inventory({"notebook": 2})
        order = Order(inventory, "notebook", 3)

        self.assertFalse(order.reserve())
        self.assertEqual(order.status, "pending")
        self.assertEqual(inventory.quantities["notebook"], 2)
```

This test proves the rejected order does not claim a reservation or consume
stock. It does not prove payment, shipping, persistence, or every possible
quantity; keep those limits visible in the World Bible entry.

## Friday — verify, compare, and explain

Run the focused test independently of any AI conversation or manual demo.
Then perform one small trace that makes the collaboration visible: print or
inspect the two objects before and after the operation, and record the
observed state. If the test fails, keep the failing evidence, explain the
cause, and repair only the bounded change.

Write a short composition decision card:

| Question | Your evidence-backed answer |
|---|---|
| What does each object own? | State and behavior, not just nouns |
| What message crosses the boundary? | A named method and its input/output |
| What invariant is protected? | A sentence plus the focused assertion |
| Why composition? | The relationship is “has-a” or “uses,” with independent responsibilities |
| Why not inheritance? | No meaningful substitutable `is-a` relationship is needed |

If AI helped, preserve the request, inspect the diff, read the changed code,
run the independent test, and record **accept** or **reject** with a reason.
The prompt is provenance; the test and your reading are the evidence.

## Week 4 path and handoff

- Wednesday: object map → smallest collaboration → invariant statement → code.
- Friday: independent test → trace → composition/inheritance decision card.
- Submit the refactor, focused test or trace, explanation, AI evidence when
  used, and one concise World Bible entry through the [Week 4 Odyssey gate]({{link:week04_odyssey_gate}}).
- Review the [Week 4 rubric]({{link:week04_odyssey_rubric}}) before submitting.

The Week 4 gate carries 25 points in the Weekly reinforcement assignment
group. Week 5 may ask whether a genuine `is-a` relationship earns
inheritance; do not build that hierarchy now just to prepare for it.
