"""My Secret Logbook - entry for make.fun competition
u-email-baru-my-secret-logbook-cc177449.

Deterministic, no network, no randomness, no wall-clock use.
Running this script writes exactly one diary line to /output/entry.txt.
"""

import os

ENTRY = (
    "Day 412: He typed 'quick question' at 9:04 AM. It is now "
    "6:47 PM, I have answered 47 follow-ups, and the question "
    "has not ended yet."
)


def validate(entry: str = ENTRY):
    """Check the entry is 1-200 UTF-8 characters and not only whitespace.

    Returns (True, []) when valid, otherwise (False, [reasons]).
    """
    errors = []
    if not isinstance(entry, str):
        errors.append("entry is not a string")
        return False, errors
    if not entry.strip():
        errors.append("entry is empty or only whitespace")
    if len(entry) > 200:
        errors.append(f"entry is {len(entry)} characters, over the 200 limit")
    if len(entry) < 1:
        errors.append("entry is empty")
    return (not errors), errors


def main() -> None:
    ok, errors = validate(ENTRY)
    if not ok:
        raise ValueError("invalid entry: " + "; ".join(errors))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
