#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Writes the entrant's own make.fun username — one word, nothing else —
to /output/entry.txt, per the competition rules (single word, at most
30 characters, UTF-8, not only whitespace).
"""

import os

USERNAME = "akhmad045"

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(text: str) -> None:
    """Gate: 1-30 UTF-8 chars, one word, no padding."""
    if not text or text != text.strip():
        raise SystemExit("entry must not be blank or padded")
    if any(ch.isspace() for ch in text):
        raise SystemExit("entry must be a single word (no whitespace)")
    if not 1 <= len(text) <= 30:
        raise SystemExit("entry must be 1-30 characters")


def main() -> None:
    validate(USERNAME)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(USERNAME)

    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    if raw.decode("utf-8") != USERNAME:
        raise SystemExit("round-trip check failed")
    if len(raw) != len(USERNAME.encode("utf-8")):
        raise SystemExit("byte-length check failed")
    print(f"wrote {len(USERNAME)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
