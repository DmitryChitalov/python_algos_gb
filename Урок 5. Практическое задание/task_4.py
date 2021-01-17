"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from random import randint
from timeit import timeit

# сделаны замеры для операций заполнение словарей, обращение по ключу,
# получение ключей и значений
# согласно замерам время выполнения операций для обычного словаря и сортированного словаря не отличаются

dct = dict()
ord_dct = OrderedDict()
# заполнение словарей


def dct_append(d):
    for i in range(0, 11):
        d[i] = randint(10, 100)
    return d


def ord_dct_append(od):
    for i in range(0, 11):
        od[i] = randint(10, 100)
    return od

# обращение к словарям по случайному ключу


def dct_appeal(d):
    return d[randint(0, 10)]


def ord_dct_appeal(od):
    return od[randint(0, 10)]

# получение ключей и значений


def dct_keys_values(d):
    keys = []
    values = []
    keys.append(d.keys())
    values.append(d.values())
    return keys, values


def ord_dct_keys_values(od):
    keys = []
    values = []
    keys.append(od.keys())
    values.append(od.values())
    return keys, values


print(dct_append(dct))
print(ord_dct_append(ord_dct))
print(dct_appeal(dct))
print(ord_dct_appeal(ord_dct))
print(dct_keys_values(dct))
print(ord_dct_keys_values(ord_dct))
print(dct_keys_values(dct))
print(ord_dct_keys_values(ord_dct))

print('dct_append', timeit("dct_append(dct)", setup="from __main__ import dct_append, dct", number=1000))
print('ord_dct_append', timeit("ord_dct_append(ord_dct)",
                               setup="from __main__ import ord_dct_append, ord_dct", number=1000))
print('dct_appeal', timeit("dct_appeal(dct)", setup="from __main__ import dct_appeal, dct", number=1000))
print('ord_dct_appeal', timeit("ord_dct_appeal(ord_dct)",
                               setup="from __main__ import ord_dct_appeal, ord_dct", number=1000))
print('dct_keys_values', timeit("dct_keys_values(dct)", setup="from __main__ import dct_keys_values, dct", number=1000))
print('ord_dct_keys_values', timeit("ord_dct_keys_values(ord_dct)",
                               setup="from __main__ import ord_dct_keys_values, ord_dct", number=1000))
