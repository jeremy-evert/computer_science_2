# Contract and Swap: Suggested Exploration Order

This refactoring uses short, numbered teaching steps. Read or run them in this order:

1. `step_01_values.py` — the data that crosses the boundary and the domain errors.
2. `step_02_contracts.py` — the explicit ABC contract and optional Protocol comparison.
3. `step_03_validation.py` — focused input-validation helpers.
4. `step_04_warehouse.py` — the first stateful implementation.
5. `step_05_trading_post.py` — the second implementation and its different rule.
6. `step_06_planner.py` — the caller boundary, decision-making, and enforcement.
7. `step_07_tests.py` — tests that prove the shared contract and the swap.
8. `step_08_demo.py` — the runnable narrative demonstration.
9. `step_09_world_bible.py` — the design reflection.

`class_example.py` remains the entry point. It still supports `all`, `test`,
`demo`, and `bible`; it now only coordinates the numbered modules.

