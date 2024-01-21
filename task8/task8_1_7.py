import itertools

word_for_letters = sorted(set("АРСЕНИЙ"))
not_list = list(map(''.join, itertools.product("РСНЙ", repeat=2)))
words = list(map(''.join, itertools.product(word_for_letters, repeat=6)))

k = 0
for index, word in enumerate(words, start=1):
    if index % 2 == 0 and not word.startswith("Р") and not word.startswith("С") and not any(
            map(lambda x: x in word, not_list)):
        k = index
print(k)
