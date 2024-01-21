import itertools

word_for_letters = sorted(set("АБИКМНОРТ"))
dic = {
    char: i for i, char in enumerate(word_for_letters)
}
print(dic)
s = ''
for char in "КОМБИНАТОРИКА":
    s += str(dic[char])
print(int(s, 9))
