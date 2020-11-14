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
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


col = 10000
arr = [i for i in range(int(col / 10))]

setup = "from __main__ import func_1, arr"
print(timeit('func_1(arr)', setup, number=col))
setup = "from __main__ import func_2, arr"
print(timeit('func_2(arr)', setup, number=col))

"""
print(func_1(arr))
print(func_2(arr))
"""

# Вывод. Генераторные выражения чуть более оптимальные по скорости исполнения.
#2.8421562
#2.4519685000000004