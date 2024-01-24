import itertools

word_for_letters = sorted(set("01234567"))

words = list(map(''.join, itertools.product(word_for_letters, repeat=5)))
not_list = list(filter(lambda x: '6' in x and x != "66", map(''.join, itertools.product("13576", repeat=2))))
s = ''
k = 0
for word in words:
    if word[0] != "0" and word.count("6") == 2 and not any([x in word for x in not_list]):
        k += 1

print(k)
