"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from timeit import timeit

dict = {i: i for i in range(100)}
order_dict = OrderedDict(dict)

n = 1000


def filling_dict():
    dict = {i: i ** 2 for i in range(n) if i % 2 == 0}
    return dict


def filling_orderdict():
    order_dict = {i: i ** 2 for i in range(n) if i % 2 == 0}
    return order_dict


def copy_dict():
    return dict.copy()


def copy_orderdict():
    return order_dict.copy()


def popitem_dict():
    for i in range(-1):
        dict.pop(i)
    return dict


def popitem_orderdict():
    for i in range(-1):
        order_dict.pop(i)
    return order_dict

# print(filling_dict())
# print(copy_dict())
# print(copy_orderdict())
# print(popitem_dict())
# print(popitem_orderdict())
#

print(f'filling_dict {timeit("filling_dict()",globals=globals(), number=1000)} ')
print(f'filling_orderdict {timeit("filling_orderdict()",globals=globals(), number=1000)} ')
print(f'copy_dict {timeit("copy_dict()",globals=globals(), number=100000)} ')
print(f'copy_orderdict {timeit("copy_orderdict()",globals=globals(), number=100000)} ')
print(f'popitem_dict {timeit("popitem_dict()",globals=globals(), number=100000)} ')
print(f'popitem_orderdict {timeit("popitem_orderdict()",globals=globals(), number=100000)} ')
"""
#заполнение словарей одинаково
filling_dict 0.36381810000000003 
filling_orderdict 0.4127197 

# copy order_dict медленнее
copy_dict 0.0693975 
copy_orderdict 0.9727062000000001 

#popitem одинаково
popitem_dict 0.0328966 
popitem_orderdict 0.032679200000000005 

Разница времени выполнения несущественна, в новых версиях python (с 3.7) словари оптимизированы на сохранение порядка
"""
