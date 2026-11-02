# 009. Baseline Comparison Results

## What I ran
I hashed the files already in `out/`, ran `python .\\beast.py`, and hashed the generated files again. I also compared the three protected baseline artifacts with their new outputs. No files in `baseline/` or `beast_as_given.py` were changed.

## Files that changed

- `out/timings.csv` changed because it records elapsed execution time measured with `time.perf_counter()`; timings naturally vary between runs.
- `out/report.log` changed during LaTeX compilation. The file is compiler output and can include run-specific details. The comparison recorded that its bytes changed; it did not preserve a line-by-line diff to identify the exact changed text.
- `out/report.pdf` changed at the byte level. PDF generation can record timestamps or other metadata, so a binary difference does not by itself mean the report's content changed.

## Files that stayed the same

- `out/sort_counts.csv` matched `baseline/sort_counts.csv` exactly. The fixed random seeds make the tested inputs repeatable, so the sorting counts remain stable.
- `out/search_counts.csv` matched `baseline/search_counts.csv` exactly. Search inputs and targets are generated from fixed seeds.
- `out/report.tex` matched `baseline/report.tex` exactly. It is built from the stable count results and fixed report text.
- `out/sort_counts.png` and `out/search_probes.png` stayed byte-identical; they plot the same deterministic data.
- `out/report.aux` stayed byte-identical in this run.
- The existing summary documents in `out/` stayed byte-identical; this run did not write or alter them.

## What this shows
The baseline comparison produced exact matches for all three files that define the behavior baseline. The timing CSV and LaTeX-generated binary artifacts can vary even when the deterministic counts and report source remain unchanged. This is why timing and PDF bytes are poor exact-match characterization targets.
