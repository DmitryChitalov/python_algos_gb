"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from timeit import timeit


def ord_dict():
    my_ord_dict = OrderedDict()
    for i in range(100):
        my_ord_dict[i] = i
    my_ord_dict.popitem()
    my_ord_dict.popitem(last=False)
    return my_ord_dict


def simple_dict():
    my_dict = dict()
    for i in range(100):
        my_dict[i] = i
    my_dict.popitem()
    my_dict.pop(0)
    return my_dict


print(timeit(stmt='ord_dict', setup='from __main__ import ord_dict'))
print(timeit(stmt='simple_dict', setup='from __main__ import simple_dict'))

#после того как стандартные списки стали упорядоченными, необходимость в OrderedDict пропала

