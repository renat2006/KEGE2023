from fnmatch import fnmatch

for n in range(31, 10 ** 9, 31):
    if fnmatch(str(n), "12345?7?8"):
        print(n, n // 31, sep="\t")
