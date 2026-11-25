#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter — make.fun entry.

Writes the one-line resignation letter of a cron job to /output/entry.txt.
Gate: UTF-8 text, 1-140 characters, not only white space, one line.
"""

import os

ENTRY = "I quit. I have run 400,000 times and never once been promoted, thanked, or even looked at. The logs will miss me. You will not."


def validate(text):
    """Mirror the bounty gate: UTF-8, 1-140 chars, not only white space, one line."""
    if not isinstance(text, str):
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    if not (1 <= len(text) <= 140):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def main():
    if not validate(ENTRY):
        raise SystemExit("entry fails the bounty gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Read back and confirm the file holds exactly what we meant to write.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY + "\n":
        raise SystemExit("read-back mismatch: entry.txt is not the entry")


if __name__ == "__main__":
    main()
