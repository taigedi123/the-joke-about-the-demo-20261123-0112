#!/usr/bin/env python3
"""Write one one-line joke about demos crashing beside an AI coding agent."""

import os

JOKE = (
    "My coding agent didn't panic when the demo crashed live — it calmly "
    "presented the post-mortem it had written yesterday."
)


def main() -> None:
    text = JOKE.strip()
    assert "\n" not in text and "\r" not in text, "joke must be a single line"
    assert 1 <= len(text) <= 280, f"joke must be 1-280 characters, got {len(text)}"
    try:
        out_dir = "/output"
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(text)
    except OSError:
        out_dir = os.path.join(".", "output")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(text)
    print(f"{len(text)} characters -> {out_path}")


if __name__ == "__main__":
    main()
