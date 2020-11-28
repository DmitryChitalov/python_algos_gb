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


print(timeit("func_1([0, 1, 2, 3, 4, 5, 6, 7, 8])", setup="from __main__ import func_1"))


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


print(timeit("func_2([0, 1, 2, 3, 4, 5, 6, 7, 8])", setup="from __main__ import func_2"))


def func_3(nums):
    new_arr = nums[::2]
    return new_arr


print(timeit("func_3([0, 1, 2, 3, 4, 5, 6, 7, 8])", setup="from __main__ import func_3"))

"""
Добавил 2 реализации задачи в виде функций (func_2, funk_3):
1. func_2 реализовал через генераторное выражение, стало еще медленнее (не значительно, но в среднем на 10-15%)
2. func_3 реализовал через срез с шагом 2, скорость возрасла в разы, т.к. удалось избавится от цикла и
операции деления, которые являются достатьчно медленными.
"""

