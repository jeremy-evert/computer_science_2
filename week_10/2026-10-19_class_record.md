# CS2 Week 10 Monday (2026-10-19): class record

Instructor-side record of what was built and taught, for Canvas and the next run.
Source: the Flo working session of 2026-10-19. A fuller transcript (Morgan/Susie) may be added later.

## Headline decision
The lesson is **event-driven programming**, not Tkinter. Tkinter is one vehicle; a web page is another.
The logic stays the same: event -> handler -> model -> view. Python setup trouble is incidental, not the lesson.
Careful framing for hardware: interrupts and state machines (CPU/FPGA) are *cousins* of event-driven
programming. Do not claim they "stem from" it.

## What was used in class
- Deck: `presentations/beamer/week10_event_driven/week10_event_driven.pdf` (15 slides, Anna, commits 1a32097, ce4fd72).
  The earlier `week10_compact_gui` deck is kept as backup.
- Code kit: `week_10/compact_gui/`
  - Model + test: `inventory.py`, `test_inventory.py` (no window needed).
  - Tkinter: `view.py` (every class/object labeled), `view_traced.py`, `view_broken_boundary.py`.
  - Web (stdlib only, no installs): `view_web.py`.
  - Terminal / no window: `view_terminal.py`, `no_window_trace.py`. Peer swap: `contract_test.py`.
  - Two items: `inventory_rope_and_shovel.py` + `test_inventory_rope_and_shovel.py`,
    `view_rope_and_shovel.py` (Tkinter), `view_web_rope_and_shovel.py` (web).
  - Setup check: `check_my_setup.sh` (WSL/Linux).

## Same idea, different syntax (Tkinter -> web)
| Tkinter | Web |
|---|---|
| `tk.Tk()` window | browser tab + `HTTPServer` |
| `tk.Label` + `StringVar` | HTML rebuilt from the model each request |
| `tk.Button(command=handler)` | `<form action="/restock/rope">` + a `ROUTES` table |
| `refresh()` | `render_page()` |
| `root.mainloop()` | `server.serve_forever()` |
| event: mouse click | event: HTTP request |
The model file is identical in both. That is the proof of the boundary.

## What went wrong, and the fixes
- Code slides (6-8): the first build had dark code on a dark background. Fixed in ce4fd72 (restored the light code color).
- `check_my_setup.sh` failed on Windows: git converted it to CRLF line endings. Fixed with a `.gitattributes` (`*.sh`, `*.py` as LF).
- WSL: use `bash ./script.sh` (forward slash); backslashes get eaten. Tkinter on WSL needs `apt install -y python3-tk`.
  On the Windows lab machine `py -3` already had Tkinter; no install needed.
- The slides show the short `view.py`; the repo copy now carries the class/object/pairing labels. Same behavior.

## For next time
- Open with the event-driven framing, then Tkinter pass, then web pass, then "what changed vs what did not".
- Ask: why does adding a third item change the model and buttons but barely touch `refresh()`?
- Gate (Reasoning Odyssey / World Bible): the rule moved + a click trace, due Friday 11:59 PM Central.
