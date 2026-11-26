import os

# Write a single sunflower emoji to entry.txt in the output directory.
EMOJI = "🌻"

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
# file must contain only the emoji plus a trailing newline because the gate allows 1-8 characters
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(EMOJI + "\n")

if __name__ == "__main__":
    main()