for i in range(1500000, 3000000):
    c = 0
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            if j % 2 != 0:
                c += 1
            if (i / j) % 2 != 0 and (i / j) != j:
                c += 1
    if c == 7:
        print(i)
