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

num_list = [randint(1, 150) for i in range(1000)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(
    timeit(
        "func_1(num_list)",
        globals=globals(),
        number=10000),)


def func_2(nums):
    return [el for el in nums if el % 2 == 0]


print(
    timeit(
        "func_2(num_list)",
        globals=globals(),
        number=10000))

"""Использовал генератор списка, так как он, по найденной мною информации, является самым быстрым способом создания
 списка"""
