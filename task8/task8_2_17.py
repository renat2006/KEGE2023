import itertools

word_for_letters = sorted(set("НАСТЯ"))

words = list(map(''.join, itertools.permutations(word_for_letters, 5)))
not_list = list(map(''.join, itertools.product("АЯ", repeat=2)))

s = ''
k = 0
for word in words:
    if not any(map(lambda x: x in word, not_list)):
        k += 1

print(k)
