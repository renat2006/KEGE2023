import itertools

word_for_letters = sorted(set("ЛАСТИК"))
words = list(map(''.join, itertools.product(word_for_letters, repeat=5)))
cas_ind = words.index("КАСКА")
s = ''
not_list = list(map(''.join, itertools.product("ЛСТК", repeat=2)))
not_list += list(map(''.join, itertools.product("АИ", repeat=2)))
k = 0
for word in words[cas_ind:4045]:
    if not any(map(lambda x: x in word, not_list)):
        k += word.count("И")

print(k)
