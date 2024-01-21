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

m = 0
for x in letters[:15]:
    t1 = f"131{x}1"
    t2 = f"13{x}3"
    t = int(t1, 15) + int(t2, 17)
    if t % 11 == 0:
        m = t
print(m / 11)
