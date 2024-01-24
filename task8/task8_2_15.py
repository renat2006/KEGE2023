import itertools

word_for_letters = sorted(set("ВИКУЛЯ"))

words = list(map(''.join, itertools.permutations(word_for_letters, 6)))
not_list = list(map(''.join, itertools.product("ИУЯ", repeat=2)))
not_list += list(map(''.join, itertools.product("ВКЛ", repeat=2)))
s = ''
k = 0
for word in words:
    if not any(map(lambda x: x in word, not_list)):
        k += 1

print(k)
