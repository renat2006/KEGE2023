with open("data.txt") as f:
    s = f.readline().strip()
    local_max_ind = 0
    max_dist = 0
    for i in range(2, len(s)):
        c1 = s[i - 2]
        c2 = s[i - 1]
        c3 = s[i]
        if c2 > c1 and c2 > c3:
            if abs(i - 1 - local_max_ind) > max_dist:
                max_dist = abs(i - 1 - local_max_ind)
            local_max_ind = i - 1
print(max_dist)
