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


a = [1, 2, 3, 4, 56, 342, 2134, 4143]

print(func_1(a))

print(timeit(stmt="func_1(a)", setup='from __main__ import func_1, a', number=100000))


def foo(num):
    return [i for i in range(len(num)) if not num[i] % 2]

# включение списков работает быстре цикла for


print(foo(a))

print(timeit(stmt="foo(a)", setup='from __main__ import foo, a', number=100000))


