# Report 013: Imprint Computer Science II into Savnac and Read It Back

**Closes:** `sidecar/prompts/013_imprint_cs2_to_savnac_and_read_back.md`
**Superseding evidence:** `sidecar/reports/021_full_fucking_load_savnac.md` (full
detail; this report is the Prompt 013-shaped acceptance record Prompt 013
itself required).

## Why this closes now, not earlier

Prompt 013 asked for a minimum inspection slice: Course Information, Week 1,
Week 2, Week 3, plus "if the existing compiler and source already support
additional weeks cleanly, imprint the broader source-backed course rather
than arbitrarily stopping at Week 3." At the time Prompt 013 was authored,
that broader support did not yet exist end-to-end and verified. It does now
-- Prompt 021 (2026-08-17) exercised the exact same Course Foundry/Imprint
path Prompt 013 specified and went past Week 3 to the full honest semester,
so Prompt 013's own instruction to keep going was followed, just later than
Prompt 013 itself anticipated.

## Evidence against Prompt 013's specific acceptance checklist

1. **Current CS2 source is visibly represented in Savnac.** Confirmed --
   course 3 ("Computer Science 2 (CS2)") carries 20 modules covering Week 1
   (shared kickoff, 3 sub-modules) through Week 17, 121 assignments, 69
   pages, 15 assignment groups summing to exactly 100%. See Report 021's
   "Whole-course read-back" section for the full inventory.
2. **The result is useful for Jeremy to inspect.** Confirmed by the
   professor-walk and student-walk sections of Report 021 -- module
   sequence, gate/checkpoint placement, and assignment/rubric coherence are
   all readable directly in Savnac without cross-referencing GitHub, with
   one honest navigation defect disclosed (see Report 021's YELLOW list),
   not hidden.
3. **No production Canvas or ZyBooks write occurred.** Confirmed --
   `CANVAS_API_BASE_URL` was `http://192.168.122.172:3000` (the Savnac host
   marker) for every write in this session; `require_host_marker` in
   `imprint/config.py` would have raised rather than silently proceeding
   against any other host. Zero ZyBooks references found anywhere in the
   read-back (assignment names/descriptions and page titles both scanned).
4. **Unsupported course mechanics were not invented.** Confirmed -- the
   `cs2_savnac_desired_course` compiler used here is the same one Prompt 013
   named, and it still declines to invent late/drop policy, textbook
   requirements, or production settings; see Report 021's YELLOW list for
   what remains genuinely unresolved in source.
5. **The deployment reused the established Course Foundry/Imprint path.**
   Confirmed -- `course_foundry.savnac_deploy` (the unified, Savnac-gated
   CLI covering cs1/cs2/dsct/architecture) and `imprint.reconcile.push_course`
   were used directly. No parallel deployment code was written for this
   prompt or for Prompt 021.
6. **Immediate re-run behavior is understood and does not silently
   duplicate course objects.** Confirmed -- two consecutive dry-runs
   immediately after the live push both returned `0 create / 0 update / 169
   unchanged / 0 delete`, a genuine idempotent fixed point.

## Residual note, not a 013 gap

Prompt 013 also asked to verify "no obvious duplicate objects created by the
imprint." None were created by this session's write (only 1 pre-existing
object was updated; 0 created). A pre-existing Week 1 module-ordering
oddity was found during read-back (Wednesday/Friday/A07 sub-modules for
Week 1 sort after Week 17 in Canvas module position) -- this predates this
session's write entirely (`prune_scope=none` never touches Week 1, which
`cs2_desired_course.py` intentionally does not model), is owned by the
separate `semester_kickoff_week` pipeline rather than CS2's builder, and is
recorded as a YELLOW in Report 021 rather than fixed here, per Prompt 021's
explicit instruction not to create a second deployment stack to reach into
another pipeline's scope.

## Verdict

Prompt 013's acceptance condition -- "Jeremy can open Savnac and inspect a
recognizable, current Computer Science II course produced from the
repository's current course truth" -- is satisfied, with a real course
substantially exceeding the originally-requested minimum slice. Moved to
`sidecar/prompts/completed/`.
