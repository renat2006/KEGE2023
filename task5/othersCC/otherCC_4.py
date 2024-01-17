from string import ascii_lowercase, digits


def n_to_p(n, p):
    letters = digits + ascii_lowercase
    num = ''
    while n:
        num = letters[n % p] + num
        n //= p
    return num


def f1(n):
    s = n_to_p(n, 7)
    s_sum = sum(int(digit) for digit in s)
    s_sum_sept = n_to_p(s_sum, 7)
    return '10' + s[2:] + s_sum_sept


def f2(s):
    s_sum = sum(int(digit) for digit in s)
    s_sum_sept = n_to_p(s_sum, 7)
    return '100' + s[3:] + s_sum_sept


def f3(s):
    s_sum = sum(int(digit) for digit in s)
    s_sum_sept = n_to_p(s_sum, 7)
    return int('1000' + s[4:] + s_sum_sept, 7)


min_N = 1e9
for N in range(100, int(1e5)):
    result1 = f1(N)
    result2 = f2(result1)
    result3 = f3(result2)
    if result3 < min_N and result3 > 1e5:
        min_N = result3
print(min_N)
