def f(c, e):
    if c > e:
        return 0
    if c == e: return 1
    return f(c + 2, e) + f(c * 2, e)


print(f(1, 18) * f(18, 52))
