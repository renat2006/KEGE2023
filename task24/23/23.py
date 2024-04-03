import re

f = open('data.txt')
s = f.readline().strip()
print(len(s))

d = r"R{1,}T{1,}"
res = re.findall(d, s)
lm = 0
for el in res:
    if lm < len(el):
        lm = len(el)
        print(lm, el)
