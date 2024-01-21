import itertools

word_for_letters = sorted(set("КЕГЭАИТОВ"))

words = list(map(''.join, itertools.product(word_for_letters, repeat=6)))

k = 0
for index, word in enumerate(words[1::2], start=1):
    if not word.startswith("Т") and word.count("Е") == 2:
        k += 1
print(k)
