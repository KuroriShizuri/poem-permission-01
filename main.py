#!/usr/bin/env python3
"""Write a short poem about permission to /output/entry.txt.

Deterministic, stdlib only, no network. The poem is a fixed string
constant; the program simply writes it to /output/entry.txt.

Design: the poem treats agency as the power to ask and be given — not
the key itself, but the question. The turn is that the asking is the
gift: nothing is handed over except the asking, and a door opens only
when the knock becomes someone else's hands. Permission is therefore
framed as a question that learned to lift, rather than a possession
to be kept or granted.
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
    if not POEM:
        raise SystemExit("poem is empty; nothing to write")
    if len(POEM) > 280:
        raise SystemExit(
            f"poem too long: {len(POEM)} code points (max 280)"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
