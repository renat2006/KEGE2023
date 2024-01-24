import itertools

word_for_letters = sorted(set("ЭМИЛЬ"))

words = list(map(''.join, itertools.permutations(word_for_letters, 5)))

s = ''
k = 0
for word in words:
    if word[0] != "Ь" and not "ИЭ" in word:
        k += 1

print(k)
