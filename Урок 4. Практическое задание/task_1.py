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


arr = [n for n in range(1, 11111) if n % 2 == 0]

print(timeit("func_1(arr)", setup="from __main__ import func_1, arr", number=1000))
print(timeit("func_2(arr)", setup="from __main__ import func_2, arr", number=1000))

"""
результат:
0.47990150000000004
0.3471668

Заменил цикл генераторным выражением, достаточно быстрый способ создания списка.
"""