# Week 6 — Earned Substitution, built through tests

**Week 6 target (`planning/week-06.md`, "Earned Substitution (S02)"):** look for a genuine `is-a`
relationship, show two subtypes receiving one shared operation with meaningfully different
behavior, or document why composition is the better design. Use a focused test or trace. Do not
invent a hierarchy.

This example gets to that target from the other direction. Instead of starting from the vocabulary
(`is-a`, inheritance, polymorphism), we start from a test and let the shared operation show up.

## Run it

From this directory:

```bash
python -m unittest -v
```

All 8 tests pass. (The test file does `from cooking_appliance import ...`, so run it from here.)

## What happened in class (Wednesday, September 23)

Jeremy said the planned `is-a` versus `has-a` conversation did not resonate with him this week, so he
spent the session on unit testing and source control instead: a live, unscripted red-green-refactor
run with Copilot as a steered tool. The rhythm, paraphrased from the recording:

| Step | What the test asked for | Why it failed (red) | Smallest fix (green) |
|---|---|---|---|
| 1 | `Oven.cook("bread")` returns `"The oven bakes the bread."` | there was no `cooking_appliance` module at all | create the module with `Oven` |
| 2 | `Grill.cook("bread")` returns `"The grill sears the bread."` | `Grill` could not be imported | add `Grill` |
| 3 | `Oven.can_cook("pizza")` is true | `Oven` had no `can_cook` | add `can_cook` |
| 4 | `Grill` can cook burgers, cannot cook cake, reports `"direct heat"` | three errors, then one, as each method was added | add `can_cook` and `cooking_method` to `Grill` |
| 5 | `prepare_meal(appliance, food)` works with any appliance, **without an `if` statement checking which one it is** | `cannot import prepare_meal` | the class stopped here, on red |

Ground rules Jeremy stated along the way: write the test before the code; ask for "the dumbest
implementation that makes the test pass" (dumbest, not simplest); if you catch yourself doing
something stupid to pass, ask what test would have stopped you; the tests are the contract. His
three takeaways: you don't have to know how to do everything because you have a digital assistant to
coach; source control lets you break things safely; write the test first, or you won't write it.

Two things worth noticing, because they are exactly what the Week 6 target is about:

- **Step 2 already contains the whole idea.** An oven and a grill both take `cook(food)` and give
  meaningfully different results. That is "two subtypes, one shared operation, different behavior."
- **Step 5 is the substitution claim, stated as a test.** Can another part of the program use either
  appliance without knowing which one it got? If so, you have earned the right to say the two are
  substitutable. Not because a class diagram said so, but because a test says so.

## Finishing the red test (done after class)

The class ended with `prepare_meal` missing. It is finished here in the same style:

1. **Red:** `test_prepare_meal_uses_each_appliances_cook_behavior` already existed and failed.
2. **Green, dumbest implementation that obeys the rule:**
   ```python
   def prepare_meal(appliance, food):
       return appliance.cook(food)
   ```
   No `if`, no type checks. It just asks the appliance to cook.
3. **Refactor:** nothing to refactor, so nothing was changed. (Same call the class made at step 1.)
4. **What stupid thing still passes?** An implementation that says `if isinstance(appliance, Oven): ...
   else: ...` passes both existing tests, because those only try an `Oven` and a `Grill`. This was
   checked, not assumed: with that version in place all the original tests still pass.
5. **The test that stops it:** `test_prepare_meal_accepts_an_appliance_it_has_never_seen` hands
   `prepare_meal` a `Smoker` that did not exist when the function was written. The `isinstance`
   version fails it; the real one passes. That is the difference between "works for the two things
   we tried" and "substitution is earned."

## An honest note about inheritance

In the recorded session the class asked out loud whether an oven and a grill being appliances counts as
inheritance, and moved on. **The committed code has no `Appliance` class.** `Oven`, `Grill`, and the
`Smoker` in the guard test are unrelated classes that happen to share the same operation, `cook(food)`.
In Python that is enough for `prepare_meal` to work, because it only needs the operation to exist.

So what was earned here is the *shared contract* (`cook(food)`), not a base class. Adding an
`Appliance` parent later would be an honest next red test: what would a base class give us that the
tests are currently missing (for example, a clear error when a subtype forgets to implement `cook`)?
If nothing fails without it, the base class has not been earned yet. That is the same "don't invent a
hierarchy" warning the Week 6 target gives.

## The originally planned material still stands

Nothing was replaced. Two routes to the same idea:

- `../01_smallest_substitution.py` — `Defender` / `Guard` / `Turret`: substitution through an
  explicit parent class.
- `../02_composition_not_inheritance.py` — `Key` / `Lock` / `Vault`: when composition is the better design.
- `../03_test_substitution.py` and `../03_c_inherited_traits_and_substitution.py` — the same
  Defender example already expressed as tests.
- `../04_week6_submission_example.py` — the shape of a Week 6 submission.

This example and those are both legitimate. Pick whichever example makes the idea click, then find the
same shape in your own world.

## Try it (optional, good Show & Tell material)

1. Add a `Microwave` that can cook `"popcorn"`. Write the failing test first. Do **not** edit
   `prepare_meal`.
2. Write a test that would fail if someone added `if isinstance(...)` to `prepare_meal`. (Does the
   guard test already cover it? Try the cheat and find out.)
3. Find one real `is-a` in your own project's world, or make the case that composition fits better,
   and show the test or trace that supports your choice.
