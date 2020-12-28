"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(timeit('func_1(range(10000))', setup='from __main__ import func_1', number=1000))


def func_2(nums):
    new_arr = [i for i, j in enumerate(nums) if j % 2 == 0]
    return new_arr


print(timeit('func_2(range(10000))', setup='from __main__ import func_2', number=1000))

"""Время для func_1 - 1.8013255
   Время для func_2 - 0.8352696
   func_1 оптимизировали заменой цикла на генераторное выражение"""
