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


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


NUM = [i for i in range(1, 51)]

my_time_1 = timeit.Timer("func_1(NUM)", "from __main__ import func_1, NUM")
print(f"Время работы функции {func_1.__name__} равно {my_time_1.timeit()} секунд"
      f"\n{func_1(NUM)}")
# Время работы функции func_1 равно 5.5093274999999995 секунд


def func_2(nums):
    return list(i for i in range(0, len(nums)) if nums[i] % 2 == 0)
# Время работы функции func_2 равно 4.906452900000001 секунд
# - незначительно увеличивается производительность при n == 50, чем выше, правда, тем нагляднее


my_time_2 = timeit.Timer("func_2(NUM)", "from __main__ import func_2, NUM")
print(f"Время работы функции {func_2.__name__} равно {my_time_2.timeit()} секунд"
      f"\n{func_2(NUM)}")
