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

for x in range(2, 80):
    t1 = 5 * x ** 4 + 5 * x ** 3 + 1 * x ** 2 + 1 * x ** 1 + 3 * x ** 0
    t2 = 7 * 80 ** 3 + x * 80 ** 2 + x * 80 ** 1 + 5 * 80 ** 0
    t = abs(t1 - t2)
    if t <= 1e6:
        k += 1
print(k)
