"""CS2 Week 16 Farkle + ML experiment bench.

The computational machine is supplied by the provenance-pinned canonical
``farkle_ml`` package. This package owns only the CS2-facing experiment lens.
"""

import json
from pathlib import Path

SCHEMA_VERSION = "cs2-farkle-result-v2"

_PROVENANCE_PATH = (
    Path(__file__).resolve().parents[1]
    / "farkle_ml"
    / "_SHARED_PROVENANCE.json"
)
_PROVENANCE = json.loads(_PROVENANCE_PATH.read_text(encoding="utf-8"))

SHARED_REPOSITORY = _PROVENANCE["shared_repository"]
SHARED_SOURCE_COMMIT = _PROVENANCE["shared_commit"]
SHARED_REPO_HEAD = _PROVENANCE["shared_repo_head"]
