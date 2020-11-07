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
from random import randint


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


sum = [randint(-1000, 1000) for _ in range(1000)]
setup = f'from __main__ import func_1, func_2, sum'

print(timeit('func_1(sum)', setup, number=10000))
print(timeit('func_2(sum)', setup, number=10000))

"""
func_1 = 1.6493223000000001
func_2 = 1.0511811999999998

генераторы работают быстрее
"""