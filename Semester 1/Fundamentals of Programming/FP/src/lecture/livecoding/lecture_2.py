def fact(n: int) -> int:
    # Base case of recursion
    if n == 0:
        return 1

    # Recursion progresses towards the base case
    return n * fact(n - 1)


# for i in range(1050):
#     print(i, fact(i))


def fib(n: int) -> int:
    if n < 2:
        return 1

    return fib(n - 2) + fib(n - 1)


# key 0 has associated value 1
# key 1 has associated value 1
cache = {0: 1, 1: 1}


def fib_cached(n: int) -> int:
    if n in cache:
        return cache[n]

    cache[n] = fib_cached(n - 2) + fib_cached(n - 1)
    return cache[n]


for i in range(35):
    # print(i, fib(i))
    print(i, fib_cached(i))
