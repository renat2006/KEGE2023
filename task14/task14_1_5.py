from collections import Counter
from string import digits, ascii_lowercase


def n_to_p(n, p):
    letters = digits + ascii_lowercase
    num = ''
    while n:
        num = letters[n % p] + num
        n //= p
    return num


print(Counter(n_to_p(3*19**5 + 361**4 - 17*19**3 - 37, 19)))
