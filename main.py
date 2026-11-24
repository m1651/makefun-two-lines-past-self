#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun entry.

Writes a two-line warning to /output/entry.txt:
line 1 warns the past self about one specific moment in a single
sentence; line 2 says in one sentence why that moment mattered and
what changed because of it. Stdlib only, no network.
"""

import os

ENTRY_TEXT = (
    "Don't board the last train home on March 3rd \u2014 stay and submit "
    "the application before midnight.\n"
    "Missing that deadline cost me the scholarship, and losing it is why "
    "I never leave anything to the last night again."
)

MIN_CHARS = 1
MAX_CHARS = 280


def main():
    text = ENTRY_TEXT
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            "entry must be %d-%d chars, got %d" % (MIN_CHARS, MAX_CHARS, len(text))
        )
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    lines = text.split("\n")
    if len(lines) != 2:
        raise SystemExit("entry must be exactly two lines, got %d" % len(lines))
    # Each line must be a single sentence: exactly one sentence-ending
    # period, at the end of the line.
    for i, line in enumerate(lines, 1):
        if line.count(".") != 1 or not line.endswith("."):
            raise SystemExit("line %d must be exactly one sentence" % i)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote /output/entry.txt (%d chars)" % len(text))


if __name__ == "__main__":
    main()
