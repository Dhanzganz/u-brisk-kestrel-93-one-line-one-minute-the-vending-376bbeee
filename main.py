"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single original pickup line, spoken by a vending machine to a
passing human, to /output/entry.txt.
"""

import os

ENTRY = "I only take exact change, but for you I'll take a chance \u2014 press B4 and see what drops."


def main() -> None:
    # Competition gate: /output/entry.txt must be UTF-8 text of 1 to 200
    # characters, not only white space. Fail loudly instead of writing
    # an entry the gate would refuse.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate allows 1-200"
    assert ENTRY.strip(), "entry must not be only white space"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
