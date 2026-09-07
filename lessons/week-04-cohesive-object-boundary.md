# Week 4 — Cohesive Object Boundary

**Objectives:** reopen your Week 3 World Bible; test one predicted noun as a
possible software object; give that object meaningful state and behavior when
the evidence supports it; explain the boundary in plain language; and run one
focused `unittest` independently.

**Monday bridge — Labor Day:** there is no Monday class this week because
September 7 is a holiday. Use Monday to reopen your World Bible v0.1 and pick
one candidate from its predicted-object list. Bring the candidate, one real
flow it participates in, and one boundary question to Wednesday. You do not
need to invent a larger design to make up the missed meeting.

## Start with the World Bible, not a class diagram

Week 3 asked you to write a short World Bible: a premise, 5–8 nouns, one real
flow, software questions, known unknowns, and 3–5 predicted objects. Those
predictions were deliberately provisional. This week, reopen the [Week 3
World Bible gate]({{link:week03_odyssey_gate}}) and investigate exactly one of
them.

Ask four small questions:

1. What state does this candidate own?
2. What behavior naturally uses or changes that state?
3. Would those state changes and behaviors still make sense together if the
   rest of the world changed?
4. What is the smallest test that could show the boundary is useful?

A cohesive boundary is a small promise: the object owns related state and can
perform behavior that belongs with that state. It is not a synonym for every
noun in the World Bible, and it is not a requirement to create a class for
every noun.

## Worked example: a predicted `SupplyCrate`

Imagine a **Frontier Settlement** World Bible with this flow:

```text
settlement receives a crate -> supplies are counted -> a crew claims supplies
-> the settlement records what remains
```

The predicted-object list includes `SupplyCrate`. Before writing a class, make
the boundary claim precise:

> A `SupplyCrate` owns its contents and can release a requested quantity only
> when that quantity is available.

That claim gives the object meaningful state (`item_name` and `quantity`) and
one behavior (`claim`). Counting and claiming belong together because claiming
changes the quantity the crate owns. The settlement's larger receiving flow
does not belong inside the crate; it can decide which crate to ask and record
the result.

```python
class SupplyCrate:
    def __init__(self, item_name, quantity):
        self.item_name = item_name
        self.quantity = quantity

    def claim(self, amount):
        if amount <= 0:
            raise ValueError("claim amount must be positive")
        if amount > self.quantity:
            return False
        self.quantity -= amount
        return True
```

The boundary is useful because one operation protects the relationship
between the crate's state and its behavior. A caller does not need to repeat
the subtraction rule or guess whether an over-sized claim should change the
quantity.

But predictions are allowed to be wrong. Suppose the World Bible evidence
shows that a “crate” is only a delivery label: the settlement immediately
unpacks everything, and no later action treats the crate as a thing with
state. Then `SupplyCrate` does not deserve a cohesive boundary. Record that
finding and choose a better candidate, or explain why the label remains plain
data. “I predicted wrong” is legitimate evidence for this gate, not a failed
assignment.

## One focused `unittest`

The test should construct the object, exercise one meaningful behavior, and
assert the resulting state or value. Run it independently of any manual
walkthrough.

```python
import unittest


class SupplyCrateTest(unittest.TestCase):
    def test_claim_reduces_owned_quantity(self):
        crate = SupplyCrate("water", 10)

        claimed = crate.claim(3)

        self.assertTrue(claimed)
        self.assertEqual(crate.quantity, 7)


if __name__ == "__main__":
    unittest.main()
```

Run the file with Python, for example:

```text
python -m unittest test_supply_crate.py
```

Your World Bible update should say what changed, what evidence you used, and
what debt remains. Include one sentence such as: “The test proves that a
successful claim reduces the crate's quantity by the requested amount; it does
not prove every invalid input or the whole settlement flow.”

## AI accountability

AI use is allowed, but an AI response is a proposal, not proof. If AI helped,
retain the useful prompt or request as provenance and record this trail:

```text
proposal -> inspected diff -> independent test -> read/reasoned about result
-> accept or reject decision
```

Your decision should name evidence. For example: “Accepted the method because
the diff changed only the crate boundary and the independently run test passed;
rejected the suggested Settlement class because the World Bible did not show
that responsibility belonging there.” If AI was not used, say so briefly. The
[Week 4 Odyssey gate]({{link:week04_odyssey_gate}}) and [rubric]({{link:week04_odyssey_rubric}})
describe the submission evidence and scoring contract.

## Keep the bite small

This is one boundary and one focused test, not a mini-project. Do not add a
hierarchy, GUI, persistence layer, or broad refactor to make the work appear
more advanced. A narrow object whose responsibility you can explain and
verify is stronger evidence than a large design you cannot defend.
