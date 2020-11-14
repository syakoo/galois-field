import pytest

from galois_field.GFp import GFp
from galois_field.ElementInGFp import ElementInGFp


@pytest.mark.parametrize('p', [(5), (2), (123456791)])
def test_GFp_init(p):
    gf = GFp(p)
    assert gf.p == p


@pytest.mark.parametrize('p, expected', [
    (5, 'GF(5)'),
    (2, 'GF(2)')
])
def test_GFp_str(p, expected):
    gf = GFp(p)
    assert str(gf) == expected


@pytest.mark.parametrize('integer, p', [
    (1, 5),
    (2, 11),
    (3, 123456791)
])
def test_GFp_elm(integer, p):
    gf = GFp(p)
    result = gf.elm(integer)

    assert isinstance(result, ElementInGFp)
