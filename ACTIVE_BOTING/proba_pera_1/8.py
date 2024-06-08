import itertools

word = "ЦАПЛЯ"
word = sorted(list(word))
words = map("".join, itertools.product(word, repeat=5))
for ind, w in enumerate(words, start=1):
    if w.count("А") <= 1 and w.count("Ц") == 2 and w.count("Л") == 0:
        print(ind, w)
        break
