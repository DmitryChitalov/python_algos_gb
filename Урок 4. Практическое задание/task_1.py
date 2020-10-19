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
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


nums_example = list(range(100))
print(timeit('func_1(nums_example)', 'from __main__ import func_1, nums_example'))
print(timeit('func_2(nums_example)', 'from __main__ import func_2, nums_example'))
"""
func_2 использует генераторное выражение, 
вместо используемого в func_1 перебора в цикле,
что оказывается более быстродейственным, при большом количестве элементов.
"""
