import itertools

alph = "012345678"
c = 0
words = list(map(''.join, itertools.product(alph, repeat=6)))
for w in words:
    if w[0] not in "01357" and w[-1] not in "23" and  w.count("1") >= 2:
        c += 1
print(c)