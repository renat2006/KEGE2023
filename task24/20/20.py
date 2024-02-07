with open("data.txt") as f:
    s = f.readline().strip()
    k = 0
    m = 0
    i = s.find("KEGE")

    while i < len(s):
        if s[i:i + 4] == "KEGE":
            k += 4
            i += 3
        elif k:
            if s[i:i + 3] == "KEG":
                k += 3
                i += 2
            elif s[i:i + 2] == "KE":
                k += 2
                i += 1
            elif s[i] == "K":
                k += 1
            m = max(m, k)
            k = 0
        i += 1


print(m)
