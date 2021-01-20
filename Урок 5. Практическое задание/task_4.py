"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
import timeit

abc = {}
xyz = OrderedDict(abc)


def create_dict():
    abc = {i: i / 2 for i in range(10000)}
    return abc


def create_order_dict():
    xyz = {i: i / 2 for i in range(10000)}
    return xyz


def pop_dict():
    for i in abc:
        abc.pop(i)
    return abc


def pop_order_dict():
    for i in xyz:
        xyz.pop(i)
    return xyz


def dict_items():
    for i in abc:
        abc.items()


def order_dict_items():
    for i in xyz:
        xyz.items()


print('CREATE:')
print(timeit.timeit('create_dict', setup='from __main__ import create_dict', number=10000))
print(timeit.timeit('create_order_dict', setup='from __main__ import create_order_dict', number=10000))
print('POP')
print(timeit.timeit('pop_dict', setup='from __main__ import pop_dict', number=10000))
print(timeit.timeit('pop_order_dict', setup='from __main__ import pop_order_dict', number=10000))
print('ITEMS')
print(timeit.timeit('dict_items', setup='from __main__ import dict_items', number=10000))
print(timeit.timeit('order_dict_items', setup='from __main__ import order_dict_items', number=10000))

'''
CREATE:
0.0005156000000000605
0.0005797000000000718
POP
0.0005182000000000242
0.0005213000000000578
ITEMS
0.0005139000000000671
0.0005140999999999618

получились идентичные результаты, каких либо преимуществ, кроме отслеживания порядка ввода значений в OrderedDict
(при случае может оказаться полезным инструментом), я не увидел 
'''