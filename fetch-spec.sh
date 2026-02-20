#!/usr/bin/env bash
# Fetch the latest upstream OpenAPI spec from SwaggerHub.
#
# Files:
#   upstream.json  — last-known upstream version (tracked in git, merge base)
#   1.0.json       — our local version with additions (used by generate.sh)
#
# This script fetches a fresh copy and compares it against upstream.json
# to detect upstream changes.  It does NOT modify 1.0.json.

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
FETCHED=".fetched-spec.json"

echo "Fetching upstream spec..."
curl -s "$SPEC_URL" > "$FETCHED"

# Compare against last-known upstream
if [ ! -f "$UPSTREAM" ]; then
    echo "No $UPSTREAM found — saving this as the initial baseline."
    cp "$FETCHED" "$UPSTREAM"
    echo "✓ Created $UPSTREAM"
elif diff -q "$FETCHED" "$UPSTREAM" > /dev/null 2>&1; then
    echo "✓ No upstream changes since last fetch."
else
    echo "⚠ Upstream spec has changed!"
    echo ""
    echo "Semantic diff (upstream.json → fresh download):"
    $PYTHON compare_spec.py "$UPSTREAM" "$FETCHED" || true
    echo ""
    echo "Next steps:"
    echo "  1. Review:      python compare_spec.py $UPSTREAM $FETCHED"
    echo "  2. Merge:       python merge_spec.py $UPSTREAM 1.0.json $FETCHED"
    echo "  3. Update base: cp $FETCHED $UPSTREAM"
    echo "  4. Regenerate:  bash generate.sh"
fi

echo ""
echo "Remaining local additions (ours vs upstream):"
$PYTHON compare_spec.py "$FETCHED" 1.0.json || true

# Clean up
rm -f "$FETCHED"