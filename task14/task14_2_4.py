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
goody = 0

for x in letters[:24]:
    for y in letters[:24]:
        t1 = f"3{x}{y}3"
        t2 = f" 1{y}31"
        t = int(t1, 24) + int(t2, 24)
        if t % 5 != 0:
            break
    else:
        goody = x

print(goody)
t1 = f"3{goody}73"
t2 = f" 1731"
t = int(t1, 24) + int(t2, 24)
print(t / 5)
