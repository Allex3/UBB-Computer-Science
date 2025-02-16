"""
    Return the product of the positive numbers on even positions in a list, knowing that at least one such number exists
"""

data = [-2, -1, 5, 8, -6, -5, 2, -4, -3, 10, 11]


def product_chip_conquer(data: list) -> int:
    """
    Calculate the product of the positive numbers in the given list
    :param data: The list
    :return: The product value
    """
    if len(data) < 3:
        # if data[0] > 0:
        #     return data[0]
        # else:
        #     return 1
        return data[0] if data[0] > 0 else 1

    return (data[0] if data[0] > 0 else 1) * product_chip_conquer(data[2:])


def product_chip_conquer_better(data: list, index=0) -> int:
    """
    Calculate the product of the positive numbers in the given list
    :param data: The list
    :return: The product value
    """
    if len(data) - index < 3:
        # if data[0] > 0:
        #     return data[0]
        # else:
        #     return 1
        return data[index] if data[index] > 0 else 1

    return (data[index] if data[index] > 0 else 1) * product_chip_conquer_better(data, index + 2)


def product_divide_halves_impl(data: list, left: int, right: int) -> int:
    if left == right:
        return data[left] if data[left] > 0 and left % 2 == 0 else 1

    m = (left + right) // 2
    return product_divide_halves_impl(data, left, m) * product_divide_halves_impl(data, m + 1, right)


def product_divide_halves(data: list) -> int:
    return product_divide_halves_impl(data, 0, len(data) - 1)


def product_divide_halves_iter(data: list) -> tuple:
    stack = [(0, len(data) - 1)]
    max_stack = len(stack)  # max size of stack
    product = 1

    while len(stack) > 0:
        left, right = stack.pop()

        if left == right:
            # print(len(stack))
            product *= data[left] if data[left] > 0 and left % 2 == 0 else 1
            # continue -- in place of the else statement below
        else:
            m = (left + right) // 2
            stack.append((left, m))
            stack.append((m + 1, right))
            max_stack = max(max_stack, len(stack))
    return max_stack, product  # returns a tuple


# print(product_chip_conquer(data))
# print(product_chip_conquer_better(data))
# print(product_divide_halves(data))

data = list(range(1024))
# print(product_divide_halves(data))
print(product_divide_halves_iter(data))
