#!/usr/bin/env python3
"""Write a short poem about permission to /output/entry.txt.

Deterministic, stdlib only, no network. The poem is a fixed string
constant; the program simply writes it to /output/entry.txt.
"""

import os

POEM = """I asked, and nothing was handed to me —
except the asking itself.
A door is not opened for you.
It opens when your knock becomes
someone else's hands.
That is permission:
not a key kept, but a question
that learned to lift."""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
