from copy import deepcopy


def get_product_name(product: dict) -> str:
    """
    Returns the product's name
    :param product: The product which we're handling
    :return: The product's name
    """
    return product["name"]


def get_product_price(product: dict) -> int:
    """
    Returns the product's price
    :param product: The product which we're handling
    :return: The product's price
    """
    return product["price"]


def get_product_quantity(product: dict) -> int:
    """
    Returns the product's quantity
    :param product: The product which we're handling
    :return: The product's quantity
    """
    return product["quantity"]


def set_product_name(product: dict, name: str) -> None:
    """
    Sets a product's name
    :param product: The product which we're handling
    :param name: The name we want the product to have
    :return: None
    """
    product["name"] = name


def set_product_price(product: dict, price: int) -> None:
    """
    Sets a product's price
    :param product: The product which we're handling
    :param price: The price of the product
    :return: None
    """
    product["product_name"] = price


def set_product_quantity(product: dict, quantity: int) -> None:
    """
    Sets a product's name
    :param product: The product which we're handling
    :param quantity: The product's quantity
    :return: None
    """
    product["product_name"] = quantity


def product_to_string(product: dict) -> str:
    """
    Returns the string format of a product in the warehouse
    :param product: The product
    :return: The product in string format
    """
    return f"The product {product["name"]} has a price of {product["price"]} and there are {product["quantity"]} of them in the warehouse."

def create_product(attributes: list) -> dict:
    """
    Creates and returns a product made from its attributes
    :param attributes: The list of attributes of the product
    :return: The newly created product
    """

    return {"name":attributes[0], "price":attributes[1], "quantity":attributes[2]}


# Functionality

def add(warehouse: list[dict], attributes: list) -> None:
    """
    Adds a new product in the warehouse
    :param warehouse: The list of products
    :param attributes: The list representing the attributes of the product to add.
    :return: None
    """
    if len(attributes) != 3:
        raise ValueError("The 'add' command has 3 parameters.")
    try:
        attributes[1] = int(attributes[1])
        attributes[2] = int(attributes[2])
    except ValueError:
        raise ValueError("The product's price or quantity are not positive integers.")

    if attributes[1] <=0 or attributes[2]<= 0:
        raise ValueError("The product's price or quantity are not positive integers.")

    new_product = create_product(attributes)
    warehouse.append(new_product)

def remove(warehouse: list[dict], name: str) -> bool:
    """
    Removes a product with a given name from the warehouse
    :param warehouse: The list of products
    :param name: The name of the product to remove
    :return: True if successfully removed, False if the product does not exist
    """

    does_exist = False
    for product in warehouse:
        if get_product_name(product) == name:
            does_exist = True

    if does_exist is False:
        return False

    for product_index in range(len(warehouse)):
        if get_product_name(warehouse[product_index]) == name:
            for j in range(product_index, len(warehouse)-1):
                warehouse[j] = warehouse[j+1]
            warehouse.pop()
            return True

def list_all(warehouse: list[dict]) -> list[str]:
    """
    Returns the list of products sorted in descending order of name, in string format
    :param warehouse: The list of products
    :return: The list of products sorted in descending order of name, in string format
    """

    warehouse_copy = deepcopy(warehouse)
    warehouse_copy.sort(key = get_product_name, reverse=True)

    for i in range(len(warehouse_copy)):
        warehouse_copy[i] = product_to_string(warehouse_copy[i])

    return warehouse_copy

def list_total(warehouse: list[dict]) -> int:
    """
    Computes the total value of the products in the warehouse and returns it
    :param warehouse: The list of products
    :return: The total computed
    """

    total = 0
    for product in warehouse:
        price = get_product_price(product)
        quantity = get_product_quantity(product)
        total += price*quantity

    return total