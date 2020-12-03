import numpy as np
import pytest

from galois_field.core import primitive_roots as pr
from galois_field.core.ElementInGFp import ElementInGFp
from galois_field.core.ElementInGFpn import ElementInGFpn


@pytest.mark.parametrize('inputs, expected', [
    ((ElementInGFp(2, 5),), True),
    ((ElementInGFp(4, 5),), False),
    ((ElementInGFp(11, 31),), True),
    ((ElementInGFp(9, 31),), False),
    ((ElementInGFp(295, 499),), True),
    ((ElementInGFp(296, 499),), False),
    ((ElementInGFp(2, 5), [2, 2]), True),
    ((ElementInGFp(4, 5), [2, 2]), False),
    ((ElementInGFp(11, 31), [2, 3, 5]), True),
    ((ElementInGFp(9, 31), [2, 3, 5]), False),
    ((ElementInGFp(295, 499), [2, 3, 83]), True),
    ((ElementInGFp(296, 499), [2, 3, 83]), False),
    ((ElementInGFpn(np.array([1, 0]), 2, np.poly1d([1, 1, 1])),), True),
    ((ElementInGFpn(np.array([1]), 2, np.poly1d([1, 1, 1])),), False),
    ((ElementInGFpn(np.array([2, 2, 3]), 7, np.poly1d([1, 0, 0, 2])),), True),
    ((ElementInGFpn(np.array([2, 3]), 7, np.poly1d([1, 0, 0, 2])),), False),
    ((ElementInGFpn(np.array([2, 3]), 11, np.poly1d([1, 0, 1, 4])),), True),
    ((ElementInGFpn(np.array([2, 2, 3]),
                    11, np.poly1d([1, 0, 1, 4])),), False),
    ((ElementInGFpn(np.array([1, 0]), 2, np.poly1d([1, 1, 1])), [2, 2]), True),
    ((ElementInGFpn(np.array([1]), 2, np.poly1d([1, 1, 1])), [2, 2]), False),
])
def test_is_primitive_root(inputs, expected):
    result = pr.is_primtive_root(*inputs)

    assert result == expected


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
def test_random_primitive_root_over_Fp(p, expected_contain):
    LOOP_NUM = 5

    for _ in range(LOOP_NUM):
        result = pr.random_primitive_root_over_Fp(p)

        assert isinstance(result, ElementInGFp)
        assert result.value in expected_contain


@pytest.mark.parametrize('p, mod_coeffs, expected_contain', [
    (2, [1, 1, 1], [[1, 0], [1, 1]]),
    (3, [1, 1, 0, 2], [[1, 2], [2, 0], [2, 2], [1, 0, 1], [1, 0, 2], [1, 2, 0],
                       [2, 0, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]),
])
def test_random_primitive_root_over_Fpn(p, mod_coeffs, expected_contain):
    LOOP_NUM = 5
    expected_contain_str = list(map(str, expected_contain))

    for _ in range(LOOP_NUM):
        result = pr.random_primitive_root_over_Fpn(p, mod_coeffs)

        assert isinstance(result, ElementInGFpn)
        assert str(list(result.coeffs)) in expected_contain_str
