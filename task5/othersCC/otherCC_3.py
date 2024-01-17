from string import ascii_lowercase, digits


def n_to_p(n, p):
    letters = digits + ascii_lowercase
    num = ''
    while n:
        num = letters[n % p] + num
        n //= p
    return num


def f(n):
    f1 = n_to_p(n, 3)
    if n % 3 == 0:
        f2 = '1' + f1 + '02'
    else:
        f2 = f1 + n_to_p((n % 3) * 4, 3)
    return int(f2, 3)


max_n = 0
for n in range(1, 100000):
    res = f(n)
    if n > max_n and res < 1199:
        max_n = n

print(max_n)
