#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
PROMPT="sidecar/prompts/022_flo_production_closeout.md"

fail() {
    printf 'CS2 Flo launcher STOP: %s\n' "$*" >&2
    exit 1
}

[[ -z "${CS2_FLO_LAUNCHED:-}" ]] || fail "recursive launch refused; this Flo seat is already launched"
command -v git >/dev/null 2>&1 || fail "git is required"
command -v flock >/dev/null 2>&1 || fail "flock is required for single-Foreman ownership"
command -v claude >/dev/null 2>&1 || fail "Claude Code CLI is required for the Flo Lead Foreman seat"
[[ -f "$PROMPT" ]] || fail "canonical burn prompt is missing: $PROMPT"

branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null)" || fail "not a Git checkout"
[[ "$branch" == "main" ]] || fail "launch from CS2 main; current branch is $branch"

# Preserve meaningful human work. Untracked scratch/evidence is not erased or
# normalized here; Git itself safely refuses a pull if an untracked path
# conflicts with incoming tracked content.
tracked_dirt="$(git -c core.fileMode=false status --porcelain --untracked-files=no)"
[[ -z "$tracked_dirt" ]] || {
    printf '%s\n' "$tracked_dirt" >&2
    fail "tracked CS2 worktree changes are present; preserved without stash/reset/clean"
}

# One Flo seat owns this production campaign at a time. Keep the lock in Git
# metadata so it never becomes course source or Sidecar dirt.
lock_file="$(git rev-parse --git-path cs2-flo-production.lock)"
exec 9>"$lock_file"
flock -n 9 || fail "another CS2 Flo production seat already owns the lock"

echo ">>> Updating Computer Science II main"
git fetch origin main
git -c core.fileMode=false pull --ff-only origin main
[[ "$(git rev-parse HEAD)" == "$(git rev-parse origin/main)" ]] || fail "local main is not exactly origin/main after fast-forward sync"

bootstrap=$(cat <<EOF
You are Flo, the Lead Foreman for Computer Science II.

You are already launched. Never invoke sidecar/launch_flo.sh from inside this session.
Read $PROMPT and execute that one canonical burn.
Repository: $ROOT

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
