import itertools

word_for_letters = sorted(list("АИТОВРУ"))

words = list(map(''.join, itertools.product(word_for_letters, repeat=5)))

print(words.index("ТОВАР") + 1)
