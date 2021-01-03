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
    return [i for i in nums if i % 2 == 0]


print(timeit('func_1(range(10000))', setup='from __main__ import func_1', number=1000))
print(timeit('func_2(range(10000))', setup='from __main__ import func_2', number=1000))

"""
В своём варианте оптимизации я использовал list comprehension вместо цикла и добавления элементов в массив.
Это сократило время выполнения кода.
"""