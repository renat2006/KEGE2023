with open("data.txt") as f:
    SN = f.readline().split()
    S = int(SN[0])
    N = int(SN[1])
    sizes = sorted(list(map(lambda x: int(x.strip()), f.readlines())))

    k = 0
    for size in sizes:
        if S - size >= 0:
            S -= size
            k += 1
        else:
            break
    m = 0
    for size in sizes:
        if size <= S + sizes[k - 1]:
            m = size
    print(k, m)
