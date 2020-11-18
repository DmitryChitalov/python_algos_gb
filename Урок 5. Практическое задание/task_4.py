"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
"""Заполнение и извлечение значений (get) в OrderedDict происходит медленнее, чем в обычном словаре
Сортировка в OrderedDict также происходит медленнее (в 2 раза), чем в обычном словаре
Т.к. начиная с версии 3.5 словари стали упорядоченны по умолчанию, видимо "под капотом" реализовали 
более эффективные алгоритмы, чем в подключаемой библиотеке.
Также замерил время для import --> импортирование коллекции целиком происходит быстрее, чем отдельных элементов из нее
"""
from collections import OrderedDict
from timeit import timeit


def func_1():
    simple_dict = dict()
    for i in range(10000):
        simple_dict[i] = i
        simple_dict.get(i)
    return simple_dict


def func_2():
    simple_dict = dict()
    for i in range(10000):
        simple_dict[i] = i
    return simple_dict


def func_3():
    order_dict = OrderedDict()
    for i in range(10000):
        order_dict[i] = i
        order_dict.get(i)
    return order_dict


def func_4():
    order_dict = OrderedDict()
    for i in range(10000):
        order_dict[i] = i
    return order_dict


def func_5():
    simple_dict = dict()
    for i in range(10000):
        simple_dict[i] = i
    return OrderedDict(sorted(simple_dict.items(), key=lambda t: t[1]))


def func_6():
    simple_dict = dict()
    for i in range(10000):
        simple_dict[i] = i
    new_dict = sorted(simple_dict.items(), key=lambda t: t[1])
    return new_dict


def func_7():
    from collections import deque


def func_8():
    import collections


functions = ["func_1()", "func_2()", "func_3()", "func_4()", "func_5()", "func_6()", "func_7()", "func_8()"]
setup_data = "from __main__ import func_1, func_2, func_3, func_4, func_5, func_6, func_7, func_8"

for fn in functions:
    print(f'Время выполнения функции {fn}',
          timeit(fn, setup=setup_data, number=1000))
