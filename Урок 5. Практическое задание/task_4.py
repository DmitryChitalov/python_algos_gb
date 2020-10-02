"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
"""Класс collections.OrderedDict()"""

import timeit

from collections import OrderedDict as o_dict

dict_new = dict(banana=3, apple=4, pear=1, orange=2)
"""
OrderedDict(sorted(dict_new.items(), key=lambda t: t[0]))

OrderedDict(sorted(dict_new.items(), key=lambda t: t[1]))

OrderedDict(sorted(dict_new.items(), key=lambda t: len(t[0])))
"""


def filling_dict(num):
    a = dict()
    for i in range(num):
        a[str(i)] = i


def filling_o_dict(num):
    a = o_dict()
    for i in range(num):
        a[str(i)] = i


def for_every_kv_dict(dict_new):
    for key, value in dict_new.items():
        a = key
        b = value


def for_every_kv_o_dict(dict_new):
    for key, value in dict_new.items():
        a = key
        b = value


def list_sorting_dict(dict_new):
    a = sorted(dict_new.items(), key=lambda item: item[1])


def list_sorting_o_dict(dict_new):
    a = sorted(dict_new.items(), key=lambda item: item[1])


def list_sorting_dict_zero(dict_new):
    a = sorted(dict_new.items(), key=lambda item: item[0])


def list_sorting_o_dict_zero(dict_new):
    a = sorted(dict_new.items(), key=lambda item: item[0])


# popitem(last=True) - удаляет последний элемент если last=True, и первый, если last=False.

def popitem_dict(dict_new):
    for i in range(len(dict_new)):
        a = dict_new.popitem()


def popitem_o_dict(dict_new):
    for i in range(len(dict_new)):
        a = filled_dict.popitem()


def get_dict(dict_new):
    for i in range(len(dict_new)):
        dict_new.get(str(i))


def get_o_dict(dict_new):
    for i in range(len(dict_new)):
        dict_new.get(str(i))


# move_to_end(key, last=True) - добавляет ключ в конец если last=True, и в начало, если last=False.
def move_to_end_dict(dict_new):
    for i in range(len(dict_new)):
        dict_new.move_to_end(str(i), last=False)


def move_to_end_o_dict(dict_new):
    for i in range(len(dict_new)):
        dict_new.move_to_end(str(i), last=False)


name_list = 'filling_dict filling_o_dict for_every_kv_dict for_every_kv_o_dict list_sorting_dict ' \
            'list_sorting_o_dict list_sorting_dict_zero list_sorting_o_dict_zero popitem_dict popitem_o_dict ' \
            'get_dict get_o_dict move_to_end_dict move_to_end_o_dict'.split()

num_time = 1000

for id, func_name in enumerate(name_list):
    if id % 2 == 0:
        print()
    if id == 0 or id == 1:
        print(
            f"{func_name} -\t{timeit.timeit(stmt=func_name + f'(1000)', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")
    else:
        if id % 2 == 0:
            print(
                f"{func_name} -\t{timeit.timeit(stmt=func_name + f'(dict_new)', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")
        else:
            print(
                f"{func_name} -\t{timeit.timeit(stmt=func_name + f'(dict_new)', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")

"""
collections.OrderedDict - ещё один похожий на словарь объект, но он помнит порядок, в котором ему были даны ключи. Методы:

popitem(last=True) - удаляет последний элемент если last=True, и первый, если last=False.

move_to_end(key, last=True) - добавляет ключ в конец если last=True, и в начало, если last=False.


"""