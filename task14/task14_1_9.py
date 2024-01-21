from collections import Counter
from string import digits, ascii_lowercase


def n_to_p(n, p):
    letters = digits + ascii_lowercase
    num = ''
    while n:
        num = letters[n % p] + num
        n //= p
    return num


m = -1
for n in range(1, int(1e6)):
    if len(n_to_p(n, 12)) == 2 and n_to_p(n, 16)[-1] == "3" and n_to_p(n, 5)[-1] == "1" and n > m:
        m = n
print(m)
