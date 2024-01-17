def f(n):
    f1 = bin(n)[2:]

    f2 = f1 + "1" if f1.count("1") > f1.count("0") else f1 + "0"
    return int(f2, 2)


min_r = 1e9
for n in range(1, int(1e5)):
    result = f(n)
    if 100 < result < min_r:
        min_r = result
print(min_r)