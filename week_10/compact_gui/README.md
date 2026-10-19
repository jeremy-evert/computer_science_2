# Week 10 Monday: compact GUI over a tested model

Start: `bash check_my_setup.sh` (tells you whether it is a good day or a Plan B day).

Order of the hour (matches the slides):
1. `python3 -m unittest test_inventory` - model passes, no window.
2. `python3 view.py` - click Restock three times: "Items: 3".
3. `python3 view_traced.py` - click once, read the terminal trace.
4. `view_broken_boundary.py` vs `view.py` - how would you test the left one?
5. Peer swap: `python3 contract_test.py their_module`.

Pass 2 (same model, web page, no pip): `python3 view_web.py`, open http://localhost:8000, click Restock.
Third front end: `python3 view_terminal.py`.

Plan B (no window anywhere): `python3 no_window_trace.py`. Same lesson.

WSL/Ubuntu: `apt install -y python3-tk`; windows open on the Windows desktop via WSLg (WSL2).
Keep files in the WSL home folder, not /mnt/c.
