# Honest Charts from Project Data

An original two-voice instructor listening script for preparing Computer Science Two Week 11, beginning October 26, 2026. Dana and Maria are the speakers; the manifest maps them to the established renderer voices af_sarah and af_heart. This package contains text and a rendering handoff only. No audio is included.

## Sources and credit

The script follows the Computer Science Two Week 11 plan, the instructor-owned data storytelling micro-lab and its Python script, the supplied Frontier Settlement resource CSV, the Week 11 Odyssey gate and rubric, and the Odyssey/capability planning material. These course sources define the activity, evidence, limits, and rubric. The narration is original explanatory prose; it does not reproduce course passages.

The sample values discussed are exactly those in the supplied teaching CSV. They are a single set of current recorded resource levels, not student data, a time series, or a measurement of cause.

## Contents

- `scripts/01_honest_charts_from_project_data.md` — episode script
- `manifest.json` — source hash, voice map, spoken word count, and estimated duration
- `production/render_on_maisie.sh` — single-episode render and private library handoff for Flo

## How Flo and Anna render it

On Maisie, use the existing Audio Foundry checkout and Kokoro environment. Verify their paths, then from this directory run:

```bash
export AUDIO_FOUNDRY_CHECKOUT=/verified/existing/audio_foundry/checkout
export KOKORO_PYTHON=/verified/existing/kokoro-venv/bin/python
bash production/render_on_maisie.sh render 01
```

Inspect and spot-listen to the rendered file. Before using `publish 01`, independently verify that the live Audiobookshelf mount is the private instructor library, then set `PRIVATE_AUDIOBOOKSHELF_MOUNT_VERIFIED=YES`. The script refuses publication without that explicit check and refuses to overwrite a different existing file. Library refresh and device playback checks remain separate. Generated files and receipts stay under the configured Audio Foundry runtime, outside this repository. Anna reviews this package before rendering; this helper has not rendered or published it.

## Claims for Anna to check

- The micro-lab’s CSV has four current resource levels and does not supply time history or causal evidence; the narration’s comparison and limits should stay aligned with the lesson.
- A zero-baseline bar chart is the lesson’s defensible comparison for the supplied categorical current amounts; a line chart would imply a time trend, and a truncated vertical scale can exaggerate differences.
- The gate assigns 25 points as eight for question/visualization, seven for reproducible evidence, six for representation/pitfall/World Bible, and four for AI accountability when used.
- Estimated minutes use 150 spoken words per minute and are not a rendered duration. Confirm actual duration from the Kokoro receipt.
