import numpy as np
import pytest

from src.GFpn import GFpn
from src.core.types import Fpn


@pytest.mark.parametrize('coeffs, p, mod_coeffs, expected_coeffs', [
    (np.array([4, 3, 2, 1]), 5, np.array([1, 0, 1]), np.array([3, 3])),
    (np.array([2, 1]), 11, np.array([1, 0, 1]), np.array([2, 1])),
    (np.array([4, 3, 2, 1]), 123456791, np.array(
        [1, 0, 1]), np.array([123456789, 123456789]))
])
def test_GFpn_init(coeffs: Fpn, p: int, mod_coeffs: Fpn, expected_coeffs: Fpn):
    result = GFpn(coeffs, p, mod_coeffs)
    print(result.coeffs)

    assert (result.coeffs == expected_coeffs).all()
