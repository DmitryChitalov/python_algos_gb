"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
"""Первый вариант работает дольше т.к. в нём каждый элемент добавляется функцией append"""
"""Первый вариант работает дольше т.к. в нём каждый элемент добавляется функцией append"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


"""Второй вариант быстрее т.к. в нем используется генератор"""


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


print(timeit('func_1(list(range(20)))', 'from __main__ import func_1'))
print(timeit('func_2(list(range(20)))', 'from __main__ import func_2'))
