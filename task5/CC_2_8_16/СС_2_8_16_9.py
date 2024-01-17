def f(n):
    f1 = oct(n)[2:]

    f2 = f1 + f1[1]
    f3 = f2 + f2[-2]
    return int(f3, 8)


N = 100

while True:
    result = f(N)
    if result > 32768:
        break
    N += 1

print(N)
