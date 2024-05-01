def find_div(num: int):
    divs = set()
    for d in range(2, round(num ** 0.5) + 1):
        if num % d == 0:
            divs.add(d)
            divs.add(num // d)
    return sorted(list(divs))


def get_M(divs: list):
    return 0 if not divs else divs[0] + divs[-1]


k = 0
for i in range(777829, 10000000000):
    M = get_M(find_div(i))
    if M % 100 == 16:
        k += 1
        print(i, M, sep="*", end="-")
    if k == 5:
        break
