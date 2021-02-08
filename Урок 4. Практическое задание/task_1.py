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
    new_arr = []
    i = 0
    for rec in nums:
        if rec % 2 == 0:
            new_arr.append(i)
        i += 1
    return new_arr


g_lst = [77, 55, 22, 33, 99, 66, 88, 11]

print(timeit('func_1(g_lst)',
             setup="from __main__ import func_1, g_lst", number=1000000))
print(timeit('func_2(g_lst)',
             setup="from __main__ import func_2, g_lst", number=1000000))
# В func_1 перебор элементов осуществляется через доступ по индексу.
# В func_2 перебор элементов осуществляется через встроенный механизм
#   итераторов(парадигма foreach).
# Встроенные механизмы чаще всего работают быстреее, чем те же самые
#   действия, выполненные вручную.
# Это и показывают замеры через timeit: func_2 работает быстрее, чем func_1.
