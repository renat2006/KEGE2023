f = open("24 (2).txt")
s = f.readline().strip()
mx = 0
l = r = kA = kO = 0
for r in range(len(s)):
    if s[r] == "A": kA += 1
    if s[r] == "O": kO += 1
    while kA > 100 or kO > 100:
        if s[l] == "A": kA -= 1
        if s[l] == "O": kO -= 1
        l += 1
    if kA <= 100 and kO <= 100: mx = max(mx, r - l + 1)
print(mx)