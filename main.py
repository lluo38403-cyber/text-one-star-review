"""One-Star Review of Something Essential — make.fun entry.

Writes a deadpan one-star review of sleep to /output/entry.txt.
The grievance is real — eight hours in, it still wakes you at
3 a.m. to worry — and the fix is nowhere in sight.
"""

import os

ENTRY = 'One star. Sleep: eight hours for a full charge, then it still wakes you up at 3 a.m. to worry. Would not recommend.'

MAX_CHARS = 160


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
