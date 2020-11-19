"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit

normal_dict = {x: [x] for x in range(10)}
print(normal_dict)


order_dict = OrderedDict(normal_dict)
print(order_dict)


def dict_get(dict):
    deus = dict.get(0)
    return deus


def o_dict_get(dict):
    deus = dict.get(0)
    return deus

#############


def dict_items(dict):
    deus = dict.items()
    return deus


def o_dict_items(dict):
    deus = dict.items()
    return deus
###################


def dict_pop(dict):
    deus = dict.popitem()
    return deus


def o_dict_pop(dict):
    deus = dict.popitem()
    return deus


print(timeit("dict_get(normal_dict)",
             setup="from __main__ import dict_get,normal_dict"))

print(timeit("o_dict_get(order_dict)",
             setup="from __main__ import o_dict_get,order_dict"))


print("dict_items", timeit("dict_items(normal_dict)",
                           setup="from __main__ import dict_items,normal_dict"))

print("o_dict_items", timeit("o_dict_items(order_dict)",
                             setup="from __main__ import o_dict_items,order_dict"))


print("dict_pop", timeit("dict_pop(normal_dict)",
                         setup="from __main__ import dict_pop,normal_dict"))

print("o_dict_pop", timeit("o_dict_pop(order_dict)",
                           setup="from __main__ import o_dict_pop,order_dict"))

''' 0.16556569999999998
0.16794370000000003'''
''' 
dict_items 0.1772817
o_dict_items 0.17905860000000007'''
""" Вычисления указывают на то,что операции в OrderedDict выполняются медленней"""
