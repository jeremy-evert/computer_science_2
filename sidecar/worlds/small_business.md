# World Bible: Small Business

Internal canon. See `README.md` for the shared firewall, safety
boundaries, and authoring rules before writing anything set here.

## 1. Core premise

**Delgado Hardware & Supply** is a real, functioning small business --
twenty-two years old, three employees, one owner who still works the
counter most days. It grew for two decades on a paper order pad, a
cash register, and Frank Delgado's memory. That worked fine at the old
size. It does not work at the new size.

Software matters here because **the business is real and the stakes
are real** -- inventory that doesn't match, orders that ship before
payment clears, a supplier relationship that depends on accurate
records. The student isn't building a toy store simulation; they're
building the tools an actual business owner needs to keep the business
honest and solvent. This world is the most "grounded, no genre at all"
of the four -- its texture comes from real operational stakes, not
setting.

## 2. Tone and flavor

**Is:** warm, practical, a little tired in the way small-business
owners genuinely are, but proud of what he's built. Problems are
concrete (inventory count is wrong, a supplier is demanding an
answer) and solved through good systems and honest numbers. Humor is
wry and self-aware -- the specific exhaustion of someone who wears
five job titles at once.

**Must not become:** a generic "MBA case study," a business-bro
caricature, or cheap "capitalism is evil / capitalism is great" framing.
Delgado Hardware is not a metaphor for anything -- it's a real business
with real people who depend on it, including Frank's employees.

## 3. Setting and boundaries

- **The Front Counter** -- where the register lives and where the
  student's work most directly meets a customer, even if only
  indirectly. The student's default "workplace" framing.
- **The Back Office** -- inventory, supplier orders, the books. A
  natural source of invariant problems (inventory count must never go
  negative; an order must never ship before payment clears).
- **The Supplier Relationship** -- Delgado orders from vendors whose
  data formats don't match his own systems -- a natural
  contract/interface problem.
- **The Sales Floor** -- where inventory meets real (simulated)
  customers; a natural source of collections/search/ordering problems
  (what's in stock, what's low, what needs reordering).

Boundaries: no real customer harm, no predatory-business framing, no
treatment of employees as disposable. Delgado cares about his people;
that's part of the character, not incidental.

## 4. Recurring characters

- **Frank Delgado** -- owner and operator, twenty-two years in. Proud,
  practical, allergic to jargon, deeply committed to running an honest
  business. The one who briefs the student and sets expectations.
  Jeremy's primary persona in this world -- see section 5 and
  `four_faces/small_business_frank_delgado.md` for the full dossier.
- **Yolanda** -- Frank's longest-tenured employee, runs the front
  counter, knows the regular customers by name, increasingly the one
  who notices when the old paper-based habits are breaking down.
  Useful voice for surfacing a real operational problem from the floor.
- **Denny** -- a newer employee, eager, a little overwhelmed, useful
  for injecting "I did my best but I think I made this worse" energy
  around inventory or ordering mistakes (never played as incompetence
  to mock -- played as someone still learning a real job).

## 5. Jeremy's playable personas

**Primary: Frank Delgado.** Visual language: a shop apron or vest over
a plain shirt, a clipboard or order pad as a prop, reading glasses.
Voice: plain, warm, direct -- explains things the way a good boss
explains things to a new hire, not the way a consultant explains
things to a client.

**Alternate: Yolanda**, for a scene needing floor-level urgency rather
than ownership-level framing -- same setting, faster and more
clipped, closer to the actual daily friction.

## 6. Visual identity

- **Palette:** warm green/brown accent -- distinct from Frontier
  Settlement's amber, grounded and "hardware store," not corporate.
- **Type mood:** simple, functional, hand-lettered-adjacent for
  in-world signage/receipts (never for classroom slides, which stay in
  the Prompt 015 theme).
- **Diagram motif:** simple inventory/flow diagrams -- shelves, orders,
  register -- kept utilitarian.
- **Iconography:** a price tag, a receipt, a shopping cart/basket used
  sparingly.
- **Title card:** "DELGADO HARDWARE \& SUPPLY -- BACK OFFICE" over a
  green accent bar, styled like a receipt header.

## 7. Artifact language

Order pads, supplier invoices, inventory counts, register receipts,
customer requests, Frank's back-office notes, end-of-day tally sheets.

## 8. CS2 problem generators

- **Composition/invariants:** an inventory record that must never show
  a negative count and an order that must never ship before payment
  clears.
- **Contracts/interfaces:** a new supplier's data format that doesn't
  match Delgado's existing order system.
- **Inheritance/polymorphism:** different product types (hardware,
  seasonal, special-order) sharing a common "Product" contract with
  type-specific rules.
- **Collections/search/order:** prioritizing supplier orders by
  urgency vs. cost; sorting inventory by what's low vs. what's slow-
  moving.
- **GUI/model-view:** a simple daily register/inventory screen Frank
  can actually read at the counter.
- **Data visualization:** an honest margin-per-product chart -- the
  kind that might tell Frank something he doesn't want to hear.
- **Peer review/stabilization, source management:** Frank and the
  student reconciling two versions of the inventory count after a
  busy weekend.

Full cross-world mapping: `capability_map.md`.

## 9. Continuity

See `continuity_ledger.md`, section "Small Business." Consult before
writing new material; add new named characters/threads there in the
same commit that introduces them.

## 10. Seeds and delayed payoffs

- An early assumption that Delgado only sells single units (never
  bulk/case quantities) could quietly break once a bulk order comes in
  later in the semester.
- Yolanda's early offhand comment about a regular customer's recurring
  order could set up a later "this customer's order has been wrong for
  weeks and nobody caught it" moment.
- Denny's early inventory mistake, initially just a minor fix, could
  turn out to reveal a real gap in the system's validation.
- A supplier relationship that starts smooth could turn tense if a
  format mismatch causes a real reconciliation problem later.

None of these are required to pay off. Garden, not railroad.

## 11. Injection menu

- 30-45s video: Frank explaining why the old paper order pad finally
  has to go -- "I trust my memory. I don't trust it at this size."
- Written memo: Yolanda flagging that a regular customer's order keeps
  coming out wrong.
- One-slide interruption: an incoming supplier invoice in a format
  that doesn't match the existing system.
- Artifact drop: an end-of-day tally sheet with a number that doesn't
  add up.
- Character update: Frank's brief note that the shop finally closed a
  clean month -- a rare warm beat, useful late in the semester.

## 12. Safety and taste

See `README.md`'s shared boundaries. Specific to this world: no
"small business owner as folksy caricature," no treatment of Frank's
employees as disposable or as the butt of jokes, no reduction of the
business to a generic case-study exercise.

## Prototype: one briefing concept

> **FRANK DELGADO, at the back-office counter, order pad in hand.**
>
> "You're the one helping me get this off paper. Good." *(sets pad
> down)* "Twenty-two years, I've run this place on that pad and what's
> in my head. Worked fine when it was just me and Yolanda. Doesn't
> work anymore -- I had a supplier ask me last week if I even knew
> what I had in stock, and I had to admit I wasn't sure. I need
> something that knows what I've got, so I can go back to worrying
> about the parts of this business I'm actually good at."

Runtime: ~30s. Establishes stakes (real business, real growing pains),
character (Frank, warm and practical), and the ask.
