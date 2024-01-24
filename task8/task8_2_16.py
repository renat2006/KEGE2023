import itertools

word_for_letters = sorted(set("РАВИЛЬ"))

words = list(map(''.join, itertools.permutations(word_for_letters, 6)))
not_list = ["АЬ", "ИЬ"]

s = ''
k = 0
for word in words:
    if word[0] != "Ь" and not any(map(lambda x: x in word, not_list)):
        k += 1

print(k)
