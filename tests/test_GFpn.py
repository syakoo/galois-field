import numpy as np
import pytest

from galois_field.GFpn import GF
from galois_field.ElementInGFpn import ElementInGFpn
from galois_field.ElementInGFp import ElementInGFp


@pytest.mark.parametrize('p, mod_coeffs, expected_coeffs', [
    (5, np.array([1, 2, 3]), np.array([1, 2, 3])),
    (2, np.array([1, 2, 3]), np.array([1, 0, 1]))
])
def test_GFpn_init(p, mod_coeffs, expected_coeffs):
    gf = GF(p, mod_coeffs)
    assert gf.p == p
    assert (gf.mod_coeffs == expected_coeffs).all()


@pytest.mark.parametrize('p', [(5), (2), (123456791)])
def test_GFp_init(p):
    gf = GF(p)
    assert gf.p == p
    assert gf.mod_coeffs is None
    assert gf.mod_poly is None


@pytest.mark.parametrize('p, mod_coeffs, expected', [
    (5, np.array([1, 2, 3]), 'GF(5^2)'),
    (2, np.array([1, 2, 3, 4, 5]), 'GF(2^4)')
])
def test_GFpn_str(p, mod_coeffs, expected):
    gf = GF(p, mod_coeffs)
    assert str(gf) == expected


@pytest.mark.parametrize('p, expected', [
    (5, 'GF(5)'),
    (2, 'GF(2)')
])
def test_GFp_str(p, expected):
    gf = GF(p)
    assert str(gf) == expected


@pytest.mark.parametrize('coeffs, p, mod_coeffs', [
    (np.array([4, 3, 2, 1]), 5, np.array([1, 0, 1])),
    (np.array([2, 1]), 11, np.array([1, 0, 1])),
    (np.array([4, 3, 2, 1]), 123456791, np.array([1, 0, 1]))
])
def test_GFpn_elm(coeffs, p, mod_coeffs):
    gf = GF(p, mod_coeffs)
    result = gf.elm(coeffs)

    assert isinstance(result, ElementInGFpn)


@pytest.mark.parametrize('integer, p', [
    (1, 5),
    (2, 11),
    (3, 123456791)
])
def test_GFp_elm(integer, p):
    gf = GF(p)
    result = gf.elm(integer)

    assert isinstance(result, ElementInGFp)
