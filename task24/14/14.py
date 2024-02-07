with open("data.txt") as f:
    s = f.readline().strip()
    k = 0
    m = 0
    for i in range(1, len(s)):
        c1 = s[i - 1]
        c2 = s[i]
        k += 1
        if c1 + c2 == "BD" or c1 + c2 == "DB":
            if k > m:
                m = k
            k = 0
print(m)


