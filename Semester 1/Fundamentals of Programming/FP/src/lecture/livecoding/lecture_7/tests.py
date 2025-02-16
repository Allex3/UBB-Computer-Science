from lecture.livecoding.lecture_7.calc import create_calc, get_calc_value, add_calculator
from lecture.livecoding.lecture_7.rational_as_dict import create_rational, get_numerator, get_denominator, add_rational

"""
    1. Test functions don't take parameters and return nothing :(
    2. Test functions can be run in amy order
    3. Test functions do not interact with the user
    4. Test function executions don't produce an effect as long as the test passes
    5. Test functions result in an AssertionError in case of problems
"""


def test_rational():
    q = create_rational(10, 2)
    assert get_numerator(q) == 5
    assert get_denominator(q) == 1

    q = create_rational(2, 3)
    assert get_numerator(q) == 2
    assert get_denominator(q) == 3
    """
    Syntax:
    assert <condition>
    if <condition> == True, nothing happens => test has passed
    if <condition> == False, AssertionError is raised => test has failed :(
    """

    q = create_rational(47, 1)
    assert get_numerator(q) == 47
    assert get_denominator(q) == 1

    q = create_rational(23)
    assert get_numerator(q) == 23
    assert get_denominator(q) == 1

    q = create_rational(0)
    assert get_numerator(q) == 0
    assert get_denominator(q) == 1

    try:
        q = create_rational(5, 0)
        assert False  # the function above should have raised a ValueError
    except ValueError:
        assert True

    q1 = create_rational(2, 3)
    q2 = create_rational(2, 3)
    q3 = add_rational(q1, q2)  # 4/3
    assert get_numerator(q3) == 4
    assert get_denominator(q3) == 3

    q1 = create_rational(6, 3)
    q2 = create_rational(6, 3)
    q3 = add_rational(q1, q2)  # 12/3 == 4
    assert get_numerator(q3) == 4
    assert get_denominator(q3) == 1


def test_calculator():
    calc = create_calc()
    val = get_calc_value(calc)
    assert get_numerator(val) == 0
    assert get_denominator(val) == 1

    add_calculator(calc, create_rational(1, 4))
    val = get_calc_value(calc)
    assert get_numerator(val) == 1
    assert get_denominator(val) == 4

    add_calculator(calc, create_rational(3, 4))
    val = get_calc_value(calc)
    assert get_numerator(val) == 1
    assert get_denominator(val) == 1

"""
    A few problems with this implementation :(
    1. We have to explicitly call test functions
    2. Separate running the tests from running the program
    3. Keep running existing tests, even when some of them fail
    4. How do I know I've written enough tests?
    5. A fancier way of examining test results :)
"""
test_rational()
test_calculator()