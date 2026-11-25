#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes one original one-line office joke to /output/entry.txt.
Pure stdlib; deterministic.
"""

import os

JOKE = "The office fridge says 'label your food,' so I labeled mine 'evidence' \u2014 nobody's touched it since."


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
