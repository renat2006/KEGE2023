from collections import Counter
from string import digits, ascii_lowercase


def n_to_p(n, p):
    letters = digits + ascii_lowercase
    num = ''
    while n:
        num = letters[n % p] + num
        n //= p
    return num


for x in "0123456789abcdefghij":
    t1 = f"12345{x}78"
    t2 = f"9{x}765"
    t = int(t1, 20) + int(t2, 20)
    if t % 19 == 0:
        print(t / 19)
