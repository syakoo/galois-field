import numpy as np
import pytest

from galois_field.GFpn import GFpn
from galois_field.core.ElementInGFpn import ElementInGFpn


@pytest.mark.parametrize('p, mod_coeffs, expected_coeffs', [
    (5, np.array([1, 0, 2]), np.array([1, 0, 2])),
    (2, np.array([1, 1, 1]), np.array([1, 1, 1]))
])
def test_GFpn_init(p, mod_coeffs, expected_coeffs):
    gf = GFpn(p, mod_coeffs)
    assert gf.p == p
    assert (gf.mod_coeffs == expected_coeffs).all()


@pytest.mark.parametrize('p, mod_coeffs', [
    (4, np.array([1, 0, 1])),
    (5, np.array([1, 0, 1])),
    (11, np.array([1, 0, 0, 0, 0, 1, 1]))
])
def test_GFpn_raises(p, mod_coeffs):
    with pytest.raises(ValueError):
        GFpn(p, mod_coeffs)


@pytest.mark.parametrize('p, mod_coeffs, expected', [
    (5, np.array([1, 0, 2]), 'GF(5^2)'),
    (2, np.array([1, 0, 0, 1, 1]), 'GF(2^4)')
])
def test_GFpn_str(p, mod_coeffs, expected):
    gf = GFpn(p, mod_coeffs)
    assert str(gf) == expected


@pytest.mark.parametrize('coeffs, p, mod_coeffs', [
    (np.array([1, 0, 1, 1]), 5, np.array([1, 0, 2])),
    (np.array([1, 0, 1]), 11, np.array([1, 0, 1])),
    (np.array([1, 0, 0, 2]), 7, np.array([1, 0, 1]))
])
def test_GFpn_elm(coeffs, p, mod_coeffs):
    gf = GFpn(p, mod_coeffs)
    result = gf.elm(coeffs)

    assert isinstance(result, ElementInGFpn)


@pytest.mark.parametrize('p, mod_coeffs, expected_contain', [
    (2, [1, 1, 1], [[1, 0], [1, 1]]),
    (3, [1, 1, 0, 2], [[1, 2], [2, 0], [2, 2], [1, 0, 1], [1, 0, 2], [1, 2, 0],
                       [2, 0, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]),
])
def test_random_primitive_elm(p, mod_coeffs, expected_contain):
    LOOP_NUM = 5
    expected_contain_str = list(map(str, expected_contain))
    gfpn = GFpn(p, mod_coeffs)

    for _ in range(LOOP_NUM):
        result = gfpn.random_primitive_elm()

        assert isinstance(result, ElementInGFpn)
        assert str(list(result.coeffs)) in expected_contain_str
