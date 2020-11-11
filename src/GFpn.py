from __future__ import annotations
from typing import Union, List

import numpy as np

from src.core import types, modulus


class GF:
    def __init__(self, p: int,
                 mod_coeffs: Union[types.Fpn, List[types.Fp], None] = None):
        self.__p = p

        if mod_coeffs is not None:
            modulus_mod_coeffs = modulus.modulus_coeffs(
                np.array(mod_coeffs), p)
            self.__mod_poly = np.poly1d(modulus_mod_coeffs)
        else:
            self.__mod_poly = None

    @property
    def p(self) -> int:
        return self.__p

    @property
    def mod_coeffs(self) -> Union[types.Fpn, None]:
        if self.__mod_poly is None:
            return None

        return self.__mod_poly.coeffs

    @property
    def mod_poly(self) -> np.poly1d:
        return self.__mod_poly

    def __str__(self) -> str:
        if self.__mod_poly is None:
            return f'GF({self.p})'

        return f'GF({self.p}^{len(self.mod_coeffs) - 1})'
