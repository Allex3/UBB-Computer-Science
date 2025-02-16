from src.functions import *
# Testing functions

def test_add():
    l1 = []
    add([-2, 0, 10], l1)
    assert l1==[] # not added

    l2 = []
    add([2, 5, 7], l2)
    assert l2==[create_participant([2, 5, 7], 0)]

    l3 = [create_participant([6, 1 , 7], 0), create_participant([7 ,5, 8], 1)]
    add([6, 8, 9], l3)
    assert l3 == [create_participant([6, 1 , 7], 0), create_participant([7 ,5, 8], 1), create_participant([6, 8, 9], 2)]

def test_insert():
    l1 = []
    try:
        insert([1, 5, 3, 5], l1) #at pos 5
        assert False
    except IndexError:
        assert True

    l2 = []
    try:
        insert([1, 5, 3, 0], l2) #at pos 0
    except IndexError:
        assert True

    l3 = [0, 1, 2, 3, 4, 5] #random list just for testing
    insert([6, 1, 4, 3], l3) # insert at position 3 which this time exists
    assert l3 == [0, 1, 2, create_participant([6, 1, 4], 3), 4, 5]

def test_remove():
    l1 = []
    try:
        remove([3], l1)
        assert False
    except IndexError:
        assert True

    l2 = []
    try:
        remove([2, 4], l2)
        assert False
    except IndexError:
        assert True

    l3 = []
    remove([4, 2], l3)
    assert l3 == [] # no index error, because 4>2

    l4 = [create_participant([1, 5, 3], 0), create_participant([3, 5, 3], 1), create_participant([1, 5, 8], 2)]
    remove([0, 2], l4)
    assert l4 == [create_participant([0, 0, 0], 0), create_participant([0, 0, 0], 1), create_participant([0, 0, 0], 2)]

    l5 = [create_participant([3, 5, 3], 0), create_participant([3, 7, 3], 1), create_participant([1, 3, 8], 2)]
    remove([1], l5)
    assert l5 == [create_participant([3, 5, 3], 0), create_participant([0, 0, 0], 1), create_participant([1, 3, 8], 2)]

    # remove p to q
    l6 = [create_participant([1, 1, 1], 0), create_participant([5, 3, 8], 1), create_participant([3, 4, 3], 2)]
    remove(["<", 4], l6)
    assert l6 == [create_participant([0, 0, 0], 0), create_participant([5, 3, 8], 1), create_participant([0, 0, 0], 2)]

    l7 = [create_participant([4, 4, 5], 0), create_participant([10, 1, 1], 1), create_participant([3, 4, 3], 2)]
    remove(["=", 4], l7)
    assert l7 == [create_participant([0, 0, 0], 0), create_participant([0, 0, 0], 1), create_participant([3, 4, 3], 2)]

    l8 = [create_participant([5, 5, 6], 0), create_participant([10, 1, 5], 1), create_participant([4, 4, 4], 2)]
    remove([">", 4], l8)
    assert l8 == [create_participant([0, 0, 0], 0), create_participant([0, 0, 0], 1), create_participant([4, 4, 4], 2)]

def test_replace():
    l1 = []
    try:
        replace([4, "p2", 5], l1)
        assert False
    except IndexError:
        assert True

    l2 = [create_participant([1, 5, 3], 0), create_participant([3, 5, 3], 1), create_participant([1, 5, 8], 2)]
    replace([1, "p1", 10], l2)
    assert l2 == [create_participant([1, 5, 3], 0), create_participant([10, 5, 3], 1), create_participant([1, 5, 8], 2)]

    l3 = [create_participant([1, 5, 3], 0), create_participant([3, 5, 3], 1), create_participant([1, 5, 8], 2)]
    replace([0, "p2", 10], l3)
    assert l3 == [create_participant([1, 10, 3], 0), create_participant([3, 5, 3], 1), create_participant([1, 5, 8], 2)]

    l4 = [create_participant([1, 5, 3], 0), create_participant([3, 5, 3], 1), create_participant([1, 5, 8], 2)]
    replace([2, "p3", 10], l4)
    assert l4 == [create_participant([1, 5, 3], 0), create_participant([3, 5, 3], 1), create_participant([1, 5, 10], 2)]


def test_parse_command() -> None:
    """

    :return: Does not return anything, only runs tests
    """
    commands = ["add", "insert", "remove", "replace", "list", "top", "undo"]
    incorrect = [0]
    assert parse_command("add", commands) == incorrect
    assert parse_command("ad 615 1531 gjgj", commands) == [-1]

    assert parse_command("insert 10 10 10 at 5", commands) == [2, 10, 10, 10, 5]

    assert parse_command("remove 4", commands) == [3, 4]
    assert parse_command("remove 5 to 7", commands) == [3, 5, 7]

    assert parse_command("replace 4 p22 with 5", commands) == incorrect
    assert parse_command("replace 4 p2 with 5", commands) == [4, 4, "p2", 5]

    assert parse_command("list lol", commands) == incorrect
    assert parse_command("list", commands) == [5]
    assert parse_command("list sorted", commands) == [5, "sorted"]
    assert parse_command("list < 6", commands) == [5, "<", 6]
    assert parse_command("list <= 7", commands) == incorrect

    assert parse_command("top 1 1 1", commands) == incorrect
    assert parse_command("top 4", commands) == [6, 4]
    assert parse_command("top 4 p3", commands) == [6, 4, "p3"]
    assert parse_command("top 4 p5", commands) == incorrect

    assert parse_command("remove 51 2", commands) == incorrect
    assert parse_command("remove < 4", commands) == [3, "<", 4]

    assert parse_command("undo 41421", commands) == incorrect
    assert parse_command("undo", commands) == [7]


if __name__ == "__main__":
    test_parse_command()
    test_add()
    test_insert()
    test_remove()
    test_replace()