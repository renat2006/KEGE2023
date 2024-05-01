def find_divs(num: int):
    divs = set()
    for d in range(1, round(num ** 0.5) + 1):
        if num % d == 0:
            divs.add(d)
            divs.add(num // d)
    return sorted(list(divs))


def get_S_and_M(divs: list):
    m = 1
    for d in divs: m *= d
    return 0 if not divs else (sum(divs), m)


k = 0
for i in range(1500100, 10000000000):
    divs = find_divs(i)
    S_M = get_S_and_M(divs)
    if S_M and S_M[0] % 2 != 0 and S_M[1] % 2 != 0 and 10 < len(divs) < 30:
        k += 1
        print(i, len(divs), sep="*", end="-")
    if k == 5:
        break
