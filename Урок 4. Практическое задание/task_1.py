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
    for i in range(len(my_lst)):
        if my_lst[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

my_lst = [el for el in range(10000)]


def func_2(nums):
    return [i for i, el in enumerate(my_lst) if el % 2 == 0]

my_lst = [el for el in range(10000)]


print(timeit.timeit("func_1(my_lst)", setup="from __main__ import func_1, my_lst", number=1000))
print(timeit.timeit("func_2(my_lst)", setup="from __main__ import func_2, my_lst", number=1000))

'''Обе функции имеют сложность О(N), но вторая функция выполняется быстрее за счет генераторного выражения'''
