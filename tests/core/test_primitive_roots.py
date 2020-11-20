import pytest

from galois_field.core import primitive_roots as pr


@pytest.mark.parametrize('inputs, expected', [
    ((2, 5), True),
    ((4, 5), False),
    ((11, 31), True),
    ((9, 31), False),
    ((295, 499), True),
    ((296, 499), False),
    ((2, 5, [2, 2]), True),
    ((4, 5, [2, 2]), False),
    ((11, 31, [2, 3, 5]), True),
    ((9, 31, [2, 3, 5]), False),
    ((295, 499, [2, 3, 83]), True),
    ((296, 499, [2, 3, 83]), False)
])
def test_is_primitive_root_over_Fp(inputs, expected):
    result = pr.is_primtive_root_over_Fp(*inputs)

    assert result == expected
