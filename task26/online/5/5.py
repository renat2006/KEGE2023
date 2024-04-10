with open("data2.txt") as f:
    SN = f.readline().strip().split()
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

    mx = sizes[k - 1]
    for size in sizes:
        if sizes[k-1] + S >= size:
            mx = size
    print(k, mx)

