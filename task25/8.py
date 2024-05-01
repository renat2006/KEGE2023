def find_divs(num: int):
    divs = set()
    c = 2
    while c * c < num + 1:
        if num % c == 0:
            divs.add(c)
            while num % c == 0:
                num //= c
        c += 1
    if num > 1:
        divs.add(num)

    return sorted(list(divs))


def get_E(divs: list):
    return 0 if not divs else sum(divs)


k = 0
p = []
for i in range(700000, 0, -1):
    E = get_E(find_divs(i))
    if E and E % 7 == 0 and i % 5 != 0:
        k += 1
        p.append(f"{i}*{E}")
    if k == 5:
        break
print('-'.join(p[::-1]))
