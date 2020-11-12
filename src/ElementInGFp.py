from __future__ import annotations

from src.core import types, modulus


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
