from __future__ import annotations
from typing import Union

from . import types, modulus, inverse


class ElementInGFp:
    """An Element in GF(p) class.

    Args:
        value (int): An Element in GF(p).
        p (int): A prime number.
    """

    def __init__(self, value: int, p: int):
        self.__p = p
        self.__value: types.Fp = modulus.modulus_el(value, p)

    @property
    def value(self) -> types.Fp:
        """An Element in GF(p). Read-only."""
        return self.__value

    @property
    def p(self):
        """A prime number. Read-only."""
        return self.__p

    def inverse(self) -> ElementInGFp:
        """Compute the inverse of the value modulo p.

        Returns:
            ElementInGFp: The inverse of the value in GF(p).
        """
        return ElementInGFp(inverse.inverse_el(self.value, self.p), self.p)

    def __str__(self) -> str:
        return f'{str(self.value)} (mod {self.p})'

    def __repr__(self) -> str:
        return f'ElementInGFp({self.value}, {self.p})'

    def __add__(self, other: ElementInGFp) -> ElementInGFp:
        return ElementInGFp(self.value + other.value, self.p)

    def __sub__(self, other: ElementInGFp) -> ElementInGFp:
        return ElementInGFp(self.value - other.value, self.p)

    def __mul__(self, other: Union[ElementInGFp, int]) -> ElementInGFp:
        if isinstance(other, int):
            return ElementInGFp(self.value * other, self.p)

        return ElementInGFp(self.value * other.value, self.p)

    def __rmul__(self, other: Union[ElementInGFp, int]) -> ElementInGFp:
        if isinstance(other, int):
            return ElementInGFp(self.value * other, self.p)

        return ElementInGFp(self.value * other.value, self.p)

    def __truediv__(self, other: Union[ElementInGFp, int]) -> ElementInGFp:
        if isinstance(other, int):
            other_value = other
        else:
            other_value = other.value

        inv_value = inverse.inverse_el(other_value, self.p)
        return ElementInGFp(self.value * inv_value, self.p)

    def __rtruediv__(self, other: Union[ElementInGFp, int]) -> ElementInGFp:
        if isinstance(other, int):
            other_value = other
        else:
            other_value = other.value

        inv_value = inverse.inverse_el(self.value, self.p)
        return ElementInGFp(other_value * inv_value, self.p)

    def __pow__(self, other: Union[int, ElementInGFp]) -> ElementInGFp:
        if isinstance(other, ElementInGFp):
            other = other.value

        new_value = pow(self.value, other, self.p)

        return ElementInGFp(new_value, self.p)

    def __int__(self) -> int:
        return int(self.value)

    def __eq__(self, other: Union[ElementInGFp, int]) -> bool:
        if isinstance(other, int):
            return self.value == other
        if not isinstance(other, ElementInGFp):
            return False

        return self.value == other.value
