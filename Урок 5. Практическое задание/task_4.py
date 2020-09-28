"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
import collections
from timeit import timeit


def dict_operations():
    my_dict = {}
    my_dict[1] = 1
    my_dict.get(1)


def order_dict_operations():
    my_dict = collections.OrderedDict([])
    my_dict[1] = 1
    my_dict.get(1)


print(f"dict  {timeit('dict_operations()', setup='from __main__ import dict_operations', number=1000000)}")
print(f"order dict  {timeit('order_dict_operations()', setup='from __main__ import order_dict_operations', number=1000000)}")