"""The Router Confesses — make.fun entry.

Writes one line (<=200 characters) in which a home Wi-Fi router excuses
itself for dropping the connection at the climax of a movie.

Deterministic: no network, no randomness, no time, no environment input.
The text is a fixed constant; the program only writes it to /output/entry.txt.
"""

import os

ENTRY = (
    "Sorry \u2014 I fainted. The twist was so good I forgot I was a router "
    "and just stood there, stunned, like you."
)


def main() -> None:
    # Self-check gate (mirrors the competition gate in RULES.txt):
    # 1-200 characters, not only whitespace, single line, no control chars.
    assert isinstance(ENTRY, str)
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of 1..200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert all(ord(ch) >= 0x20 and ord(ch) != 0x7F for ch in ENTRY), (
        "entry must contain no control characters"
    )
    ENTRY.encode("utf-8")  # must be valid UTF-8 text

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
