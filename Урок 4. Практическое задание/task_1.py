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


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_3(nums):
    return [i for i, x in enumerate(nums) if x % 2 == 0]


nums = [random.randint(0, 1000) for i in range(10000)]
print(timeit("func_1(nums)", setup="from __main__ import func_1, nums", number=1000))
print(timeit("func_2(nums)", setup="from __main__ import func_2, nums", number=1000))
print(timeit("func_3(nums)", setup="from __main__ import func_3, nums", number=1000))

"""Генератор эффективнее метода append, т.к. список генерируется сразу целиком. 
    Причем, использование enumerate() вместо range(len()) еще больше повышает эффективность.
    Функция enumerate() не обращается к каким-то внутренним атрибутам коллекции, 
    а просто реализует счетчик обработанных элементов"""
