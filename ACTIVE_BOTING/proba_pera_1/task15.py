mn = 1e9
for a1 in range(160, 810):
    for a2 in range(a1 + 1, 810):
        for x in range(160, 810):
            f = (not (170 <= x <= 580)) or (not ((290 <= x <= 800) and not (a1 <= x <= a2)) or (not (170 <= x <= 580)))
            if not f:
                break
        else:
            mn = min(mn, a2-a1)
print(mn / 10)