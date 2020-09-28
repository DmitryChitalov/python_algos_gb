"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from timeit import timeit
from collections import OrderedDict

d = {k: k for k in range(10)}
od = {k: k for k in range(10)}
od = OrderedDict(od)


def items_d():
    return d.items()


def items_od():
    return od.items()


def get_d():
    return d.get(1)


def get_od():
    return od.get(1)


print(timeit('items_d()', setup='from __main__ import items_d', number=1000))  # 0.0001370000000000017
print(timeit('get_d()', setup='from __main__ import get_d', number=1000))   # 0.00012790000000000024
print(timeit('items_od()', setup='from __main__ import items_od', number=1000))   # 0.0001337999999999999
print(timeit('get_od()', setup='from __main__ import get_od', number=1000))   # 0.0001238000000000003
# исходя из замеров можно сделать вывод, что оба вида словарей работают одинаково, OrderDict был сделан
# для упорядочивания элементов словаря. Начиная с версии 3,7 словарь приобрел данный функционал.
