# Entry: Write a single hugging-face emoji to /output/entry.txt
# This small program creates the output directory if necessary and writes
# exactly one emoji (🤗) followed by a newline, encoded in UTF-8.

import os

EMOJI = "\U0001F917"

if __name__ == "__main__":
    os.makedirs("/output", exist_ok=True)
# file must contain only the emoji plus a trailing newline because the gate allows 1-8 characters
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI + "\n")
