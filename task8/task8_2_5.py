import itertools

word_for_letters = sorted(set("ЭЛИНА"))

words = list(map(''.join, itertools.product(word_for_letters, repeat=5)))
not_list = list(map(''.join, itertools.product("ЭИА", repeat=2)))
not_list += list(map(''.join, itertools.product("ЛН", repeat=2)))
s = ''
k = 0
for word in words:
    if not any(map(lambda x: x in word, not_list)):
        k += 1

print(k)
