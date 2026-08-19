#!/usr/bin/env bash
set -euo pipefail

SOURCE_ROOT="${CS2_SOURCE_ROOT:-$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)}"
cd "$SOURCE_ROOT"
PROMPT_REL="sidecar/prompts/022_flo_production_closeout.md"

fail() {
    printf 'CS2 Flo launcher STOP: %s\n' "$*" >&2
    exit 1
}

[[ -z "${CS2_FLO_LAUNCHED:-}" ]] || fail "recursive launch refused; this Flo seat is already launched"
command -v git >/dev/null 2>&1 || fail "git is required"
command -v flock >/dev/null 2>&1 || fail "flock is required for single-Foreman ownership"
command -v claude >/dev/null 2>&1 || fail "Claude Code CLI is required for the Flo Lead Foreman seat"
[[ -d .git ]] || fail "source checkout is not a Git repository: $SOURCE_ROOT"

branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null)" || fail "not a Git checkout"
[[ "$branch" == "main" ]] || fail "launch from the CS2 main checkout; current branch is $branch"

# The source checkout is a control plane only. Preserve local work exactly as-is.
# Production inputs are fresh shallow clones from each repository's origin.
local_status="$(git -c core.fileMode=false status --porcelain)"
if [[ -n "$local_status" ]]; then
    echo ">>> Preserving local CS2 checkout dirt; isolated production workspace will not consume it"
fi

# One Flo seat owns this production campaign at a time. Keep the lock in Git
# metadata so it never becomes course source or Sidecar dirt.
lock_file="$(git rev-parse --git-path cs2-flo-production.lock)"
exec 9>"$lock_file"
flock -n 9 || fail "another CS2 Flo production seat already owns the lock"

# Use the known-good Python environment only as an interpreter/package layer.
# Source imports still come from the isolated clones below.
CF_VENV="$SOURCE_ROOT/../course_foundry/.venv"
[[ -x "$CF_VENV/bin/python3" ]] || fail "Course Foundry Python 3 environment missing: $CF_VENV/bin/python3"
export PATH="$CF_VENV/bin:$PATH"

WORK_BASE="${CS2_FLO_WORK_BASE:-$SOURCE_ROOT/../computer_science_2.worktrees/flo-production}"
mkdir -p "$WORK_BASE"
CAMPAIGN_ID="$(date -u +%Y%m%dT%H%M%SZ)-$$"
CAMPAIGN_ROOT="$WORK_BASE/$CAMPAIGN_ID"
mkdir -p "$CAMPAIGN_ROOT"

clone_origin() {
    local name="$1"
    local source="$SOURCE_ROOT/../$name"
    [[ "$name" == "computer_science_2" ]] && source="$SOURCE_ROOT"
    [[ -d "$source/.git" ]] || fail "required local repository control checkout missing: $source"

    local remote_url
    remote_url="$(git -C "$source" remote get-url origin 2>/dev/null)" || fail "origin remote missing for $name"
    echo ">>> Cloning clean $name production input"
    git clone --quiet --no-tags --depth 1 "$remote_url" "$CAMPAIGN_ROOT/$name" || fail "could not clone $name from origin"
    [[ -z "$(git -C "$CAMPAIGN_ROOT/$name" status --porcelain)" ]] || fail "fresh $name clone is unexpectedly dirty"
}

for repo in computer_science_2 course_foundry harbor imprint local_ai_lab_setup; do
    clone_origin "$repo"
done

FLO_ROOT="$CAMPAIGN_ROOT/computer_science_2"
[[ -f "$FLO_ROOT/$PROMPT_REL" ]] || fail "canonical burn prompt missing from clean origin clone: $PROMPT_REL"

# Prove that every dependency is a clean origin snapshot before Claude starts.
echo ">>> Clean Flo production runway"
for repo in computer_science_2 course_foundry harbor imprint local_ai_lab_setup; do
    printf '    %-24s %s\n' "$repo" "$(git -C "$CAMPAIGN_ROOT/$repo" rev-parse --short=12 HEAD)"
done

cd "$FLO_ROOT"
bootstrap=$(cat <<EOF
You are Flo, the Lead Foreman for Computer Science II.

You are already launched. Never invoke sidecar/launch_flo.sh from inside this session.
Read $PROMPT_REL and execute that one canonical burn.
Repository: $FLO_ROOT
Production workspace root: $CAMPAIGN_ROOT

This is a launcher-created isolated workspace cloned from repository origins. The ordinary checkouts under $SOURCE_ROOT/.. may contain active CS1 or other human work; they are out of scope and must remain untouched.
Production writes are forbidden until the prompt's explicit human gate.
Computer Architecture and Computer Science 1 are out of bounds.
Do not make an unpromoted Luna branch a prerequisite unless fresh CS2 evidence proves a real dependency blocker.
Jeremy is not the message bus: keep the full preflight-to-closeout job in this one seat.
EOF
)

args=(--model sonnet)
if claude --help 2>&1 | grep -q -- '--effort'; then
    args+=(--effort medium)
fi

echo ">>> Launching Flo for bounded CS2 production closeout"
CS2_FLO_LAUNCHED=1 exec claude "${args[@]}" "$bootstrap"
