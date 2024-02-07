import re


def count(input_string):
    pattern = re.compile(r'K.{2}E')
    matches = pattern.findall(input_string)
    count = len(matches)
    return count


k = 0
input_strings = open("data.txt").readlines()
for string in input_strings:
    s = string.strip()
    if count(s) > 0:
        k += 1

print(k)
