from __future__ import annotations
from typing import Any, Union

import numpy as np
from nptyping import NDArray

from . import types, modulus, inverse


class ElementInGFpn:
    """An Element in GF(p^n) class.

    Args:
        coeffs (NDArray[Any, int]): Coefficients of an element in GF(p^n).
        p (int): A prime number.
        mod_poly (np.poly1d): A monic irreducible polynomial.
    """

    def __init__(self, coeffs: NDArray[Any, int], p: int, mod_poly: np.poly1d):
        self.p = p
        self.mod_poly = mod_poly
        self.__poly = modulus.modulus_poly(np.poly1d(coeffs), mod_poly, p)

    @property
    def poly(self) -> np.poly1d:
        """A polynomial in GF(p^n). Read-only."""
        return self.__poly

    @property
    def coeffs(self) -> types.Fpn:
        """Coefficients of the polynomial in GF(p^n)."""
        return self.__poly.coeffs

    def inverse(self) -> ElementInGFpn:
        """Compute the inverse of the element in GF(p^n).

        Returns:
            ElementInGFpn: The inverse of the element in GF(p^n).
        """
        inv_poly = inverse.inverse_poly(self.poly, self.p, self.mod_poly)
        return ElementInGFpn(inv_poly.coeffs, self.p, self.mod_poly)

    def __str__(self):
        result = []
        for i, coeff in enumerate(self.coeffs[::-1]):
            if i == len(self.coeffs) - 1:
                sig = ""
            else:
                sig = " + "

            if coeff == 0:
                dig = ''
            elif i == 0:
                dig = f'{sig}{coeff}'
            elif i == 1:
                dig = f'{sig}{coeff}x'
            else:
                dig = f'{sig}{coeff}x^{i}'
            result.append(dig)

        return "".join(result[::-1])

    def __repr__(self) -> str:
        def c2str(array): return str(list(array))
        mod_str = c2str(self.mod_poly.coeffs)
        return f'ElementInGFpn({c2str(self.coeffs)}, {self.p}, {mod_str})'

    def __add__(self, other: ElementInGFpn) -> ElementInGFpn:
        result = self.poly + other.poly

        return ElementInGFpn(result.coeffs, self.p, self.mod_poly)

    def __sub__(self, other: ElementInGFpn) -> ElementInGFpn:
        result = self.poly - other.poly

        return ElementInGFpn(result.coeffs, self.p, self.mod_poly)

    def __mul__(self, other: Union[ElementInGFpn, types.Fp]) -> ElementInGFpn:
        if isinstance(other, types.Fp):
            result = self.poly * other
        else:
            result = self.poly * other.poly

        return ElementInGFpn(result.coeffs, self.p, self.mod_poly)

    def __rmul__(self, other: Union[ElementInGFpn, types.Fp]) -> ElementInGFpn:
        if isinstance(other, types.Fp):
            result = self.poly * other
        else:
            result = self.poly * other.poly

        return ElementInGFpn(result.coeffs, self.p, self.mod_poly)

    def __truediv__(self,
                    other: Union[ElementInGFpn, types.Fp]) -> ElementInGFpn:
        if isinstance(other, types.Fp):
            result = self.poly * inverse.inverse_el(other, self.p)
        else:
            result = self.poly * \
                inverse.inverse_poly(other.poly, self.p, self.mod_poly)

        return ElementInGFpn(result.coeffs, self.p, self.mod_poly)

    def __rtruediv__(self,
                     other: Union[ElementInGFpn, types.Fp]) -> ElementInGFpn:
        if isinstance(other, types.Fp):
            result = other * \
                inverse.inverse_poly(self.poly, self.p, self.mod_poly)
        else:
            result = other.poly * \
                inverse.inverse_poly(self.poly, self.p, self.mod_poly)

        return ElementInGFpn(result.coeffs, self.p, self.mod_poly)

    def __pow__(self, other: int) -> ElementInGFpn:
        result = modulus.modulus_pow_poly(
            self.poly, other, self.p, self.mod_poly)

        return ElementInGFpn(result.coeffs, self.p, self.mod_poly)

    def __eq__(self, other) -> bool:
        if isinstance(other, list):
            return (self.coeffs == other).all()
        elif isinstance(other, int):
            return len(self.coeffs) == 1 and self.coeffs[0] == other
        elif not isinstance(other, ElementInGFpn):
            return False

        return (self.poly == other.poly).all()
