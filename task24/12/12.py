with open("data.txt") as f:
    s = f.readline().strip()
    s_split = s.split("V")

    k = dict()
    for line in s_split[:-1]:
        if not line:
            continue
        if not line[0] in k.keys():
            k[line[0]] = 1
        else:
            k[line[0]] += 1
sorted_dict = sorted(k.items(), key=lambda x: x[1], reverse=True)
print(f'{sorted_dict[0][0]}{sorted_dict[0][1]}')
