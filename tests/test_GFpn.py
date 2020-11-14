import numpy as np
import pytest

from galois_field.GFpn import GFpn
from galois_field.ElementInGFpn import ElementInGFpn


@pytest.mark.parametrize('p, mod_coeffs, expected_coeffs', [
    (5, np.array([1, 2, 3]), np.array([1, 2, 3])),
    (2, np.array([1, 2, 3]), np.array([1, 0, 1]))
])
def test_GFpn_init(p, mod_coeffs, expected_coeffs):
    gf = GFpn(p, mod_coeffs)
    assert gf.p == p
    assert (gf.mod_coeffs == expected_coeffs).all()


@pytest.mark.parametrize('p, mod_coeffs, expected', [
    (5, np.array([1, 2, 3]), 'GF(5^3)'),
    (2, np.array([1, 2, 3, 4, 5]), 'GF(2^5)')
])
def test_GFpn_str(p, mod_coeffs, expected):
    gf = GFpn(p, mod_coeffs)
    assert str(gf) == expected


@pytest.mark.parametrize('coeffs, p, mod_coeffs', [
    (np.array([4, 3, 2, 1]), 5, np.array([1, 0, 1])),
    (np.array([2, 1]), 11, np.array([1, 0, 1])),
    (np.array([4, 3, 2, 1]), 123456791, np.array([1, 0, 1]))
])
def test_GFpn_elm(coeffs, p, mod_coeffs):
    gf = GFpn(p, mod_coeffs)
    result = gf.elm(coeffs)

    assert isinstance(result, ElementInGFpn)
