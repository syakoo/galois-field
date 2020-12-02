from functools import reduce
import random as rd
from typing import List, Union
from itertools import combinations

from . import prime
from .ElementInGFp import ElementInGFp
from .ElementInGFpn import ElementInGFpn


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
        prime_factories = prime.prime_factorization(el.p - 1)
        print(prime_factories)

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

    for _ in range(p*2):
        value = rd.randint(1, p-1)
        el = ElementInGFp(value, p)
        if is_primtive_root(el, factories):
            return el
