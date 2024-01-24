import collections
import itertools

word_for_letters = list("0123456789ABCDEFGHIJ")

not_list = list(map(''.join, itertools.product(word_for_letters[2::2], repeat=2)))
not_list += list(map(''.join, itertools.product(word_for_letters[1::2], repeat=2)))
s = ''
k = 0
for a in word_for_letters:
    for b in word_for_letters[int(a, 20) + 1::2]:
        for c in word_for_letters[int(b, 20) + 1::2]:
            for d in word_for_letters[int(c, 20) + 1::2]:
                for e in word_for_letters[int(d, 20) + 1::2]:
                    for f in word_for_letters[int(e, 20) + 1::2]:
                        for g in word_for_letters[int(f, 20) + 1::2]:
                            for h in word_for_letters[int(g, 20) + 1::2]:
                                for i in word_for_letters[int(h, 20) + 1::2]:
                                    for j in word_for_letters[int(i, 20) + 1::2]:
                                        for l in word_for_letters[int(j, 20) + 1::2]:
                                            for m in word_for_letters[int(l, 20) + 1::2]:
                                                for n in word_for_letters[int(m, 20) + 1::2]:
                                                    for o in word_for_letters[int(n, 20) + 1::2]:
                                                        for p in word_for_letters[int(o, 20) + 1::2]:
                                                            for q in word_for_letters[int(p, 20) + 1::2]:
                                                                for r in word_for_letters[int(q, 20) + 1::2]:
                                                                    for t in word_for_letters[int(r, 20) + 1::2]:
                                                                        for u in word_for_letters[int(t, 20) + 1::2]:
                                                                            for w in word_for_letters[int(u, 20) + 1::2]:
                                                                               print(a+b+c+d+e+f+g+h+i+j+l+m+n+o+p+q+r+t+u+w)

print(k)
