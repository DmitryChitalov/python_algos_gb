"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from timeit import timeit
from random import randint
my_dict = {a: randint(0, 100) for a in range(10)}
my_ord_dict = OrderedDict(my_dict)


def my_dict_values():
    my_dict.values()


def my_ord_dict_values():
    my_ord_dict.values()


def my_dict_keys():
    my_dict.keys()


def my_ord_dict_keys():
    my_ord_dict.keys()


def my_dict_get():
    my_dict.get(1)


def my_ord_dict_get():
    my_ord_dict.get(1)


print(timeit("my_dict_values()", globals=globals(), number=100000))
print(timeit("my_ord_dict_values()", globals=globals(), number=100000))
print(timeit("my_dict_keys()", globals=globals(), number=100000))
print(timeit("my_ord_dict_keys()", globals=globals(), number=100000))
print(timeit("my_dict_get()", globals=globals(), number=100000))
print(timeit("my_ord_dict_get()", globals=globals(), number=100000))

"""
OrderedDict не дает преимуществ в быстродействии при работе как с маленькими словарями, так и с большими.
Считаю его использование на старших версиях питона нецелесообразным.
"""
