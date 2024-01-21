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
for x in letters[:11]:
    for y in letters[:11]:
        t1 = f"7{y}23{x}5"
        t2 = f"67{x}9{y}"
        t = int(t1, 25) + int(t2, 11)
        if t % 131 == 0:
                s = t

print(s / 131)
