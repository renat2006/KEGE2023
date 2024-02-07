with open("data.txt") as f:
    s = f.readline().strip()

    k = [0] * 40
    for i in range(2, len(s)):
        c1 = s[i - 2]
        c2 = s[i - 1]
        c3 = s[i]

        if c1 == c3 == "S":
            k[ord(c2) - ord("A")] += 1

print(sorted(k))  # min = 260
print(chr(len(k) - k[::-1].index(260) - 1 + ord("A")), 260, sep="")
