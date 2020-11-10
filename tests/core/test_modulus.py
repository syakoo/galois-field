from typing import Union
import pytest

from src.core import modulus as mod, types


@pytest.mark.parametrize('el, p, expected', [
    (-1, 2, 1),
    (123, 7, 4),
    (-1.0, 2, 1),
    (3.2, 11, 7),
    (-1.2, 123456791, 61728395)
])
def test_modulus_el(el: Union[types.Fp, float], p: int, expected: types.Fp):
    """el = expected (mod p)"""
    result = mod.modulus_el(el, p)

    assert result == expected
