from collections import Counter
from string import digits, ascii_lowercase


def n_to_p(n, p):
    letters = digits + ascii_lowercase
    num = ''
    while n:
        num = letters[n % p] + num
        n //= p
    return num


print(Counter(n_to_p(45*400**10 - 8**5*5**8 + 16*20**3 - 33, 20)))
