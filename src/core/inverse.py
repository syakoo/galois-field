import numpy as np

from . import modulus
from .types import Fp


def inverse_el(el: Fp, p: int) -> Fp:
    """Compute the inverse of an element over Fp

    Args:
        el (Fp): An element in Fp
        p (int): A prime number

    Returns:
        Fp: The inverse of the element over Fp
    """
    return pow(int(el), p-2, p)


def inverse_poly(poly: np.poly1d, p: int, mod_poly: np.poly1d) -> np.poly1d:
    if len(poly.coeffs) == 1:
        print(poly.coeffs, type(poly.coeffs[0]))
        inverse_of_el = inverse_el(poly.coeffs[0], p)
        return np.poly1d(np.array([inverse_of_el]))

    ans = 1
    for _ in range(p**(len(mod_poly.coeffs)-1)-2):
        ans = modulus.modulus_poly(ans * poly, mod_poly, p)

    return ans
