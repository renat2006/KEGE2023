from string import ascii_lowercase, digits

def n_to_p(n, p):
    letters = digits + ascii_lowercase
    num = ''
    while n:
        num = letters[n % p] + num
        n //= p
    return num

def f(n):
    f1 = n_to_p(n, 4)
    if n % 2 == 1:
        f1 = '2' + f1 + '11'
    else:
        f1 = '13' + f1 + '02'
    return int(f1, 4)

min_v = 1e9
for n in range(1, 100000):
    res = f(n)
    if 1000 <res < min_v:
        min_v = res


print(min_v)
