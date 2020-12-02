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


def func_2(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


nums = [el for el in range(1000)]
print(
    timeit(
        "func_1(nums)",
        setup="from __main__ import func_1, nums",
        number=10000))

nums_2 = [el for el in range(1000)]
print(
    timeit(
        "func_2(nums_2)",
        setup="from __main__ import func_2, nums_2",
        number=10000))
