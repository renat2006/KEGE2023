from itertools import product

nums = list(map(''.join, product("01234567", repeat=5)))
k = 0
for num in nums:
    if num[0] != "0" and num.count("2") == 2 and not "22" in num:
        k += 1
print(k)
