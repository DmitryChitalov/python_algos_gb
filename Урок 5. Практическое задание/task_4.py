"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""


import collections
from timeit import timeit

"""Ordered Dict"""

def odict_popitem(odict):
    odict.popitem(last=True)
    return odict

def odict_move_to_end(odict):
    odict.move_to_end(1, last=True)
    return odict

"""Dict"""

def dict_copy(dict):
    p = dict.copy()
    return p

def dict_fromkeys():
    new_dict = dict.fromkeys(['1', '2', 'arrr'])
    return new_dict


def dict_get(dict):
    p = dict.get(3, ["default"])
    return p

def dict_items(dict):
    item = dict.items()
    return item

def dict_keys(dict):
    item = dict.keys()
    return item

def dict_popitem(dict):
    dict.popitem(2)
    return dict


def dict_pop(dict):
    dict.pop(1)
    return dict

def dict_values(dict):
    p = dict.values()
    return p



user_dict = {1 : 2, 3 : 4, 5 : 6}
user_odict = collections.OrderedDict(user_dict)



dict_of_dicts = {}
dict_of_odicts = {}

dict_of_odicts["popitem"] = (timeit('odict_popitem', setup='from __main__ import odict_popitem', number=10000000))
dict_of_odicts["move_to_end"] = (timeit('odict_move_to_end', setup='from __main__ import odict_move_to_end', number=10000000))

dict_of_dicts["popitem"] = (timeit('dict_popitem', setup='from __main__ import dict_popitem', number=10000000))

print(f'Ordered dict: {dict_of_odicts}')
print(f'Dict: {dict_of_dicts}')

print("Dict: ")
print(f" copy: {timeit('dict_copy', setup='from __main__ import dict_copy', number=10000000)}")
print(f" fromkeys: {timeit('dict_fromkeys', setup='from __main__ import dict_fromkeys', number=10000000)}")
print(f" get: {timeit('dict_get', setup='from __main__ import dict_get', number=10000000)}")
print(f" items: {timeit('dict_items', setup='from __main__ import dict_items', number=10000000)}")
print(f" keys: {timeit('dict_keys', setup='from __main__ import dict_keys', number=10000000)}")
print(f" pop: {timeit('dict_pop', setup='from __main__ import dict_pop', number=10000000)}")
print(f" values: {timeit('dict_values', setup='from __main__ import dict_values', number=10000000)}")


"""Вывод: 
Ordered dict удобен, если использовать постоянную коллекцию (что-то подтасовать в ней и т.д.)
Обычный dict хорош тем, что у него больше функций. 
Время выполнение везде примерно одинаковое (от 0.3 до 0.39), хотя один раз dict.keys показал больше 5 секунд. 
"""