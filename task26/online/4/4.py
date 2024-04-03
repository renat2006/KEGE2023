with open("data.txt") as f:
    NM = f.readline().split()
    N = int(NM[0])
    M = int(NM[1])
    sizes = sorted(list(map(lambda x: int(x.strip()), f.readlines())))
    k1 = 0
    k2 = 0
    twenny_sizes = sorted(list(filter(lambda x: 200 <= x <= 220, sizes)), reverse=True)
    print(M, twenny_sizes)
    m = twenny_sizes[0]
    other_sizes = sorted(list(filter(lambda x: not (200 <= x <= 220), sizes)))
    print(other_sizes)

    for s in twenny_sizes:
        if M - s >= 0:
            M -= s
            k1 += 1
        else:
            break
    print(m, M)
    for s in other_sizes:
        if M - s >= 0:
            M -= s
            k2 += 1
        else:
            break
    print(M, M + other_sizes[k2 - 1])
    kandidates = list(filter(lambda x: M + other_sizes[k2 - 1] >= x > m, other_sizes))
    print(k1 + k2, max(max(kandidates), m))
