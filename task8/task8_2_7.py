import itertools

word_for_letters = sorted(set("ВИКТОР"))

words = list(map(''.join, itertools.product(word_for_letters, repeat=6)))
# not_list = list(map(''.join, itertools.product("ЭИА", repeat=2)))
# not_list += list(map(''.join, itertools.product("ЛН", repeat=2)))
s = ''
k = 0
for word in words:
    if word.count("В") + word.count("К") + word.count("Т") + word.count("Р") >= 3:
        k += 1

print(k)
