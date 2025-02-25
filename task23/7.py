"""
У исполнителя Калькулятор три команды, которым присвоены номера:

вычти 1
раздели на 2
раздели на 3
Программа для исполнителя – это последовательность команд. Команду 2 можно применять только к числам, которые делятся на 2, а команду 3 - только к числам, которые делятся на 3.

Сколько существует программ, которые число 30 преобразуют в число 1?
"""
a = [0] * 100
a[30] = 1
for i in range(30, 1, -1):
    if i - 1 >= 1: a[i - 1] += a[i]
    if i % 2 == 0 and i / 2 >= 1: a[i // 2] += a[i]
    if i % 3 == 0 and i / 3 >= 1: a[i // 3] += a[i]
print(a[1])