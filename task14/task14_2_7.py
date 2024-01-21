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
for x in letters[1:22]:
    for y in letters[:13]:
        t1 = f"{x}23{x}5"
        t2 = f"67{y}9{y}"
        t = int(t1, 22) - int(t2, 13)
        if t % 57 == 0:
            if int(x, 22) + int(y, 13) < sxy:
                sxy = int(x, 22) + int(y, 13)
                s = t

print(s / 57)
