import pytest

from galois_field.GFp import GFp
from galois_field.core.ElementInGFp import ElementInGFp


@pytest.mark.parametrize('p', [(5), (2), (123456791)])
def test_GFp_init(p):
    gf = GFp(p)
    assert gf.p == p


@pytest.mark.parametrize('p', [(6), (4), (123456789)])
def test_GFp_raises(p):
    with pytest.raises(ValueError):
        GFp(p)


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


@pytest.mark.parametrize('p, expected_contain', [
    (5, [2, 3]),
    (31, [3, 11, 12, 13, 17, 21, 22, 24]),
    (499, [7, 10, 11, 15, 17, 19, 23, 28, 35, 40, 41, 42, 44, 50, 53, 58, 60,
           61, 63, 65, 66, 68, 71, 75, 76, 79, 85, 86, 87, 89, 90, 92, 94, 95,
           98, 99, 102, 112, 113, 114, 129, 135, 138, 141, 146, 147, 153, 157,
           160, 163, 164, 168, 171, 173, 176, 179, 182, 185, 193, 200, 202, 205,
           206, 207, 210, 212, 214, 217, 218, 219, 223, 229, 232, 238, 240, 241,
           242, 244, 246, 252, 260, 262, 264, 266, 271, 272, 273, 274, 275, 278,
           284, 286, 295, 300, 301, 302, 303, 304, 309, 310, 311, 315, 316, 318,
           319, 321, 325, 327, 329, 340, 341, 344, 347, 348, 349, 356, 357, 362,
           363, 366, 367, 368, 369, 373, 376, 377, 378, 379, 380, 383, 390, 392,
           393, 394, 396, 398, 399, 408, 411, 415, 417, 419, 426, 429, 430, 442,
           443, 448, 450, 452, 453, 454, 456, 461, 465, 466, 469, 470, 474, 477,
           478, 479, 485, 494]),
])
def test_GFp_random_primitive_root(p, expected_contain):
    LOOP_NUM = 5
    gfp = GFp(p)

    for _ in range(LOOP_NUM):
        result = gfp.random_primitive_elm()

        assert isinstance(result, ElementInGFp)
        assert result.value in expected_contain
