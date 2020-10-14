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
import random


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [num for num in nums if num % 2 == 0]
    return new_arr


user_array = [random.randint(0, 100) for num in range(0, 100)]


print(
    'Время выполнения func_1: '
    f'{timeit(f"func_1({user_array})", setup="from __main__ import func_1", number=1000)}')
print(
    'Время выполнения func_2: '
    f'{timeit(f"func_2({user_array})", setup="from __main__ import func_2", number=1000)}')

# Время выполнения func_1: 0.020818599999999993
# Время выполнения func_2: 0.0109784

# Вывод: достигнуто снижение времени выполнения функции за счет использования list comprehension
