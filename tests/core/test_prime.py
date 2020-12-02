import pytest

from galois_field.core import prime


@pytest.mark.parametrize('n, expected', [
    (4, [2, 2]),
    (30, [2, 3, 5]),
    (498, [2, 3, 83]),
    (123456789, [3, 3, 3607, 3803])
])
def test_is_primitive_root_over_Fp(n, expected):
    result = prime.prime_factorization(n)

    assert result == expected
