import itertools

word_for_letters = sorted(set("КАРИМ"))

words = list(map(''.join, itertools.product(word_for_letters, repeat=5)))
# not_list = list(map(''.join, itertools.product("ЭИА", repeat=2)))
# not_list += list(map(''.join, itertools.product("ЛН", repeat=2)))
s = ''
k = 0
for word in words:
    if word.count("КА") + word.count("КИ") == word.count("К") and word.count("К") <= 2:
        print(word)
        k += 1

print(k)
