# Course-development prompts

Prompts here guide CS2 curriculum development and Monday Moments.

Before drafting, read `README.md`, `monday_moments/README.md`, `monday_moments/template.md`, the relevant lesson, assignment, and project rubric. For AI content, also read `../../ai_fluency/prompts/002_ai_ii_source_walk.md` and the AI II Drive export in `../../drive_raw_pull_2026-07-14/`.

## Development workflow

For substantial course work, prefer:

1. current-state report;
2. target map;
3. implementation plan;
4. prompts/work orders with explicit validation;
5. actual implementation plus raw work receipts;
6. postmortem/closure report.

Working doctrine:

> Ask to do it once: leave breadcrumbs.  
> Ask to do it twice: script it.  
> Ask to do it three times: tie it into automation.

Prompts are work orders, not the product.

## Week 16 Farkle / ML campaign

Parent: `014_build_cs2_week16_farkle_extension.md`

Subprompts:

- `014_a_reconcile_hardened_cs1_farkle_baseline.md`
- `014_b_build_cs2_farkle_experiment_bench.md`
- `014_c_build_week16_student_instructor_package.md`
- `014_d_script_validate_and_capture_week16_receipts.md`
- `014_e_postmortem_and_close_week16_farkle_build.md`

Current implementation state: **IMPLEMENTED WITH REAL-CHECKOUT VALIDATION YELLOW**. Source, tests, lesson, instructor guide, receipt, and one-command validator exist. Run `python scripts/validate_week16_farkle.py` on a real checkout to produce the raw validation receipt before promoting the campaign to fully GREEN.
