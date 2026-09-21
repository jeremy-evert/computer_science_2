# 032 — Build CS2 Week 6 composition-not-inheritance example with Hanna

## Owner
Computer Science II, Fall 2026

## Mission
Build the second, smallest student-facing code example for Week 6: **Composition instead of inheritance**.

This is intentionally one-file-at-a-time work.

Read the existing first example before editing:

`week_06/01_smallest_substitution.py`

File 1 demonstrates a case where inheritance is earned:

```text
Defender
├── Guard
└── Turret
```

File 2 must teach the opposite design decision: objects may work together closely without one being a kind of the other.

## Build exactly one student-facing file
Create:

`week_06/02_composition_not_inheritance.py`

Do not create additional Week 6 teaching files in this mission.

## Teaching goal
Students should learn that collaboration does not automatically imply inheritance.

Use a tiny Vault / Lock / Keyholder example.

A reasonable relationship is:

```text
Vault HAS-A Lock

Keyholder HAS-A Key

Keyholder uses the Key to work with the Vault's Lock.
```

The important design claim is:

- A Vault is not a kind of Keyholder.
- A Keyholder is not a kind of Vault.
- A Lock is not a kind of Vault.
- These objects collaborate, so composition is the honest model.

Do not invent a parent class merely to make the objects look related.

## Keep it deliberately small
Use ordinary Python only.

Do not use:
- `abc` / `ABC`
- `Protocol`
- dataclasses
- decorators
- external packages
- advanced typing
- automated tests yet
- multiple code files
- inheritance in this example

This example should be approximately as small and readable as
`01_smallest_substitution.py`.

## Suggested behavior
A simple shape is enough:

- `Key` stores a small identifying value.
- `Lock` knows what key value opens it.
- `Vault` owns a `Lock`.
- `Keyholder` owns a `Key`.
- `Keyholder.open_vault(vault)` attempts to use its key with the vault.

The exact method names may vary if Hanna finds a clearer beginner-friendly shape.

The runnable example at the bottom should show the collaboration succeeding.

A simple output such as:

```text
The key fits. Vault opened.
```

is enough.

Avoid adding extra game mechanics, security rules, error systems, inventories, or abstractions.

## Student-learning comments
This file is a teaching artifact, not merely working code.

Use short comments with the same marker as File 1:

```python
# STUDENT LEARNING:
```

The comments should explain the design reasoning more than Python syntax.

Make sure the file clearly teaches these four ideas:

1. **Ask "is-a?" before inheriting.**
   Students should be able to say the relationship aloud. "A Vault is a Keyholder" is false, so inheritance would be dishonest.

2. **Has-a suggests composition.**
   A Vault has a Lock. A Keyholder has a Key. That relationship is represented by one object containing or referring to another.

3. **Collaboration does not require inheritance.**
   Objects can call each other's operations and solve a problem together while remaining different kinds of things.

4. **Keep responsibilities separate.**
   The Vault should not become responsible for being a Keyholder, and the Keyholder should not become responsible for being the Vault.

Include one especially clear comment stating something close to:

> Working together does not make two objects members of the same family.

Also include the contrast with File 1 in one brief comment:

> Guard is-a Defender. Vault has-a Lock.

Do not turn this file into a lecture. Prefer a few sharp comments placed beside the code that demonstrates the idea.

## Important anti-example
It is useful to mention in a comment that code like this would be conceptually wrong:

```python
class Vault(Keyholder):
    ...
```

Do not actually implement the wrong hierarchy.

Explain in plain language that the sentence "a Vault is a Keyholder" fails the is-a test.

## Verification
Before claiming completion:

1. Inspect current repository truth and preserve unrelated work.
2. Read `week_06/01_smallest_substitution.py` so File 2 feels like its conceptual twin.
3. Run the new file with Python.
4. Confirm the collaboration succeeds.
5. Review the comments for early-CS-II readability.
6. Confirm no inheritance is used in File 2.
7. Confirm only the intended student-facing code file was added or changed for this teaching step, apart from durable sidecar evidence Hanna may need to record.

## Git / publication authority
This mission authorizes Hanna to make an ordinary forward commit and push the completed bounded change to `main` if the repository is clean enough to do so safely and no unrelated local work would be swept into the commit.

Never force-push, amend published history, or stage unrelated paths.

If Morgan's default SSH configuration again blocks publication, Hanna may reuse the already-discovered existing authorized Morgan GitHub identity and the same safe `ssh -F /dev/null` workaround from Mission 031. Do not modify system SSH configuration as part of this mission.

If unrelated local work prevents a safe commit, preserve it and report the exact conflict instead of touching it.

## Completion report
When finished, report:
- exact file created,
- command used to run it,
- observed output,
- the four student-learning points present in the comments,
- how the file contrasts with File 1,
- commit SHA if published,
- any real human gate that remains.

Do not continue to File 3.

File 3 will introduce automated behavioral evidence later. Stop after this one-file composition example is complete.
