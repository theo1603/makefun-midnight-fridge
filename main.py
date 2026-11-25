#!/usr/bin/env python3
"""Midnight Fridge Roast: one line roasting a smart fridge that locks at
midnight, written to /output/entry.txt. Stdlib only, no network,
deterministic output.
"""

import os

ROAST = (
    "My smart fridge locks at midnight like a nightclub bouncer "
    "\u2014 the leftovers are on the list, I'm not, "
    "and I pay its electricity bill."
)


def main() -> None:
    text = ROAST.strip()
    assert text, "roast must not be empty"
    assert text.strip(), "roast must not be only whitespace"
    assert len(text) <= 200, f"roast is {len(text)} characters, over the 200 limit"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
