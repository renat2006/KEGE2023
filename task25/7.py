def find_div(num: int):
    divs = set()
    for d in range(2, round(num ** 0.5) + 1):
        if num % d == 0:
            divs.add(d)
            divs.add(num // d)
    return sorted(list(divs))


def get_S(divs: list):
    return 0 if not divs else sum(divs)


k = 0
for i in range(131131, 10000000000):
    S = get_S(find_div(i))
    if S and S % 5 == 0:
        k += 1
        print(i, S, sep="*", end="-")
    if k == 5:
        break
