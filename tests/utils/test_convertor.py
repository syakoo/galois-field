import pytest

from galois_field.utils import convertor as conv


@pytest.mark.parametrize('value, p, expected', [
    (3, 5, [3]),
    (3, 2, [1, 1]),
    (123, 11, [1, 0, 2]),
    (123, 3, [1, 1, 1, 2, 0]),
])
def test_dec2nary(value, p, expected):
    result = conv.dec2nary(value, p)

    assert result == expected
