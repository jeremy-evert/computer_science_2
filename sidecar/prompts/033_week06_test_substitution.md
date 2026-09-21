# 033 — Build CS2 Week 6 smallest substitution test with Hanna

## Owner
Computer Science II, Fall 2026

## Mission
Build the third student-facing Week 6 example: turn the substitution claim from File 1 into small automated behavioral evidence.

This remains one-file-at-a-time teaching work.

## Read first
Before editing, read:

- `week_06/01_smallest_substitution.py`
- `week_06/02_composition_not_inheritance.py`

The first file teaches when inheritance is honest.
The second file teaches when composition is more honest.
This third file teaches how a small automated test can support the inheritance/polymorphism claim.

## Build exactly one student-facing file
Create:

`week_06/03_test_substitution.py`

Do not create additional Week 6 teaching files in this mission.
Do not modify Files 1 or 2.

## Teaching goal
Students should learn that saying "these subtypes behave differently" is a design claim, and a test can provide evidence for that claim.

The test should demonstrate:

- a `Guard` and a `Turret` are both usable through the same operation,
- both receive `respond_to_intruder()`,
- the operation produces meaningfully different behavior for each subtype,
- automated assertions make that difference explicit.

## Important beginner constraint
The existing teaching filenames begin with numbers, so directly importing File 1 would require distracting Python import machinery.

Do NOT introduce:
- `importlib`
- `runpy`
- dynamic imports
- path manipulation
- mocks
- stdout-capture machinery

Those are not the lesson.

For this isolated teaching example, it is acceptable to repeat the tiny `Defender` / `Guard` / `Turret` definition inside the test file so the testing idea remains obvious.

Include one short comment explaining that a real project would normally import the classes from the application module; the repetition exists only to keep this teaching example focused.

## Make the behavior test-friendly
In this file, prefer returning simple strings from `respond_to_intruder()` instead of printing them.

For example:

```python
class Guard(Defender):
    def respond_to_intruder(self):
        return "Guard walks toward the intruder."
```

This lets the test assert directly on behavior without introducing mocking or output-capture techniques.

Keep this distinction explicit in a brief student comment: returning a value makes behavior easy to check automatically.

## Use unittest
Use Python's standard-library `unittest`.

Keep the test suite extremely small.

A reasonable shape is:

```python
class TestDefenderSubstitution(unittest.TestCase):
    def test_subtypes_respond_differently(self):
        guard = Guard()
        turret = Turret()

        guard_response = guard.respond_to_intruder()
        turret_response = turret.respond_to_intruder()

        self.assertNotEqual(guard_response, turret_response)
        self.assertEqual(guard_response, "...")
        self.assertEqual(turret_response, "...")
```

Hanna may improve the exact names or assertion arrangement if a simpler beginner-friendly version is clearer.

Use the normal:

```python
if __name__ == "__main__":
    unittest.main()
```

so students can run the file directly.

## Student-learning comments
Use short comments with the existing marker:

```python
# STUDENT LEARNING:
```

Comments should teach the reasoning, not narrate every line of syntax.

Make sure the file clearly teaches these four ideas:

1. **Same operation.**
   Both subtype objects receive `respond_to_intruder()`.

2. **Different behavior.**
   Guard and Turret return different meaningful results.

3. **Assertions are evidence.**
   The test converts "I think they behave differently" into something Python verifies.

4. **Test the contract, not the concrete type.**
   Do not use `isinstance()` or branch on Guard versus Turret to make the behavior work.

Include a concise comment making the bridge to the Week 6 assignment explicit:

> This test is evidence that one shared operation can produce subtype-specific behavior.

## Keep it deliberately small
Do not introduce:

- external packages
- pytest
- parameterized tests
- fixtures
- mocks
- abstract base classes
- Protocol
- advanced typing
- logging
- multiple test classes
- multiple files

One test method is enough if it proves the concept clearly.

## Verification
Before claiming completion:

1. Inspect current repository truth and preserve unrelated work.
2. Read Files 1 and 2.
3. Create only `week_06/03_test_substitution.py`.
4. Run it directly with Python.
5. Also run it through unittest if useful.
6. Confirm the test passes.
7. Confirm the test actually calls `respond_to_intruder()` on both subtype objects.
8. Confirm the asserted behavior differs.
9. Confirm there is no `isinstance()` or concrete-type branching.
10. Review comments for early-CS-II readability.
11. Confirm only the intended student-facing code file was added or changed for this teaching step, apart from durable Hanna mission evidence.

## Git / publication authority
This mission authorizes Hanna to make an ordinary forward commit and push the completed bounded change to `main` when safe.

Never force-push, amend published history, or stage unrelated paths.

Morgan has already shown a bad system SSH config ownership state. If the normal push fails for that same reason, Hanna may reuse the existing authorized Morgan GitHub identity with the previously verified `ssh -F /dev/null` workaround. Do not modify system SSH configuration.

If unrelated local work prevents a safe commit, preserve it and report the exact conflict.

## Completion report
When finished, report:

- exact file created,
- command used to run the test,
- observed unittest result,
- the four student-learning points present,
- how File 3 connects Files 1 and 2 to the Week 6 Canvas evidence requirement,
- code commit SHA if published,
- Hanna ledger ref if published,
- any real human gate that remains.

Do not continue to File 4.

Stop after this one-file automated behavioral-evidence example is complete.
