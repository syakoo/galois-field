import numpy as np

from . import modulus, inverse


def gcd_poly(poly1: np.poly1d, poly2: np.poly1d, p: int) -> np.poly1d:
    """Seek the gcd of two polynomials over Fp.

    Args:
        poly1 (np.poly1d): A polynomial.
        poly2 (np.poly1d): A polynomial.
        p (int): A prime number.

    Returns:
        np.poly1d: gcd(poly1, poly2) over Fp.
    """
    def poly2monic(p: np.poly1d) -> np.poly1d:
        highest_degree_coeff = p.coeffs[0]
        if highest_degree_coeff == 1:
            return p

        coeffs = p.coeffs * inverse.inverse_el(highest_degree_coeff, p)
        return np.poly1d(modulus.modulus_coeffs(coeffs, p))

    if len(poly1.coeffs) < len(poly2.coeffs):
        poly1, poly2 = poly2, poly1

    poly2_monic = poly2monic(poly2)
    _, r = np.polydiv(poly1, poly2_monic)
    r = np.poly1d(modulus.modulus_coeffs(r.coeffs, p))

    if r.coeffs[0] == 0:
        return poly2

    return gcd_poly(poly2, r, p)
