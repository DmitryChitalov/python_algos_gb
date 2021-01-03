"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from string import ascii_lowercase
from timeit import timeit


def fill_dict():
    my_dict = {letter: [1] for letter in ascii_lowercase}
    return my_dict


def fill_odict():
    my_ordered_dict = OrderedDict([(letter, [1]) for letter in ascii_lowercase])
    return my_ordered_dict


def dict_get():
    my_value = my_dict.get('y')
    return my_value


def odict_get():
    my_od_value = my_odict.get('y')
    return my_od_value


def dict_pop():
    my_dict.pop('c')
    return my_dict


def odict_pop():
    my_odict.pop('c')
    return my_odict


def dict_insert():
    my_dict['c'] = 1
    return my_dict


def odict_insert():
    my_odict['c'] = 1
    return my_odict


my_dict = fill_dict()
my_odict = fill_odict()


print(timeit("fill_dict()", setup="from __main__ import fill_dict", number=1000))
print(timeit("fill_odict()", setup="from __main__ import fill_odict", number=1000))
print(timeit("dict_get()", setup="from __main__ import dict_get, my_dict", number=10000))
print(timeit("odict_get()", setup="from __main__ import odict_get, my_odict", number=10000))
print(timeit("dict_pop()", setup="from __main__ import dict_pop, my_dict", number=1))
print(timeit("odict_pop()", setup="from __main__ import odict_pop, my_odict", number=1))
print(timeit("dict_insert()", setup="from __main__ import dict_insert, my_dict", number=1))
print(timeit("odict_insert()", setup="from __main__ import odict_insert, my_dict", number=1))


"""
Время заполнения словаря и OrderedDict соответственно (1000 повторений):
0.0021945
0.0049313

Время доступа к ключу словаря и OrderedDict соответственно (10000 повторений):
0.0009287
0.0009472

Время удаления пары по ключу из словаря и OrderedDict соответственно (1 повторение):
1.300000000002688e-06
5.699999999997374e-06

Время вставки пары ключ - значаение в словарь и OrderedDict соответственно (1 повторение):
8.999999999981245e-07
1.000000000001e-06

С точки зрения скорости выполнения базовых операций обычный словарь имеет преимущество перед OrderedDict.
"""
