"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from timeit import timeit


def add_dict():
    my_dict = {}
    for i in range(100):
        my_dict[i] = i

    return my_dict


def add_ordered_dict():
    my_dict = OrderedDict()
    for i in range(100):
        my_dict[i] = i

    return my_dict


print("Добавление элементов")
print(timeit("add_dict()", "from __main__ import add_dict", number=1000))
print(timeit("add_ordered_dict()", "from __main__ import add_ordered_dict", number=1000))


def rm_dict():
    my_dict = {}
    for i in range(100):
        my_dict[i] = i

    return my_dict


def rm_ordered_dict():
    my_dict = OrderedDict()
    for i in range(100):
        my_dict[i] = i

    return my_dict


print("Удаление элементов")
print(timeit("rm_dict()", "from __main__ import rm_dict", number=1000))
print(timeit("rm_ordered_dict()", "from __main__ import rm_ordered_dict", number=1000))

"""
Добавление элементов
dict - 0.008469900000000002
OrderedDict - 0.015973299999999996

Удаление элементов
dict - 0.0087671
OrderedDict - 0.022273200000000007

Добавление и удаление элементов из OrderedDIct просиходит почти в 2 раза дольше, чем из стандартного dict.
Сейчас OrderedDict нецелесообразно оспользовать, т.к. начиная с версии Python 3.6 словари уже упорядочены.
"""
