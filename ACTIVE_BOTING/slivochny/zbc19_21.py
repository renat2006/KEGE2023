def f(s, m):
    if s >= 69:
        return m % 2 == 0
    if m == 0:
        return 0
    dp = [f(s + 1, m - 1), f(s * 2, m - 1)]
    return any(dp) if (m - 1) % 2 == 0 else all(dp)


print(19, [x for x in range(1, 69) if f(x, 2)])
print(20, [x for x in range(1, 69) if not f(x, 1) and f(x, 3)])
print(20, [x for x in range(1, 69) if not f(x, 2) and f(x, 4)])

