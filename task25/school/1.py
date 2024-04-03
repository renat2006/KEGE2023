import fnmatch

for i in range(1, int(1e9)):
    if fnmatch.fnmatch(str(i), "1?31*437?") and i % 2025 == 0:
        print(f'{i}*{i // 2025}', end='-')