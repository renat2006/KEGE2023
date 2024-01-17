from string import ascii_lowercase, digits


def n_to_p(n, p):
    letters = digits + ascii_lowercase
    num = ''
    while n:
        num = letters[n % p] + num
        n //= p
    return num


def f_new(N):
    N_base20 = n_to_p(N, 20)
    R_base20 = ''

    for digit in N_base20:

        if digit != 'j':
            alp = digits + ascii_lowercase

            R_base20 += alp[int(digit, 20) + 1]
        else:
            R_base20 += 'j'
    print(N_base20, R_base20)
    R_decimal = int(R_base20, 20)
    return R_decimal


different_numbers = set()

for N in range(1, 10000 + 1):
    R = f_new(N)
    if 1000 <= R <= 10000:
        different_numbers.add(R)

print(len(different_numbers))