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


def func_mod(num):
    element = [inx for inx, elm in enumerate(num) if elm % 2 == 0]
    return element


list_nums = [el for el in range(1000)]
print(timeit("func_1(list_nums)", globals=globals(), number=1000))
print(timeit("func_mod(list_nums)", globals=globals(), number=1000))

list_nums = [el for el in range(10000)]
print(timeit("func_1(list_nums)", globals=globals(), number=1000))
print(timeit("func_mod(list_nums)", globals=globals(), number=1000))

list_nums = [el for el in range(100000)]
print(timeit("func_1(list_nums)", globals=globals(), number=1000))
print(timeit("func_mod(list_nums)", globals=globals(), number=1000))

# Списковые включения работают быстрее.
