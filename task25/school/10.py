def F(k):
    return 777555 - k


def divs(num: int) -> list:
    dvs = {1, num}
    for n in range(2, round(num ** 0.5) + 1):
        if num % n == 0:
            dvs.add(n)
            dvs.add(num // n)
    return sorted(dvs)


def even_dvs(divs: list) -> list:
    return list(filter(lambda x: x % 2 == 0, divs))


c = 0
for k in range(10 ** 10):
    fk = F(k)
    dv = divs(fk)
    ed = even_dvs(dv)
    if len(ed) % 2 != 0:
        print(f'{k}*{len(ed)}', end='-')
        c += 1
    if c == 5:
        break
