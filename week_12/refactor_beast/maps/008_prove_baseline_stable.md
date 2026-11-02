# 008. Prove the Baseline Is Stable

## Idea
Rerun `beast.py` and compare its deterministic outputs with the saved baseline. Compare `sort_counts.csv`, `search_counts.csv`, and `report.tex`; no diff output means those generated files still match the recorded definition of “still works.” `timings.csv` and the PDF are excluded because runtime measurements and PDF metadata can vary between runs.

## Baseline protection
The baseline is the fixed reference for later characterization tests. If a comparison fails, investigate the program or the comparison process; do not update the baseline to make the mismatch disappear.

## Repository note
The baseline is already committed on branch `refactor`. The before map is at `maps/before_map.md`, so any future commit that includes it should stage that path, not a root-level `before_map.md`. Generated files under `out/` are not part of the stable reference.
