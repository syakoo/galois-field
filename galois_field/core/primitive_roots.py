from functools import reduce
from galois_field.core.prime import prime_factorization
from typing import List, Union
from itertools import combinations

from . import types, prime


def is_primtive_root_over_Fp(el: types.Fp, p: int,
                             prime_factories: Union[None, List[int]] = None) -> bool:
    """Determining whether a primitive root.

    Args:
        el (types.Fp): An element in GF(p).
        p (int): A prime number.
        prime_factories (Union[None, List[int]], optional): 
            List of prime factorization of el. Defaults to None.

    Returns:
        bool: Is the el a primitive root.
    """
    if prime_factories is None:
        prime_factories = prime.prime_factorization(p - 1)
        print(prime_factories)

    for i in range(1, len(prime_factories)):
        for facts in combinations(prime_factories, i):
            exp = reduce(lambda a, b: a*b, facts, 1)
            # el is not a primitive root
            # if and only if el^exp == 1 s.t. exp | p-1.
            if pow(el, exp, p) == 1:
                return False

    return True
