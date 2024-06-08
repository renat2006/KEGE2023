f = open("24 (1).txt")
s = f.readline()
s = "A" + s + "A"
strs = s.split("A")
c = 0
for i in range(len(s) - 241):
    sr = "A".join(strs[i:i+241])
    c = max(c, len(sr))
print(c)

