# Week 9 benchmark notes

`week_09_gate.py` (stdlib only) prints a hardware profile, then times linear
lookup vs sort-once + `bisect` on the same data, then a World Bible entry.
`benchmark_output.txt` is the captured run on the instructor machine
(2026-10-12), so the numbers are tied to the hardware that produced them.

- The original prompt assumed `week_09_gate.py` already existed. It did not,
  so it was created fresh with a lookup benchmark plus the hardware profile.
- `wmic` is gone on current Windows 11, so free memory uses
  `GlobalMemoryStatusEx` via `ctypes`; `wmic` is only a fallback. Peak memory
  uses `resource` on Linux/Mac and `GetProcessMemoryInfo` via `ctypes` on Windows.
- The CPU loop proxy is a rough relative number, not a rigorous benchmark.
