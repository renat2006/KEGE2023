with open("task1.txt") as f:
    store, n = f.readline().strip().split()
    store = int(store)
    files = sorted(list(map(lambda x: int(x.strip()), f.readlines())))
    print(fil)

    k = 0
    m = 0
    for file in files:
        if store - file >= 0:
            store -= file
            k += 1
            if file > m:
                m = file
        else:
            break
    print(k, m)


