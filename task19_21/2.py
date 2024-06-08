from functools import lru_cache

END = 0


@lru_cache(None)
def f(a):
    if a <= END:
        return 0
    t = [f(int(a // 3))]
    if a >= 5:
        t.append(f(a - 5))
    n = [i for i in t if i <= 0]
    if n:
        return -max(n) + 1
    else:
        return -max(t)


for i in range(1000, 0, -1):
    if f(i) == -1:
        print(i)
        break
