# Week 10 micro-lab — From question to honest visual to useful story

## Purpose

This instructor-owned activity models the thinking sequence rather than a
plotting recipe: **question → available data → representation → interpretation
→ limitation → decision**. It uses a tiny Frontier Settlement CSV and a small
Matplotlib script, but the same questions apply to a case queue, ship log, or
small-business inventory. It is a pattern for Odyssey work, not a disconnected
homework assignment.

## Run it

From the repository root, run:

```text
python lessons/week-10-data-storytelling-micro-lab.py
```

The script reads `lessons/data/frontier-resource-levels.csv` and writes
`frontier-resource-levels.png` beside the script when Matplotlib is available.
It uses Python's built-in `csv` module plus Matplotlib; it does not use or
require pandas. A small standard-library SVG fallback keeps the activity
runnable when Matplotlib is unavailable, without changing the visualization
judgment being practiced. No paid text or account is a dependency.

## Worked judgment

**Question:** Which settlement resource needs attention before the next supply
decision?

**Data actually available:** four named current resource levels, not a time
series and not evidence of causes.

**Representation:** a zero-baseline bar chart permits an honest comparison of
current amounts. A line chart would imply a time trend that this data does not
contain. Truncating the vertical scale would exaggerate the smallest
difference.

**Supported story:** Water is the lowest currently recorded resource, so the
team should inspect its consumption and replenishment before the next action.
This does not prove why water is low, forecast a shortage, or establish a
causal relationship.

**Decision:** prioritize a water-status check or a replenishment feature; name
the missing time/history data that would make the claim stronger.

## Optional short reps

- Choose a bar, line, or table for three different questions and defend one.
- Compare the supplied zero-baseline chart with a truncated-axis version and
  identify what the latter exaggerates.
- Rewrite `Resource levels` as a cautious claim title supported by the data.
- Explain why an apparent association in a project visual does not prove
  causation.

These are in-class, pair, low-stakes, or optional supports—not a second
required homework sequence.
