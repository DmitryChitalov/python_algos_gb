"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from timeit import timeit


def filling_dict(val):
    a = dict()
    for i in range(val):
        a[str(i)] = i


def filling_o_dict(val):
    a = OrderedDict()
    for i in range(val):
        a[str(i)] = i


def for_every_kv_dict(val):
    for key, value in val.items():
        a = key
        b = value


def for_every_kv_o_dict(val):
    for key, value in val.items():
        a = key
        b = value


def list_sorting_dict(val):
    a = sorted(val.items(), key=lambda item: item[1])


def list_sorting_o_dict(val):
    a = sorted(val.items(), key=lambda item: item[1])


def popitem_dict(val):
    for i in range(len(val)):
        a = val.popitem()


def popitem_o_dict(val):
    for i in range(len(val)):
        a = val.popitem()


val_1 = 10101
my_dict = {str(i): i for i in range(10101)}
o_my_dict = OrderedDict(my_dict)

print('filling_dict = ',
      timeit("filling_dict(val_1)",
             setup="from __main__ import filling_dict, val_1",
             number=10101))

print('filling_o_dict = ',
      timeit("filling_o_dict(val_1)",
             setup="from __main__ import filling_o_dict, val_1",
             number=10101))

print('for_every_kv_dict = ',
      timeit("for_every_kv_dict(my_dict)",
             setup="from __main__ import for_every_kv_dict, my_dict",
             number=10101))

print('for_every_kv_o_dict = ',
      timeit("for_every_kv_o_dict(o_my_dict)",
             setup="from __main__ import for_every_kv_o_dict, o_my_dict",
             number=10101))

print('list_sorting_dict = ',
      timeit("list_sorting_dict(my_dict)",
             setup="from __main__ import list_sorting_dict, my_dict",
             number=10101))

print('list_sorting_o_dict = ',
      timeit("list_sorting_o_dict(o_my_dict)",
             setup="from __main__ import list_sorting_o_dict, o_my_dict",
             number=10101))

print('popitem_dict = ',
      timeit("popitem_dict(my_dict)",
             setup="from __main__ import popitem_dict, my_dict",
             number=10101))

print('popitem_o_dict = ',
      timeit("popitem_o_dict(o_my_dict)",
             setup="from __main__ import popitem_o_dict, o_my_dict",
             number=10101))
