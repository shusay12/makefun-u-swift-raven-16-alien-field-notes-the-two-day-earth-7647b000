#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line -- an alien tourist's review of Earth -- to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The line is a fixed, hand-crafted text: deterministic, stdlib only, no
network, no file reads outside this script. The gate requires UTF-8 text
of 1 to 200 characters, not only white space.
"""

import os
import sys

# v3: verdict line now judges the locals ("Lovely planet, baffling
# locals") instead of repeating the planet, so the review's verdict
# and the joke's subject match.
ENTRY = (
    "Came to Earth for the weekend. The locals scoop their pets' "
    "droppings into little bags and carry them around like treasure. "
    "Lovely planet, baffling locals - 4/5 stars, would abduct again."
)


def main() -> int:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry length {len(text)} out of range 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only white space", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
