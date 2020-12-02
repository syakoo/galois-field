from typing import Union

import numpy as np
import pytest

from galois_field.core.ElementInGFpn import ElementInGFpn
from galois_field.core.types import Fp, Fpn


@pytest.mark.parametrize('coeffs, p, mod_coeffs, expected_coeffs', [
    (np.array([4, 3, 2, 1]), 2, np.array([1, 1, 1]), np.array([1, 0])),
    (np.array([4, 3, 2, 1]), 5, np.array([1, 0, 2]), np.array([4, 0])),
    (np.array([2, 1]), 11, np.array([1, 0, 1]), np.array([2, 1]))
])
def test_ElementInGFpn_init(coeffs, p, mod_coeffs, expected_coeffs):
    result = ElementInGFpn(coeffs, p, mod_coeffs)

    assert (result.coeffs == expected_coeffs).all()


@pytest.mark.parametrize('coeffs, p, mod_coeffs, expected', [
    (np.array([4, 3, 2, 1]), 2, np.array([1, 1, 1]), '1x'),
    (np.array([4, 3, 2, 1]), 5, np.array([1, 0, 2]), '4x'),
    (np.array([2, 1]), 11, np.array([1, 0, 1]), '2x + 1')
])
def test_ElementInGFpn_str(coeffs, p, mod_coeffs, expected):
    result = ElementInGFpn(coeffs, p, mod_coeffs)

    assert str(result) == expected


@pytest.mark.parametrize('coeffs, p, mod_coeffs, expected', [
    (np.array([4, 3, 2, 1]), 2, np.array([1, 1, 1]),
     'ElementInGFpn([1, 0], 2, [1, 1, 1])'),
    (np.array([4, 3, 2, 1]), 5, np.array([1, 0, 2]),
     'ElementInGFpn([4, 0], 5, [1, 0, 2])'),
    (np.array([2, 1]), 11, np.array([1, 0, 1]),
     'ElementInGFpn([2, 1], 11, [1, 0, 1])')
])
def test_ElementInGFpn_repr(coeffs, p, mod_coeffs, expected):
    result = ElementInGFpn(coeffs, p, np.poly1d(mod_coeffs))

    assert repr(result) == expected


@pytest.mark.parametrize('coeffs1, coeffs2, p, mod_coeffs, expected_coeffs', [
    (np.array([1, 2, 3, 4]), np.array([1, 2, 3, 4]), 5,
     np.array([1, 0, 0, 0, 2]), np.array([2, 4, 1, 3])),
    (np.array([1, 2, 3, 4]), np.array([1, 2, 3, 4]),
     11, np.array([1, 0, 1]), np.array([4, 4]))
])
def test_GFpn_add(coeffs1: Fpn, coeffs2: Fpn,
                  p: int, mod_coeffs: Fpn, expected_coeffs: Fpn):
    el1 = ElementInGFpn(coeffs1, p, np.poly1d(mod_coeffs))
    el2 = ElementInGFpn(coeffs2, p, np.poly1d(mod_coeffs))
    result = el1 + el2

    assert (result.coeffs == expected_coeffs).all()


@pytest.mark.parametrize('coeffs1, coeffs2, p, mod_coeffs, expected_coeffs', [
    (np.array([1, 2, 3, 4]), np.array([4, 3, 2, 1]),
     5, np.array([1, 0, 0, 0, 2]), np.array([2, 4, 1, 3])),
    (np.array([1, 2, 3, 4]), np.array([4, 3, 2, 1]),
     11, np.array([1, 0, 1]), np.array([4, 4]))
])
def test_GFpn_sub(coeffs1: Fpn, coeffs2: Fpn,
                  p: int, mod_coeffs: Fpn, expected_coeffs: Fpn):
    el1 = ElementInGFpn(coeffs1, p, np.poly1d(mod_coeffs))
    el2 = ElementInGFpn(coeffs2, p, np.poly1d(mod_coeffs))
    result = el1 - el2

    assert (result.coeffs == expected_coeffs).all()


@pytest.mark.parametrize('coeffs1, coeffs2, p, mod_coeffs, expected_coeffs', [
    (np.array([1, 2, 3, 4]), np.array([1, 2]), 5,
     np.array([1, 0, 0, 0, 2]), np.array([4, 2, 0, 1])),
    (np.array([1, 2]), np.array([1, 2, 3, 4]),
     11, np.array([1, 0, 1]), np.array([6, 2])),
    (np.array([1, 2, 3, 4]), 15, 11, np.array(
        [1, 0, 0, 1, 2]), np.array([4, 8, 1, 5])),
    (15, np.array([1, 2, 3, 4]), 11, np.array(
        [1, 0, 0, 1, 2]), np.array([4, 8, 1, 5])),
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


@pytest.mark.parametrize("coeffs1, coeffs2, p, mod_coeffs, expected_coeffs", [
    (np.array([1, 1]), np.array([4]), 11,
     np.array([1, 0, 1]), np.array([3, 3])),
    (np.array([1, 2]), np.array([1, 1]), 5,
     np.array([1, 0, 2]), np.array([3, 3])),
    (2, np.array([1, 1]), 7,
     np.array([1, 0, 0, 1, 1]), np.array([5, 2, 5, 0])),
    (np.array([1, 1]), 5, 7,
     np.array([1, 0, 0, 1, 1]), np.array([3, 3]))
])
def test_GFpn_div(coeffs1: Union[Fpn, Fp],
                  coeffs2: Union[Fpn, Fp], p, mod_coeffs, expected_coeffs):
    """poly^{-1} = expected (mod mod_poly)"""
    if isinstance(coeffs1, Fp):
        el1 = coeffs1
    else:
        el1 = ElementInGFpn(coeffs1, p, np.poly1d(mod_coeffs))

    if isinstance(coeffs2, Fp):
        el2 = coeffs2
    else:
        el2 = ElementInGFpn(coeffs2, p, np.poly1d(mod_coeffs))

    result = el1 / el2

    assert (result.coeffs == expected_coeffs).all()


@pytest.mark.parametrize("el, exp, expected_coeffs", [
    (ElementInGFpn(np.array([4]), 11, np.poly1d([1, 0, 1])), 3, np.array([9])),
    (ElementInGFpn(np.array([1, 1]), 5,
                   np.poly1d([1, 0, 2])), 23, np.poly1d([3, 2])),
    (ElementInGFpn(np.array([1, 1]), 7,
                   np.poly1d([1, 0, 0, 1, 1])), 2399, np.poly1d([6, 1, 6, 0]))
])
def test_GFpn_pow(el, exp, expected_coeffs):
    result = el ** exp

    assert (result.coeffs == expected_coeffs).all()


@pytest.mark.parametrize("el1, el2, expected", [
    (ElementInGFpn(np.array([1, 1]), 11, np.array([1, 0, 1])),
     ElementInGFpn(np.array([1, 1]), 11, np.array([1, 0, 1])), True),
    (ElementInGFpn(np.array([1, 2]), 11, np.array([1, 0, 1])),
     ElementInGFpn(np.array([1, 1]), 11, np.array([1, 0, 1])), False),
    (ElementInGFpn(np.array([1, 1]), 11, np.array([1, 0, 1])),
     ElementInGFpn(np.array([1, 1]), 7, np.array([1, 0, 1])), True),
    (ElementInGFpn(np.array([1, 1]), 11, np.array([1, 0, 1])),
     ElementInGFpn(np.array([1, 1]), 11, np.array([1, 0, 1, 4])), True),
    (ElementInGFpn(np.array([1, 1]), 11, np.array([1, 0, 1])), [1, 1], True),
    (ElementInGFpn(np.array([1]), 11, np.array([1, 0, 1])), 1, True),
])
def test_GFpn_equal(el1, el2, expected):
    result = el1 == el2

    assert result == expected


@pytest.mark.parametrize("el, expected_coeffs", [
    (ElementInGFpn(np.array([1, 1]), 7,
                   np.poly1d([1, 0, 0, 0, 1])), np.array([3, 4, 3, 4])),
    (ElementInGFpn(np.array([4]), 11, np.poly1d([1, 0, 1])), np.poly1d([3])),
    (ElementInGFpn(np.array([1, 1]), 5,
                   np.poly1d([1, 0, 2])), np.poly1d([3, 2])),
    (ElementInGFpn(np.array([1, 1]), 7, np.poly1d(
        [1, 0, 0, 1, 1])), np.poly1d([6, 1, 6, 0]))
])
def test_GFpn_inverse(el, expected_coeffs):
    result = el.inverse()

    assert (result.coeffs == expected_coeffs).all()
