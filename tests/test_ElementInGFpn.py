from typing import Union

import numpy as np
import pytest

from src.ElementInGFpn import ElementInGFpn
from src.core.types import Fp, Fpn


@pytest.mark.parametrize('coeffs, p, mod_coeffs, expected_coeffs', [
    (np.array([4, 3, 2, 1]), 5, np.array([1, 0, 1]), np.array([3, 3])),
    (np.array([2, 1]), 11, np.array([1, 0, 1]), np.array([2, 1])),
    (np.array([4, 3, 2, 1]), 123456791, np.array(
        [1, 0, 1]), np.array([123456789, 123456789]))
])
def test_ElementInGFpn_init(coeffs, p, mod_coeffs, expected_coeffs):
    result = ElementInGFpn(coeffs, p, mod_coeffs)

    assert (result.coeffs == expected_coeffs).all()


@pytest.mark.parametrize('coeffs, p, mod_coeffs, expected', [
    (np.array([4, 3, 2, 1]), 5, np.array([1, 0, 1]), '3x + 3'),
    (np.array([2, 1]), 11, np.array([1, 0, 1]), '2x + 1'),
    (np.array([4, 3, 2, 1]), 123456791, np.array(
        [1, 0, 1]), '123456789x + 123456789')
])
def test_ElementInGFpn_str(coeffs, p, mod_coeffs, expected):
    result = ElementInGFpn(coeffs, p, mod_coeffs)

    assert str(result) == expected


@pytest.mark.parametrize('coeffs1, coeffs2, p, mod_coeffs, expected_coeffs', [
    (np.array([1, 2, 3, 4]), np.array([1, 2, 3, 4]), 5,
     np.array([1, 0, 0, 0, 1]), np.array([2, 4, 1, 3])),
    (np.array([1, 2, 3, 4]), np.array([1, 2, 3, 4]),
     31, np.array([1, 0, 1]), np.array([4, 4]))
])
def test_GFpn_add(coeffs1: Fpn, coeffs2: Fpn,
                  p: int, mod_coeffs: Fpn, expected_coeffs: Fpn):
    el1 = ElementInGFpn(coeffs1, p, np.poly1d(mod_coeffs))
    el2 = ElementInGFpn(coeffs2, p, np.poly1d(mod_coeffs))
    result = el1 + el2

    assert (result.coeffs == expected_coeffs).all()


@pytest.mark.parametrize('coeffs1, coeffs2, p, mod_coeffs, expected_coeffs', [
    (np.array([1, 2, 3, 4]), np.array([4, 3, 2, 1]),
     5, np.array([1, 0, 0, 0, 1]), np.array([2, 4, 1, 3])),
    (np.array([1, 2, 3, 4]), np.array([4, 3, 2, 1]),
     31, np.array([1, 0, 1]), np.array([4, 4]))
])
def test_GFpn_sub(coeffs1: Fpn, coeffs2: Fpn,
                  p: int, mod_coeffs: Fpn, expected_coeffs: Fpn):
    el1 = ElementInGFpn(coeffs1, p, np.poly1d(mod_coeffs))
    el2 = ElementInGFpn(coeffs2, p, np.poly1d(mod_coeffs))
    result = el1 - el2

    assert (result.coeffs == expected_coeffs).all()


@pytest.mark.parametrize('coeffs1, coeffs2, p, mod_coeffs, expected_coeffs', [
    (np.array([1, 2, 3, 4]), np.array([1, 2]), 5,
     np.array([1, 0, 0, 0, 1]), np.array([4, 2, 0, 2])),
    (np.array([1, 2]), np.array([1, 2, 3, 4]),
     31, np.array([1, 0, 1]), np.array([6, 2])),
    (np.array([1, 2, 3, 4]), 15, 31, np.array(
        [1, 0, 0, 0, 1]), np.array([15, 30, 14, 29])),
    (15, np.array([1, 2, 3, 4]), 31, np.array(
        [1, 0, 0, 0, 1]), np.array([15, 30, 14, 29])),
])
def test_GFpn_mul(coeffs1: Union[Fpn, Fp],
                  coeffs2: Union[Fpn, Fp],
                  p: int, mod_coeffs: Fpn, expected_coeffs: Fpn):
    if isinstance(coeffs1, Fp):
        el1 = coeffs1
    else:
        el1 = ElementInGFpn(coeffs1, p, np.poly1d(mod_coeffs))

    if isinstance(coeffs2, Fp):
        el2 = coeffs2
    else:
        el2 = ElementInGFpn(coeffs2, p, np.poly1d(mod_coeffs))

    result = el1 * el2

    assert (result.coeffs == expected_coeffs).all()