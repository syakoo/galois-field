from __future__ import annotations
from typing import Any, Union, List

import numpy as np
from nptyping import NDArray

from .core.ElementInGFpn import ElementInGFpn
from .core import types, modulus, validator, primitive_roots as pr


class GFpn:
    """Galois Field: GF(p^n).

    Args:
        p (int): A prime number.
        mod_coeffs (Union[List[int], NDArray[Any, int]]):
            Coefficients of a monic irreducible polynomial.

    Examples:
        >>> from galois_field import GFpn

        In this case, p = 5, a monic irreducible polynomial = x^4 + 2.
        >>> gf = GFpn(5, [1, 0, 0, 0, 2])

        Generate the element in GF(5^4).
        >>> gf.elm([1, 2]) # 1x + 2
        ElementInGFpn([1, 2], 5, [1, 0, 0, 0, 2])

        >>> gf.elm([1, 2, 3, 4, 5]) # 2x^3 + 3x^2 + 4x + 3
        ElementInGFpn([2, 3, 4, 3], 5, [1, 0, 0, 0, 2])
    """

    def __init__(self, p: int,
                 mod_coeffs: Union[List[int], NDArray[Any, int]]):
        if not validator.is_prime(p):
            raise ValueError(f"{p} is not a prime number.")

        if not validator.is_irreducible_poly(np.poly1d(mod_coeffs), p):
            raise ValueError(
                f"{mod_coeffs} is not an irreducible polynomial over F{p}.")

        self.__p = p

        modulus_mod_coeffs = modulus.modulus_coeffs(np.array(mod_coeffs), p)
        self.__mod_poly = np.poly1d(modulus_mod_coeffs)

    @property
    def p(self) -> int:
        """A prime number. Read-only."""
        return self.__p

    @property
    def mod_coeffs(self) -> types.Fpn:
        """Coefficients of the monic irreducible polynomial. Read-only."""

        return self.__mod_poly.coeffs

    @property
    def mod_poly(self) -> np.poly1d:
        """The monic irreducible polynomial. Read-only."""
        return self.__mod_poly

    def __str__(self) -> str:
        return f'GF({self.p}^{len(self.mod_coeffs) - 1})'

    def elm(self, coeffs: Union[NDArray[Any, int], List[int]]) -> ElementInGFpn:
        """Generate the Element from coeffs in GF(p^n).

        Returns:
            ElementInGFpn: The element in GF(p^n).
        """
        return ElementInGFpn(np.array(coeffs), self.p, self.mod_poly)

    def random_primitive_elm(self) -> ElementInGFpn:
        """Return a primitive element in GF(p^n) randomly.

        Returns:
            ElementInGFpn: A primitive root in GF(p^n)
        """
        return pr.random_primitive_root_over_Fpn(self.__p, self.mod_coeffs)
