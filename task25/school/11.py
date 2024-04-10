import fnmatch


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
for i in range(135001, 10 ** 10):
    dv = divs(i)
    ed = even_dvs(dv)
    if fnmatch.fnmatch(str(i), "1*717*1?") and len(ed) > 4:
        print(f'{i}*{sum(ed)}', end='-')
        c += 1
    if c == 6:
        break
