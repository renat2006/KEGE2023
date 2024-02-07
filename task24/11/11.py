with open("data.txt") as f:
    s = f.readline().strip()
    k = 1
    count = 0
    for i in range(1, len(s)):
        c1 = s[i - 1]
        c2 = s[i]
        if int(c2) >= int(c1):
            k += 1
        else:
            if k == 6:
                count += 1
            k = 1
if k == 6:
    count += 1
print(count)
