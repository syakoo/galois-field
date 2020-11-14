from typing import Any, Union

import numpy as np
from nptyping import NDArray
import pytest

from galois_field.core import modulus as mod, types


@pytest.mark.parametrize('el, p, expected', [
    (-1, 2, 1),
    (123, 7, 4),
    (-1.0, 2, 1),
    (3.2, 11, 7),
    (-1.2, 123456791, 61728395)
])
def test_modulus_el(el: Union[types.Fp, float], p: int, expected: types.Fp):
    """el = expected (mod p)"""
    result = mod.modulus_el(el, p)

    assert result == expected


@pytest.mark.parametrize('coeffs, p, expected', [
    (np.array([1, 2, 3], int), 2, np.array([1, 0, 1])),
    (np.array([-1, 3.2, -3.0]), 11, np.array([10, 7, 8])),
    (np.array([-1.2, 10000000000]), 123456791, np.array([61728395, 123456720]))
])
def test_modulus_coeffs(coeffs: Union[types.Fpn, NDArray[Any, float]],
                        p: int,
                        expected: types.Fpn):
    """coeffs = expected (mod p)"""
    result = mod.modulus_coeffs(coeffs, p)

    assert (result == expected).all()


@pytest.mark.parametrize('poly, p, expected', [
    (np.poly1d([1, 2, 3]), 2, np.poly1d([1, 0, 1])),
    (np.poly1d([-1, 3.2, -3.0]), 11, np.poly1d([10, 7, 8])),
    (np.poly1d([-1.2, 10000000000]), 123456791,
     np.poly1d([61728395, 123456720]))
])
def test_modulus_poly_over_fp(poly, p, expected):
    """poly = expected (mod p)"""
    result = mod.modulus_poly_over_fp(poly, p)

    assert (result == expected).all()


@pytest.mark.parametrize('poly1, poly2, p, expected', [
    (np.poly1d([4, 3, 2, 1]), np.poly1d([1, 0, 2]), 5, np.poly1d([4, 0])),
    (np.poly1d([2, 1]), np.poly1d([1, 0, 1]), 11, np.poly1d([2, 1])),
    (np.poly1d([4, 3, 2, 1]), np.poly1d([1, 1, 1]), 2, np.poly1d([1, 0]))
])
def test_modulus_poly(poly1: np.poly1d,
                      poly2: np.poly1d, p: int, expected: np.poly1d):
    """poly1 = expected (mod poly2 over p)"""
    result = mod.modulus_poly(poly1, poly2, p)

    assert (result == expected).all()


@pytest.mark.parametrize('poly, e, p, mod_poly, expected', [
    (np.poly1d([1, 1]), 23, 5, np.poly1d([1, 0, 2]), np.poly1d([3, 2])),
    (np.poly1d([1, 1]), 2399, 7,
     np.poly1d([1, 0, 0, 1, 1]), np.poly1d([6, 1, 6, 0]))
])
def test_modulus_pow_poly(poly, e, p, mod_poly, expected):
    result = mod.modulus_pow_poly(poly, e, p, mod_poly)

    assert (result == expected).all()
