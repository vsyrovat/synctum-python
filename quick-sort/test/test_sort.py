import pytest

from lib.entry import gt, sign
from lib.sort import qsort, swap


@pytest.mark.parametrize(
    "given,cmp,expected",
    [
        ([1, 2], lambda a, b: a < b, [1, 2]),
        ([2, 1], lambda a, b: a < b, [1, 2]),
        ([1, 2], lambda a, b: a > b, [2, 1]),
        ([2, 1], lambda a, b: a > b, [2, 1]),
        ([3, 2, 1], lambda a, b: a < b, [1, 2, 3]),
        ([2, 3, 1], lambda a, b: a < b, [1, 2, 3]),
        ([1, 2, 3, 4, 3, 5], lambda a, b: a < b, [1, 2, 3, 3, 4, 5]),
        ([5, 3, 2, 4], lambda a, b: a < b, [2, 3, 4, 5]),
        (
            [9, 3, 7, 4, 8, 1, 1, 9, -4],
            lambda a, b: a < b,
            [-4, 1, 1, 3, 4, 7, 8, 9, 9],
        ),
        (
            [9, 3, 7, 4, 8, 1, 1, 9, -4],
            lambda a, b: a > b,
            [9, 9, 8, 7, 4, 3, 1, 1, -4],
        ),
    ],
)
def test_qsort_numeric(given, cmp, expected):
    qsort(given, cmp)
    assert given == expected


@pytest.mark.parametrize(
    "given,expected",
    [
        ([], []),
        ([("alla", 4, 6), ("gena", 6, 1000)], [("gena", 6, 1000), ("alla", 4, 6)]),
        (
            [("alla", 4, 6), ("gena", 6, 1000), ("gosha", 2, 90)],
            [("gena", 6, 1000), ("alla", 4, 6), ("gosha", 2, 90)],
        ),
        (
            [
                ("alla", 4, 100),
                ("gena", 6, 1000),
                ("gosha", 2, 90),
                ("rita", 2, 90),
                ("timofey", 4, 80),
            ],
            [
                ("gena", 6, 1000),
                ("timofey", 4, 80),
                ("alla", 4, 100),
                ("gosha", 2, 90),
                ("rita", 2, 90),
            ],
        ),
        (
            [
                ("alla", 0, 0),
                ("gena", 0, 0),
                ("gosha", 0, 0),
                ("rita", 0, 0),
                ("timofey", 0, 0),
            ],
            [
                ("alla", 0, 0),
                ("gena", 0, 0),
                ("gosha", 0, 0),
                ("rita", 0, 0),
                ("timofey", 0, 0),
            ],
        ),
    ],
)
def test_qsort(given, expected):
    qsort(given, lambda a, b: sign(a, b) > 0)
    assert given == expected


def test_swap():
    entries = [("alla", 1, 1), ("gena", 2, 2)]
    swap(entries, 0, 1)
    assert entries == [("gena", 2, 2), ("alla", 1, 1)]
