import itertools

word_for_letters = sorted(set("АРСЕНИЙ"))

words = list(map(''.join, itertools.permutations(word_for_letters, 5)))


s = ''
k = 0
for word in words:
    if not "РАЙ" in word and word[0] != "Й":
        k += 1

print(k)
