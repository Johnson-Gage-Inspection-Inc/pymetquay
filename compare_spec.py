#!/usr/bin/env python3
"""Semantic comparison of two OpenAPI spec JSON files.

Uses DeepDiff for robust structural comparison. Reports added, removed,
and changed properties grouped by schema, giving a clear picture of
structural differences rather than raw line diffs.

Usage:
    python compare_spec.py <file_a> <file_b>
    python compare_spec.py upstream.json 1.0.json      # what we added locally
    python compare_spec.py upstream.json theirs.json    # what they changed upstream

Exit codes:
    0 - no differences found
    1 - differences found
    2 - error (file not found, invalid JSON, etc.)
"""

import json
import re
import sys
from pathlib import Path

from deepdiff import DeepDiff


def path_to_dotted(path: str) -> str:
    """Convert DeepDiff's root['key1']['key2'] notation to dotted paths."""
    # root['components']['schemas']['Foo'] → components.schemas.Foo
    parts = re.findall(r"\['([^']+)'\]|\[(\d+)\]", path)
    segments = []
    for key, idx in parts:
        segments.append(key if key else f"[{idx}]")
    return ".".join(segments)


def group_by_schema(
    paths: list[str],
) -> dict[str, list[str]]:
    """Group dotted paths by schema or endpoint for readability."""
    schema_prefix = "components.schemas."
    grouped: dict[str, list[str]] = {}

    for path in paths:
        if path.startswith(schema_prefix):
            rest = path[len(schema_prefix) :]  # noqa: E203
            schema_name = rest.split(".")[0]
            key = f"Schema: {schema_name}"
        elif path.startswith("paths."):
            parts = path.split(".")
            endpoint = ".".join(parts[:2]) if len(parts) >= 2 else parts[0]
            key = f"Endpoint: {endpoint}"
        else:
            key = "Other"

        grouped.setdefault(key, []).append(path)

    return grouped


def main() -> int:
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <file_a> <file_b>")
        print("  Compares file_a (old/base) against file_b (new/modified).")
        print("  Reports what was added/removed/changed going from A to B.")
        return 2

    file_a, file_b = Path(sys.argv[1]), Path(sys.argv[2])

    for f in (file_a, file_b):
        if not f.exists():
            print(f"Error: {f} not found", file=sys.stderr)
            return 2

    try:
        with open(file_a, encoding="utf-8") as fa:
            data_a = json.load(fa)
        with open(file_b, encoding="utf-8") as fb:
            data_b = json.load(fb)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON - {e}", file=sys.stderr)
        return 2

    diff = DeepDiff(data_a, data_b, verbose_level=2)

    if not diff:
        print(f"✓ No differences between {file_a} and {file_b}")
        return 0

    # Collect all changes into a flat list for display
    entries: list[tuple[str, str, str]] = []  # (type, path, detail)

    for raw_path in diff.get("dictionary_item_added", []):
        entries.append(("added", path_to_dotted(raw_path), ""))

    for raw_path in diff.get("dictionary_item_removed", []):
        entries.append(("removed", path_to_dotted(raw_path), ""))

    for raw_path, change in diff.get("values_changed", {}).items():
        old = json.dumps(change["old_value"], ensure_ascii=False)
        new = json.dumps(change["new_value"], ensure_ascii=False)
        entries.append(("changed", path_to_dotted(raw_path), f"{old} → {new}"))

    for raw_path, change in diff.get("type_changes", {}).items():
        old_type = type(change["old_value"]).__name__
        new_type = type(change["new_value"]).__name__
        entries.append(
            (
                "changed",
                path_to_dotted(raw_path),
                f"type {old_type} → {new_type}",
            )
        )

    for raw_path in diff.get("iterable_item_added", {}):
        entries.append(("added", path_to_dotted(raw_path), ""))

    for raw_path in diff.get("iterable_item_removed", {}):
        entries.append(("removed", path_to_dotted(raw_path), ""))

    print(f"Comparing {file_a} → {file_b}")
    print(f"Found {len(entries)} difference(s):\n")

    # Group and display
    all_paths = [path for _, path, _ in entries]
    path_info = {path: (dtype, detail) for dtype, path, detail in entries}
    grouped = group_by_schema(all_paths)

    symbols = {"added": "+", "removed": "-", "changed": "~"}
    labels = {"added": "ADDED", "removed": "REMOVED", "changed": "CHANGED"}

    for group_name in sorted(grouped):
        paths = grouped[group_name]
        print(f"  {group_name} ({len(paths)} changes)")
        for path in sorted(paths):
            dtype, detail = path_info[path]
            suffix = f"  ({detail})" if detail else ""
            symbol = symbols[dtype]
            label = labels[dtype]
            print(f"  {symbol} {label:>8}  {path}{suffix}")
        print()

    return 1


if __name__ == "__main__":
    sys.exit(main())
