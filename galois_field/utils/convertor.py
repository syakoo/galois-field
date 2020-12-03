from typing import List


def dec2nary(value: int, n: int) -> List[int]:
    """Convert decimal to n-ary.

    Args:
        value (int): A decimal value.
        n (int): A number you want to convert.

    Returns:
        List[int]: n-ary.
    """
    r = value
    result = []
    while r > 0:
        r, q = r // n, r % n
        result.append(q)

    return result[::-1]
