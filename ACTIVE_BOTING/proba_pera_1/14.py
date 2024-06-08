import string


def n_to_p(n, p):
    alh = string.digits + string.ascii_uppercase
    s = ''
    num = n
    while num > 0:
        s = alh[num % p] + s
        num //= p
    return s


nu = 3 * 3125**8 + 2 * 625 ** 7 - 4 * 625**6 + 3 * 125 ** 5 - 2 * 25 ** 4 - 2024
print(nu)
nu = n_to_p(nu, 25)
print(nu)
print(str(nu).count("0"))

