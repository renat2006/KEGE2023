from itertools import product

with open("data.txt") as f:
    s = f.readline().strip()
    k = 0
    m = 0
    not_list = list(map("".join, product("KEG", repeat=2)))

    for i in range(1, len(s)):
        c1 = s[i - 1]
        c2 = s[i]
        k += 1
        if any([x == c1 + c2 for x in not_list]):
            if k > m:
                m = k
            k = 0
print(m)
