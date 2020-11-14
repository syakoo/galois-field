from typing import Tuple

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
    def poly2monic(poly: np.poly1d)\
            -> Tuple[np.poly1d, Tuple[np.poly1d, np.poly1d]]:
        highest_degree_coeff = poly.coeffs[0]
        if highest_degree_coeff == 1:
            return poly, (np.poly1d([1]), np.poly1d([1]))

        inv_hdc = inverse.inverse_el(highest_degree_coeff, p)
        coeffs = poly.coeffs * inv_hdc
        return np.poly1d(modulus.modulus_coeffs(coeffs, p)),\
            (np.poly1d([highest_degree_coeff]), np.poly1d([inv_hdc]))

    if len(poly1.coeffs) < len(poly2.coeffs):
        poly1, poly2 = poly2, poly1

    poly2_monic, hdc = poly2monic(poly2)
    _, r = np.polydiv(poly1 * hdc[1], poly2_monic)
    r = np.poly1d(modulus.modulus_coeffs(r.coeffs, p)) * hdc[0]
    r = modulus.modulus_poly_over_fp(r, p)

    if r.coeffs[0] == 0:
        return poly2

    return gcd_poly(poly2, r, p)
