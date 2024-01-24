import itertools

word_for_letters = sorted(list("АЛИНА"))

words = list(map(''.join, itertools.permutations(word_for_letters, 5)))

s = ''
k = 0
for word in words:
    print(word)
    if not "АА" in word:
        print(word)
        k += 1

print(k)
