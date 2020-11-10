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
    if isinstance(coeffs, Fpn):
        return coeffs % p

    return np.array([modulus_el(el, p) for el in coeffs], int)
