from typing import Union, List

import numpy as np

from src.core import types, modulus


class GFpn_meta(type):
    def __init__(cls, *args, **kwargs):
        cls.__mod_poly: Union[np.poly1d, None] = None
        cls.__p: Union[int, None] = None

    @property
    def mod_poly(cls):
        return cls.__mod_poly

    @property
    def mod_coeffs(cls):
        if cls.__mod_poly is None:
            return None

        return cls.__mod_poly.coeffs

    @mod_coeffs.setter
    def mod_coeffs(cls, coeffs: Union[types.Fpn, List[types.Fp]]):
        cls.__mod_poly = np.poly1d(coeffs)

    @property
    def p(cls):
        return cls.__p

    @p.setter
    def p(cls, p: int):
        cls.__p = p


class GFpn(metaclass=GFpn_meta):
    def __init__(self, coeffs: Union[types.Fpn, List[types.Fp]],
                 p: Union[int, None] = None,
                 mod_coeffs: Union[types.Fpn, List[types.Fp], None] = None) -> None:
        if p is not None:
            GFpn.p = p
        if mod_coeffs is not None:
            GFpn.mod_coeffs = mod_coeffs

        self.coeffs = coeffs

    @property
    def poly(self):
        return self._poly

    @property
    def coeffs(self):
        return self._poly.coeffs

    @coeffs.setter
    def coeffs(self, coeffs: Union[types.Fpn, List[types.Fp]]):
        if GFpn.p is not None and GFpn.mod_poly is not None:
            poly_fpn = modulus.modulus_poly(
                np.poly1d(coeffs), GFpn.mod_poly, GFpn.p)
            self._poly = poly_fpn
        else:
            self._poly = np.poly1d(coeffs)
