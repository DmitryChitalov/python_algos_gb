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


nums = [randint(1, 1000) for i in range(200)]
print(timeit("func_1(nums)", "from __main__ import func_1, nums"))
print(timeit("func_2(nums)", "from __main__ import func_2, nums"))
# Сделал создание массива через list comprehension
# получилось быстрее по времени
# не создается дополнительный массив, в который затем добавляются значения
# значения проверяются сразу, если подходят - добавляются
