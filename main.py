#!/usr/bin/env python3
"""Funniest Autocorrect Fail - make.fun entry.

Writes a single line - one autocorrect fail, nothing else - to
/output/entry.txt, or to $MAKEFUN_OUTPUT_DIR/entry.txt when that
variable is set. No trailing newline, so the file holds exactly one
line of 1-199 UTF-8 characters.
"""

import os

LINE = "I miss you so much, can't wait to sue you"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
