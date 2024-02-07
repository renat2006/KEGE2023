with open("data.txt") as f:
    s = f.readline().strip()

    k = 1
    m = 0

    for i in range(1, len(s)):
        c1 = s[i - 1]
        c2 = s[i]

        if (c2.isalpha() and c1.isdigit()) or (c2.isdigit() and c1.isalpha()):
            k += 1
        else:
            k = 1
        m = max(k, m)

print(m)
