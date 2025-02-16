from math import gcd


def create_rational(num: int, denom: int = 1):
    """
    Create a rational number
    :param num: numerator
    :param denom: non-zero denominator
    :return: the created number

    :raises: Raises ValueError in case the denom is 0
    """
    if denom == 0:
        raise ValueError("Denominator must be non-0")

    _gcd = gcd(num, denom)
    return [num // _gcd, denom // _gcd]


def get_numerator(q) -> int:
    return q[0]


def get_denominator(q) -> int:
    return q[1]


def to_str(q) -> str:
    # TODO fix 1/-2, 5/-1 etc.
    if get_denominator(q) == 1:
        return str(get_numerator(q))
    return str(get_numerator(q)) + "/" + str(get_denominator(q))


def add_rational(q1, q2):
    gn = get_numerator  # () -- function call operator
    gd = get_denominator
    num = gn(q1) * gd(q2) + gn(q2) * gd(q1)
    denom = gd(q1) * gd(q2)
    return create_rational(num, denom)
