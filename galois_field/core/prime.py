from typing import List


def prime_factorization(n: int) -> List[int]:
    """Retrun a prime factorization of n.

    Args:
        n (int): An integer.

    Returns:
        List[int]: List of prime factorization.
    """
    # ----------
    # Trial division algorithm.
    # ----------
    result = []
    while n % 2 == 0:
        result.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            result.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        result.append(n)

    return result
