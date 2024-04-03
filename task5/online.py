mr = 1e9
for n in range(1000):
    r1 = bin(n)[2:]
    if n % 2 == 0:
        r2 = r1 + "00"
    else:
        r2 = r1 + "11"
    r3 = r2 + str((r2.count("1") % 2))
    r = int(r3, 2)
    if r < mr and r > 177:
        mr = r
print(mr)
