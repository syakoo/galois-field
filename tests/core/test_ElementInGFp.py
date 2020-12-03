import pytest

from galois_field.core.ElementInGFp import ElementInGFp


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
    (1, 5, '1 (mod 5)'),
    (222, 11, '2 (mod 11)'),
    (-2, 123456791, '123456789 (mod 123456791)')
])
def test_GFElementInGFp_str(value, p, expected):
    result = ElementInGFp(value, p)

    assert str(result) == expected


@pytest.mark.parametrize('value, p, expected', [
    (1, 5, 'ElementInGFp(1, 5)'),
    (222, 11, 'ElementInGFp(2, 11)'),
    (-2, 123456791, 'ElementInGFp(123456789, 123456791)')
])
def test_GFElementInGFp_repr(value, p, expected):
    result = ElementInGFp(value, p)

    assert repr(result) == expected


@pytest.mark.parametrize('value1, value2, p, expected_value', [
    (1, 1, 5, 2),
    (111, 111, 11, 2),
    (-5, 3, 123456791, 123456789)
])
def test_GFElementInGFp_add(value1, value2, p, expected_value):
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
def test_GFElementInGFp_sub(value1, value2, p, expected_value):
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
def test_GFElementInGFp_mul(el1, el2, expected_value):
    result = el1 * el2

    assert isinstance(result, ElementInGFp)
    assert result.value == expected_value


@pytest.mark.parametrize('el1, el2, expected_value', [
    (ElementInGFp(4, 5), ElementInGFp(2, 5), 2),
    (ElementInGFp(2, 11), ElementInGFp(8, 11), 3),
    (ElementInGFp(-2, 123456791), ElementInGFp(123456789, 123456791), 1),
    (ElementInGFp(4, 5), 2, 2),
    (2, ElementInGFp(8, 11), 3),
])
def test_GFElementInGFp_div(el1, el2, expected_value):
    result = el1 / el2

    assert isinstance(result, ElementInGFp)
    assert result.value == expected_value


@pytest.mark.parametrize('el1, exp, expected_value', [
    (ElementInGFp(4, 7), 5, 2),
    (ElementInGFp(2, 11), 5, 10),
    (ElementInGFp(2, 11), ElementInGFp(5, 11), 10),
    (ElementInGFp(-2, 123456791), 123456789, 61728395),
])
def test_GFElementInGFp_pow(el1, exp, expected_value):
    result = el1 ** exp

    assert isinstance(result, ElementInGFp)
    assert result.value == expected_value


@pytest.mark.parametrize('el1, el2, expected', [
    (ElementInGFp(4, 5), ElementInGFp(4, 5), True),
    (ElementInGFp(2, 11), ElementInGFp(8, 11), False),
    (ElementInGFp(-2, 123456791), ElementInGFp(123456789, 123456791), True),
    (ElementInGFp(2, 5), 2, True),
    (ElementInGFp(2, 5), ElementInGFp(2, 8), True),
    (2, ElementInGFp(2, 11), True),
])
def test_GFElementInGFp_equal(el1, el2, expected):
    result = el1 == el2

    assert result == expected


@pytest.mark.parametrize('value, p, expected', [
    (1, 5, 1),
    (222, 11, 2),
    (-2, 123456791, 123456789)
])
def test_ElementInGFp_int(value, p, expected):
    el = ElementInGFp(value, p)

    assert int(el) == expected


@pytest.mark.parametrize("el, expected_value", [
    (ElementInGFp(1, 2), 1),
    (ElementInGFp(-1, 7), 6),
    (ElementInGFp(123456789, 123456791), 61728395),
])
def test_GFElementInGFp_inverse(el, expected_value):
    """el^{-1} = expected (mod p)"""
    result = el.inverse()

    assert result.value == expected_value
