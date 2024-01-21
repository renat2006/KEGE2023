import itertools

word_for_letters = sorted(set("ИЛЬДАР"))

words = list(map(''.join, itertools.product(word_for_letters, repeat=5)))

s = ''
k = 0
for word in words:
    if word.count("И") > 0 and not word.startswith("Ь"):
        k += 1

print(k)
