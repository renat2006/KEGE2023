import collections
import itertools

word_for_letters = sorted(set("01234"))

words = list(map(''.join, itertools.product(word_for_letters, repeat=5)))
not_list = ["00", "11", "22", "33", "44"]
s = ''
k = 0
for word in words:
    c = sorted(list(collections.Counter(word).values()), reverse=True)

    if word[0] != "0" and c.count(2) == 1 and c[0] <= 2 and not any(
            [x in word for x in not_list]):
        k += 1

print(k)
