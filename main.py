"""One Word for Your Wi-Fi — entry program.

Writes a single word to the grader's output file. The word names the
entrant's home Wi-Fi the way it actually behaves: it vanishes in the
middle of a call, mid-download, mid-sentence — it ghosts you.
"""

import os
import sys


WORD = "Ghosting"


def output_dir():
    """Return the directory the grader wants the entry in."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or "./output"
    return chosen


def valid(word):
    """Gate mirror: 1 to 20 characters of UTF-8 text, not only space."""
    if not isinstance(word, str):
        return False
    if not 1 <= len(word) <= 20:
        return False
    return word.strip() != ""


def report(word, target):
    """Print a one-line summary of what the entry did, for the log."""
    size = len(word.encode("utf-8"))
    print("entry %r (%d bytes) written to %s" % (word, size, target))


def main():
    if not valid(WORD):
        print("entry word fails the gate", file=sys.stderr)
        return 1
    folder = output_dir()
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)
    report(WORD, target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
