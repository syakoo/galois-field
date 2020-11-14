import numpy as np
import pytest

from galois_field.core import gcd


@pytest.mark.parametrize('poly1, poly2, p, expected', [
    (np.poly1d([1, 0, 1]), np.poly1d([1, 2]), 5, np.poly1d([1, 2])),
    (np.poly1d([1, 0, 1, 1]), np.poly1d([1, 2]), 5, np.poly1d([1])),
    (np.poly1d([1, 0, 1]), np.poly1d([1, 4, 2, 1]), 5, np.poly1d([1, 2])),
    (np.poly1d([1, 0, 0, 0, 0, 0, 1, 1]),
     np.poly1d([1, 0, 0, 0, 4, 0]), 5, np.poly1d([2]))
])
def test_gcd_poly(poly1, poly2, p, expected):
    assert gcd.gcd_poly(poly1, poly2, p) == expected
