from collections import Counter
from string import digits, ascii_lowercase


def n_to_p(n, p):
    letters = digits + ascii_lowercase
    num = ''
    while n:
        num = letters[n % p] + num
        n //= p
    return num


letters = digits + ascii_lowercase
k = 0
sxy = 1e9
s = 0
for p in range(2, int(1e6)):
    for x in range(0, p):
        for y in range(1, p):
            for z in range(0, p):
                t1 = 6 * p ** 3 + x * p ** 2 + 5 * p ** 1 + x * p ** 0
                t2 = 1 * p ** 3 + x * p ** 2 + 6 * p ** 1 + 5 * p ** 0
                t3 = y * p ** 3 + 8 * p ** 2 + z * p ** 1 + 0 * p ** 0
                t = t1 + t2
                if t == t3:
                    xyz = x * p ** 2 + y * p ** 1 + z * p ** 0
                    print(f'{p=}, {x=}, {y=}, {z=}, {xyz=}')
                    break


