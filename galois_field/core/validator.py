import numpy as np

from . import gcd, modulus


def is_irreducible_poly(poly: np.poly1d, p: int) -> bool:
    """Detect whether a polynomial is irreducible or not.

    Args:
        poly (np.poly1d): A polynomial.
        p (int): A prime number.

    Returns:
        bool: Is the polynomial irreducible.
    """
    gx = np.poly1d([1, 0])
    for _ in range(1, len(poly.coeffs)//2 + 1):
        gx = modulus.modulus_pow_poly(gx, p, p, poly)
        if (gx == np.poly1d([1, 0])):
            # if gx = x (mod poly), x is the root of a smaller polynomial.
            return False
        gcd_poly = gcd.gcd_poly(
            poly, modulus.modulus_poly_over_fp(gx + np.poly1d([p-1, 0]), p), p)
        if len(gcd_poly.coeffs) != 1:
            return False

    return True
