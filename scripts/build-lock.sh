#!/usr/bin/env bash
# build-lock.sh — serialize `astro build` so parallel sessions never collide.
#
# WHY: `astro build` shares dist/ .astro/ node_modules/.vite. Two builds in the
# same working dir race on hashed-chunk emission (OG image step) and the
# content-layer cache, producing flaky ENOENT errors (e.g. PostDetails,
# _---slug_). This wrapper takes an atomic lock so only ONE build runs at a
# time; a second `pnpm build` waits instead of corrupting the first.
#
# macOS has no `flock`, so we use `mkdir` (atomic on POSIX) as the lock.
# Usage: invoked automatically by `pnpm build`. Runs `pnpm build:unlocked`.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOCK_DIR="$REPO_ROOT/.astro-build.lock"
PID_FILE="$LOCK_DIR/pid"
TIMEOUT="${BUILD_LOCK_TIMEOUT:-1800}"   # max seconds to wait for the lock
WAITED=0

acquire() {
  while ! mkdir "$LOCK_DIR" 2>/dev/null; do
    # Lock held — check if the holder is still alive (steal stale locks).
    if [ -f "$PID_FILE" ]; then
      holder="$(cat "$PID_FILE" 2>/dev/null || echo '')"
      if [ -n "$holder" ] && ! kill -0 "$holder" 2>/dev/null; then
        echo "build-lock: stale lock from dead PID $holder — reclaiming." >&2
        rm -rf "$LOCK_DIR"
        continue
      fi
    fi
    if [ "$WAITED" -ge "$TIMEOUT" ]; then
      echo "build-lock: timed out after ${TIMEOUT}s waiting for another build." >&2
      exit 1
    fi
    if [ "$((WAITED % 15))" -eq 0 ]; then
      echo "build-lock: another build is running (held by PID $(cat "$PID_FILE" 2>/dev/null || echo '?')) — waiting…" >&2
    fi
    sleep 1
    WAITED=$((WAITED + 1))
  done
  echo "$$" > "$PID_FILE"
  trap 'rm -rf "$LOCK_DIR"' EXIT
}

acquire
echo "build-lock: acquired (PID $$). Running build…" >&2
pnpm run build:unlocked
