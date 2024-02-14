import pytest

from lib.entry import sign


@pytest.mark.parametrize(
    "given,expected",
    [
        ([("alla", 4, 6), ("gena", 6, 9)], -1),
        ([("gena", 6, 9), ("alla", 4, 6)], 1),
        ([("alla", 4, 6), ("olya", 4, 9)], 1),
        ([("olya", 4, 9), ("alla", 4, 6)], -1),
        ([("alla", 4, 6), ("igor", 4, 6)], 1),
        ([("igor", 4, 6), ("alla", 4, 6)], -1),
        ([("alla", 4, 6), ("alla", 4, 6)], 0),
    ],
)
def test_sign(given, expected):
    assert sign(*given) == expected
