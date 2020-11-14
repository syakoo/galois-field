import numpy as np
import pytest

from galois_field.core import inverse as inv
from galois_field.core.types import Fp


@pytest.mark.parametrize("el, p, expected", [
    (1, 2, 1),
    (-1, 7, 6),
    (123456789, 123456791, 61728395),
])
def test_inverse_el(el: Fp, p: int, expected: Fp):
    """el^{-1} = expected (mod p)"""
    result = inv.inverse_el(el, p)
    assert result == expected


@pytest.mark.parametrize("poly, p, mod_poly, expected", [
    (np.poly1d([4]), 11, np.poly1d([1, 0, 1]), np.poly1d([3])),
    (np.poly1d([1, 1]), 5, np.poly1d([1, 0, 2]), np.poly1d([3, 2])),
    (np.poly1d([1, 1]), 7, np.poly1d([1, 0, 0, 1, 1]), np.poly1d([6, 1, 6, 0]))
])
def test_inverse_poly(poly, p, mod_poly, expected):
    """poly^{-1} = expected (mod mod_poly)"""
    result = inv.inverse_poly(poly, p, mod_poly)

    assert result == expected
