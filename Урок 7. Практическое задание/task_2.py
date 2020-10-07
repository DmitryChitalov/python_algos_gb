"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import random
from timeit import timeit


def merge_sort(value):
    if len(value) > 1:
        mid = len(value) // 2
        left_side = value[:mid]
        right_side = value[mid:]

        merge_sort(left_side)
        merge_sort(right_side)

        i, j, k = 0, 0, 0
        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                value[k] = left_side[i]
                i += 1
            else:
                value[k] = right_side[j]
                j += 1
            k += 1

        while i < len(left_side):
            value[k] = left_side[i]
            i += 1
            k += 1

        while j < len(right_side):
            value[k] = right_side[j]
            j += 1
            k += 1
    return value


val = [random() * 50 for i in range(5)]

print(f'Исходный = {val}')
print(f'Отсортированный = {merge_sort(val[:])}')
print(timeit('merge_sort(val[:])',
             setup='from __main__ import merge_sort, val'))

'''
Исходный = [20.126873746146924, 46.15922142076582, 24.272890924987863, 5.466752893953042, 48.49887563733694]
Отсортированный = [5.466752893953042, 20.126873746146924, 24.272890924987863, 46.15922142076582, 48.49887563733694]
10.213943975
'''
