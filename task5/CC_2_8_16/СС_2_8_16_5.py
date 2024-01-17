def f(n):
    f1 = bin(n)[2:]
    fist_1 = f1.find("1")
    second_1 = f1.find("1", fist_1 + 1)

    f2 = "0" if second_1 == -1 else f1[second_1:]
    print(f'{fist_1= }, {second_1= }, {f1=}, {f2=}')
    return int(f2, 2)


diff = set()
for n in range(131, 3131):
    result = f(n)
    print(n, result, result - n)
    diff.add(result - n)
print(f'{diff=}, {len(diff)}')
