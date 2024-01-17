def f(n):
    f1 = bin(n)[2:]
    f2 = f1[:-1]
    f3 = f2 + "01" if n % 2 == 0 else f1 + "10"
    return int(f3, 2)


for n in range(1, int(1e9)):
    result = f(n)
    if result == 2025:
        print(n)
        break
