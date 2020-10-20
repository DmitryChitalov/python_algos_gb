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


def func_3(nums):
    return [ind for ind, el in enumerate(nums) if el % 2 == 0]


def func_4(nums):
    return [ind for ind, el in enumerate(nums) if not el & 1]


test_nums = [i for i in range(1000)]

print(timeit(
        stmt='func_1(test_nums)',
        setup='from __main__ import func_1, test_nums',
        number=10000))

print(timeit(
        stmt='func_3(test_nums)',
        setup='from __main__ import func_3, test_nums',
        number=10000))

print(timeit(
        stmt='func_4(test_nums)',
        setup='from __main__ import func_4, test_nums',
        number=10000))

"""
Выводы:
- генераторное выражение работает быстрее цикла for
- проверка четности при помощи побитогового сравнения (not n & 1)
    работает быстрее опреации извлечения остатка целочисленного деления
"""
