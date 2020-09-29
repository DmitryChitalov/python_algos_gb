"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

import timeit
import random
from collections import OrderedDict

n = 10000


def set_dict(n):
    dct = {i: random.randint(0, n) for i in range(n)}
    return dct


def set_o_dict(n):
    o_dct = OrderedDict(set_dict(n))
    return o_dct


def items_dict(dict):
    dict.items()


def items_o_dict(dict):
    dict.items()


def update_dict(dict, other):
    dict.update(other)


def update_o_dict(dict, other):
    dict.update(other)


def popitem_dict(dict):
    dict.popitem()


def popitem_o_dict(dict):
    dict.popitem()


dct = set_dict(n)
o_dct = set_o_dict(n)
other = {'a': 11,
         'b': 22,
         'c': 33
         }

print(timeit.timeit('set_dict(n)', setup="from __main__ import set_dict, n", number=1000))
print(timeit.timeit('set_o_dict(n)', setup="from __main__ import set_o_dict, n", number=1000))
print(timeit.timeit('items_dict(dct)', setup="from __main__ import items_dict, dct", number=1000))
print(timeit.timeit('items_o_dict(o_dct)', setup="from __main__ import items_o_dict, o_dct", number=1000))
print(timeit.timeit('update_dict(dct, other)', setup="from __main__ import update_dict, dct, other", number=1000))
print(
    timeit.timeit('update_o_dict(o_dct, other)', setup="from __main__ import update_o_dict, o_dct, other", number=1000))
print(timeit.timeit('popitem_dict(dct)', setup="from __main__ import popitem_dict, dct", number=1000))
print(timeit.timeit('popitem_o_dict(o_dct)', setup="from __main__ import popitem_o_dict, o_dct", number=1000))

"""Порядок времени выполнения функций одинаков, обычный словарь работает немного быстрее"""
