"""make.fun entry: Everyday Things, Two Lines, Longer Run.

Writes the two-line entry text to entry.txt in the output directory.
Line 1 explains a traffic jam to a 10-year-old through one analogy;
line 2 says honestly what that analogy maps and what it leaves out.
"""

import os

LINE1 = (
    "A traffic jam is a giant zipper made of cars: each car is a tooth, "
    "and a tooth can only slide forward when the tooth in front of it "
    "moves first."
)
LINE2 = (
    "It maps why one slow car can freeze a whole road behind it, but it "
    "leaves out that drivers are not really teeth: they can change lanes, "
    "turn off, or just lose patience."
)

TEXT = LINE1 + "\n" + LINE2

MAX_CHARS = 400


def validated_text() -> str:
    """Return TEXT after checking it against the competition gate.

    The gate requires UTF-8 text of 1 to 400 characters, not only white
    space; this entry additionally must be exactly two non-empty lines.
    """
    data = TEXT.encode("utf-8")  # raises if not UTF-8 encodable
    assert data.decode("utf-8") == TEXT
    assert 1 <= len(TEXT) <= MAX_CHARS, f"entry is {len(TEXT)} chars"
    assert TEXT.strip(), "entry is only white space"
    lines = TEXT.split("\n")
    assert len(lines) == 2, f"entry must be exactly two lines, got {len(lines)}"
    assert all(line.strip() for line in lines), "each line must be non-empty"
    return TEXT


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    payload = (validated_text() + "\n").encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(payload)
    # Read the file back so a bad write can never pass silently.
    with open(path, "rb") as fh:
        assert fh.read() == payload, "written bytes differ from payload"


if __name__ == "__main__":
    main()
