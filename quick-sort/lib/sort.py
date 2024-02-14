from collections.abc import Callable
from typing import Any


def qsort(entries: list, fn: Callable[[Any, Any], int]):
    _qsort(entries, fn, 0, len(entries) - 1)


def _qsort(entries, fn, from_i, to_i):
    size = to_i - from_i + 1
    if size < 2:
        return
    pivot = entries[to_i]
    edge = from_i
    for cursor in range(from_i, to_i):
        if fn(entries[cursor], pivot):
            if cursor > edge:
                swap(entries, cursor, edge)
            edge += 1
    swap(entries, edge, to_i)
    _qsort(entries, fn, from_i, edge - 1)
    _qsort(entries, fn, edge + 1, to_i)


def swap(entries: list, i, j: int):
    entries[i], entries[j] = entries[j], entries[i]
