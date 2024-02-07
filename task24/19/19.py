with open("data.txt") as f:
    s = f.readline().strip()
    k = 0
    m = 0
    i = 0
    while i < len(s) - 3:
        c1 = s[i]
        c2 = s[i + 1]
        c3 = s[i + 2]
        c4 = s[i + 3]

        if (c1 + c2 + c3 == "GET" or c1 + c2 + c3 == "EGE") or (c2 + c3 + c4 == "GET" or c2 + c3 + c4 == "EGE"):
            k += 1
            i += 3
        else:
            k = 0

            i += 1
        if k > m:
            m = k

print(m)
