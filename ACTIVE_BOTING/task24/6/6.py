f = open("24 (5).txt")
s = f.readline().strip()
strr = s.split("E")
print(strr)
mn = 1e9
for i in range(1, len(strr) - 99):
    t = ''.join(strr[i:i + 99])

    mn = min(mn, len(t) + 100)
print(mn)