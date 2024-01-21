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
for x in letters[:25]:
    t1 = f"3{x}4{x}3{x}3"
    t2 = f"1{x}3{x}1{x}"
    t = int(t1, 25) + int(t2, 25)
    if t % 24 == 0:
        k += 1
print(k)