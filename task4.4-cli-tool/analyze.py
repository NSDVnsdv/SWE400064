#!/usr/bin/env python3
"""
Word-frequency analyzer (non-web CLI tool, Task 4.4).

Reads a text file, counts word frequencies, and writes a report.
Designed to run as a one-shot container: it does its job, logs progress
to stdout, and exits (exit code 0 on success, 1 on failure) rather than
running as a long-lived service like a web app.

Typical usage inside the container:
    python analyze.py --input /data/input/input.txt --output /data/output/report.txt --top 10
"""

import argparse
import logging
import re
import sys
from collections import Counter
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("analyze")


def parse_args():
    parser = argparse.ArgumentParser(description="Word-frequency analyzer CLI tool")
    parser.add_argument(
        "--input", default="/data/input/input.txt", help="Path to the input text file"
    )
    parser.add_argument(
        "--output", default="/data/output/report.txt", help="Path to write the report to"
    )
    parser.add_argument(
        "--top", type=int, default=10, help="Number of top words to report"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)

    log.info("Starting word-frequency analysis")
    log.info("Input file:  %s", input_path)
    log.info("Output file: %s", output_path)

    if not input_path.exists():
        log.error("Input file not found: %s", input_path)
        sys.exit(1)

    text = input_path.read_text(encoding="utf-8", errors="ignore").lower()
    words = re.findall(r"[a-z']+", text)
    log.info("Read %d words from input file", len(words))

    counts = Counter(words)
    top_words = counts.most_common(args.top)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        f.write("Word Frequency Report\n")
        f.write("======================\n")
        f.write(f"Total words analyzed: {len(words)}\n")
        f.write(f"Unique words: {len(counts)}\n\n")
        f.write(f"Top {args.top} words:\n")
        for rank, (word, count) in enumerate(top_words, start=1):
            line = f"{rank:2d}. {word:<15} {count}\n"
            f.write(line)
            log.info(line.strip())

    log.info("Report written to %s", output_path)
    log.info("Analysis complete. Exiting 0.")


if __name__ == "__main__":
    main()
