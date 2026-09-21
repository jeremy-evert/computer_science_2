# 031 — Build CS2 Week 6 smallest earned-substitution example with Hanna

## Owner
Computer Science II, Fall 2026

## Mission
Build the first, smallest student-facing code example for Week 6: **Earned Substitution**.

This is intentionally one-file-at-a-time work.

## Current teaching context
Week 6 asks students to reopen Week 5 collaborating objects and decide whether an honest **is-a** relationship exists.

If it does, students should be able to recognize that:
- two subtypes can share one operation,
- each subtype can implement that operation differently,
- client code can call the same operation without branching on concrete type,
- inheritance is justified by the model, not by a desire to reuse code.

If an honest is-a relationship does not exist, composition remains the better design. Do not teach or build that second path yet in this first file. We will add it later.

## Build exactly one student-facing file
Create:

`week_06/01_smallest_substitution.py`

Do not create additional Week 6 teaching files in this mission.

## Example
Use this tiny world:

```text
Defender
├── Guard
└── Turret
```

- A `Guard` is a kind of `Defender`.
- A `Turret` is a kind of `Defender`.
- Every `Defender` responds to an intruder through `respond_to_intruder()`.
- The Guard and Turret must behave meaningfully differently.

Keep the implementation ordinary and readable for early Computer Science II students.

## Keep it small
Use ordinary Python.

Do not use:
- `abc` / `ABC`
- `Protocol`
- dataclasses
- decorators
- external packages
- advanced typing
- automated tests yet
- multiple code files

A plain parent class and two child classes are enough.

The bottom of the file should contain a tiny runnable example that puts a Guard and Turret into the same collection and calls `respond_to_intruder()` on both without type-checking.

## Student-learning comments
This file is a teaching artifact, not merely working code.

Add short comments that explicitly point out what students should learn while reading the code.

Use a clear marker such as:

```python
# STUDENT LEARNING:
# Guard inherits from Defender because a Guard really is a kind of Defender.
```

The comments should teach design reasoning more than Python syntax.

Make sure the file clearly teaches these five ideas:

1. **Is-a earns inheritance.**
   `Guard(Defender)` is justified only if a Guard honestly is a kind of Defender.

2. **Shared operation.**
   The parent establishes `respond_to_intruder()` as the operation every Defender supports.

3. **Different subtype behavior.**
   Guard and Turret respond differently.

4. **Same call, different result.**
   Client code sends the same `respond_to_intruder()` message to each object and gets subtype-specific behavior.

5. **No type-checking required.**
   The client should not need `if isinstance(...)` or another concrete-type branch.

Also include one short comment stating:

> Similar code alone does not justify inheritance. The child must honestly be a kind of the parent.

## Preferred output
Something approximately this simple is appropriate:

```text
Guard walks toward the intruder.
Turret rotates and fires at the intruder.
```

Exact wording may vary.

## Verification
Before claiming completion:

1. Inspect current repository truth and preserve unrelated work.
2. Run the new file with Python.
3. Confirm the output demonstrates visibly different behavior.
4. Review the comments for student readability.
5. Confirm only the intended student-facing code file was added or changed for this teaching step, apart from durable sidecar evidence Hanna may need to record.

## Git / publication authority
This mission authorizes Hanna to make an ordinary forward commit and push the completed bounded change to `main` if the repository is clean enough to do so safely and no unrelated local work would be swept into the commit.

Never force-push, amend published history, or stage unrelated paths.

If unrelated local work prevents a safe commit, preserve it and report the exact conflict instead of touching it.

## Completion report
When finished, report:
- exact file created,
- command used to run it,
- observed output,
- the five student-learning points present in the comments,
- commit SHA if published,
- any real human gate that remains.

Do not continue to File 2. Stop after this one-file teaching example is complete.
