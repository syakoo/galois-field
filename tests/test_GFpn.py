from typing import Union

import numpy as np
import pytest

from src.GFpn import GFpn
from src.core.types import Fpn


@pytest.mark.parametrize('coeffs, p, mod_coeffs, expected_coeffs', [
    (np.array([4, 3, 2, 1]), None, None, np.array([4, 3, 2, 1])),
    (np.array([4, 3, 2, 1]), 5, np.array([1, 0, 1]), np.array([3, 3])),
    (np.array([2, 1]), 11, np.array([1, 0, 1]), np.array([2, 1])),
    (np.array([4, 3, 2, 1]), 123456791, np.array(
        [1, 0, 1]), np.array([123456789, 123456789]))
])
def test_GFpn_init(coeffs: Fpn, p: int, mod_coeffs: Fpn, expected_coeffs: Fpn):
    if p is None and mod_coeffs is None:
        result = GFpn(coeffs)
    else:
        result = GFpn(coeffs, p, mod_coeffs)

    assert (result.coeffs == expected_coeffs).all()


@pytest.mark.parametrize('coeffs, p, mod_coeffs, expected', [
    (np.array([4, 3, 2, 1]), None, None, '4x^3 + 3x^2 + 2x + 1'),
    (np.array([2, 1]), 11, np.array([1, 0, 1]), '2x + 1 (mod F_11^2)'),
])
def test_GFpn_str(coeffs: Fpn, p: Union[int, None],
                  mod_coeffs: Union[Fpn, None], expected: str):
    if p is None and mod_coeffs is None:
        GFpn.p = None
        GFpn.mod_coeffs = None
        result = GFpn(coeffs)
    else:
        result = GFpn(coeffs, p, mod_coeffs)

    assert str(result) == expected


@pytest.mark.parametrize('coeffs1, coeffs2, p, mod_coeffs, expected_coeffs', [
    ([1, 2, 3, 4], [1, 2, 3, 4], 5, [1, 0, 0, 0, 1], [2, 4, 1, 3]),
    ([1, 2, 3, 4], [1, 2, 3, 4], 31, [1, 0, 1], [4, 4])
])
def test_GFpn_add(coeffs1: Fpn, coeffs2: Fpn,
                  p: int, mod_coeffs: Fpn, expected_coeffs: Fpn):
    el1 = GFpn(coeffs1, p, mod_coeffs)
    el2 = GFpn(coeffs2, p, mod_coeffs)
    result = el1 + el2

    assert (result.coeffs == expected_coeffs).all()


@pytest.mark.parametrize('coeffs1, coeffs2, p, mod_coeffs, expected_coeffs', [
    ([1, 2, 3, 4], [4, 3, 2, 1], 5, [1, 0, 0, 0, 1], [2, 4, 1, 3]),
    ([1, 2, 3, 4], [4, 3, 2, 1], 31, [1, 0, 1], [4, 4])
])
def test_GFpn_add(coeffs1: Fpn, coeffs2: Fpn,
                  p: int, mod_coeffs: Fpn, expected_coeffs: Fpn):
    el1 = GFpn(coeffs1, p, mod_coeffs)
    el2 = GFpn(coeffs2, p, mod_coeffs)
    result = el1 - el2

    assert (result.coeffs == expected_coeffs).all()
