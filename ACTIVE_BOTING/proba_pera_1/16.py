def F(n):
    if n >= 2025:
        return n
    return n + 3 + F(n + 3)


print(F(23) - F(21))
