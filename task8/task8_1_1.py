import itertools

word_for_letters = sorted(set("СНЕГУРОЧКА"))

words = list(map(''.join, itertools.product(word_for_letters, repeat=5)))

print(words.index("ЧУКЧА") - words.index("РУЧКА") + 1)
