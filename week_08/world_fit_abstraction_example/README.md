# Week 8 — World-Fit Data Abstraction, worked example (kitchen)

**Target (`planning/week-08.md`, S05):** choose a real List ADT / stack / queue flow from the world's
actual process, state the client operations, demonstrate FIFO/LIFO with a small test/trace, and
explain why the abstraction is more honest than Python `list` syntax alone.

**The world:** the Week 6 kitchen. Two things really pile up in it:

- **Order tickets wait in a line.** The oldest ticket gets cooked first. → queue (FIFO)
- **The cook's actions pile up so they can be undone.** The newest action is undone first. → stack (LIFO)

Files: `kitchen_flow.py` (about 95 lines), `test_kitchen_flow.py` (8 tests).
Run from this directory: `python -m pytest -v` and `python kitchen_flow.py` (the trace).
Pytest was used here, so `pip install pytest` if a student machine lacks it.

## Walkthrough (~20 minutes)

### 1. The world and the operations (3 min)
Say: "A ticket line has four things a client may do: **enqueue** a ticket, **dequeue** the next one,
**peek** at the next one, ask **is_empty** / **size**. That's the whole contract. Notice what's not
on the list: nobody reaches into the middle of a ticket line." Write the operations on the board
before any code. Same for the undo stack: **push, pop, peek, is_empty, size**.

### 2. Tests first, small red/green steps (10 min)
Open `test_kitchen_flow.py` empty. Add one test at a time, run it, watch it go red (import error or
missing method), then write the dumbest code that makes it green. The file is in teaching order:

| Step | Test | Red because | Smallest fix |
|---|---|---|---|
| 1 | new line `is_empty()`, `size() == 0` | no `kitchen_flow` module | `TicketLine` with `__init__`, `is_empty`, `size` |
| 2 | soup enqueued before burger comes out first | no `enqueue`/`dequeue` | `append` and `pop(0)` |
| 3 | `peek` shows the next ticket, size unchanged | no `peek` | return first item |
| 4 | `dequeue`/`peek` on empty raise `EmptyError` | `IndexError` or wrong error type | explicit check, raise `EmptyError("no tickets waiting")` |
| 5 | undo stack undoes the newest action first | no `UndoStack` | `push`, `pop`, `peek`, `is_empty`, `size` |
| 6 | same input, opposite order | no `trace_same_input` | feed both, drain both |
| 7 | clients can't index or insert | (passes already, it documents the contract) | none |

Say at step 4: "What should a real kitchen do with *dequeue* on an empty line? There is no ticket.
We choose to fail loudly with our own error, not return `None` and let the bug travel."

### 3. The LIFO vs FIFO moment (2 min)
Run `python kitchen_flow.py`:

```
in:   soup, burger, pizza
FIFO out: soup, burger, pizza
LIFO out: pizza, burger, soup
```
Same three items in, opposite order out. The *structure* decides the order, not the data.

### 4. Why the abstraction is more honest than `list` (5 min)
Open a Python prompt and do this live:

```python
tickets = ["soup", "burger", "pizza"]
tickets[2]            # 'pizza'  -- the line has no "third place" you can grab
tickets.insert(0, "VIP")  # cutting in line; a real kitchen forbids this
tickets.pop()         # takes the NEWEST ticket: stack behavior on what we called a line
tickets.sort()        # reorders the line; tickets must stay in arrival order
```
Then:

```python
from kitchen_flow import TicketLine
line = TicketLine()
line.insert(0, "VIP")   # AttributeError
line[2]                 # TypeError
```
Say: "`list` can do everything, so it says nothing. It can't tell you whether this is a line or a
pile. `TicketLine` makes the promise: a ticket enters at the back and leaves from the front, and
nothing else is allowed. The operations *are* the process." Bonus honesty: `pop(0)` on a list is
slow for huge lines (`collections.deque` fixes that), and that is a good reason the interface is
separate from the implementation. We could swap the inside and no client code would change.

## What a student gate submission looks like (3 lines)
Tie each line to the gate's criteria (`assignments/odyssey_gates/week-08.md`):

1. **Flow and operations:** "In my lighthouse world, ships wait for the dock: `enqueue(ship)`, `dequeue()`, `peek()`, `is_empty()`, `size()`; the harbor master serves the earliest arrival."
2. **Test/trace evidence:** "`test_ships_dock_in_arrival_order` enqueues A, B, C and asserts the dock order is A, B, C; the trace shows the reverse for a stack." (link the test file)
3. **Rationale + World Bible:** "A raw `list` would let me `insert(0, ...)` and let a ship cut in, which my world forbids; the queue exposes only operations the harbor allows. World Bible: added the dock queue; debt: priority ships not modeled."

## Three likely student questions

**Q1. Why not just use a list? It already has `append` and `pop`.**
It does, and under the hood `TicketLine` uses one. The difference is what clients are *allowed* to do.
A list permits `insert`, `sort`, and `items[3]`, which break the line's rules. The class exposes only the
operations your world's process has.

**Q2. Should `dequeue` on an empty line return `None` instead of raising?**
Either is a legitimate design, but you must *choose* and test it. `None` is easy to ignore and the
mistake shows up later somewhere else. Raising stops at the cause. For the gate, state which you chose and
test it.

**Q3. My world doesn't have a queue or stack. What do I do?**
Look at Week 3's flow again: anything that waits (queue), anything undone or backtracked (stack), anything
ordered that you add to and remove from in the middle (list ADT). If a thing really never piles up, pick
the nearest honest one and say so in the rationale. Don't invent a queue just to have one.
