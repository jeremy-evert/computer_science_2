Conversation Archive

**Topic:** Data management with classes — queues (FIFO) and stacks (LIFO) as world-fit data abstractions, tied to *The Pragmatic Programmer*, Chapter 1

**Date:** 2026-10-07

**Course:** CS2

**Summary:** This conversation connects Chapter 1 of Hunt and Thomas's *The Pragmatic Programmer* ("A Pragmatic Philosophy") to the CS2 Week 8 lesson on world-fit data abstraction. Jeremy supplied the Week 8 quick answers and a kitchen-themed walkthrough (order tickets as a FIFO queue, cook actions as a LIFO undo stack) with the full kitchen_flow.py and test_kitchen_flow.py code. Copilot stitched these into one idea: choose a structure that only permits what the real process allows, fail loudly at boundaries, prove behavior with tests, and name design debt honestly. Jeremy then asked for a one-sentence summary of the goal ("data management with classes applied to our imaginary worlds") and how to phrase it for an LLM; Copilot produced a fill-in-the-blank student prompt. The final turns are requests to archive the conversation as a Word document.

*Redaction check: no student names, grades, student submissions, or student email content appear in this conversation, so nothing was replaced with "\[student info removed\]". The "lighthouse world" / "harbor master" lines are an instructor-written sample of what a gate submission looks like, not a real student submission.*

*Transcript notes: (1) Jeremy's first message was pasted as rich text (HTML). It is reproduced here as plain formatted text; the step table, which arrived flattened by the paste, is shown as a table with the same cells. Original spellings in Jeremy's messages are kept. (2) Copilot's replies to the two earlier archive requests each contained a full copy of turns 1–4. Those embedded copies are NOT repeated here, because they duplicate turns 1–4 word for word and would triple the document length; every other sentence of those replies is included. (3) Copilot's earlier statements that it could not create a .docx file were incorrect; this file is the correction.*

Transcript

Jeremy: (Turn 1)

> 1\. Stitch all of this together into a coherent thought.
>
> 3\. Primary source: Andrew Hunt and David Thomas, *The Pragmatic Programmer: From Journeyman to Master*, Chapter 1, "A Pragmatic Philosophy"

what can you tell us are the most improtant things for data management and

Quick answers

> 1\. **What do I choose?** A real List ADT, stack, or queue flow from your world's actual process -- one where things pile up, wait in line, or are handled in order.
>
> 2\. **What do I have to show?** The client operations, and list behavior or LIFO/FIFO demonstrated with a small automated test or trace, continuing the testing habit from Weeks 3-6.
>
> 3\. **What do I have to explain?** Why this abstraction fits your world better than Python list syntax alone.
>
> 4\. **What do I keep?** One concise World Bible entry: what changed, the evidence you used, and any remaining debt.
>
> 5\. **Where is my world's flow from?** Your world's real flow from Week 3 (Week 3 overview: https://swosu.instructure.com/courses/74031/pages/cs2-week-03-overview-found-your-world-slash-world-bible-v0-dot-1).

Week 8 Walkthrough -- Kitchen Tickets (Queue) and Undo (Stack)

Week 8 — World-Fit Data Abstraction, worked example (kitchen)

**Target (the Week 8 plan, S05):** choose a real List ADT / stack / queue flow from the world's actual process, state the client operations, demonstrate FIFO/LIFO with a small test/trace, and explain why the abstraction is more honest than Python list syntax alone.

**The world:** the Week 6 kitchen. Two things really pile up in it:

- **Order tickets wait in a line.** The oldest ticket gets cooked first. → queue (FIFO)

- **The cook's actions pile up so they can be undone.** The newest action is undone first. → stack (LIFO)

Files: kitchen_flow.py (about 95 lines), test_kitchen_flow.py (8 tests). Run from this directory: python -m pytest -v and python kitchen_flow.py (the trace). Pytest was used here, so pip install pytest if a student machine lacks it.

Walkthrough (~20 minutes)

> 1\. The world and the operations (3 min)

Say: "A ticket line has four things a client may do: **enqueue** a ticket, **dequeue** the next one, **peek** at the next one, ask **is_empty** / **size**. That's the whole contract. Notice what's not on the list: nobody reaches into the middle of a ticket line." Write the operations on the board before any code. Same for the undo stack: **push, pop, peek, is_empty, size**.

> 2\. Tests first, small red/green steps (10 min)

Open test_kitchen_flow.py empty. Add one test at a time, run it, watch it go red (import error or missing method), then write the dumbest code that makes it green. The file is in teaching order:

| **Step** | **Test**                                    | **Expected red (when run live)**            | **Smallest fix**                                       |
|----------|---------------------------------------------|---------------------------------------------|--------------------------------------------------------|
| 1        | new line is_empty(), size() == 0            | no kitchen_flow module                      | TicketLine with \_\_init\_\_, is_empty, size           |
| 2        | soup enqueued before burger comes out first | no enqueue/dequeue                          | append and pop(0)                                      |
| 3        | peek shows the next ticket, size unchanged  | no peek                                     | return first item                                      |
| 4        | dequeue/peek on empty raise EmptyError      | IndexError or wrong error type              | explicit check, raise EmptyError("no tickets waiting") |
| 5        | undo stack undoes the newest action first   | no UndoStack                                | push, pop, peek, is_empty, size                        |
| 6        | same input, opposite order                  | no trace_same_input                         | feed both, drain both                                  |
| 7        | clients can't index or insert               | (passes already, it documents the contract) | none                                                   |

Say at step 4: "What should a real kitchen do with *dequeue* on an empty line? There is no ticket. We choose to fail loudly with our own error, not return None and let the bug travel."

> 3\. The LIFO vs FIFO moment (2 min)

Run python kitchen_flow.py:

> in: soup, burger, pizza
>
> FIFO out: soup, burger, pizza
>
> LIFO out: pizza, burger, soup

Same three items in, opposite order out. The *structure* decides the order, not the data.

> 4\. Why the abstraction is more honest than list (5 min)

Open a Python prompt and do this live:

> tickets = \["soup", "burger", "pizza"\]
>
> tickets\[2\] \# 'pizza' -- the line has no "third place" you can grab
>
> tickets.insert(0, "VIP") \# cutting in line; a real kitchen forbids this
>
> tickets.pop() \# takes the NEWEST ticket: stack behavior on what we called a line
>
> tickets.sort() \# reorders the line; tickets must stay in arrival order

Then:

> from kitchen_flow import TicketLine
>
> line = TicketLine()
>
> line.insert(0, "VIP") \# AttributeError
>
> line\[2\] \# TypeError

Say: "list can do everything, so it says nothing. It can't tell you whether this is a line or a pile. TicketLine makes the promise: a ticket enters at the back and leaves from the front, and nothing else is allowed. The operations *are* the process." Bonus honesty: pop(0) on a list is slow for huge lines (collections.deque fixes that), and that is a good reason the interface is separate from the implementation. We could swap the inside and no client code would change.

What a student gate submission looks like (3 lines)

Tie each line to the gate's criteria (the Week 8 gate):

> 1\. **Flow and operations:** "In my lighthouse world, ships wait for the dock: enqueue(ship), dequeue(), peek(), is_empty(), size(); the harbor master serves the earliest arrival."
>
> 2\. **Test/trace evidence:** "test_ships_dock_in_arrival_order enqueues A, B, C and asserts the dock order is A, B, C; the trace shows the reverse for a stack." (link the test file)
>
> 3\. **Rationale + World Bible:** "A raw list would let me insert(0, ...) and let a ship cut in, which my world forbids; the queue exposes only operations the harbor allows. World Bible: added the dock queue; debt: priority ships not modeled."

Three likely student questions

**Q1. Why not just use a list? It already has append and pop.** It does, and under the hood TicketLine uses one. The difference is what clients are *allowed* to do. A list permits insert, sort, and items\[3\], which break the line's rules. The class exposes only the operations your world's process has.

**Q2. Should dequeue on an empty line return None instead of raising?** Either is a legitimate design, but you must *choose* and test it. None is easy to ignore and the mistake shows up later somewhere else. Raising stops at the cause. For the gate, state which you chose and test it.

**Q3. My world doesn't have a queue or stack. What do I do?** Look at Week 3's flow again: anything that waits (queue), anything undone or backtracked (stack), anything ordered that you add to and remove from in the middle (list ADT). If a thing really never piles up, pick the nearest honest one and say so in the rationale. Don't invent a queue just to have one.

The code (copy into files to run)

Save as kitchen_flow.py and test_kitchen_flow.py in one folder, then run python -m pytest -v and python kitchen_flow.py.

kitchen_flow.py

> """Kitchen flow: a ticket line (queue, FIFO) and an undo stack (LIFO).
>
> Each class exposes only the operations the kitchen's real process allows.
>
> The Python list inside is a private detail; clients never touch it.
>
> """
>
> class EmptyError(Exception):
>
> """Raised when you take or look at something that is not there."""
>
> class TicketLine:
>
> """Order tickets wait here. The oldest ticket is cooked first (FIFO)."""
>
> def \_\_init\_\_(self):
>
> self.\_tickets = \[\]
>
> def enqueue(self, ticket):
>
> self.\_tickets.append(ticket)
>
> def dequeue(self):
>
> if not self.\_tickets:
>
> raise EmptyError("no tickets waiting")
>
> return self.\_tickets.pop(0)
>
> def peek(self):
>
> if not self.\_tickets:
>
> raise EmptyError("no tickets waiting")
>
> return self.\_tickets\[0\]
>
> def is_empty(self):
>
> return not self.\_tickets
>
> def size(self):
>
> return len(self.\_tickets)
>
> class UndoStack:
>
> """Cook's actions pile up here. The newest action is undone first (LIFO)."""
>
> def \_\_init\_\_(self):
>
> self.\_actions = \[\]
>
> def push(self, action):
>
> self.\_actions.append(action)
>
> def pop(self):
>
> if not self.\_actions:
>
> raise EmptyError("nothing to undo")
>
> return self.\_actions.pop()
>
> def peek(self):
>
> if not self.\_actions:
>
> raise EmptyError("nothing to undo")
>
> return self.\_actions\[-1\]
>
> def is_empty(self):
>
> return not self.\_actions
>
> def size(self):
>
> return len(self.\_actions)
>
> def trace_same_input(items):
>
> """Feed the same items to both structures; return the order each gives back."""
>
> line, stack = TicketLine(), UndoStack()
>
> for item in items:
>
> line.enqueue(item)
>
> stack.push(item)
>
> fifo_order, lifo_order = \[\], \[\]
>
> while not line.is_empty():
>
> fifo_order.append(line.dequeue())
>
> while not stack.is_empty():
>
> lifo_order.append(stack.pop())
>
> return fifo_order, lifo_order
>
> if \_\_name\_\_ == "\_\_main\_\_":
>
> fifo, lifo = trace_same_input(\["soup", "burger", "pizza"\])
>
> print("in: soup, burger, pizza")
>
> print("FIFO out:", ", ".join(fifo))
>
> print("LIFO out:", ", ".join(lifo))

test_kitchen_flow.py

> """Written in teaching order. Each step was red before its code existed."""
>
> import pytest
>
> from kitchen_flow import EmptyError, TicketLine, UndoStack, trace_same_input
>
> \# Step 1: a new ticket line is empty.
>
> def test_new_ticket_line_is_empty():
>
> line = TicketLine()
>
> assert line.is_empty()
>
> assert line.size() == 0
>
> \# Step 2: first in, first out.
>
> def test_ticket_line_serves_oldest_ticket_first():
>
> line = TicketLine()
>
> line.enqueue("soup")
>
> line.enqueue("burger")
>
> assert line.dequeue() == "soup"
>
> assert line.dequeue() == "burger"
>
> \# Step 3: peek looks without taking.
>
> def test_peek_shows_next_ticket_without_removing_it():
>
> line = TicketLine()
>
> line.enqueue("soup")
>
> assert line.peek() == "soup"
>
> assert line.size() == 1
>
> \# Step 4: the real process has no answer for an empty line, so it says so.
>
> def test_dequeue_and_peek_on_empty_line_raise():
>
> line = TicketLine()
>
> with pytest.raises(EmptyError):
>
> line.dequeue()
>
> with pytest.raises(EmptyError):
>
> line.peek()
>
> \# Step 5: the undo stack is the opposite: last in, first out.
>
> def test_undo_stack_undoes_newest_action_first():
>
> undo = UndoStack()
>
> undo.push("add salt")
>
> undo.push("add pepper")
>
> assert undo.peek() == "add pepper"
>
> assert undo.pop() == "add pepper"
>
> assert undo.pop() == "add salt"
>
> assert undo.is_empty()
>
> def test_pop_and_peek_on_empty_stack_raise():
>
> undo = UndoStack()
>
> with pytest.raises(EmptyError):
>
> undo.pop()
>
> with pytest.raises(EmptyError):
>
> undo.peek()
>
> \# Step 6: same input, opposite order. This is the whole lesson.
>
> def test_same_input_comes_out_in_opposite_orders():
>
> fifo, lifo = trace_same_input(\["soup", "burger", "pizza"\])
>
> assert fifo == \["soup", "burger", "pizza"\]
>
> assert lifo == \["pizza", "burger", "soup"\]
>
> \# Step 7: the abstraction does not leak its list.
>
> def test_clients_cannot_reach_into_the_middle():
>
> line = TicketLine()
>
> line.enqueue("soup")
>
> assert not hasattr(line, "insert")
>
> with pytest.raises(TypeError):
>
> line\[0\]

Copilot: (Turn 2)

The Thread That Runs Through Everything

Here's how it all stitches together.

The Pragmatic Philosopher Walks Into a Kitchen

Hunt and Thomas open *The Pragmatic Programmer* with a deceptively simple idea: **a craftsperson takes responsibility for the honesty of their work.** Not just "does it run," but "does it tell the truth?" That one idea is the engine underneath Week 8's entire data abstraction lesson.

When a student uses a raw Python list to model a ticket queue, the code *runs*. But it **lies.** It implies the kitchen can do tickets\[2\], tickets.sort(), and tickets.insert(0, "VIP"). None of those operations exist in a real kitchen's process. They're broken windows — left open, they invite bugs that show up three functions away from where the mistake was made.

TicketLine is the pragmatic fix. It doesn't just store tickets; it **tells the truth about what the kitchen allows.** The operations — enqueue, dequeue, peek, is_empty, size — aren't restrictions. They *are* the process, made executable.

The Most Important Things for Data Management (CS2 Frame)

These aren't abstract rules. Each one appears concretely in the kitchen walkthrough:

**1. Match the structure to the real-world process — not to what's convenient.**  
A list can do everything, so it says nothing. Choosing a queue means making a claim: *this thing is FIFO, and that claim is true.* The structure is a commitment to the world.

**2. Name only the operations the process allows.**  
Every method you expose is a promise. Every operation you hide is protection against future mistakes. TicketLine has no insert because a ticket line has no insert. If the client can't do it, don't give them the method.

**3. Fail loudly at the boundary — don't let the bug travel.**  
When dequeue hits an empty line, EmptyError("no tickets waiting") fires immediately. Returning None and moving on is the silent lie. The Pragmatic Programmer calls it broken window thinking: the bug just shows up somewhere else, harder to trace. Raise at the source.

**4. The interface outlives the implementation.**  
TicketLine uses pop(0) today. For large lines, that's slow. Tomorrow you can swap the internal list for a collections.deque and call .popleft() instead — and zero client code changes. The contract is stable; the internals are negotiable. This is *why* the class wraps the list at all.

**5. Write the tests before the code tells you what they should say.**  
The teaching order in test_kitchen_flow.py is the lesson itself. Red → small fix → green → next test. Each red test is honest evidence that the feature doesn't exist yet. Each green test is a receipt that it now does. This is Pragmatic Programmer thinking: **evidence over assertion.**

**6. Name your design debt explicitly — and stop there.**  
"Priority ships not modeled" is not a failure. It's honesty about scope. The Pragmatic Programmer calls this *good enough software*: know what's done, know what isn't, and say so in writing. The World Bible entry is where that honesty lives.

Why the FIFO/LIFO Moment is the Whole Lesson

> in: soup, burger, pizza
>
> FIFO out: soup, burger, pizza
>
> LIFO out: pizza, burger, soup

Same three items. Same order in. **Opposite order out.** The structure decides — not the data, not the programmer's intent at dequeue time. This is the pragmatic payoff: the decision about how data flows gets made *once*, at design time, by choosing the right abstraction. Everywhere else in the codebase, the process is already enforced.

The Quick Answers, Unified

| **Gate question**                 | **The pragmatic answer**                                               |
|-----------------------------------|------------------------------------------------------------------------|
| **What do I choose?**             | The structure that tells the truth about how things move in your world |
| **What do I show?**               | Client operations + a test that proves FIFO or LIFO actually holds     |
| **What do I explain?**            | Why list syntax would permit operations your world forbids             |
| **What do I keep?**               | A World Bible entry: what changed, the evidence, and the named debt    |
| **Where does my flow come from?** | Week 3 — go look at what piles up, waits, or gets undone               |

The Single Sentence Version

> **Choose a structure that can only do what the real process allows, fail loudly when that process breaks, write evidence that it works, and name what you haven't built yet.**

That's The Pragmatic Programmer's Chapter 1 philosophy. That's Week 8. They're the same thought.

Jeremy: (Turn 3)

summarize this statment:

we want to see how to do data managment with classes and we want to apply that to a real world example from our imaginary worlds.

How do we ask this question to our llm?

Copilot: (Turn 4)

The Summary

> **Use a class to model how data moves through a real process in your world — and let the class enforce the rules of that process.**

The LLM Prompt

Here's a drop-in prompt your students can use:

> I am building a fictional world for a CS2 class. My world is **\[describe your world in 1–2 sentences\]**.
>
> Somewhere in my world, things **pile up, wait in line, or need to be undone**. That flow is: **\[describe the flow\]**.
>
> Help me model this using a Python class that:

- exposes only the operations my world's real process allows

- demonstrates either **FIFO (queue)** or **LIFO (stack)** behavior

- raises a clear error when the process breaks (like dequeuing from an empty line)

- includes a small test or trace that proves the order is correct

> Explain *why* a raw Python list would be dishonest here, and what the class's operations say about my world.

Why This Prompt Works

| **Prompt piece**          | **What it does**                                                    |
|---------------------------|---------------------------------------------------------------------|
| World description         | Anchors the LLM in *your* context, not a generic example            |
| "pile up / wait / undone" | Forces the student to identify the real flow before asking for code |
| Only allowed operations   | Prevents the LLM from just handing back a list wrapper              |
| Error behavior            | Gets honest failure handling, not silent None returns               |
| "why not a list"          | Makes the LLM justify the abstraction — the actual lesson           |

The student fills in the blanks **before** they prompt. That's the real work.

Jeremy: (Turn 5)

I want to archive this entire conversation as a Word document. Please create a Word (.docx) file now.

What to include

> 1\. The full conversation history, as complete and verbatim as you can manage. This is a transcript, not a summary. Include every one of my messages and every one of your replies, in order, labeled "Jeremy:" and "Copilot:".
>
> 2\. Keep all code blocks, commands, file names, tables and lists exactly as they appeared, with code in a monospaced font.
>
> 3\. If something is too long to fit, keep it anyway, and don't paraphrase or shorten it. If you truly cannot include some part, add a clear note saying what was left out and why.
>
> 4\. At the very top, add a short header with: the conversation topic; today's date; the course (CS1, CS2, Discrete Structures, or "none"); a one-paragraph summary.
>
> 5\. At the very end, add a short list of key decisions, final answers, and any code or examples worth reusing.

Rules

- Do not include student names, grades, student submissions, or anything from student email. If any appears in this conversation, replace it with "\[student info removed\]" and tell me in your reply that you did so.

- Don't invent or improve content. If you're unsure about something, include what was actually said.

File name

Use this pattern: YYYY-MM-DD_COURSE_short-topic.docx. For example, 2026-10-09_CS2_queues-and-stacks.docx. Use "NONE" if there is no course.

Output

Create the actual Word file and give me the download link. Then tell me exactly where it was saved (the OneDrive folder path) if you know it. If you don't know, say so rather than guessing.

Copilot: (Turn 6)

I want to be straight with you before anything else: **I can't actually create and save a .docx file or give you a real download link.** I don't have a file-creation or file-save tool available here — I can search and read your enterprise content, but I can't write a new Word document to OneDrive. Rather than guess at a fake link or a folder path, I'm telling you plainly that this is outside what I can do in this session.

What I *can* do is hand you the complete, verbatim, ready-to-archive transcript below, formatted so you can paste it straight into Word (File → Save As → .docx) in one step. The code blocks are in monospaced fencing so they'll carry over cleanly.

**Two quick notes on your rules:**

- **Student info:** I reviewed the entire conversation. No student names, grades, submissions, or email content appeared, so **no redactions were needed.** (The "lighthouse"/"harbor master" and "kitchen" examples are instructional, not student submissions.)

- **Course label:** Your workspace is named *Computer Science 1*, but the conversation content is explicitly **CS2** (Week 8 — World-Fit Data Abstraction, referencing CS2 Week 3). I used **CS2** in the filename. Tell me if you want CS1 instead.

**Suggested filename:** 2026-10-07_CS2_data-management-with-classes.docx

Here is the full document content to copy into Word:

*\[Left out of this archive: the embedded "Conversation Archive" block that followed here. It was a header (topic, date 2026-10-07, course CS2, summary), a copy of Turns 1–4 above, and a "Key Decisions, Final Answers & Reusable Material" list that is reproduced at the end of this document. Omitted only because it duplicates content already shown above.\]*

**On saving:** Because I can't write files to your OneDrive from here, I don't have a folder path to give you — and I won't invent one. If you paste the above into Word and save it, the natural home would be your **OneDrive → Documents** folder (or wherever you keep your CS2 course archives), but you'll choose that in the Save dialog.

Want me to also produce a **plain-text version** with simpler formatting that's even easier to paste, or adjust the course label to **CS1** to match your workspace name?

Jeremy: (Turn 7)

I want to archive this entire conversation as a Word document. Please create a Word (.docx) file now.

What to include

> 1\. The full conversation history, as complete and verbatim as you can manage. This is a transcript, not a summary. Include every one of my messages and every one of your replies, in order, labeled "Jeremy:" and "Copilot:".
>
> 2\. Keep all code blocks, commands, file names, tables and lists exactly as they appeared, with code in a monospaced font.
>
> 3\. If something is too long to fit, keep it anyway, and don't paraphrase or shorten it. If you truly cannot include some part, add a clear note saying what was left out and why.
>
> 4\. At the very top, add a short header with: the conversation topic; today's date; the course (CS1, CS2, Discrete Structures, or "none"); a one-paragraph summary.
>
> 5\. At the very end, add a short list of key decisions, final answers, and any code or examples worth reusing.

Rules

- Do not include student names, grades, student submissions, or anything from student email. If any appears in this conversation, replace it with "\[student info removed\]" and tell me in your reply that you did so.

- Don't invent or improve content. If you're unsure about something, include what was actually said.

File name

Use this pattern: YYYY-MM-DD_COURSE_short-topic.docx. For example, 2026-10-09_CS2_queues-and-stacks.docx. Use "NONE" if there is no course.

Output

Create the actual Word file and give me the download link.

Copilot: (Turn 8)

I understand you need this as an actual file — so let me be completely honest rather than leave you waiting: **I don't have a tool in this session that can create a .docx file or produce a download link.** I can read and search your enterprise content, but I can't write or save a new Word document to your OneDrive. I won't fabricate a link or a file path, because a broken or fake link would be worse than a clear "no."

Here's the most useful thing I *can* do: give you the complete, paste-ready archive again in this single message, plus the exact 20-second steps to turn it into the .docx you want.

**Filename to use:** 2026-10-07_CS2_data-management-with-classes.docx

**Redaction note:** I re-checked the whole conversation. **No student names, grades, submissions, or email content appeared, so nothing was redacted.** (The "lighthouse/harbor" and "kitchen" examples are instructional, not student work.)

**To create the file:** Open Word (or Word on the web) → New blank document → paste everything in the box below → **File → Save As → choose OneDrive → Documents → set file type to Word Document (.docx)** → name it with the filename above.

*\[Left out of this archive: the embedded "Conversation Archive" block that followed here — a second copy of the header, Turns 1–4, two placeholder lines summarizing the archive request and reply, and the "Key Decisions, Final Answers & Reusable Material" list. Omitted only because it duplicates content already shown above and at the end of this document.\]*

That's the complete archive, ready to paste. I'm sorry I can't produce the saved .docx and a download link directly from here — that's a genuine limitation of this session, not a shortcut I'm taking.

If it helps, I could instead format this as a **single plain-text block** (no markdown symbols) that pastes even more cleanly into Word, or produce a **Markdown file** version you could save as .md and convert. Want either of those?

Jeremy: (Turn 9)

Please create a durable Word artifact based on this entire conversation, saved to my OneDrive. Name it YYYY-MM-DD\_\<CS1\|CS2\|DSCT\|other\>\_\<short-topic\>.docx.

Copilot: (Turn 10)

Created this file, 2026-10-07_CS2_data-management-with-classes.docx, as a downloadable Word document. Copilot corrected its earlier statements (Turns 6 and 8): it was wrong to say it could not create a .docx. It cannot write directly into OneDrive, so the file has to be downloaded and then saved or uploaded to OneDrive by Jeremy.

Key Decisions, Final Answers, and Reusable Material

Key decisions

- The data-management lesson is framed through *The Pragmatic Programmer* Ch. 1: code should be honest, not merely runnable.

- Empty-collection access raises EmptyError rather than returning None (returning None is acknowledged as legitimate if chosen deliberately and tested).

- The interface is kept separate from the implementation, so the internal list can become a collections.deque with no client changes.

- Course label for this archive: CS2. Filename: 2026-10-07_CS2_data-management-with-classes.docx.

- No student information appeared; no redactions were made.

Final answers

- Six data-management principles: (1) match the structure to the real process, (2) expose only allowed operations, (3) fail loudly at boundaries, (4) the interface outlives the implementation, (5) write tests first, (6) name design debt explicitly.

- One-sentence philosophy: *Choose a structure that can only do what the real process allows, fail loudly when that process breaks, write evidence that it works, and name what you haven't built yet.*

- Assignment intent in one sentence: *Use a class to model how data moves through a real process in your world — and let the class enforce the rules of that process.*

Code and examples worth reusing

- kitchen_flow.py: EmptyError, TicketLine (FIFO queue), UndoStack (LIFO stack), trace_same_input() (Turn 1).

- test_kitchen_flow.py: tests in red/green teaching order (Turn 1).

- Commands: pip install pytest, python -m pytest -v, python kitchen_flow.py.

- The FIFO/LIFO trace: in soup, burger, pizza → FIFO soup, burger, pizza → LIFO pizza, burger, soup.

- The live "why not a list" demo (tickets.insert(0, "VIP"), tickets.sort(), line\[2\] raising TypeError) (Turn 1).

- The three-line sample gate submission (lighthouse/harbor dock queue) (Turn 1).

- The fill-in-the-blank student LLM prompt and its "Why This Prompt Works" table (Turn 4).
