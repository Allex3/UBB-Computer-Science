def func(n, l):
    n = n/2
    l.append(n)
    return n

a = int(input("a: "))
l = []
print(func( a, l))
print(a)
print(l)