import itertools

words = list(map(''.join, itertools.permutations("ПЕРЕВЫБОРЫ", 10)))
not_list = list(map(''.join, itertools.product("ПРВБР", repeat=2)))
not_list += list(map(''.join, itertools.product("ЕЫО", repeat=2)))
s = ''
k = 0

for word in words:
    if not any(map(lambda x: x in word, not_list)):
        k += 1

print(k)
