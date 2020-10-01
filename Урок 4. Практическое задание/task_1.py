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


def func_2(num):
    return [i for i, el in enumerate(num) if el % 2 == 0]


val = [el for el in range(10101)]

print(f'func_1 = '
      f'{timeit("func_1(val)", setup="from __main__ import func_1, val", number=10000)}')

print(f'func_2 = '
      f'{timeit("func_2(val)", setup="from __main__ import func_2, val", number=10000)}')

'''
сделал вторую функцию через генератор, т.к. он работает быстрее
'''
