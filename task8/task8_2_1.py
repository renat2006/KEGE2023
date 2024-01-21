import itertools

word_for_letters = sorted(set("ЛИЦЕЙ"))
words = list(map(''.join, itertools.product(word_for_letters, repeat=4)))

s = ''
k = 0
print(len(words))

