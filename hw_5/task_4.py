"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

d_obj = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5'}
od_obj = OrderedDict({1: '1', 2: '2', 3: '3', 4: '4', 5: '5'})
print(d_obj)


def d_pop(d_1):
    d_1.pop(3)


def od_pop(d_1):
    d_1.pop(3)


def d_keys():
    d_obj.keys()


def od_keys():
    od_obj.keys()


def d_get():
    d_obj.get(1)


def od_get():
    od_obj.get(1)


print(timeit("d_obj = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5'}; d_pop(d_obj)", globals=globals()))
print(timeit("od_obj = OrderedDict({1: '1', 2: '2', 3: '3', 4: '4', 5: '5'}); od_pop(od_obj)", globals=globals()))
print(timeit("d_keys()", globals=globals()))
print(timeit("od_keys()", globals=globals()))
print(timeit("d_get()", globals=globals()))
print(timeit("od_get()", globals=globals()))
'''
Стоит версия питона 3.8
Поэтому думаю, что использовать OrderedDict не имеет смысла, так как и обычный словарь теперь упорядоченен.
По времени, выдача get:
dict:        0.1242276
OrderedDict: 0.13264199999999993
keys()
dict:        0.13991740000000003
OrderedDict: 0.1402803
pop(3)
dict:        0.30125100000000005
OrderedDict: 1.1183097000000002
Если доступ примерно одинаков, то удаление элемента у OrderedDict заметно выше.
'''