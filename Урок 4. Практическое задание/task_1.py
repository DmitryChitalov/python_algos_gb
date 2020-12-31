"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

import random
from timeit import timeit

nums = random.sample(range(1, 50), 30)


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = []
    for index, value in enumerate(nums, start=0):
        if value % 2 == 0:
            new_arr.append(index)
    return new_arr


def func_3(nums):
    new_arr = []
    for index, value in enumerate(nums, start=0):
        if not value % 2:
            new_arr.append(index)
    return new_arr


def func_4(nums):
    return [i for i, elem in enumerate(nums) if elem % 2 == 0]


print(timeit('func_1(nums)', 'from __main__ import func_1, nums'))
print(timeit('func_2(nums)', 'from __main__ import func_2, nums'))
print(timeit('func_3(nums)', 'from __main__ import func_3, nums'))
print(timeit('func_4(nums)', 'from __main__ import func_4, nums'))

"""
Результаты:
func_1 - 3.52274747 - самый медленный вариант
func_2 - 3.340647511 - быстрее за счет использование enumerate
func_3 - 3.0450043189999993 - быстрее за счет предыдущей оптимизации + использования условия if not
func_4 - 2.8462127860000006 - быстрее за счет предыдущих оптимизаций + использования list comprehension
"""
