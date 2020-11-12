from __future__ import annotations
from typing import Union

from src.core import types, modulus, inverse


class ElementInGFp:
    def __init__(self, value: int, p: int):
        self.__p = p
        self.__value: types.Fp = modulus.modulus_el(value, p)

    @property
    def value(self) -> types.Fp:
        return self.__value

    @property
    def p(self):
        return self.__p

    def __str__(self) -> str:
        return str(self.value)

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

    def __eq__(self, other: Union[ElementInGFp, int]) -> bool:
        if not isinstance(other, ElementInGFp):
            return False

        return self.value == other.value and self.p == other.p