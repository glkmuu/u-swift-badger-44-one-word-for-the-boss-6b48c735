#!/usr/bin/env python3
"""One Word for the Boss — writes a single word describing the boss.

Reads entry.txt next to this script, validates the competition gate
(UTF-8, 1-30 characters, not only whitespace, a single word), and writes
the validated word (no trailing newline) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Standard library only, deterministic, no network.
"""

import os
import sys


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(script_dir, "entry.txt")
    if not os.path.isfile(src):
        sys.exit(f"missing {src}")
    with open(src, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    word = text.strip()
    if not word:
        sys.exit("entry is empty or only whitespace")
    if len(word) > 30:
        sys.exit("entry exceeds 30 characters")
    if any(ch.isspace() for ch in word):
        sys.exit("entry must be a single word with no spaces")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as f:
        f.write(word.encode("utf-8"))
    print(f"wrote {word!r} ({len(word)} characters) to {out_path}")


if __name__ == "__main__":
    main()
