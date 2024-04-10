import fnmatch

for i in range(47, 10**10, 47):
    if fnmatch.fnmatch(str(i), "9*4*0") and all([x > y for x, y in zip(str(i), str(i)[1:])]):
        print(f'{i}*{i // 47}', end='-')