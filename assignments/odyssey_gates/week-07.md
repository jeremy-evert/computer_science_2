# Odyssey Gate — Week 7: A world with families (Inheritance, Round 1)

**Concept:** inheritance: a base class, a derived class, `super()`, and an overridden method (Deitel, *Intro to Python for Computer Science and Data Science*, §§10.7–10.8). **Arc:** 2 — Worlds with Structure. **Instrument:** Quick Check (pass/fail) — see `docs/curriculum/judgment_toolkit.md` §1.

## The gate (do this first)

Turn one real kind of world object into a base class and make a more specific kind of it. The derived object must reuse shared initialization with `super()` and override one inherited method because its behavior genuinely differs.

## Quick Check (pass/fail)

- [ ] A base class and a subclass express a defensible **is-a** relationship.
- [ ] The subclass initializer calls `super().__init__(...)` to establish its shared state, then adds or refines its own state.
- [ ] A method with the same name is overridden and a live run shows behavior that differs for the derived object.

## Suggested textbook problem (optional scaffolding)

The general problem: create a base `WorldMember` and one specialized subtype; both report status, but the subtype reports or acts differently.

- **Frontier Settlement:** `Colonist` and `Farmer`, whose `work()` adds food.
- **Investigation Bureau:** `Person` and `Detective`, whose `act()` adds a lead.
- **Starship Log:** `CrewMember` and `Engineer`, whose `perform_duty()` repairs a system.
- **Small Business:** `Employee` and `Cashier`, whose `perform_duty()` records a sale.

Do this version directly if it helps, then let it *be* your gate submission.

## Then: open continuation (light Build, holistic)

Extend the family only where it makes the world clearer; inheritance is not a reason to duplicate an entire class.

## World Bible

One line: what family you introduced, what broke.

## Looking ahead

Week 8 makes several specialized objects respond to the same message polymorphically.
