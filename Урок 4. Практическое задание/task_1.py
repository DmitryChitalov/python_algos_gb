"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
"""При проведении замеров получил следующие значения:
11.034423579
7.709664846000001
при 1 млн повторов
Для оптимизации применил генераторное выражение вместо цикла for, т.к. оно работает быстрее
генераторное выражение быстрее на 42%"""

from timeit import timeit

numbers = list(range(101))


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(timeit("func_1(numbers)", setup="from __main__ import func_1, numbers"))


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if i % 2 == 0]
    return new_arr


print(timeit("func_2(numbers)", setup="from __main__ import func_2, numbers"))
