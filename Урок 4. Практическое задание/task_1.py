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
    return list(i for i in range(len(nums)) if nums[i] % 2 == 0)


def func_3(nums):
    return list(index for index, i in enumerate(nums) if i % 2 == 0)


def func_4(nums):
    return list(nums.index(i) for i in nums if i % 2 == 0)


test_arr = list(randint(0, 100) for i in range(50))
print(test_arr)
print(func_1(test_arr))
print(func_2(test_arr))
print(func_3(test_arr))
print(func_4(test_arr))

print(timeit('func_1(test_arr)', setup='from __main__ import func_1, test_arr'))
print(timeit('func_2(test_arr)', setup='from __main__ import func_2, test_arr'))
print(timeit('func_3(test_arr)', setup='from __main__ import func_3, test_arr'))
print(timeit('func_4(test_arr)', setup='from __main__ import func_4, test_arr'))
