from functools import reduce
import random as rd
from typing import List, Union
from itertools import combinations
import math

import numpy as np

from . import prime
from .ElementInGFp import ElementInGFp
from .ElementInGFpn import ElementInGFpn
from ..utils import convertor


def is_primtive_root(el: Union[ElementInGFp, ElementInGFpn],
                     prime_factories: Union[None, List[int]] = None) -> bool:
    """Determining whether a primitive root.

    Args:
        el (Union[ElementInGFp, ElementInGFpn]): An element in GF(p) or GF(p^n).
        prime_factories (Union[None, List[int]], optional):
            List of prime factorization of el. Defaults to None.

    Returns:
        bool: Is the el a primitive root.
    """

    if prime_factories is None:
        ord_GF = el.p if isinstance(el, ElementInGFp) \
            else el.p**(len(el.mod_poly.coeffs)-1)
        prime_factories = prime.prime_factorization(ord_GF-1)

    if not prime_factories or el == 1:
        return False

    for i in range(1, len(prime_factories)):
        for facts in combinations(prime_factories, i):
            exp = reduce(lambda a, b: a*b, facts, 1)
            # el is not a primitive root
            # if and only if el^exp == 1 s.t. exp | p-1.
            if el**exp == 1:
                return False

    return True


def random_primitive_root_over_Fp(p: int) -> ElementInGFp:
    """Return the primitive root over GF(p) randomly.

    Args:
        p (int): A prime number.

    Returns:
        ElementInGFp: A primitive root over GF(p).
    """
    factories = prime.prime_factorization(p-1)

    # TODO: Huge amount of calculations X(.
    for value in rd.sample(list(range(1, p)), p-int(math.sqrt((p-1)/2))):
        el = ElementInGFp(value, p)
        if is_primtive_root(el, factories):
            return el


def random_primitive_root_over_Fpn(p: int, mod_coeffs: List[int]) -> ElementInGFpn:
    """Return the primitive root over GF(p^n) randomly.

    Args:
        p (int): A prime number.
        mod_coeffs  (List[int]): A coefficients of modulus polynomials.

    Returns:
        ElementInGFpn: A primitive root over GF(p^n).
    """
    q = p**(len(mod_coeffs)-1)
    factories = prime.prime_factorization(q-1)

    # TODO: Huge amount of calculations X(.
    for value in rd.sample(list(range(1, q)), q-int(math.sqrt((q-1)/2))):
        coeffs = convertor.dec2nary(value, p)

        el = ElementInGFpn(coeffs, p, np.poly1d(mod_coeffs))
        if is_primtive_root(el, factories):
            return el
