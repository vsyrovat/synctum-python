import pytest

from lib.circular import broken_search


# fmt: off
@pytest.mark.parametrize("array,search_value,expected", [
    ([19, 21, 100, 101, 1, 4, 5, 7, 12], 5, 6),
    ([19, 21, 100, 101, 1, 4, 5, 7, 12], 9, -1),
    ([1, 4, 5, 7, 12, 19, 21, 100, 101], 5, 2),
    ([19, 21, 100, 101, 1, 4, 5, 7, 12], 19, 0),
    ([19, 21, 100, 101, 1, 4, 5, 7, 12], 12, 8),
    ([19, 21, 100, 101, 1, 4, 5, 7, 12], 200, -1),
    ([5, 1], 1, 1),
])
# fmt: on
def test_broken_search(array, search_value, expected):
    assert broken_search(array, search_value) == expected
