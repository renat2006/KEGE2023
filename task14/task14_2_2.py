from collections import Counter
from string import digits, ascii_lowercase


def n_to_p(n, p):
    letters = digits + ascii_lowercase
    num = ''
    while n:
        num = letters[n % p] + num
        n //= p
    return num


for x in "123456789abcdef":
    t1 = f"{x}131{x}131"
    t2 = f"100400{x}"
    t = int(t1, 16) + int(t2, 16)
    if t % 15 == 0:
        print(t / 15)
