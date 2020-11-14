from __future__ import annotations

from .ElementInGFp import ElementInGFp


class GFp:
    def __init__(self, p: int):
        """Galois Field: GF(p)

        Args:
            p (int): A prime number.
        """
        self.__p = p

    @property
    def p(self):
        """A prime number. Read-only."""
        return self.__p

    def __str__(self) -> str:
        return f'GF({self.p})'

    def elm(self, value: int) -> ElementInGFp:
        """Generate the element from a value in GF(p).

        Args:
            value (int): An input value.

        Returns:
            ElementInGFp: The element in GF(p).
        """
        return ElementInGFp(value, self.p)
