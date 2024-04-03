
for i in range(194567, 194570 + 1):
    d = []
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            if j % 2 != 0:
                d.append(j)
            if (i / j) % 2 != 0 and (i / j) != j:
                d.append(i // j)
    if len(d) == 4:
        print(sorted(d, reverse=True))
