# def fact(n) -> int:
#     if (n==0):
#         return 1
#     return n*fact(n-1)
#
# for i in range(100):
#     print(i, fact(i))

cache = {0: 1, 1: 1} #first two fibonacci numbers

def fib_cached(n: int) -> int:
    if n in cache: #key n (nth fibonacci number) in cache
        return cache[n]

    cache[n] = fib_cached(n-1) + fib_cached(n-2)
    return cache[n]