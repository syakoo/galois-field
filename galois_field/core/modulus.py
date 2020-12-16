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


def modulus_poly_over_fp(poly: np.poly1d, p: int) -> np.poly1d:
    """Compute a polynomial modulo Fp.

    Args:
        poly (np.poly1d): An Element in Fpn.
        p (int): A prime number.

    Returns:
        np.poly1d: A polynomial modulo Fp.
    """
    coeffs = modulus_coeffs(poly.coeffs, p)
    return np.poly1d(coeffs)


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
    """Compute the e-th power of a polynomial modulo mod_poly.

    Args:
        poly (np.poly1d): An element in Fpn.
        e (int): An exponent.
        p (int): A prime number.
        mod_poly (np.poly1d): An monic irreducible polynomial.

    Returns:
        np.poly1d: the e-th power of a polynomial modulo mod_poly.
    """
    ans = 1
    cur_exp = 1
    stack_polys = [poly]
    # poly^e' === poly^e (over GF) s.t e' = e (mod p**n - 1)
    e %= p ** (len(mod_poly.coeffs) - 1) - 1
    if e == 0:
        return np.poly1d([1])

    while cur_exp*2 < e:
        cur_exp *= 2
        cur_poly = modulus_poly(stack_polys[-1]*stack_polys[-1], mod_poly, p)
        stack_polys.append(cur_poly)

    while 0 < e:
        e_times = e // cur_exp
        for _ in range(e_times):
            ans = modulus_poly(ans*stack_polys[-1], mod_poly, p)

        e -= e_times * cur_exp
        cur_exp //= 2
        stack_polys = stack_polys[:-1]

    return ans
