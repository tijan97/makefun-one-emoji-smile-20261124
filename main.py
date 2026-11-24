"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji to /output/entry.txt: U+1FAC2 PEOPLE HUGGING.
Two people in a warm embrace — the warmest single glyph in the set:
no words, no caption, just a hug. The judge picks the warmer of each
pair, and nothing reads warmer at a glance than two arms around someone.
"""

import os

EMOJI = "\U0001FAC2"  # 🫂 people hugging


def validate(text):
    """Enforce the brief's gate: exactly one emoji, nothing else."""
    if len(text) != 1:
        raise ValueError(f"entry must be exactly 1 character, got {len(text)}")
    if text.isspace():
        raise ValueError("entry must not be whitespace")
    code = ord(text)
    if not (0x1F000 <= code <= 0x1FAFF or 0x2600 <= code <= 0x27BF):
        raise ValueError(f"entry must be a single emoji, got U+{code:04X}")


def main():
    validate(EMOJI)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Read back and re-validate what was actually written.
    with open(path, "r", encoding="utf-8", newline="") as f:
        validate(f.read())
    print(f"entry: {EMOJI}")


if __name__ == "__main__":
    main()
