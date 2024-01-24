import itertools

word_for_letters1 = sorted(set("БИЛЛ"))
word_for_letters2 = sorted(set("СТИВ"))
words1 = list(map(''.join, itertools.product(word_for_letters1, repeat=2)))
words2 = list(map(''.join, itertools.product(word_for_letters2, repeat=2)))
s = ''
k = 0
print(len(words1) * len(words2) * 4 * 3 * 2 * 2 )

