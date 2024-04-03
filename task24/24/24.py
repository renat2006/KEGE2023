import re

with open("data.txt") as f:
    s = f.readline().strip()

    i = 1
    k = 0
    m = 0
    while i < len(s) - 1:
        if (s[i + 1] == "3" and s[i - 1] == "3") or (s[i + 1] == "1" and s[i - 1] == "1"):
            k += 1
            i += 3
        else:
            k = 0
            i += 1
        if k > m:
            m = k
    if k > m:
        m = k
    print(m)
