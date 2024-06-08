for i in range(100, 1500000):

    n = str(i)
    n2 = []
    for j in range(len(n) - 2):

        n2.append(int(n[j:j+3]))
    if max(n2) - min(n2) == 415:
        print(n)

