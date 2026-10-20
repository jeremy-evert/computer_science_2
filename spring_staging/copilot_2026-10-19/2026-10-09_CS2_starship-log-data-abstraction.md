**Starship Mission Log**

CS2 Week 08 -- World-Fit Data Abstraction with SQLite, Python, and TDD

*Durable artifact \| 2026-10-09 \| Jeremy Evert, SWOSU \| Built with Microsoft Copilot*

1\. What We Set Out To Do

Request: run a Week 8 data abstraction project in a new way. Use a starship log as the world, walk through a SQLite-backed project, then use Python and test-driven development to build and use an example. The worked kitchen example (TicketLine queue + UndoStack) was the model to beat.

The Week 8 Gate (S05) in brief

- **Learning:** choose a real List ADT, stack, or queue flow from your world's actual process, and explain why that abstraction is more honest than Python list syntax alone.

- **Build:** state the client operations and demonstrate FIFO/LIFO or list behavior with a small automated test or trace.

- **Evidence:** one concise World Bible entry -- what changed, evidence used, remaining debt.

- **Carries forward:** Week 9 traces a real lookup or ordering operation over the world's state.

| **Rubric criterion**                     | **Points** | **Meets expectation**                                       |
|------------------------------------------|------------|-------------------------------------------------------------|
| World-fit abstraction                    | 8          | Structure is meaningful for the world, not arbitrary        |
| Correct operation trace                  | 7          | Test/trace demonstrates the claimed FIFO/LIFO/list behavior |
| Client-operation reasoning / World Bible | 6          | Explains why the abstraction beats raw list syntax          |
| AI accountability                        | 4          | Proposal, diff, independent test, reasoning, accept/reject  |
| Total                                    | 25         |                                                             |

2\. The World Fit

Two things genuinely pile up aboard the starship, and they need opposite structures:

| **Flow**          | **Structure** | **Why it fits**                                                        |
|-------------------|---------------|------------------------------------------------------------------------|
| Incoming missions | Queue (FIFO)  | Oldest mission launches first; nobody jumps ahead of a pending mission |
| Red alerts        | Stack (LIFO)  | The newest crisis is on top and is cleared first                       |

**Client operations.** MissionQueue: enqueue, dequeue, peek, is_empty, size. AlertStack: push, pop, peek, is_empty, size. Nothing else. No indexing, no inserting in the middle, no sorting, no SQL.

3\. The SQLite Walkthrough

The twist versus the kitchen example: instead of a private Python list, each class hides a SQLite table. The client contract is identical; only the storage engine changed. SQLite ships with Python (import sqlite3), so nothing extra is installed.

Step by step

1.  **Connect.** sqlite3.connect(':memory:') makes a throwaway in-RAM database (perfect for tests). Pass 'starship.db' instead to keep data on disk.

2.  **Create the table.** CREATE TABLE IF NOT EXISTS missions (id INTEGER PRIMARY KEY AUTOINCREMENT, mission TEXT NOT NULL). The auto-increment id records arrival order permanently.

3.  **Insert = enqueue/push.** INSERT INTO missions (mission) VALUES (?). The ? placeholder keeps data separate from SQL (no injection).

4.  **Read the front or top.** Queue: SELECT ... ORDER BY id ASC LIMIT 1 (oldest). Stack: SELECT ... ORDER BY id DESC LIMIT 1 (newest). Same table shape, opposite read direction -- that one word IS the FIFO/LIFO difference.

5.  **Delete what you took.** DELETE FROM missions WHERE id = ?, then commit().

6.  **Count.** SELECT COUNT(\*) drives size() and is_empty().

7.  **Close.** close() releases the connection. Reopening a file-backed database shows the queue survived -- something a plain list cannot do.

4\. The TDD Red/Green Story

Each step was written as a failing test first, then the smallest code to turn it green.

| **Step** | **Test**                               | **Expected red**    | **Smallest green fix**                                 |
|----------|----------------------------------------|---------------------|--------------------------------------------------------|
| 1        | New queue is empty, size 0             | ModuleNotFoundError | MissionQueue.\_\_init\_\_ creates table; is_empty/size |
| 2        | Missions launch in arrival order       | No enqueue/dequeue  | INSERT + SELECT ORDER BY id ASC + DELETE               |
| 3        | peek shows next, size unchanged        | No peek             | SELECT LIMIT 1 without DELETE                          |
| 4        | dequeue/peek on empty raise EmptyError | Wrong error / None  | if row is None: raise EmptyError                       |
| 5        | size tracks enqueue/dequeue cycles     | Wrong count         | SELECT COUNT(\*)                                       |
| 6        | New alert stack is empty               | No AlertStack       | Same shape, alerts table                               |
| 7        | Newest alert cleared first             | Wrong order         | ORDER BY id DESC                                       |
| 8        | pop/peek on empty stack raise          | Wrong error         | Explicit EmptyError                                    |
| 9        | Same input, opposite orders            | No trace_same_input | Feed both, drain both                                  |
| 10-11    | No SQL/indexing leaks to clients       | Passes already      | None -- documents the contract                         |

**Design choice at step 4:** returning None on an empty queue lets the bug travel silently and surface somewhere else. Raising EmptyError stops at the cause. Either design is legitimate, but you must choose it and test it.

5\. Evidence

pytest output (python -m pytest -v)

test_starship_log.py::test_new_mission_queue_is_empty PASSED \[ 9%\]

test_starship_log.py::test_mission_queue_serves_oldest_mission_first PASSED \[ 18%\]

test_starship_log.py::test_peek_shows_next_mission_without_removing PASSED \[ 27%\]

test_starship_log.py::test_dequeue_and_peek_on_empty_queue_raise_EmptyError PASSED \[ 36%\]

test_starship_log.py::test_size_tracks_enqueue_and_dequeue PASSED \[ 45%\]

test_starship_log.py::test_new_alert_stack_is_empty PASSED \[ 54%\]

test_starship_log.py::test_alert_stack_clears_newest_alert_first PASSED \[ 63%\]

test_starship_log.py::test_pop_and_peek_on_empty_stack_raise_EmptyError PASSED \[ 72%\]

test_starship_log.py::test_same_input_comes_out_in_opposite_orders PASSED \[ 81%\]

test_starship_log.py::test_clients_cannot_reach_the_sql_table PASSED \[ 90%\]

test_starship_log.py::test_clients_cannot_reach_the_alert_table PASSED \[100%\]

============================== 11 passed in 0.21s ==============================

Trace output (python starship_log.py)

Missions received: Scan Nebula-7, Rescue Beacon Alpha, Dock at Starbase 9

Queue launch order (FIFO): Scan Nebula-7, Rescue Beacon Alpha, Dock at Starbase 9

Alert clear order (LIFO): Dock at Starbase 9, Rescue Beacon Alpha, Scan Nebula-7

Same input. Opposite order. The structure decides.

Persisted 2 missions to 'starship.db'.

Peek at the queue: 'Refuel at Deep Space 4'

Launched: 'Refuel at Deep Space 4'

Missions remaining: 1

Reopening the database -- does the mission survive?

Next mission: 'Investigate anomaly near Rigel'

Yes. SQLite persisted the queue across connections.

**The lesson in one line:** same input, opposite order. The structure decides, not the data.

6\. Why This Beats Raw list Syntax

A Python list can do everything, so it says nothing about the process. With a list called missions, a client could:

- missions\[2\] -- grab the third mission, but a mission queue has no 'third place' you can reach into

- missions.insert(0, 'VIP') -- cut in line, which the bridge forbids

- missions.pop() -- take the NEWEST mission, accidentally making the queue a stack

- missions.sort() -- reorder arrival history

MissionQueue makes a promise: a mission enters at the back and leaves from the front, and nothing else is allowed. The operations are the process. And because the interface is separate from the implementation, we swapped a list for SQLite with zero client-code changes -- proof that the abstraction is real.

7\. World Bible Entry (paste-ready)

**Week 8 -- Mission Queue & Alert Stack**

- **What changed:** Added MissionQueue (FIFO) and AlertStack (LIFO), both backed by SQLite via the standard-library sqlite3 module. Clients see only enqueue/dequeue/push/pop/peek/is_empty/size; no SQL is exposed.

- **Evidence:** python -m pytest -v -\> 11/11 passed. python starship_log.py traces the same input in opposite orders and shows a file-backed queue surviving a reconnect.

- **Why better than raw list:** a list allows insert(0, ...), sort(), and indexing, all of which violate a mission queue's rules. The classes enforce the contract at the API.

- **Remaining debt:** priority missions not modeled; concurrent multi-ship access not tested.

8\. Sample Three-Line Gate Submission

1.  **Flow and operations:** On my starship, missions wait to launch: enqueue(mission), dequeue(), peek(), is_empty(), size(); the captain launches the earliest received mission.

2.  **Test/trace evidence:** test_mission_queue_serves_oldest_mission_first enqueues three missions and asserts they launch in the same order; the trace shows the reverse order for the alert stack.

3.  **Rationale + World Bible:** a raw list would let a mission cut in with insert(0, ...), which my world forbids; the queue exposes only operations the bridge allows. Debt: priority missions not modeled.

9\. AI Accountability Note

| **Element**      | **What happened**                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------------------------|
| Proposal         | Copilot proposed a starship world with two flows (mission queue, alert stack) and a SQLite backing as the new twist. |
| Diff             | Two new files: starship_log.py and test_starship_log.py, modeled on the kitchen walkthrough.                         |
| Independent test | pytest run in a clean environment: 11 passed. Trace script run and output captured above.                            |
| Reasoning        | ORDER BY id ASC vs DESC is the entire FIFO/LIFO difference; tests 10-11 prove no SQL leaks.                          |
| Accept/reject    | Instructor reviews and runs the suite locally before accepting into the course repo.                                 |

10\. How To Run

\# from the folder holding both files

python -m pytest -v \# 11 tests, all green

python starship_log.py \# trace + persistence demo

\# if pytest is missing:

python -m pip install pytest

Appendix A. starship_log.py

"""

Starship Mission Log -- World-Fit Data Abstraction

CS2 Week 8

Two real flows aboard a starship:

MissionQueue -- incoming missions wait in arrival order; oldest launches first (FIFO).

AlertStack -- red alerts pile up; the most recent is cleared first (LIFO).

TWIST vs. the kitchen example: both structures are backed by SQLite.

The client code never touches SQL. It only calls enqueue/dequeue/push/pop.

Swapping the storage engine (list -\> SQLite -\> anything else) never changes the contract.

Usage

-----

python starship_log.py \# trace: same input, opposite order

python -m pytest -v \# full TDD suite

"""

import sqlite3

class EmptyError(Exception):

"""Raised when you try to take something from an empty structure."""

class MissionQueue:

"""

Incoming starship missions wait here in arrival order.

The earliest-received mission launches first (FIFO).

Client operations: enqueue, dequeue, peek, is_empty, size.

What clients may NOT do: index into the middle, reorder, or touch SQL.

Default db_path=':memory:' keeps everything in RAM -- great for tests.

Pass a file path ('starship.db') to persist the log across program runs.

"""

def \_\_init\_\_(self, db_path: str = ":memory:"):

self.\_conn = sqlite3.connect(db_path)

self.\_conn.execute(

"""

CREATE TABLE IF NOT EXISTS missions (

id INTEGER PRIMARY KEY AUTOINCREMENT,

mission TEXT NOT NULL

)

"""

)

self.\_conn.commit()

def enqueue(self, mission: str) -\> None:

"""Add a new mission to the back of the queue."""

self.\_conn.execute("INSERT INTO missions (mission) VALUES (?)", (mission,))

self.\_conn.commit()

def dequeue(self) -\> str:

"""Remove and return the oldest mission. Raises EmptyError if empty."""

row = self.\_conn.execute(

"SELECT id, mission FROM missions ORDER BY id ASC LIMIT 1"

).fetchone()

if row is None:

raise EmptyError("no missions in queue -- the ship has nothing to do")

self.\_conn.execute("DELETE FROM missions WHERE id = ?", (row\[0\],))

self.\_conn.commit()

return row\[1\]

def peek(self) -\> str:

"""Return the oldest mission without removing it."""

row = self.\_conn.execute(

"SELECT mission FROM missions ORDER BY id ASC LIMIT 1"

).fetchone()

if row is None:

raise EmptyError("no missions in queue -- nothing to peek at")

return row\[0\]

def is_empty(self) -\> bool:

return self.size() == 0

def size(self) -\> int:

return self.\_conn.execute("SELECT COUNT(\*) FROM missions").fetchone()\[0\]

def close(self) -\> None:

self.\_conn.close()

class AlertStack:

"""

Red alerts pile up here. The most recently raised alert is cleared first (LIFO).

Client operations: push, pop, peek, is_empty, size.

LIFO comes from ORDER BY id DESC (highest id = newest row = top of stack).

"""

def \_\_init\_\_(self, db_path: str = ":memory:"):

self.\_conn = sqlite3.connect(db_path)

self.\_conn.execute(

"""

CREATE TABLE IF NOT EXISTS alerts (

id INTEGER PRIMARY KEY AUTOINCREMENT,

alert TEXT NOT NULL

)

"""

)

self.\_conn.commit()

def push(self, alert: str) -\> None:

self.\_conn.execute("INSERT INTO alerts (alert) VALUES (?)", (alert,))

self.\_conn.commit()

def pop(self) -\> str:

row = self.\_conn.execute(

"SELECT id, alert FROM alerts ORDER BY id DESC LIMIT 1"

).fetchone()

if row is None:

raise EmptyError("no alerts to clear -- all quiet on the bridge")

self.\_conn.execute("DELETE FROM alerts WHERE id = ?", (row\[0\],))

self.\_conn.commit()

return row\[1\]

def peek(self) -\> str:

row = self.\_conn.execute(

"SELECT alert FROM alerts ORDER BY id DESC LIMIT 1"

).fetchone()

if row is None:

raise EmptyError("no alerts to clear -- all quiet on the bridge")

return row\[0\]

def is_empty(self) -\> bool:

return self.size() == 0

def size(self) -\> int:

return self.\_conn.execute("SELECT COUNT(\*) FROM alerts").fetchone()\[0\]

def close(self) -\> None:

self.\_conn.close()

def trace_same_input(items):

"""Same input. Opposite output. The STRUCTURE decides the order, not the data."""

queue, stack = MissionQueue(), AlertStack()

for item in items:

queue.enqueue(item)

stack.push(item)

fifo_order, lifo_order = \[\], \[\]

while not queue.is_empty():

fifo_order.append(queue.dequeue())

while not stack.is_empty():

lifo_order.append(stack.pop())

queue.close()

stack.close()

return fifo_order, lifo_order

if \_\_name\_\_ == "\_\_main\_\_":

import os

missions = \["Scan Nebula-7", "Rescue Beacon Alpha", "Dock at Starbase 9"\]

fifo, lifo = trace_same_input(missions)

print("Missions received: ", ", ".join(missions))

print("Queue launch order (FIFO):", ", ".join(fifo))

print("Alert clear order (LIFO):", ", ".join(lifo))

print()

print("Same input. Opposite order. The structure decides.")

print()

db_file = "starship.db"

if os.path.exists(db_file):

os.remove(db_file)

log = MissionQueue(db_path=db_file)

log.enqueue("Refuel at Deep Space 4")

log.enqueue("Investigate anomaly near Rigel")

print(f"Persisted {log.size()} missions to '{db_file}'.")

print(f"Peek at the queue: '{log.peek()}'")

print(f"Launched: '{log.dequeue()}'")

print(f"Missions remaining: {log.size()}")

log.close()

print()

print("Reopening the database -- does the mission survive?")

log2 = MissionQueue(db_path=db_file)

print(f" Next mission: '{log2.dequeue()}'")

print(" Yes. SQLite persisted the queue across connections.")

log2.close()

os.remove(db_file)

Appendix B. test_starship_log.py

"""

TDD for starship_log.py -- written in teaching order.

Each numbered step was RED before its matching code existed.

Run: python -m pytest -v

"""

import pytest

from starship_log import EmptyError, MissionQueue, AlertStack, trace_same_input

\# Step 1: a brand-new mission queue is empty

def test_new_mission_queue_is_empty():

q = MissionQueue()

assert q.is_empty()

assert q.size() == 0

q.close()

\# Step 2: missions launch in the order they arrived (FIFO)

def test_mission_queue_serves_oldest_mission_first():

q = MissionQueue()

q.enqueue("Scan Nebula-7")

q.enqueue("Rescue Beacon Alpha")

q.enqueue("Dock at Starbase 9")

assert q.dequeue() == "Scan Nebula-7"

assert q.dequeue() == "Rescue Beacon Alpha"

assert q.dequeue() == "Dock at Starbase 9"

q.close()

\# Step 3: peek shows the next mission without launching it

def test_peek_shows_next_mission_without_removing():

q = MissionQueue()

q.enqueue("Scan Nebula-7")

assert q.peek() == "Scan Nebula-7"

assert q.size() == 1

q.close()

\# Step 4: empty queue fails loudly instead of returning None

def test_dequeue_and_peek_on_empty_queue_raise_EmptyError():

q = MissionQueue()

with pytest.raises(EmptyError):

q.dequeue()

with pytest.raises(EmptyError):

q.peek()

q.close()

\# Step 5: size tracks enqueue / dequeue cycles

def test_size_tracks_enqueue_and_dequeue():

q = MissionQueue()

q.enqueue("Mission A")

q.enqueue("Mission B")

assert q.size() == 2

q.dequeue()

assert q.size() == 1

q.dequeue()

assert q.is_empty()

q.close()

\# Step 6: a brand-new alert stack is empty

def test_new_alert_stack_is_empty():

stack = AlertStack()

assert stack.is_empty()

assert stack.size() == 0

stack.close()

\# Step 7: the most recently raised alert is cleared first (LIFO)

def test_alert_stack_clears_newest_alert_first():

stack = AlertStack()

stack.push("Hull breach in sector 4")

stack.push("Warp core overheating")

stack.push("Shields at 12 percent")

assert stack.peek() == "Shields at 12 percent"

assert stack.pop() == "Shields at 12 percent"

assert stack.pop() == "Warp core overheating"

assert stack.pop() == "Hull breach in sector 4"

assert stack.is_empty()

stack.close()

\# Step 8: empty stack fails loudly

def test_pop_and_peek_on_empty_stack_raise_EmptyError():

stack = AlertStack()

with pytest.raises(EmptyError):

stack.pop()

with pytest.raises(EmptyError):

stack.peek()

stack.close()

\# Step 9: same input, opposite order -- the whole lesson

def test_same_input_comes_out_in_opposite_orders():

missions = \["Scan Nebula-7", "Rescue Beacon Alpha", "Dock at Starbase 9"\]

fifo, lifo = trace_same_input(missions)

assert fifo == \["Scan Nebula-7", "Rescue Beacon Alpha", "Dock at Starbase 9"\]

assert lifo == \["Dock at Starbase 9", "Rescue Beacon Alpha", "Scan Nebula-7"\]

\# Steps 10-11: the SQL table must not leak to clients

def test_clients_cannot_reach_the_sql_table():

q = MissionQueue()

q.enqueue("Scan Nebula-7")

for name in ("execute", "insert", "cursor"):

assert not hasattr(q, name)

with pytest.raises(TypeError):

\_ = q\[0\]

q.close()

def test_clients_cannot_reach_the_alert_table():

stack = AlertStack()

stack.push("Hull breach in sector 4")

for name in ("execute", "insert", "cursor"):

assert not hasattr(stack, name)

with pytest.raises(TypeError):

\_ = stack\[0\]

stack.close()
