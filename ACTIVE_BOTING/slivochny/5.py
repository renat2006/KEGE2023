mx = 0
for n in range(1, 1000):

    bn = bin(n)[2:]
    if bn.count("1") % 2 == 0:
        bn = bn + "0"
        bn = "10" + bn[2:]
    else:
        bn = bn + "1"
        bn = "11" + bn[2:]
    r = int(bn, 2)
    if r < 35:
        mx = max(mx, n)
print(mx)
mx = 0
for n in range(1, 1000):
    bn = bin(n)[2:]
    if bn.count("1") % 2 == 0:
        bn = bn + "0"
        bn = "10" + bn[2:]
    else:
        bn = bn + "1"
        bn = "11" + bn[2:]
    r = int(bn, 2)
    if r < 35:
        mx = max(mx, n)
print(mx)
