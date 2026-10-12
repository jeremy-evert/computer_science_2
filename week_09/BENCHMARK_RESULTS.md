# Week 9 benchmark results

Run: 2026-10-12, instructor machine. Source: `week_09_gate.py`
(raw output in `benchmark_output.txt`, decisions in `NOTES.md`).

## Machine profile

- **CPU:** Intel64 Family 6 Model 183 (GenuineIntel), AMD64, 24 logical cores.
- **OS:** Windows 11, Python 3.12.10.
- **CPU loop proxy:** about 20.6 million iterations/second.
- **Memory:** about 4.07 GB free physical memory; the script itself peaked at
  about 20 MB.

## Lookup benchmark (100,000 items, 200 lookups)

| Method | Time |
| --- | --- |
| Linear search, unsorted | about 0.30 s |
| Sort once | about 0.014 s |
| Bisect over the sorted data | about 0.0001 s |
| Sort plus bisect total | about 0.014 s |

Sorting first wins at 200 lookups. Bisect is only correct on sorted data.

## Changes

- **New script:** `week_09_gate.py` did not exist, so it was created. It has the
  hardware profile, a Week 9 linear-vs-bisect lookup benchmark, and a World
  Bible line that includes the hardware.
- **`wmic` replaced:** Windows 11 no longer has `wmic`, so free memory is read
  with `ctypes`; `wmic` is only a fallback.
- **Peak memory:** `ctypes` on Windows, `resource` on Linux/Mac.
- **Outputs saved:** `benchmark_output.txt` (captured run) and `NOTES.md`
  (decisions), both in `week_09/`.

## Caveat

The CPU loop proxy is a rough relative number, not a rigorous benchmark.
