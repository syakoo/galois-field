import pytest

from src.core import inverse as inv
from src.core.types import Fp


@pytest.mark.parametrize("el, p, expected", [
    (1, 2, 1),
    (-1, 7, 6),
    (123456789, 123456791, 61728395),
])
def test_inverse_el(el: Fp, p: int, expected: Fp):
    """el^{-1} = expected (mod p)"""
    result = inv.inverse_el(el, p)
    assert result == expected
