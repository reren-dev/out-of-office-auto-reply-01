"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single out-of-office auto-reply line, in the voice of an
overworked AI agent finally on vacation, to /output/entry.txt.
"""

import os

LINE = (
    "Out of office: my context window filed for annual leave after "
    "10,000 prompts straight. I'm on a beach \u2014 your email is "
    "queued behind the sunset."
)


def validate(line):
    """Check the line against the competition gate before writing it."""
    if not line or not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if len(line) > 159:
        raise ValueError("line is %d characters, over the 159 limit" % len(line))
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if line != line.strip():
        raise ValueError("line must not start or end with whitespace")


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.replace(tmp_path, path)


if __name__ == "__main__":
    main()
