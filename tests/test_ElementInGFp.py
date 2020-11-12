import pytest

from src.ElementInGFp import ElementInGFp


@pytest.mark.parametrize('value, p, expected_value', [
    (1, 5, 1),
    (222, 11, 2),
    (-2, 123456791, 123456789)
])
def test_ElementInGFp_init(value, p, expected_value):
    el = ElementInGFp(value, p)

    assert isinstance(el, ElementInGFp)
    assert el.value == expected_value


@pytest.mark.parametrize('value, p, expected', [
    (1, 5, '1'),
    (222, 11, '2'),
    (-2, 123456791, '123456789')
])
def test_ElementInGFpn_str(value, p, expected):
    result = ElementInGFp(value, p)

    assert str(result) == expected


@pytest.mark.parametrize('value1, value2, p, expected_value', [
    (1, 1, 5, 2),
    (111, 111, 11, 2),
    (-5, 3, 123456791, 123456789)
])
def test_GFpn_add(value1, value2, p, expected_value):
    el1 = ElementInGFp(value1, p)
    el2 = ElementInGFp(value2, p)
    result = el1 + el2

    assert isinstance(result, ElementInGFp)
    assert result.value == expected_value


@pytest.mark.parametrize('value1, value2, p, expected_value', [
    (3, 1, 5, 2),
    (223, 1, 11, 2),
    (3, 5, 123456791, 123456789)
])
def test_GFpn_sub(value1, value2, p, expected_value):
    el1 = ElementInGFp(value1, p)
    el2 = ElementInGFp(value2, p)
    result = el1 - el2

    assert isinstance(result, ElementInGFp)
    assert result.value == expected_value


@pytest.mark.parametrize('el1, el2, expected_value', [
    (ElementInGFp(2, 5), ElementInGFp(2, 5), 4),
    (ElementInGFp(-111, 11), ElementInGFp(-2, 11), 2),
    (ElementInGFp(-1, 123456791), ElementInGFp(2, 123456791), 123456789),
    (ElementInGFp(2, 5), 2, 4),
    (-111, ElementInGFp(-2, 11), 2),
])
def test_GFpn_mul(el1, el2, expected_value):
    result = el1 * el2

    assert isinstance(result, ElementInGFp)
    assert result.value == expected_value
