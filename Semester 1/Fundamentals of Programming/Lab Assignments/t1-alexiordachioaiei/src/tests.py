from venv import create

from operations import *


def test_add() -> None:
    """
    Tests the add function with multiple tests
    :return: None
    """
    warehouse = [create_product(["Napkins_Pack", 10, 5]), create_product(["Biscuit", 6, 4]),
                 create_product(["Pizza", 15, 8])]
    add(warehouse, ["Jelly", 2, 4])
    assert warehouse == [create_product(["Napkins_Pack", 10, 5]), create_product(["Biscuit", 6, 4]),
                         create_product(["Pizza", 15, 8]), create_product(["Jelly", 2, 4])]

    warehouse = [create_product(["Napkins_Pack", 10, 5]), create_product(["Biscuit", 6, 4]),
                 create_product(["Pizza", 15, 8])]
    try:
        add(warehouse, ["Jelly", 2])
    except ValueError:
        assert True

    try:
        add(warehouse, ["Jelly", -2, 5])
    except ValueError:
        assert True


def test_remove() -> None:
    """
    Tests the remove operation with multiple tests
    :return: None
    """
    warehouse = [create_product(["Napkins_Pack", 10, 5]), create_product(["Biscuit", 6, 4]),
                 create_product(["Pizza", 15, 8])]
    foo = remove(warehouse, "Biscuit")
    assert warehouse == [create_product(["Napkins_Pack", 10, 5]),
                         create_product(["Pizza", 15, 8])]
    assert foo == True

    warehouse = [create_product(["Napkins_Pack", 10, 5]), create_product(["Biscuit", 6, 4]),
                 create_product(["Pizza", 15, 8])]
    bar = remove(warehouse, "Jelly")
    assert warehouse == [create_product(["Napkins_Pack", 10, 5]), create_product(["Biscuit", 6, 4]),
                         create_product(["Pizza", 15, 8])]
    assert bar == False


def test_list_all() -> None:
    """
    Tests the list_all operation with multiple tests
    :return: None
    """
    warehouse = [create_product(["Napkins_Pack", 10, 5]), create_product(["Biscuit", 6, 4]),
                 create_product(["Pizza", 15, 8]), create_product(["A", 4, 3])]
    new_warehouse = list_all(warehouse)
    assert new_warehouse == [product_to_string(create_product(["Pizza", 15, 8])), product_to_string(create_product(["Napkins_Pack", 10, 5])),
                            product_to_string(create_product(["Biscuit", 6, 4])),
                            product_to_string(create_product(["A", 4, 3]))]

def test_list_total() -> None:
    """
    Tests the list_total operation with multiple tests
    :return: None
    """
    warehouse = [create_product(["Napkins_Pack", 10, 5]), create_product(["Biscuit", 6, 4]),
                 create_product(["Pizza", 15, 8]), create_product(["A", 4, 3])]
    assert list_total(warehouse) == 10*5+6*4+15*8+4*3

    warehouse = []
    assert list_total(warehouse)==0
if __name__ == "__main__":
    test_add()
    test_remove()
    test_list_all()
    test_list_total()
