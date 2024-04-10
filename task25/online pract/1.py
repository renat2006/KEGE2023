def dividers(n: int):
    divs = {1, n}
    for g in range(2, int(n ** 0.5) + 1):
        if n % g == 0:
            divs.add(g)
            divs.add(n // g)
    return sorted(divs)


def F(divs: list):
    odd = 0
    even = 0
    for div in divs:
        if div % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd == 5 and even == 5:
        return True
    else:
        return False


for num in range(10 ** 6, 5 * 10 ** 6):

    dv = dividers(num)

    if F(dv):

        print(num, end=" ")
