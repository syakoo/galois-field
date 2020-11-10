from typing import Union

from . import inverse as inv
from .types import Fp


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
