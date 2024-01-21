import itertools

word_for_letters = sorted(list("СВЁКЛА"))

words = list(map(''.join, itertools.product(word_for_letters, repeat=5)))

print(words[1005])
