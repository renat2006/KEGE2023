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
for A in range(1, int(1e4)):
    for x in letters[:13]:
        for y in letters[:13]:
            M = f"2{y}23{x}5"
            N = f"67{x}9{y}"
            t = int(M, 15) + A
            if t % int(N, 13) == 0:
                    print(A)



