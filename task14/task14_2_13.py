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

for x in letters[:27]:
    for y in letters[:27]:

        t1 = int(f"31{x}131{y}13", 27)
        t2 = int(f"{y}{x}", 27)

        if t1 % 26 == 0 and t2 ** 0.5 % 1 == 0:
            print(f'{x=}, {y=}, {t2}')
            break
