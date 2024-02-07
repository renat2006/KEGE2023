with open("data.txt") as f:
    s = f.readline().strip()

    k = 0
    m = 0
    i = 0

    while i < len(s) - 1:
        c1 = s[i]
        c2 = s[i + 1]
        if c1 == "L" and c2 == "I":
            k += 1
        elif c1 == "I" and c2 == "S":
            k += 1
        elif c1 == "S" and c2 == "A":
            k += 1
        elif c1 == "A" and c2 == "L":
            k += 1
        else:
            m = max(m, k)
            k = 1

        i += 1

print(m)
