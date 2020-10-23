"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from timeit import timeit
from collections import OrderedDict

dict_example = {el: el for el in range(10)}
ordered_dict_example = {el: el for el in range(10)}
ordered_dict_example = OrderedDict(ordered_dict_example)


def items_d():
    return dict_example.items()


def items_od():
    return ordered_dict_example.items()


def get_d():
    return dict_example.get(1)


def get_od():
    return ordered_dict_example.get(1)


print(f"Получение пары ключ-значение из словаря: {timeit('items_d()', 'from __main__ import items_d')}")
print(f"Получение ключа из словаря: {timeit('get_d()', 'from __main__ import get_d')}")
print(f"Получение пары ключ-значение из упорядоченного словаря: {timeit('items_od()', 'from __main__ import items_od')}")
print(f"Получение ключа из упорядоченного словаря: {timeit('get_od()', 'from __main__ import get_od')}")
'''Вывод:
Оба вида словарей работают с одинаковой скоростью, однако в OrderDict элементы упорядочены'''
