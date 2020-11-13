from __future__ import annotations
from typing import Any, Union, List

import numpy as np
from nptyping import NDArray

from src.core import types, modulus
from src.ElementInGFpn import ElementInGFpn
from src.ElementInGFp import ElementInGFp


class GF:
    def __init__(self, p: int,
                 mod_coeffs: Union[List[int], NDArray[Any, int], None] = None):
        """Galois Field: GF(p^n).

        Args:
            p (int): A prime number.
            mod_coeffs (Union[List[int], NDArray[Any, int], None], optional):
                Coefficients of a monic irreducible polynomial.
                If you want to use GF(p),
                you do not need to put anything in this arg.
                Defaults to None.
        """
        self.__p = p

        if mod_coeffs is not None:
            modulus_mod_coeffs = modulus.modulus_coeffs(
                np.array(mod_coeffs), p)
            self.__mod_poly = np.poly1d(modulus_mod_coeffs)
        else:
            self.__mod_poly = None

    @property
    def p(self) -> int:
        """A prime number. Read-only."""
        return self.__p

    @property
    def mod_coeffs(self) -> Union[types.Fpn, None]:
        """Coefficients of the monic irreducible polynomial. Read-only."""
        if self.__mod_poly is None:
            return None

        return self.__mod_poly.coeffs

    @property
    def mod_poly(self) -> np.poly1d:
        """The monic irreducible polynomial. Read-only."""
        return self.__mod_poly

    def __str__(self) -> str:
        if self.__mod_poly is None:
            return f'GF({self.p})'

        return f'GF({self.p}^{len(self.mod_coeffs) - 1})'

    def elm(self, int_or_coeffs: Union[int, List[int]])\
            -> Union[ElementInGFpn, ElementInGFp]:
        """Generate the Element from the input value in GF.

        Returns:
            Union[ElementInGFpn, ElementInGFp]]:
                The Element in GF(p) or GF(p^n).
        """
        if self.mod_poly is not None:
            if isinstance(int_or_coeffs, list) \
                    or isinstance(int_or_coeffs, types.Fpn):

                return ElementInGFpn(np.array(int_or_coeffs),
                                     self.p, self.mod_poly)
            else:
                return ElementInGFpn(np.array([int_or_coeffs]),
                                     self.p, self.mod_poly)

        if isinstance(int_or_coeffs, int):
            return ElementInGFp(int_or_coeffs, self.p)
