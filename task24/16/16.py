from itertools import product

with open("data.txt") as f:
    s = f.readline().strip()
    k = 0
    m = 0

    for i in range(1, len(s), 2):
        c1 = s[i - 1]
        c2 = s[i]
        if c1 + c2 == "AT" or c1 + c2 == "AG":

            k += 1
        else:
            k = 0
        if k > m:
            m = k
print(m)
