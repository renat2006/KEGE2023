from functools import lru_cache

END = 131

moves = [0, 0, 0]


@lru_cache(None)
def f(a):
    global moves
    if a >= END:
        return 0
    t = []
    if moves[0] != 1:
        t.append(f(a + 2))
        moves = [1, 0, 0]
    elif moves[1] != 1:
        t.append(f(a + 3))
        moves = [0, 1, 0]
    elif moves[2] != 1:
        t.append(f(a * 2))
        moves = [0, 0, 1]

    n = [i for i in t if i <= 0]
    if n:
        return -max(n) + 1
    else:
        return -max(t)


min1 = 1e9
min2 = 1e9
for i in range(1, 131):
    if f(i) == -1:
        min1 = min(min1, i)
    elif f(i) == 1:
        min2 = min(min2, i)
print(min1, min2, min(min1, min2))