"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from timeit import timeit
from collections import OrderedDict

dct = {i: i for i in range(10)}
ord_dct = OrderedDict(dct)
print(dct)
print(ord_dct)


def dct_items():
    return dct.items()


def ord_dct_items():
    return ord_dct.items()


def dct_keys():
    return dct.keys()


def ord_dct_keys():
    return ord_dct.keys()


def dct_get():
    return dct.get(5)


def ord_dct_get():
    return ord_dct.get(8)


print(f"items для словаря: "
      f"{timeit('dct_items()', setup='from __main__ import dct_items', number=1000000)}")
print(f"items для OrderedDict: "
      f"{timeit('ord_dct_items()', setup='from __main__ import ord_dct_items', number=1000000)}")
print(f"keys для словаря: "
      f"{timeit('dct_keys()', setup='from __main__ import dct_keys', number=1000000)}")
print(f"keys для OrderedDict: "
      f"{timeit('ord_dct_keys()', setup='from __main__ import ord_dct_keys', number=1000000)}")
print(f"get для словаря: "
      f"{timeit('dct_get()', setup='from __main__ import dct_get', number=1000000)}")
print(f"get для OrderedDict: "
      f"{timeit('ord_dct_get()', setup='from __main__ import ord_dct_get', number=1000000)}")

'''
OrderedDict при выводе выглядит как dict.items().
операции с OrderedDict занимают немного меньше времени чем операции со словарем
'''