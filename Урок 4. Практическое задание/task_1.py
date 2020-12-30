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
    new_arr = [nums.index(el) for el in nums if el % 2 == 0]
    return new_arr


def func_3(nums):
    new_arr = [i for i, el in enumerate(nums) if el % 2 == 0]
    return new_arr


nums = [randint(0, 100) for el in range(100)]

print(
    timeit(
        "func_1(nums)",
        setup="from __main__ import func_1, nums",
        number=1000))

print(
    timeit(
        "func_2(nums)",
        setup="from __main__ import func_2, nums",
        number=1000))

print(
    timeit(
        "func_3(nums)",
        setup="from __main__ import func_3, nums",
        number=1000))

"""
Самой быстрой по времени оказалась функция три (использование генератора и функции enumerate). 
Функция enumerate работает быстрее, чем методы списка и избавляет от дополнительной переменной для хранения индекса 
"""


