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
    new_arr = []
    for i, x in enumerate(nums):
        if x % 2 == 0:
            new_arr.append(i)
    return new_arr


my_list = [1523, 47, 5646, 346]

print('Начальный код:')
print(timeit(f"func_1({my_list})", setup="from __main__ import func_1", number=10000))

print('Оптимизированный код:')
print(timeit(f"func_2({my_list})", setup="from __main__ import func_2", number=10000))

"""
Заменила цикл по номерам элементов на цикл по парам номер_элемента - значение. 
Быстрее потому что нет операции обращения к элементу массива по номеру.
"""
