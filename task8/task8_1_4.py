import itertools

word_for_letters = sorted(set("МАОУЛИЦЕЙ"), reverse=True)

words = list(map(''.join, itertools.product(word_for_letters, repeat=6)))

print(words.index("УМЕЛЕЦ") + 1)
