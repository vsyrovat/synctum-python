def broken_search(ar: list[int], value: int) -> int:
    if len(ar) == 0:
        return -1
    if ar[0] == value:
        return 0
    if len(ar) > 1 and ar[len(ar) - 1] == value:
        return len(ar) - 1
    return _broken_search(ar, value, 0, len(ar) - 1)


def _broken_search(ar, value, a, b) -> int:
    if b <= a + 1:
        return -1
    c = a + sum(divmod(b - a, 2))
    if ar[c] == value:
        return c
    if ar[a] < ar[c]:
        if ar[a] < value and value < ar[c]:
            return _broken_search(ar, value, a, c)
        else:
            return _broken_search(ar, value, c, b)
    else:
        if ar[c] < value and value < ar[b]:
            return _broken_search(ar, value, c, b)
        else:
            return _broken_search(ar, value, a, c)
