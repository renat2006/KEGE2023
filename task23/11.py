"""
Исполнитель преобразует число на экране. У исполнителя есть три команды, которые обозначены латинскими буквами:

прибавь 1
прибавь 2
умножь на 3
Программа для исполнителя – это последовательность команд.

Сколько существует программ, которые число 1 преобразуют в число 13 и при этом содержат не более двух команд B?
"""
import math
import sys
from functools import lru_cache

sys.setrecursionlimit(100000)


@lru_cache(None)
def f(c, e, c_2):
    if c > e: return 0
    if c == e: return c_2 <= 2
    return f(c + 1, e, c_2) + f(c + 2, e, c_2 + 1) + f(c * 3, e, c_2)


print(f(1, 13, 0))
