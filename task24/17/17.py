with open("data.txt") as f:
    vowel = "OIA"
    s = f.readline().strip()
    k = 0
    m = 0
    i = 0
    while i < len(s) - 1:
        c1 = s[i]
        c2 = s[i + 1]
        if c1 not in vowel and c2 in vowel:
            k += 1
            i += 2
        else:
            k = 0
            i += 1
        if k > m:
            m = k

print(m)
