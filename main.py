#!/usr/bin/env python3
"""The Peanut Butter Marathon — a one-line laugh for make.fun.

The program writes a single funny line to /output/entry.txt, the artifact
the house judge reads. The line is a fixed, hand-written joke: a fitness
tracker celebrating steps that were earned by shaking a jar of peanut butter.

Why this line: the setup is an everyday truth (trackers count anything as
steps), the punch lands at the very end (the "workout" was shaking a jar),
and every word earns its place — 128 characters, one sentence.
"""

from __future__ import annotations

import os
import sys

LINE = (
    "My fitness tracker buzzed to congratulate me on hitting my daily step "
    "goal while I was violently shaking a jar of peanut butter."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    """Enforce the competition's own gate before writing anything.

    The sealed scorer accepts UTF-8 text of 1 to 200 characters that is not
    only white space, and the judge reads a single sentence. A line that
    fails the gate is never judged, so refuse to write it.
    """
    if not line.strip():
        raise ValueError("line must not be only white space")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, over the {MAX_CHARS} cap")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("line must stand alone as a single sentence")


def main() -> None:
    try:
        validate(LINE)
    except ValueError as exc:
        print(f"invalid entry line: {exc}", file=sys.stderr)
        raise SystemExit(1)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
