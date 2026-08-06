# Odyssey Gate — Week 5 rubric: Quick Check (pass/fail) + light Build

Matches `docs/curriculum/judgment_toolkit.md` §1/§2.

## Part 1 — Quick Check (pass/fail, mechanical-checkable)

| Criterion | Pass condition |
|---|---|
| Context-managed save | `with open(...)` or an equivalent context-managed CSV operation writes meaningful world state. |
| Real reload and use | A later run reads the file, reconstructs usable values or records, and uses them in world behavior. |
| Two-run evidence | The submission demonstrates a value written in the first run affecting the second; a pre-existing static file alone does not count. |

**All three present → pass.** Any missing → not yet. The context manager and
read/write paths are mechanically checkable; two-run persistence requires a
short trace or focused demonstration.

## Part 2 — Light Build (holistic)

Same three-band shape as `rubrics/odyssey_gates/week-02_rubric.md`.

## Grading notes

- Writing a file and printing it in the same process does not prove
  persistence; require a second execution after the write.
- Raw file display alone does not meet reload-and-use: the program must
  interpret enough saved data to affect a world-facing result.
- For CSV, accept `csv.reader`/`csv.writer` and require `newline=''` when the
  student's platform and standard-library usage call for it; do not require
  CSV when a documented text format is the better fit.
- The World Bible line is required but reviewed cumulatively at finals.
