#!/usr/bin/env python3
"""Three-way structural merge for OpenAPI spec JSON files.

Performs a JSON-aware three-way merge using:
  - base:   the common ancestor (last-known upstream, i.e. upstream.json)
  - ours:   our local version with additions (1.0.json)
  - theirs: the freshly-fetched upstream version

Logic:
  - Keys added only in ours → kept (our local extensions)
  - Keys added only in theirs → pulled in (upstream additions)
  - Keys added in both with same value → kept
  - Keys removed only in theirs → removed (they intentionally dropped it)
  - Keys removed only in ours → stays removed (we intentionally dropped it)
  - Keys changed in only one side → that side's change wins
  - Keys changed in both sides differently → CONFLICT (reported, ours kept)

Usage:
    python merge_spec.py <base> <ours> <theirs> [-o output]
    python merge_spec.py upstream.json 1.0.json theirs.json -o merged.json

Exit codes:
    0 - merge completed with no conflicts
    1 - merge completed but conflicts were found (ours kept for conflicts)
    2 - error
"""

import json
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any


class MergeResult:
    """Tracks merge outcomes and conflicts."""

    def __init__(self) -> None:
        self.merged: Any = None
        self.conflicts: list[str] = []
        self.ours_kept: list[str] = []
        self.theirs_added: list[str] = []
        self.theirs_removed: list[str] = []

    def report(self) -> str:
        lines = []
        if self.theirs_added:
            lines.append(f"  Upstream additions pulled in: {len(self.theirs_added)}")
            for p in self.theirs_added[:20]:
                lines.append(f"    + {p}")
            if len(self.theirs_added) > 20:
                remaining = len(self.theirs_added) - 20
                lines.append(f"    ... and {remaining} more")

        if self.ours_kept:
            lines.append(f"  Local additions preserved: {len(self.ours_kept)}")
            for p in self.ours_kept[:20]:
                lines.append(f"    ● {p}")
            if len(self.ours_kept) > 20:
                remaining = len(self.ours_kept) - 20
                lines.append(f"    ... and {remaining} more")

        if self.theirs_removed:
            lines.append(f"  Upstream removals applied: {len(self.theirs_removed)}")
            for p in self.theirs_removed[:20]:
                lines.append(f"    - {p}")
            if len(self.theirs_removed) > 20:
                remaining = len(self.theirs_removed) - 20
                lines.append(f"    ... and {remaining} more")

        if self.conflicts:
            lines.append(f"  ⚠ CONFLICTS (ours kept): {len(self.conflicts)}")
            for p in self.conflicts:
                lines.append(f"    ✗ {p}")

        return "\n".join(lines) if lines else "  No changes needed."


def three_way_merge(
    base: Any,
    ours: Any,
    theirs: Any,
    result: MergeResult,
    path: str = "",
) -> Any:
    """Recursively three-way merge JSON structures."""
    # If all three are identical, nothing to do
    if base == ours == theirs:
        return deepcopy(ours)

    # If both sides are dicts, merge structurally
    if isinstance(base, dict) and isinstance(ours, dict) and isinstance(theirs, dict):
        merged = {}
        all_keys = sorted(set(base.keys()) | set(ours.keys()) | set(theirs.keys()))

        for k in all_keys:
            child_path = f"{path}.{k}" if path else k
            in_base = k in base
            in_ours = k in ours
            in_theirs = k in theirs

            if in_base and in_ours and in_theirs:
                # Key exists in all three — recurse
                merged[k] = three_way_merge(
                    base[k], ours[k], theirs[k], result, child_path
                )

            elif not in_base and in_ours and not in_theirs:
                # Added only in ours — keep our addition
                merged[k] = deepcopy(ours[k])
                result.ours_kept.append(child_path)

            elif not in_base and not in_ours and in_theirs:
                # Added only in theirs — pull in their addition
                merged[k] = deepcopy(theirs[k])
                result.theirs_added.append(child_path)

            elif not in_base and in_ours and in_theirs:
                # Added in both sides
                if ours[k] == theirs[k]:
                    merged[k] = deepcopy(ours[k])
                else:
                    # Both added but different — conflict, keep ours
                    merged[k] = deepcopy(ours[k])
                    result.conflicts.append(child_path)

            elif in_base and in_ours and not in_theirs:
                # Removed in theirs
                if base[k] == ours[k]:
                    # We didn't change it, they removed it — apply removal
                    result.theirs_removed.append(child_path)
                else:
                    # We changed it, they removed it — conflict, keep ours
                    merged[k] = deepcopy(ours[k])
                    result.conflicts.append(child_path)

            elif in_base and not in_ours and in_theirs:
                # Removed in ours
                if base[k] == theirs[k]:
                    # They didn't change it, we removed it — stay removed
                    pass
                else:
                    # They changed it, we removed it — conflict, stay removed
                    result.conflicts.append(child_path)

            elif not in_base and not in_ours and not in_theirs:
                pass  # shouldn't happen

            elif in_base and not in_ours and not in_theirs:
                # Both removed — stay removed
                pass

        return merged

    # For non-dict values (scalars, lists)
    if ours == theirs:
        return deepcopy(ours)
    elif base == ours:
        # Only theirs changed — take theirs
        return deepcopy(theirs)
    elif base == theirs:
        # Only ours changed — keep ours
        return deepcopy(ours)
    else:
        # Both changed differently — conflict, keep ours
        result.conflicts.append(path)
        return deepcopy(ours)


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(
        description="Three-way structural merge for OpenAPI JSON specs."
    )
    parser.add_argument("base", help="Common ancestor (upstream.json)")
    parser.add_argument("ours", help="Our local version (1.0.json)")
    parser.add_argument("theirs", help="Fresh upstream version")
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="Output file (default: overwrite ours)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would happen without writing",
    )

    args = parser.parse_args()
    output_path = args.output or args.ours

    for name, fpath in [
        ("base", args.base),
        ("ours", args.ours),
        ("theirs", args.theirs),
    ]:
        if not Path(fpath).exists():
            print(f"Error: {name} file not found: {fpath}", file=sys.stderr)
            return 2

    try:
        with open(args.base, encoding="utf-8") as f:
            base = json.load(f)
        with open(args.ours, encoding="utf-8") as f:
            ours = json.load(f)
        with open(args.theirs, encoding="utf-8") as f:
            theirs = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON - {e}", file=sys.stderr)
        return 2

    result = MergeResult()
    result.merged = three_way_merge(base, ours, theirs, result)

    print("Merge results:")
    print(result.report())

    if args.dry_run:
        print(f"\nDry run — would write to {output_path}")
    else:
        with open(output_path, "w", encoding="utf-8", newline="\n") as f:
            json.dump(result.merged, f, ensure_ascii=False, indent=4)
            f.write("\n")
        print(f"\nMerged spec written to {output_path}")

    if result.conflicts:
        print(
            f"\n⚠ {len(result.conflicts)} conflict(s) — "
            "ours was kept. Review manually."
        )
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
