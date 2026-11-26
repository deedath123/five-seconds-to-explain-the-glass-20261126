"""make.fun entry: a house cat's defence after knocking a glass off the table."""

import os

ENTRY = "It stared at me for three hours straight from the edge, so I ended the standoff — the floor and I have an understanding."


def _validate(entry):
    expected = "It stared at me for three hours straight from the edge, so I ended the standoff — the floor and I have an understanding."
    if entry != expected:
        raise ValueError("ENTRY does not match the approved entry text")
    if not 1 <= len(entry) <= 200:
        raise ValueError("ENTRY must be 1-200 chars")
    if not entry.strip():
        raise ValueError("ENTRY must not be only whitespace")
    return entry


def main():
    _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
