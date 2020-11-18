import pytest

from galois_field.core import arithmetics as arith


@pytest.mark.parametrize('n, expected', [
    (1, {}),
    (36, {2: 2, 3: 2}),
    (840, {2: 3, 3: 1, 5: 1, 7: 1}),
])
def test_prime_factorize(n, expected):
    assert arith.prime_factorize(n) == expected
