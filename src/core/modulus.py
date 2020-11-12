from typing import Any, Union

import numpy as np
from nptyping import NDArray

from . import inverse as inv
from .types import Fp, Fpn


def modulus_el(el: Union[Fp, float], p: int) -> Fp:
    """Compute an element modulo p.

    Args:
        el (Union[Fp, float]): An element in Fp. Could also be a float value.
        p (int): A prime number.

    Returns:
        Fp: An element modulo p.
    """
    if isinstance(el, Fp):
        return el % p

    inte, deci = map(int, str(el).split('.'))
    if deci == 0:
        return el % p
    elif inte == 0:
        return 0

    return inte * inv.inverse_el(deci, p) % p


def modulus_coeffs(coeffs: Union[Fpn, NDArray[Any, float]], p: int) -> Fpn:
    """Compute all coefficients modulo p.

    Args:
        coeffs (Union[Fpn, NDArray[Any, float]]): Coefficients in Fp.
        p (int): A prime number.

    Returns:
        Fpn: Coefficients modulo p.
    """
    if isinstance(coeffs, Fpn):
        return coeffs % p

    return np.array([modulus_el(el, p) for el in coeffs], int)


def modulus_poly(poly1: np.poly1d, poly2: np.poly1d, p: int) -> np.poly1d:
    """Compute a polynomial modulo poly2.

    Args:
        poly1 (np.poly1d): An Element in Fpn.
        poly2 (np.poly1d): a monic irreducible polynomial.
        p (int): A prime number.

    Returns:
        np.poly1d: A polynomial modulo poly2.
    """
    _, r = np.polydiv(poly1, poly2)
    coeffs = modulus_coeffs(r.coeffs, p)

    return np.poly1d(coeffs)


def modulus_pow_poly(poly: np.poly1d, e: int,
                     p: int, mod_poly: np.poly1d) -> np.poly1d:
    ans = 1
    for _ in range(e):
        ans = modulus_poly(ans * poly, mod_poly, p)

    return ans
