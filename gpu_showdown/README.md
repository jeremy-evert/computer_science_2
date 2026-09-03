# The GPU Showdown

A short, standalone student handout: an evidence dossier from a small local-GPU
benchmark fleet. It asks students to decide what the benchmark evidence
actually supports rather than accept a headline "which GPU wins" ranking at
face value.

Delivered as its own dedicated Canvas module ("The GPU Showdown") rather than
folded into a week module, so it stays easy to find and easy to extend later
if companion material is added. This is separate from the Week 2/3
hardware-confidence material already in this course, which is framed as
instructor research context rather than a formal handout — this artifact is
the formal, student-facing publication of the GPU Showdown packet.

Machine labels in the table (Machine A-H) are anonymized fleet host names —
the source data used real host names, relabeled before publication so the
student-facing copy doesn't expose them.

`data/benchmark_summary.csv` is the dataset the CS2 lens assignment asks
students to parse ("CS2 lens: model, validate, present") — it wasn't part of
Mission 030's original artifact list and had to be added separately so the
assignment is actually completable. It includes a CPU column alongside the
GPU data, since CPU/host pairing is one of the confounds the handout itself
discusses.

## Provenance

- Source repository: `jeremy-evert/local_ai_lab_setup`
- Source branch: `anna/gpu-showdown-latex-027`
- Source commit: `7feb3b1b8725b41a659aaa69d46221377b97a852`
- Built from: `curriculum/gpu_showdown/wrappers/cs2.tex` (machine labels
  relabeled to Machine A-H before build; see note above)
- Built on: April, 2026-09-02, via `latexmk` (pdflatex backend)
- SHA-256 (v3, relabeled + CPU column added): `44abea6b428d1ba5b90c5106f414902b8357ed99c6a0b8647000a7d541ffecf2`
- `data/benchmark_summary.csv` SHA-256: `9ebdce09d11c6d1981cdb95424962ebf856bf7922bc1062b4f01b9a9aa3f46f6`
- Live Canvas placement: course 74031 (COMSC-1053-1417), module "The GPU Showdown"
