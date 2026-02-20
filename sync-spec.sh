#!/usr/bin/env bash
# Full sync workflow: fetch upstream, merge if needed, optionally regenerate.
#
# Usage:
#   bash sync-spec.sh              # fetch, compare, and prompt
#   bash sync-spec.sh --merge      # fetch and auto-merge
#   bash sync-spec.sh --full       # fetch, merge, and regenerate SDK
#
# Files:
#   upstream.json  — last-known upstream version (merge base, tracked in git)
#   1.0.json       — our local version with additions (used by generate.sh)

set -euo pipefail

# Find python: prefer venv, fall back to system
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ -x "$SCRIPT_DIR/.venv/Scripts/python.exe" ]; then
    PYTHON="$SCRIPT_DIR/.venv/Scripts/python.exe"
elif [ -x "$SCRIPT_DIR/.venv/bin/python" ]; then
    PYTHON="$SCRIPT_DIR/.venv/bin/python"
else
    PYTHON="python"
fi

SPEC_URL="https://app.swaggerhub.com/apiproxy/registry/metquayinc-c94/Metquay.API.CRUD/1.0.0-jgi?format=json"
UPSTREAM="upstream.json"
OURS="1.0.json"
FETCHED=".fetched-spec.json"

MODE="${1:-}"

# --- Step 1: Fetch ---
echo "=== Step 1: Fetch upstream spec ==="
curl -s "$SPEC_URL" > "$FETCHED"
echo "✓ Fetched."

# --- Step 2: Compare upstream changes ---
echo ""
echo "=== Step 2: Check for upstream changes ==="
UPSTREAM_CHANGED=false
if [ ! -f "$UPSTREAM" ]; then
    echo "No $UPSTREAM found — creating initial baseline."
    cp "$FETCHED" "$UPSTREAM"
    echo "✓ Created $UPSTREAM"
elif diff -q "$FETCHED" "$UPSTREAM" > /dev/null 2>&1; then
    echo "✓ No upstream changes since last fetch."
else
    UPSTREAM_CHANGED=true
    echo "⚠ Upstream spec has changed!"
    echo ""
    $PYTHON compare_spec.py "$UPSTREAM" "$FETCHED" || true
fi

# --- Step 3: Show local additions ---
echo ""
echo "=== Step 3: Local additions (ours vs upstream) ==="
$PYTHON compare_spec.py "$FETCHED" "$OURS" || true

# --- Step 4: Merge (if requested and upstream changed) ---
if [ "$UPSTREAM_CHANGED" = true ]; then
    if [ "$MODE" = "--merge" ] || [ "$MODE" = "--full" ]; then
        echo ""
        echo "=== Step 4: Three-way merge ==="
        $PYTHON merge_spec.py "$UPSTREAM" "$OURS" "$FETCHED" -o "$OURS"
        echo ""
        echo "Updating upstream baseline..."
        cp "$FETCHED" "$UPSTREAM"
        echo "✓ upstream.json updated to latest."
    else
        echo ""
        echo "=== Step 4: Merge (skipped — run with --merge or --full) ==="
        echo "  To merge:  $PYTHON merge_spec.py $UPSTREAM $OURS $FETCHED"
        echo "  Then:      cp $FETCHED $UPSTREAM"
    fi
else
    echo ""
    echo "=== Step 4: Merge (not needed — no upstream changes) ==="
fi

# --- Step 5: Regenerate (if --full) ---
if [ "$MODE" = "--full" ]; then
    echo ""
    echo "=== Step 5: Regenerate SDK ==="
    bash generate.sh
    echo "✓ SDK regenerated."
else
    echo ""
    echo "=== Step 5: Regenerate (skipped — run with --full) ==="
fi

# Clean up
rm -f "$FETCHED"

echo ""
echo "Done."
