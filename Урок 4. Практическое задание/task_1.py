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

# в своей реализации алгоритма мне удалось добиться уменьшения времени за счет применения встроенных
# алгоритмов и добиться лаконичности кода
def func_2(nums):
    return [el for el in range(len(nums)) if nums[el] % 2 == 0]


test_arr = [_ for _ in range(1000)]

print(timeit("func_1(test_arr)",
             setup="from __main__ import func_1, test_arr",
             number=100000)) #7.9463215
print(timeit("func_2(test_arr)",
             setup="from __main__ import func_2, test_arr",
             number=100000)) #6.5645950