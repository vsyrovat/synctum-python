from typing import TypeAlias

# Name, Score, Penalty
Entry: TypeAlias = tuple[str, int, int]


def sign(a: Entry, b: Entry) -> int:
    if a[1] > b[1]:
        return 1
    if a[1] < b[1]:
        return -1
    if a[2] > b[2]:
        return -1
    if a[2] < b[2]:
        return 1
    if a[0] < b[0]:
        return 1
    if a[0] > b[0]:
        return -1
    return 0


def gt(a: Entry, b: Entry) -> bool:
    return sign(a, b) == 1
