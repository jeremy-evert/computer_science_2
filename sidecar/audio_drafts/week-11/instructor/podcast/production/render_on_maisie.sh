#!/usr/bin/env bash
# Computer Science Two Week 11: private instructor podcast. Run on Maisie with existing Audio Foundry.
# Dana and Maria are the two script speakers; generated audio and receipts stay outside Git.
set -euo pipefail

usage() {
  cat >&2 <<'HELP'
Usage: bash production/render_on_maisie.sh render 01
       bash production/render_on_maisie.sh publish 01

Required env: AUDIO_FOUNDRY_CHECKOUT, KOKORO_PYTHON
Before publish: verify the real PRIVATE Audiobookshelf library mount, then set
PRIVATE_AUDIOBOOKSHELF_MOUNT_VERIFIED=YES.
This script handles episode 01 only and never targets a student or public library.
HELP
  exit 2
}
mode="${1:-}"
selection="${2:-01}"
[[ "$mode" == render || "$mode" == publish ]] || usage
[[ "$selection" == 01 ]] || usage
base="01_honest_charts_from_project_data"
output_name="CS2 Week 11 - Honest Charts from Project Data"

: "${AUDIO_FOUNDRY_CHECKOUT:?Set to existing Audio Foundry checkout on Maisie}"
: "${KOKORO_PYTHON:?Set to existing Kokoro venv Python on Maisie}"
[[ -x "$KOKORO_PYTHON" && -f "$AUDIO_FOUNDRY_CHECKOUT/tools/kokoro_dialogue.py" ]] || {
  echo "Missing Kokoro interpreter or Audio Foundry dialogue renderer" >&2; exit 2;
}
for command_name in ffprobe sha256sum python3; do
  command -v "$command_name" >/dev/null || { echo "Missing $command_name" >&2; exit 2; }
done
here="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
work_root="${AUDIO_FOUNDRY_RUNTIME:-/srv/audio-foundry}/work/cs2-week11-20261026"
source_dir="$work_root/source"
audio_dir="$work_root/rendered"
receipt_dir="$work_root/receipts"
mkdir -p -- "$source_dir" "$audio_dir" "$receipt_dir"
original="$here/scripts/$base.md"
source="$source_dir/$base.md"
output="$audio_dir/$output_name.mp3"
receipt="$receipt_dir/$base.json"
[[ -f "$original" ]] || { echo "Missing original: $original" >&2; exit 2; }

# Verify the committed source against its manifest before rendering.
python3 - "$here/manifest.json" "$original" "$base.md" <<'PY'
import hashlib, json, sys
from pathlib import Path
manifest = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
name = sys.argv[3]
episode = next((e for e in manifest["episodes"] if Path(e["source"]).name == name), None)
if not episode:
    raise SystemExit(f"Manifest has no entry for {name}")
actual = hashlib.sha256(Path(sys.argv[2]).read_bytes()).hexdigest()
if actual != episode["sha256"]:
    raise SystemExit(f"Source SHA-256 mismatch for {name}; refusing to render")
PY

if [[ ! -e "$source" ]]; then cp -- "$original" "$source"; fi
[[ "$(sha256sum "$original" | cut -d' ' -f1)" == "$(sha256sum "$source" | cut -d' ' -f1)" ]] || {
  echo "Conflicting staged source: $source" >&2; exit 2;
}

if [[ "$mode" == render && ! -e "$output" ]]; then
  "$KOKORO_PYTHON" "$AUDIO_FOUNDRY_CHECKOUT/tools/kokoro_dialogue.py" render \
    "$source" "$output" --receipt "$receipt" --device cuda --pause-ms 300
fi

[[ -s "$output" && -s "$receipt" ]] || {
  echo "Missing validated output or receipt: $base (do not silently overwrite)" >&2; exit 2;
}
# Recheck exact source/output identity on resume and before publishing.
python3 - "$source" "$output" "$receipt" <<'PY'
import hashlib, json, sys
from pathlib import Path
source, output, receipt_path = map(Path, sys.argv[1:])
receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1048576), b""):
            h.update(block)
    return h.hexdigest()
assert digest(source) == receipt["source"]["sha256"], "Render source receipt mismatch"
assert digest(output) == receipt["output"]["sha256"], "MP3 receipt mismatch"
assert receipt["output"]["duration_seconds"] > 60, "Unexpectedly short MP3"
assert receipt["output"]["bytes"] == output.stat().st_size, "MP3 size mismatch"
print("VERIFIED", output.name, round(receipt["output"]["duration_seconds"]), "seconds", digest(output))
PY

if [[ "$mode" == render ]]; then
  echo "RENDERED 01: $audio_dir"
  echo "Spot-listen to beginning and end, then verify the private Audiobookshelf mount before publish."
  exit 0
fi

[[ "${PRIVATE_AUDIOBOOKSHELF_MOUNT_VERIFIED:-}" == YES ]] || {
  echo "Refusing publish: verify live private Audiobookshelf mount then set PRIVATE_AUDIOBOOKSHELF_MOUNT_VERIFIED=YES" >&2; exit 2;
}
media_root="${AUDIO_FOUNDRY_RUNTIME:-/srv/audio-foundry}/audiobooks"
[[ -d "$media_root" ]] || { echo "Missing private media root: $media_root" >&2; exit 2; }
series_dir="$media_root/Learning Foundry/CS2 Week 11 - Honest Charts from Project Data"
mkdir -p -- "$series_dir"
dest="$series_dir/$output_name.mp3"
if [[ -e "$dest" ]]; then
  [[ "$(sha256sum "$output" | cut -d' ' -f1)" == "$(sha256sum "$dest" | cut -d' ' -f1)" ]] || {
    echo "Existing library artifact differs; refusing overwrite: $dest" >&2; exit 2;
  }
  echo "ALREADY PUBLISHED (identity verified): $dest"
else
  cp --no-clobber -- "$output" "$dest"
  [[ "$(sha256sum "$output" | cut -d' ' -f1)" == "$(sha256sum "$dest" | cut -d' ' -f1)" ]] || {
    echo "Publish copy conflict: $dest" >&2; exit 2;
  }
  echo "PUBLISHED: $dest"
fi
echo "Library scan/refresh and Android play/seek/resume acceptance are separate checks."
echo "Receipts: $receipt_dir"
