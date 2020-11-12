import pytest

from src.ElementInGFp import ElementInGFp


@pytest.mark.parametrize('value, p, expected_value', [
    (1, 5, 1),
    (222, 11, 2),
    (-2, 123456791, 123456789)
])
def test_ElementInGFp_init(value, p, expected_value):
    el = ElementInGFp(value, p)

    assert el.value == expected_value
