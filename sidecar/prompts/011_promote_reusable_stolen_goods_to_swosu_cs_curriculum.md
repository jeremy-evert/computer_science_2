# Sidecar Prompt 011 — Promote reusable stolen goods to SWOSU CS Curriculum

**Status:** OPEN
**Owner:** Foreman
**Mode:** inspect, dispatch, promote, verify
**Related:** Prompt 010 CS1 → CS2 scavenging/parity pass

## Problem

When CS2 steals a good idea from CS1, we do not want the only surviving copies to live independently inside two course repositories if the thing is actually reusable across the curriculum.

The central curriculum repository exists for exactly this kind of durable shared truth:

`jeremy-evert/swosu_cs_curriculum`

Current root structure includes areas such as `courses/`, `shared/`, `decisions/`, `planning/`, and `scripts/`. Inspect the repository's current `README.md` and `AGENTS.md` before writing there.

## Default question

Every time Prompt 010 finds something worth stealing, ask:

> **Is this course-specific, or did we just discover something SWOSU CS should own centrally?**

And if it is reusable:

> **Did we leave a good canonical copy in `swosu_cs_curriculum`?**

## Mission

Foreman should dispatch a worker/golem to audit the reusable discoveries from the CS1 → CS2 parity work and ensure that cross-course patterns, templates, shared materials, conventions, or tooling are promoted into `swosu_cs_curriculum` where appropriate.

Do not centralize for sport. The point is to prevent good reusable ideas from becoming duplicated local folklore.

## Read first

Inspect current versions of:

- `computer_science_1/`
- `computer_science_2/`
- `swosu_cs_curriculum/README.md`
- `swosu_cs_curriculum/AGENTS.md`
- relevant existing `swosu_cs_curriculum/shared/`, `courses/`, `decisions/`, `planning/`, and `scripts/` content
- Prompt 010's accepted report, if available

Do not assume the central repo is empty or that a discovered pattern needs a new home. Check whether an authoritative/shared version already exists.

## Classification

For each high-value item copied, adapted, or identified during the CS1 → CS2 parity work, classify it as:

- `COURSE_SPECIFIC` — belongs only in the course repo; no central copy needed.
- `CENTRAL_ALREADY_EXISTS` — reusable truth already has a suitable canonical home; local courses should consume/reference it rather than fork it.
- `PROMOTE_SHARED` — reusable material/pattern should be added to `swosu_cs_curriculum/shared/` or another clearly appropriate central location.
- `PROMOTE_PATTERN_OR_TOOLING` — reusable structure, template, script, validation rule, or convention should be promoted to the appropriate central location.
- `CENTRAL_DECISION` — this is a cross-course curricular decision that belongs in the central decisions/planning surface.
- `UNCLEAR` — ownership is not obvious; record the question and do not invent a taxonomy.

## Promotion rules

When promoting:

1. Preserve the best reusable form, not a CS1-branded or CS2-branded copy with the course number scratched off.
2. Remove course-specific dates, codes, assignment names, and implementation details unless they are examples rather than the shared rule.
3. Give the central artifact enough context that another course can actually reuse it.
4. Update local course references when appropriate so courses know where shared truth lives.
5. Do not delete useful local course wrappers when those wrappers provide necessary course-specific sequencing or student context.
6. Do not create a second central copy when `swosu_cs_curriculum` already has an adequate canonical artifact.
7. Respect the central repo's own `AGENTS.md` and existing organization.

## Cross-repository proof

The worker must provide evidence for **each repository changed**.

Required report should include:

- item-by-item ownership classification;
- central paths created or updated;
- local CS1/CS2 paths updated to reference or wrap central material, if applicable;
- items deliberately left course-local and why;
- items already central and therefore not duplicated;
- unresolved ownership questions;
- `git diff --check` and relevant validation results for every changed repo;
- commit SHA(s) for every repository changed.

No Canvas, Savnac, credential, or production-student-system writes are authorized.

## Required report

Write the CS2-side receipt to:

`sidecar/reports/011_promote_reusable_stolen_goods_to_swosu_cs_curriculum.md`

If the central repo has its own required work-record convention, follow it too rather than replacing it with this report.

## Foreman acceptance

Foreman reviews the cross-repository diff and proof.

The worker does not mark itself complete. Foreman should reject work that merely says "this could be shared" without either proving an existing central canonical copy or creating the appropriate promoted artifact.

After acceptance, Foreman moves this prompt to:

`sidecar/prompts/completed/011_promote_reusable_stolen_goods_to_swosu_cs_curriculum.md`

## Done when

For every meaningful reusable thing discovered while stealing from CS1, Foreman can point to one of two outcomes:

- it is genuinely course-specific and intentionally stays local; or
- a suitable canonical version exists in `swosu_cs_curriculum`, with local courses consuming/wrapping it instead of independently reinventing it.
