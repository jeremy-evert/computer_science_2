# Week 7: Contract and Swap

Welcome to Week 7. This is a checkpoint, not a second mini-project. You will
make one real dependency in the program you have been growing since Weeks 4--6
explicit, prove that two collaborators can satisfy it, and explain the boundary
where your caller trusts that contract.

Start with the student handout: [Week 7 guided path (PDF)](week_07_guided_path.pdf).
Its editable source is `week_07_guided_path.tex`.

## The one path to follow

The numbered Frontier Settlement files are the canonical guided example. Read
or run them in order; each file adds exactly one idea.

1. `step_01_values.py` -- values and errors that cross the boundary.
2. `step_02_contracts.py` -- the explicit `SupplySource` ABC. The Protocol is
   an optional comparison, not the required mechanism.
3. `step_03_validation.py` -- small validation helpers.
4. `step_04_warehouse.py` -- the first stateful collaborator.
5. `step_05_trading_post.py` -- a second collaborator with a different rule.
6. `step_06_planner.py` -- the caller boundary: validation, delegation,
   contract enforcement, decisions, and failure context.
7. `step_07_tests.py` -- contract, swap, behavior, and boundary evidence.
8. `step_08_demo.py` -- a visible story of the swap.
9. `step_09_world_bible.py` -- the concise reflection.

Run the canonical example from this directory:

```powershell
python class_example.py test
python class_example.py demo
python class_example.py bible
```

`python class_example.py` runs all three. Do not rely on `python -m unittest
discover` at this directory level: the teaching test module is intentionally
named `step_07_tests.py`, so the entry point loads it explicitly.

## Your graded discussion post

This work is a shared learning resource: classmates will be able to see your
post. Publish a concise post with a repository link or code attachment and:

1. Name the real dependency from your own Weeks 4--6 program that you made
   explicit.
2. Show the ABC and abstract operation, plus two genuinely different,
   stateful collaborators that implement it.
3. Link or paste one focused test that sends the same request through the same
   caller with each collaborator. Assert the shared promise, not exact prose
   from one implementation.
4. Explain the caller boundary in plain language: what it validates before and
   after delegation, and how it handles a collaborator failure.
5. Include a short demonstration result and a World Bible update with the
   change, evidence, and remaining debt.
6. Reply constructively to at least two classmates. Point to a specific design
   choice or test, ask a useful question, or describe a transferable idea.

Do not copy a reference world. Your project should extend a real dependency in
your own program. Never include private or identifying information about
yourself or another student in the post.

## Reference worlds (optional)

These are short, independent illustrations of the same target, not additional
assignments and not templates to copy:

- `week_07_contract_and_swap/` -- a polished, alternate Growth Reporter
  reference with its own README, tests, demo, and World Bible (stateful
  collaborators, matching the current gate)
- `contract_swap_example/` -- kitchen notifications
- `contract_swap_example_investigation_bureau/` -- evidence logging
- `contract_swap_example_starship_log/` -- subsystem reporting

The last three predate the stateful-collaborator update and use simple
stateless collaborators -- still a valid illustration of the contract/
caller-boundary/swap-test shape, just not a model for the "stateful"
requirement specifically. Use `week_07_contract_and_swap/` for that.

Read one only if its setting helps you understand the idea. The numbered path
above is the complete guided lesson.
