import itertools

word_for_letters = sorted(set("КАМИЛЬ"))
words = list(map(''.join, itertools.product(word_for_letters, repeat=6)))

s = ''
k = 0
for word in words:
    if word.count("М") == 1 and not word.startswith("Ь"):
        k += 1

print(k)

