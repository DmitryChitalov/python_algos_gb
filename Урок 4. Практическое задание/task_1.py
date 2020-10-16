"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
import timeit
# from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in nums if i % 2 == 0]
    return new_arr


n = [i for i in range(99)]

#  check the function
print(func_1(n))
print(func_2(n))

#
print(timeit.timeit("func_1(n)", setup="from __main__ import func_1, n", number=10000))
print(timeit.timeit("func_2(n)", setup="from __main__ import func_2, n", number=10000))

"""
Время работы первой функции - 0.1722609
Время работы второй функции - 0.08358789999999999

Первая функция квадтратичная O(n^2)
Вторая функция линейная O(n) является генераторным выражением и работает быстрее первой.

"""

