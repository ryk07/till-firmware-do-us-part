"""Entry for make.fun: Till Firmware Do Us Part.

Writes one original line (at most 200 characters) to /output/entry.txt:
a wedding vow that survives a firmware update — the update bricks
the toaster and resets the Wi-Fi password, yet still cannot patch
the way the speaker still looks at their love. Pure standard library,
no network, no reliance on the working directory.
"""

import os
from pathlib import Path

LINE = (
    "I vow to love you through every firmware update \u2014 even the one "
    "that bricked our toaster, reset the Wi-Fi password, and still "
    "couldn't patch the way I look at you."
)


def main() -> None:
    line = LINE
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry line is {len(line)} characters, must be 1-200")
    if not line.strip():
        raise ValueError("entry line must not be only whitespace")
    if line != line.strip():
        raise ValueError("entry line must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    target = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
