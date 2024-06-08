k = 0
for A in range(1, 1000):
    F = True
    for x in range(1, A + 1):
        F = F * ((A % 12 == 0) and (not (530 % x == 0) or ((A % x == 0) or not (170 % x == 0))))
        if not F:
            break
    if F:
        k += 1
print(k)

