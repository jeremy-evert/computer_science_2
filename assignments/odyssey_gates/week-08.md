# Odyssey Gate — Week 8: The family acts together (Inheritance, Round 2)

**Concept:** polymorphism and multiple derived classes (Deitel, §§10.8–10.9). **Arc:** 2 — Worlds with Structure. **Instrument:** Quick Check (pass/fail) — see `docs/curriculum/judgment_toolkit.md` §1.

## The gate (do this first)

Put at least two different subclasses in the same world collection or flow. Call the same meaningful method on each object; the calls must produce different real behavior because each subtype implements that method for itself.

## Quick Check (pass/fail)

- [ ] At least two distinct subclasses share a meaningful base class.
- [ ] One loop or other shared flow calls the **same method name** on objects of both subclasses without branching on the concrete class first.
- [ ] The demonstrated calls produce different world effects (state change, computed result, or consequence), not only different labels.

## Suggested textbook problem (optional scaffolding)

The general problem: process a mixed roster and call `act()` or `update()` on every object; each subtype changes the world in its own way.

- **Frontier Settlement:** `Farmer` and `Guard` each take a `shift()`.
- **Investigation Bureau:** `Detective` and `Analyst` each `process_case()`.
- **Starship Log:** `Engineer` and `Pilot` each `perform_duty()`.
- **Small Business:** `Cashier` and `Stocker` each `work_shift()`.

Do this version directly if it helps, then let it *be* your gate submission.

## Then: open continuation (light Build, holistic)

Add a third subtype only if it earns its place; improve the shared base API instead of scattering `isinstance` checks.

## World Bible

One line: which common action became polymorphic, what broke.

## Looking ahead

Week 9 is Checkpoint 2: demonstrate the inheritance family as a working part of the world.
