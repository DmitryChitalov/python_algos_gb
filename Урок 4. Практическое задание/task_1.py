"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import Timer


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in nums if i%2 == 0]
    return new_arr


time_1 = Timer('func_1([i for i in range(1000)])', 'from __main__ import func_1')
print(f'Program execution time: {round(time_1.timeit(number=1000), 7)} milliseconds')


time_2 = Timer('func_2([i for i in range(1000)])', 'from __main__ import func_2')
print(f'Program execution time: {round(time_2.timeit(number=1000), 7)} milliseconds')


'''
Применив генераторное выражение для создания нового списка в теле функции, удалось сократить время выполнения программы
до 40-50 % от первоначальных значений'''