def f(n):
    f1 = bin(n)[2:]

    f2 = f1[::-1]
    return int(f2, 2)


for n in range(1, 201):
    result = f(n)
    if result == 21:
        print(n)
