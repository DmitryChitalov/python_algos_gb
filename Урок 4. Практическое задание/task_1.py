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


def my_func(nums):
    return [i for i, k in enumerate(nums) if i % 2 == 0]


nums = list(range(200))
print(timeit("func_1(nums)", globals=globals()))
print(timeit("my_func(nums)", globals=globals()))
print(
    "List Comprehensions быстрее, т.к. определение списка и его содержимого происходит одновременно. В первом варианте создается пустой список и проиходит постоянно добавление в конец списка ")
