from string import digits, ascii_lowercase


def n_to_p(n, p):
    letters = digits + ascii_lowercase
    num = ''
    while n:
        num = letters[n % p] + num
        n //= p
    return num


print(n_to_p(2 * 9 ** 7 - 3 ** 8 - 19, 3).count("2"))
