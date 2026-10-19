#!/usr/bin/env bash
# Run from this folder: bash check_my_setup.sh
cd "$(dirname "$0")" || exit 1
say() { printf '%s\n' "$*"; }
say "1. Python:"; python3 --version || { say "   NO python3. Stop here."; exit 1; }
say "2. Model test (no window needed):"
python3 -m unittest -q test_inventory && say "   PASS - today's core lesson works on this machine." || say "   FAIL"
say "3. No-window trace:"; python3 no_window_trace.py | tail -2
say "4. DISPLAY=${DISPLAY:-<empty>}"
if python3 -c "import tkinter" 2>/dev/null; then
  say "5. tkinter: installed."
  if [ -n "${DISPLAY:-}" ] && python3 -c "import tkinter; r=tkinter.Tk(); r.after(500, r.destroy); r.mainloop()" 2>/dev/null; then
    say "   A window opened and closed: GOOD DAY. Run: python3 view.py"
  else
    say "   tkinter installed but no window could open: use no_window_trace.py (Plan B)."
  fi
else
  say "5. tkinter missing. Fix (as root in Ubuntu/WSL): apt install -y python3-tk"
  say "   Until then: Plan B = python3 no_window_trace.py (same lesson)."
fi
