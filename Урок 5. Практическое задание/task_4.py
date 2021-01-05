"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

"""
import timeit
import collections


def dict_n():
    sum = 0
    dict = {}
    for i in range(10):
        dict[i] = i
        sum += i
    return dict, sum


def orderdict():
    sum = 0
    collections.OrderedDict = {}
    for i in range(10):
        collections.OrderedDict[i] = i
        sum += i
    return collections.OrderedDict, sum


print(dict_n())
print(orderdict())

print(timeit.timeit("dict_n()", setup="from __main__ import dict_n"))
print(timeit.timeit("orderdict()", setup="from __main__ import orderdict"))
"""
обычный дикт выполняется за
1.9386304
а ордер дист за 
2.5431133000000004
поэтому обычный дист лутче использщвать

"""