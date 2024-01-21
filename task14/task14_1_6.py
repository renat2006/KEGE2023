from collections import Counter
from string import digits, ascii_lowercase


def n_to_p(n, p):
    letters = digits + ascii_lowercase
    num = ''
    while n:
        num = letters[n % p] + num
        n //= p
    return num


t = str(n_to_p(5 * 49 ** 5 + 3 * 7 ** 8 - 7 * 7 ** 4 + 100, 7))
print(sum(map(int, t)))
