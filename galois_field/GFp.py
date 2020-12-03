from __future__ import annotations

from .core.ElementInGFp import ElementInGFp
from .core import validator, primitive_roots


class GFp:
    """Galois Field: GF(p)

    Args:
        p (int): A prime number.

    Examples:
        >>> from galois_field import GFp

        In this case, p = 11.
        >>> gf = GFp(11)

        Generate the element in GF(11).
        >>> gf.elm(5) # 5 (mod 11)
        ElementInGFp(5, 11)

        >>> gf.elm(13) # 2 (mod 11)
        ElementInGFp(2, 11)
    """

    def __init__(self, p: int):
        if not validator.is_prime(p):
            raise ValueError(f"{p} is not a prime number.")
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

    def random_primitive_elm(self) -> ElementInGFp:
        """Return a primitive element in GF(p) randomly.

        Returns:
            ElementInGFp: A primitive root in GF(p)
        """
        return primitive_roots.random_primitive_root_over_Fp(self.__p)
