"""Fortune Cookie Funnies for Engineers — make.fun entry.

Writes a single fortune-cookie line for a software engineer to
/output/entry.txt. Deterministic, offline, standard library only.
"""

import os

ENTRY = (
    "You will meet a stranger who fixes your bug tonight. "
    "The stranger is you, at 3 a.m., with no memory of writing it."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
