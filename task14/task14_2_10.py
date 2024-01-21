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

for x in range(2, 100):
    t1 = 1 * x ** 4 + 3 * x ** 3 + 1 * x ** 2 + 5 * x ** 1 + 2 * x ** 0
    t2 = 7 * 100 ** 3 + x * 100 ** 2 + 2 * 100 ** 1 + 5 * 100 ** 0
    t = t1 + t2
    if t % 11 == 0:
        k += 1
print(k)
