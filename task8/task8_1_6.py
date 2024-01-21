import itertools

word_for_letters = sorted(set("КЕГЭАИТОВРУ"))

words = list(map(''.join, itertools.product(word_for_letters, repeat=6)))

k = 0
for index, word in enumerate(words, start=1):
    if index % 2 != 0 and not word.startswith("У") and word.count("К") == 2 and word.count("В") > 0:
        k = index
print(k)
