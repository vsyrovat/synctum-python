import argparse
import os
import sys

from lib.circular import broken_search


def load_file(input_file: str) -> (list[int], int):
    if not os.path.exists(input_file):
        print(f"File not found: {input_file}", file=sys.stderr)
        exit(1)
    with open(input_file, "r") as f:
        size = int(f.readline())
        search_value = int(f.readline())
        items = [int(x) for x in f.readline().split(" ")]
        if size != len(items):
            print(
                f"File {input_file} is corrupted, expected {size} entries but {len(items)} found",
                file=sys.stderr,
            )
            exit(1)
        return items, search_value


def main():
    parser = argparse.ArgumentParser("main")
    parser.add_argument(
        "input", help="Path to input file with unsorted results", type=str
    )
    args = parser.parse_args()
    items, search_value = load_file(args.input)
    pos = broken_search(items, search_value)
    print(pos)


if __name__ == "__main__":
    main()
