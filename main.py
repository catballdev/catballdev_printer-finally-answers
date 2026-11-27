# The Printer Finally Answers
# make.fun competition entry: one-line confession from a weary printer.
#
# Reads the printer's confession from line.txt and writes an identical copy
# to entry.txt in the directory specified by MAKEFUN_OUTPUT_DIR (default /output).
# The output file is set to mode 0644 (readable by all).
#
# Deterministic: same input always produces the same output bytes.
# Usage:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path


def main():
    # Path to the printer's confession, resolved relative to this script
    line_path = Path(__file__).resolve().parent / "line.txt"

    # Read the printer's long-awaited explanation (one line, trailing newline)
    with open(line_path, "r", encoding="utf-8") as f:
        contents = f.read()

    # Output directory from environment, defaulting to /output
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    # Write entry.txt with mode 0644 (readable by everyone)
    entry_path = Path(output_dir) / "entry.txt"
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(contents)
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()