def f(n):
    f1 = bin(n)[2:].rjust(8, "0")
    f2 = "".join(list(map(lambda x: str(int(not int(x))), f1)))

    return int(f2, 2)


for n in range(1, int(1e9)):
    result = f(n)
    if result - n == 131:
        print(n)
        break
