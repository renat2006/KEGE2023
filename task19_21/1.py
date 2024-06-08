from functools import lru_cache


@lru_cache(None)
def f(a):
    if a >= 229:
        return 0
    t = [f(a * 2), f(a + 2), f(a + 3), f(a + 4)]
    n = [i for i in t if i <= 0]
    if n:
        return -max(n) + 1
    else:
        return -max(t)


for i in range(1, 229):
    if f(i) == -1:
        print(i)
