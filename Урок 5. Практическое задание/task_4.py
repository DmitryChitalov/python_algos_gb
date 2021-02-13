"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from timeit import timeit

order_dict = OrderedDict()
simple_dict = {}


def simple_dict_add():
    for el in range(1, 1000):
        simple_dict[el] = el
    return simple_dict


simple_dict = simple_dict_add()


def order_dict_add():
    for el in range(1, 1000):
        order_dict[el] = el
    return order_dict


order_dict = order_dict_add()


def simple_dict_pop(s_dict):
    a = s_dict.popitem()


def order_dict_pop(o_dict):
    a = o_dict.popitem()


def simple_dict_allel():
    for key, value in simple_dict.items():
        value = key


def order_dict_allel():
    for key, value in order_dict.items():
        value = key


print("Добавление элементов")
print(
    timeit(
        "simple_dict_add()",
        setup='from __main__ import simple_dict_add',
        number=10000))

print(
    timeit(
        "order_dict_add()",
        setup='from __main__ import order_dict_add',
        number=10000))

print("извлечение элемента")
print(
    timeit(
        "simple_dict_pop(simple_dict)",
        setup='from __main__ import simple_dict_pop , simple_dict',
        number=100))

print(
    timeit(
        "order_dict_pop(order_dict)",
        setup='from __main__ import order_dict_pop , order_dict',
        number=100))
print("Проход по всем элементам")
print(
    timeit(
        "simple_dict_allel()",
        setup='from __main__ import simple_dict_allel',
        number=10000))

print(
    timeit(
        "order_dict_allel()",
        setup='from __main__ import order_dict_allel',
        number=10000))

"""
OrderedDict сохраняет порядок добалвенных элементов
из за этого он медленне в операциях добавления извлечения данных из словаря
"""
