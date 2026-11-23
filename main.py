#!/usr/bin/env python3
"""One-word entry for the make.fun bounty
"u-0xkianno-one-word-from-grandma-f04bed16".

Writes the single word a grandma would text about AI to entry.txt.
Python 3.13, standard library only. Deterministic: no network access,
no clock reads, no randomness.
"""

import os
from pathlib import Path

WORD = "Robit"


def validate_word(word: str) -> None:
    """The entry must be exactly one word: non-empty, no whitespace."""
    if not word:
        raise ValueError("entry word must not be empty")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word (no spaces)")


def resolve_out_dir() -> Path:
    """Prefer $MAKEFUN_OUTPUT (default /output); fall back to ./output
    if the primary location is not writable."""
    primary = Path(os.environ.get("MAKEFUN_OUTPUT", "/output"))
    try:
        primary.mkdir(parents=True, exist_ok=True)
        probe = primary / ".write-test"
        probe.write_text("", encoding="utf-8")
        probe.unlink()
        return primary
    except OSError:
        fallback = Path("./output")
        fallback.mkdir(parents=True, exist_ok=True)
        return fallback


def main() -> int:
    validate_word(WORD)
    out_dir = resolve_out_dir()
    path = out_dir / "entry.txt"
    text = WORD + "\n"
    path.write_text(text, encoding="utf-8")
    # Verify the written file by reading it back.
    if path.read_text(encoding="utf-8") != text:
        raise RuntimeError("verification failed: entry.txt content mismatch")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
