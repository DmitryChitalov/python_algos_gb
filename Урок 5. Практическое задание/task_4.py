"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit

simple_dict = {0: 0}
o_dict = {0: 0}
od_dict = OrderedDict(o_dict)


def filling_dict(used_dict):
    for i in range(1, 100):
        used_dict[i] = i


def get_even(used_dict):
    result = {}
    for key, value in used_dict.items():
        if value % 2 == 0:
            result[key] = value


print(
    f'Заполнение обычного словаря: {timeit("filling_dict(simple_dict)", setup="from __main__ import filling_dict, simple_dict")}')
print(f'Заполнение order_dict: {timeit("filling_dict(od_dict)", setup="from __main__ import filling_dict, od_dict")}')
print(
    f'Нахождение четных элементов в обычном словаре: {timeit("get_even(simple_dict)", setup="from __main__ import get_even, simple_dict")}')
print(
    f'Нахождение четных элементов в order_dict: {timeit("get_even(od_dict)", setup="from __main__ import get_even, od_dict")}')

"""Заполнение обычного словаря: 3.6754183
Заполнение order_dict: 4.718720599999999
Нахождение четных элементов в обычном словаре: 7.616466800000001
Нахождение четных элементов в order_dict: 9.704160300000002
Вывод: обычный словарь работает быстрее OrderedDict.
Использование OrderedDict в новых версиях Python нецелесообразно"""
