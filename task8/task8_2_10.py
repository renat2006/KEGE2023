import itertools

word_for_letters = sorted(set("01234"))

words = list(map(''.join, itertools.product(word_for_letters, repeat=3)))
s = ''
k = 0
for word in words:
    if word[0] != "0" and sorted(set(word), reverse=True) == list(word):
        k += 1

print(k)
