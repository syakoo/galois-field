from .types import Fp


def inverse_el(el: Fp, p: int) -> Fp:
    """Inverse an element over Fp

    Args:
        el (Fp): An element in Fp
        p (int): A prime number

    Returns:
        Fp: The inverse of the element over Fp
    """
    return pow(el, p-2, p)
