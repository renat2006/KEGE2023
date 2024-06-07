import math

with open("data.txt") as f:
    N = int(f.readline().strip())
    prices = list(map(int, f.readlines()))
    L = 500
    D = 0.8

    more_than150 = sorted([x for x in prices if x > L])
    S = sum(x for x in prices if x <= L)
    nDisc = len(more_than150) // 2
    with_disc = more_than150[:nDisc]
    without_disc = more_than150[nDisc:]
    S += sum(with_disc) * D + sum(without_disc)
    print(math.ceil(S), with_disc[-1])
