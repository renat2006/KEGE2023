with open("data.txt") as f:
    s = f.readline().strip()
    k = 0
    m = 0
    i = 0
    while i < len(s) - 2:
        c1 = s[i]
        c2 = s[i + 1]
        c3 = s[i + 2]
        if c1 + c2 + c3 == "NLO" or c1 + c2 + c3 == "NOL":
            k += 1
            i += 3
        else:
            k = 0
            i += 1
        if k > m:
            m = k

print(m)
