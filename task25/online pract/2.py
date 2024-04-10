from fnmatch import fnmatch

k = 0
for i in range(2021, 10 ** 10, 2021):

    if fnmatch(str(i), "3?5919*7"):
        print(i, i // 2021)
        k += 1
    if k == 3:
        break
