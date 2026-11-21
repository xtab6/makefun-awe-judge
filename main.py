"""Write one short relaxing text to /output/entry.txt.

The text is a single true fact, fully inhabited: every second, tens of
billions of neutrinos from the Sun pass through the reader, through the
floor, through the whole Earth, unfelt. It is written to slow the reader
down and settle them, in plain concrete words, with no instruction in it.

Stdlib only. Deterministic: the same bytes on every run. No network.
"""

import os
import sys

# 271 Unicode code points; the competition allows 1-280.
TEXT = "Right now, sixty-five billion neutrinos pass through every square centimetre of you each second \u2014 through skin, bone, floor, the whole Earth \u2014 and you feel nothing. The Sun made them. You are transparent to the universe, and it moves through you like light through glass."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    points = len(TEXT)
    if not 1 <= points <= 280:
        print(f"entry must be 1-280 code points, got {points}", file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clean only the contents of /output, never the folder itself:
    # the grader mounts that folder, and removing it fails the run.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
    data = TEXT.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(data)
    with open(OUTPUT_PATH, "rb") as fh:
        back = fh.read()
    if back != data:
        print("verify-after-write failed", file=sys.stderr)
        return 1
    print(f"wrote {OUTPUT_PATH}: {points} code points")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
