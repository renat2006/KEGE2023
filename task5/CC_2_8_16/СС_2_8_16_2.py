def f(n):
    f1 = bin(n)[2:]
    f2 = f1 + f1[-1]
    f3 = f2 + str(f2.count("1") % 2)
    return int(f3, 2)


for n in range(1, int(1e9)):
    result = f(n)
    if result > 167:
        print(result)
        break
