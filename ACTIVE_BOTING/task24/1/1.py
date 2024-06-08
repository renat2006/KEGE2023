f = open("24.txt")
s = f.readline()
s = s.replace("N", "*")
s = s.replace("D", "*")
strings = s.split("E")
strings = strings[1:-1]
mx = 0
print(strings)
for el in strings:
    mx = max(mx, len(el) + 2) if el.count("*") == len(el) else mx
print(
    mx
)
