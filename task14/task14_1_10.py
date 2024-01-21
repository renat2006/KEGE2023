from collections import Counter
from string import digits, ascii_lowercase


def n_to_p(n, p):
    letters = digits + ascii_lowercase
    num = ''
    while n:
        num = letters[n % p] + num
        n //= p
    return num


print(Counter(n_to_p(int(12*32**2 + 16**3 - 0.5 * 8**2 + 12), 8)))
