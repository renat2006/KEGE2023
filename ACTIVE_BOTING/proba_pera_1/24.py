f = open("24 (4).txt")
s = f.readline().strip()
k = 0
mk = 0
s = s.replace("B", "A")
s = s.replace("C", "A")
strs = s.split("AA")
lens = list(map(len, strs))
print(max(lens) + 1)
