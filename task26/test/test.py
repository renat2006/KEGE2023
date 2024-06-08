import numpy as np


def calculate_average_and_median(ratings):
    ratings = np.array(ratings)
    p = int(len(ratings) * 0.3)
    ratings = ratings[(p // 2):-p // 2]
    ratings = ratings * 100
    return np.mean(ratings), np.median(ratings)


def find_min_avg_max_diff(ratings):
    min_avg = float('inf')
    max_diff = 0
    max_id = 0
    for id, ratings in ratings.items():
        avg, med = calculate_average_and_median(ratings)
        if avg < min_avg:
            min_avg = avg
            max_id = id
        if abs(avg - med) > max_diff:
            max_diff = abs(avg - med)
            max_id = id
    return min_avg, max_id


# Пример использования
with open('input.txt', 'r') as file:
    lines = file.readlines()
    p, n = map(int, lines[0].split())
    ratings = {}
    for _ in range(n):
        id, rating = map(int, lines[1].split())
    ratings[id] = ratings.get(id, []) + [rating]
    min_avg, max_id = find_min_avg_max_diff(ratings)
    print(f'{min_avg} {max_id}')
