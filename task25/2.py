mx = 0
k = 0
for i in range(7747, 25121 + 1):
    if i % 6 != i % 10 and (i % 11 == 0 or i % 12 == 0 or i % 17 == 0):
        k += 1
        if i > mx:
            mx = i
print(k, mx)
