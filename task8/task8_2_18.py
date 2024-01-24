import itertools

word_for_letters = sorted(set("ТИМУР"))

words = list(map(''.join, itertools.permutations(word_for_letters, 4)))
not_list = list(map(''.join, itertools.product("ТМР", repeat=2)))
not_list += list(map(''.join, itertools.product("ИУ", repeat=2)))

s = ''
k = 0
for word in words:
    if not any(map(lambda x: x in word, not_list)):
        k += 1

print(k)
