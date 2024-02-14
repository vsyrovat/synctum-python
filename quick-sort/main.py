import argparse
import os
import sys

from lib.entry import Entry, gt, sign
from lib.sort import qsort


def load_file(input_file: str) -> list[Entry]:
    if not os.path.exists(input_file):
        print(f"File not found: {input_file}", file=sys.stderr)
        exit(1)
    with open(input_file, "r") as f:
        size = int(f.readline())
        count = 0
        result: list[Entry] = [("", 0, 0)] * size
        while True:
            line = f.readline().strip()
            if not line:
                break
            if count < size:
                [login, score, penalties] = line.split(" ")
                entry = (login, int(score), int(penalties))
                result[count] = entry
            count += 1
        if count != size:
            print(
                f"File {input_file} is corrupted, expected {size} entries but {count} found",
                file=sys.stderr,
            )
            exit(1)
    return result


def main():
    parser = argparse.ArgumentParser("main")
    parser.add_argument(
        "input", help="Path to input file with unsorted results", type=str
    )
    args = parser.parse_args()
    entries = load_file(args.input)
    qsort(entries, lambda a, b: sign(a, b) > 0)
    for login, _, _ in entries:
        print(login)


if __name__ == "__main__":
    main()
