import numpy as np
import pytest

from galois_field.core import validator


@pytest.mark.parametrize('poly, p, expected', [
    (np.poly1d([1, 1, 1]), 2, True),
    (np.poly1d([1, 0, 1]), 2, False),
    (np.poly1d([1, 0, 0, 0, 2]), 5, True),
    (np.poly1d([1, 0, 0, 0, 1]), 5, False),
    (np.poly1d([1, 0, 0, 0, 0, 0, 1, 1]), 5, True),
    (np.poly1d([1, 0, 0, 0, 1, 0, 0, 1]), 5, False)
])
def test_is_irreducible_poly(poly, p, expected):
    assert validator.is_irreducible_poly(poly, p) == expected


@pytest.mark.parametrize('value, expected', [
    (11, True),
    (12, False),
    (101, True),
    (100, False),
    (1, False),
    (2, True)
])
def test_is_prime(value, expected):
    assert validator.is_prime(value) == expected
