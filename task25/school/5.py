import re

pattern = r'1[1, 3, 5, 7, 9]*3456[0, 2, 4, 6, 8]{1}8'

for i in range(157, 10 ** 10, 157):

    if re.fullmatch(pattern, str(i)):
        print(f'{i}*{i // 157}', end='-')
