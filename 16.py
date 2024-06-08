from sys import setrecursionlimit
from functools import cache, lru_cache

setrecursionlimit(400000)



def f(n):
    if n <= 1:
        return 1

    return n * f(n - 1)


print((f(2024) // 8 - f(2023)) // f(2022))
