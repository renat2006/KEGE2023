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
ny = 1e9
s = 0
for x in letters[:15]:
    for y in letters[:17]:
        t1 = f"123{x}5"
        t2 = f"67{y}9"
        t = int(t1, 15) + int(t2, 17)
        if t % 131 == 0:
            if int(y, 17) < ny:
                s = t

print(s / 131)
