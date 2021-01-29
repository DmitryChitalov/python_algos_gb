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


def func_1_optimized(nums):
    l = len(nums)
    return [i for i in range(l) if nums[i] % 2 == 0]


tlst = [randint(1, 100) for a in range(randint(1, 300))]
print(f'Длина входных данных {len(tlst)}')
print(f'Время выполнения функции func_1: ', timeit('func_1(tlst)', globals=globals()))
print(f'Время выполнения функции func_1_optimized: ', timeit('func_1_optimized(tlst)', globals=globals()))

"""
Заменил цикл списковым включением. Оно работает быстрее.
На малом количестве элементов входного массива заметил проигрыш по времени.
"""