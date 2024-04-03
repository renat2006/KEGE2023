import fnmatch

for i in range(1, int(1e9)):
    if fnmatch.fnmatch(str(i), "131*131?") and i % 143 == 0:
        print(f'{i}*{i // 143}', end='-')
