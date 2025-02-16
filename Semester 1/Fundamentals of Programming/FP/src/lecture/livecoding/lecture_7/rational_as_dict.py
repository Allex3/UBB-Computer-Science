from math import gcd

from pdoc import pdoc


def create_rational(num: int, denom: int = 1):
    """
    Create a rational number

    This is a *bit of* written **text**.

    an example of calling the function
    >>> create_rational(1, 2)

    :param num: numerator
    :param denom: non-zero denominator
    :return: the created number

    :raises: Raises ValueError in case the denom is 0
    """
    if denom == 0:
        raise ValueError("Denominator must be non-0")

    _gcd = gcd(num, denom)
    return {"num": num // _gcd, "denom": denom // _gcd}


def get_numerator(q) -> int:
    return q["num"]


def get_denominator(q) -> int:
    return q["denom"]


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


if __name__ == "__main__":
    """
    Generate HTML documentation using the pdoc package
    """
    f = open("doc.html", "wt")
    f.write(pdoc("rational_as_dict.py", ""))
    f.close()